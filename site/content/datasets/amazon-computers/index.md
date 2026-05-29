---
title: Amazon-Computers
slug: amazon-computers
benchmark: Classic
task_type: node_classification
description: Amazon co-purchase graph (Computers) node classification.
primary_metric: Accuracy
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.Amazon.html
stats: null
result_count: 508
best_model:
  model: CoE
  value: 0.9801
  metric: Accuracy
  arxiv_id: '2505.20853'
  paper_title: arXiv:2505.20853
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
  - AUC
  - AUROC
  - F1
  - HR@20
  - Macro-F1
  - Micro F1
  - Micro-F1
  - NDCG@20
  - NMI
  - Recall
  - Recall@20
  rows:
  - model: CoE
    model_plain: CoE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.20853'
    title: arXiv:2505.20853
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: https://github.com/strangeAlan/CoE
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9801
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: Mowst
    model_plain: Mowst
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.20853'
    title: arXiv:2505.20853
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: https://github.com/strangeAlan/CoE
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9789
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: InfoMGF
    model_plain: InfoMGF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.20853'
    title: arXiv:2505.20853
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: https://github.com/strangeAlan/CoE
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9778
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: GMoE
    model_plain: GMoE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.20853'
    title: arXiv:2505.20853
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: https://github.com/strangeAlan/CoE
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9778
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: WRF
    model_plain: WRF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.20853'
    title: arXiv:2505.20853
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: https://github.com/strangeAlan/CoE
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9778
    - null
    - null
    - null
    - null
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
    arxiv_id: '2505.20853'
    title: arXiv:2505.20853
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: https://github.com/strangeAlan/CoE
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9776
    - null
    - null
    - null
    - null
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
    arxiv_id: '2505.20853'
    title: arXiv:2505.20853
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: https://github.com/strangeAlan/CoE
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9772
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: RF
    model_plain: RF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.20853'
    title: arXiv:2505.20853
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: https://github.com/strangeAlan/CoE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9756
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0012
    - null
    - null
    - null
    - null
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
    arxiv_id: '2505.20853'
    title: arXiv:2505.20853
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: https://github.com/strangeAlan/CoE
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9751
    - null
    - null
    - null
    - null
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
    arxiv_id: '2505.20853'
    title: arXiv:2505.20853
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: https://github.com/strangeAlan/CoE
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9702
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: COMPGCN-SymCL
    model_plain: COMPGCN-SymCL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.10738'
    title: Knowledge Graph Contrastive Learning based on Relation-Symmetrical Structure
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9655
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: GRCN
    model_plain: GRCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.20853'
    title: arXiv:2505.20853
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: https://github.com/strangeAlan/CoE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9527
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: HDMI
    model_plain: HDMI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.20853'
    title: arXiv:2505.20853
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: https://github.com/strangeAlan/CoE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9508
    - null
    - null
    - null
    - null
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
    arxiv_id: '2505.20853'
    title: arXiv:2505.20853
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: https://github.com/strangeAlan/CoE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.941
    - null
    - null
    - null
    - null
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
    arxiv_id: '2505.20853'
    title: arXiv:2505.20853
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: https://github.com/strangeAlan/CoE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9368
    - null
    - null
    - null
    - null
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
    arxiv_id: '2505.20853'
    title: arXiv:2505.20853
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: https://github.com/strangeAlan/CoE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9312
    - null
    - null
    - null
    - null
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
    arxiv_id: '2505.20853'
    title: arXiv:2505.20853
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: https://github.com/strangeAlan/CoE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9312
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: CompGCN
    model_plain: CompGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.10738'
    title: Knowledge Graph Contrastive Learning based on Relation-Symmetrical Structure
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.931
    - null
    - null
    - null
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
    - 0.9295
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: DAM-GT
    model_plain: DAM-GT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.17660'
    title: 'DAM-GT: Dual Positional Encoding-Based Attention Masking Graph Transformer
      for Node Classification'
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9243
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: LaplaceGNN
    model_plain: LaplaceGNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.20362'
    title: Self-Supervised Graph Learning via Spectral Bootstrapping and Laplacian-Based
      Augmentations
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.923
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
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
    codebase_url: https://github.com/Zehong-Wang/GPM
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.9228
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: SGT
    model_plain: SGT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: May 22, 2024
    date_iso: '2024-05-22'
    date_display: May 2024
    codebase_url: https://github.com/liun-online/WaveGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9226
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: Graph Contrastive Transformer
    model_plain: Graph Contrastive Transformer
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.19258'
    title: Leveraging Contrastive Learning for Enhanced Node Representations in Tokenized
      Graph Transformers
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9209
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: WaveNet
    model_plain: WaveNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: May 22, 2024
    date_iso: '2024-05-22'
    date_display: May 2024
    codebase_url: https://github.com/liun-online/WaveGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9206
    - null
    - null
    - null
    - null
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
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_iso: '2025-01-30'
    date_display: Jan 2025
    codebase_url: https://github.com/Zehong-Wang/GPM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9203
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: VCR-Graphormer
    model_plain: VCR-Graphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.17660'
    title: 'DAM-GT: Dual Positional Encoding-Based Attention Masking Graph Transformer
      for Node Classification'
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9175
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0015
    - null
    - null
    - null
    - null
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
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_iso: '2025-01-30'
    date_display: Jan 2025
    codebase_url: https://github.com/Zehong-Wang/GPM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9163
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: DEFT
    model_plain: DEFT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: May 22, 2024
    date_iso: '2024-05-22'
    date_display: May 2024
    codebase_url: https://github.com/liun-online/WaveGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9163
    - null
    - null
    - null
    - null
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
    - 0.9133
    - null
    - null
    - null
    - null
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
    arxiv_id: '2406.19258'
    title: Leveraging Contrastive Learning for Enhanced Node Representations in Tokenized
      Graph Transformers
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9131
    - null
    - null
    - null
    - null
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
    - 0.9122
    - null
    - null
    - null
    - null
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
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_iso: '2025-01-30'
    date_display: Jan 2025
    codebase_url: https://github.com/Zehong-Wang/GPM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9119
    - null
    - null
    - null
    - null
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
    arxiv_id: '2505.17660'
    title: 'DAM-GT: Dual Positional Encoding-Based Attention Masking Graph Transformer
      for Node Classification'
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9112
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: VCR-Graphormer
    model_plain: VCR-Graphormer
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
    - 0.9104
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0012
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: RAW-GNN
    model_plain: RAW-GNN
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
    - 0.9098
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: GOAT
    model_plain: GOAT
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
    - 0.9096
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: FE-GNN (C)
    model_plain: FE-GNN (C)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.06142'
    title: arXiv:2305.06142
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/sajqavril/Feature-Extension-Graph-Neural-Networks.git
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9079
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0008
    - null
    - null
    - null
    - null
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
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: May 22, 2024
    date_iso: '2024-05-22'
    date_display: May 2024
    codebase_url: https://github.com/liun-online/WaveGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9075
    - null
    - null
    - null
    - null
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
    - 0.907
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
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
    codebase_url: https://github.com/Zehong-Wang/GPM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9062
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: FE-GNN (M)
    model_plain: FE-GNN (M)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.06142'
    title: arXiv:2305.06142
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/sajqavril/Feature-Extension-Graph-Neural-Networks.git
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.906
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: ANS-GT
    model_plain: ANS-GT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.17660'
    title: 'DAM-GT: Dual Positional Encoding-Based Attention Masking Graph Transformer
      for Node Classification'
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9047
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: LSGNN
    model_plain: LSGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.17660'
    title: 'DAM-GT: Dual Positional Encoding-Based Attention Masking Graph Transformer
      for Node Classification'
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9042
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0056
    - null
    - null
    - null
    - null
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
    arxiv_id: '2506.20362'
    title: Self-Supervised Graph Learning via Spectral Bootstrapping and Laplacian-Based
      Augmentations
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9034
    - null
    - null
    - null
    - null
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
    - 0.9023
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAINT
    model_plain: GraphSAINT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.17660'
    title: 'DAM-GT: Dual Positional Encoding-Based Attention Masking Graph Transformer
      for Node Classification'
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9022
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0015
    - null
    - null
    - null
    - null
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
    - 0.9019
    - null
    - null
    - null
    - null
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
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: May 22, 2024
    date_iso: '2024-05-22'
    date_display: May 2024
    codebase_url: https://github.com/liun-online/WaveGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9018
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: VCR-Graphormer
    model_plain: VCR-Graphormer
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.19258'
    title: Leveraging Contrastive Learning for Enhanced Node Representations in Tokenized
      Graph Transformers
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9014
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: ES-MLP
    model_plain: ES-MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.17660'
    title: 'DAM-GT: Dual Positional Encoding-Based Attention Masking Graph Transformer
      for Node Classification'
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9011
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: UGCL
    model_plain: UGCL
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
    - 0.901
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: SP^2GCL
    model_plain: SP^2GCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.20362'
    title: Self-Supervised Graph Learning via Spectral Bootstrapping and Laplacian-Based
      Augmentations
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9009
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: SEA-GWNN
    model_plain: SEA-GWNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: May 22, 2024
    date_iso: '2024-05-22'
    date_display: May 2024
    codebase_url: https://github.com/liun-online/WaveGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8988
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
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
    codebase_url: https://github.com/Zehong-Wang/GPM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8983
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: lrGAE (7)
    model_plain: lrGAE (7)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10241'
    title: Revisiting Graph Autoencoders as Implicit Contrastive Learners
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/EdisonLeeeee/lrGAE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.898
    - null
    - null
    - null
    - null
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
    - 0.8977
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: GiGaMAE
    model_plain: GiGaMAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10241'
    title: Revisiting Graph Autoencoders as Implicit Contrastive Learners
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/EdisonLeeeee/lrGAE
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
    - null
    - null
    - null
    - null
  - model: lrGAE (8)
    model_plain: lrGAE (8)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10241'
    title: Revisiting Graph Autoencoders as Implicit Contrastive Learners
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/EdisonLeeeee/lrGAE
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
    - 0.8968
    - null
    - null
    - null
    - null
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
    - 0.8968
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: CoCoS
    model_plain: CoCoS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.19258'
    title: Leveraging Contrastive Learning for Enhanced Node Representations in Tokenized
      Graph Transformers
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8966
    - null
    - null
    - null
    - null
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
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: May 22, 2024
    date_iso: '2024-05-22'
    date_display: May 2024
    codebase_url: https://github.com/liun-online/WaveGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8965
    - null
    - null
    - null
    - null
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
    arxiv_id: '2410.10241'
    title: Revisiting Graph Autoencoders as Implicit Contrastive Learners
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/EdisonLeeeee/lrGAE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.896
    - null
    - null
    - null
    - null
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
    arxiv_id: '2410.10241'
    title: Revisiting Graph Autoencoders as Implicit Contrastive Learners
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/EdisonLeeeee/lrGAE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.896
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: AUG-MAE
    model_plain: AUG-MAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10241'
    title: Revisiting Graph Autoencoders as Implicit Contrastive Learners
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/EdisonLeeeee/lrGAE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.896
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: RGCN-SymCL
    model_plain: RGCN-SymCL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.10738'
    title: Knowledge Graph Contrastive Learning based on Relation-Symmetrical Structure
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.896
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: ANS-GT
    model_plain: ANS-GT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.19258'
    title: Leveraging Contrastive Learning for Enhanced Node Representations in Tokenized
      Graph Transformers
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8958
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: Ada-Ugnn
    model_plain: Ada-Ugnn
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.06142'
    title: arXiv:2305.06142
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/sajqavril/Feature-Extension-Graph-Neural-Networks.git
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8956
    - null
    - null
    - null
    - null
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
    arxiv_id: '2506.20362'
    title: Self-Supervised Graph Learning via Spectral Bootstrapping and Laplacian-Based
      Augmentations
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8953
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: NCLA
    model_plain: NCLA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.19258'
    title: Leveraging Contrastive Learning for Enhanced Node Representations in Tokenized
      Graph Transformers
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8952
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: MaskGAE
    model_plain: MaskGAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10241'
    title: Revisiting Graph Autoencoders as Implicit Contrastive Learners
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/EdisonLeeeee/lrGAE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.895
    - null
    - null
    - null
    - null
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
    - 0.8939
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: UFGConvS
    model_plain: UFGConvS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: May 22, 2024
    date_iso: '2024-05-22'
    date_display: May 2024
    codebase_url: https://github.com/liun-online/WaveGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8929
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: R-GCN
    model_plain: R-GCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1703.06103'
    title: Modeling Relational Data with Graph Convolutional Networks
    date: Mar 2017
    date_iso: 2017-03
    date_display: Mar 2017
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8929
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: GraphGPS
    model_plain: GraphGPS
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.19258'
    title: Leveraging Contrastive Learning for Enhanced Node Representations in Tokenized
      Graph Transformers
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8921
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: GCN+P+L
    model_plain: GCN+P+L
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.19258'
    title: Leveraging Contrastive Learning for Enhanced Node Representations in Tokenized
      Graph Transformers
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8921
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: RGCN
    model_plain: RGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.10738'
    title: Knowledge Graph Contrastive Learning based on Relation-Symmetrical Structure
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8919
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: GCN+P+R
    model_plain: GCN+P+R
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.19258'
    title: Leveraging Contrastive Learning for Enhanced Node Representations in Tokenized
      Graph Transformers
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8918
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: S2GAE
    model_plain: S2GAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10241'
    title: Revisiting Graph Autoencoders as Implicit Contrastive Learners
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/EdisonLeeeee/lrGAE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.891
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: lrGAE (6)
    model_plain: lrGAE (6)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10241'
    title: Revisiting Graph Autoencoders as Implicit Contrastive Learners
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/EdisonLeeeee/lrGAE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.891
    - null
    - null
    - null
    - null
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
    - 0.8908
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0096
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SSGE
    model_plain: SSGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.20362'
    title: Self-Supervised Graph Learning via Spectral Bootstrapping and Laplacian-Based
      Augmentations
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8905
    - null
    - null
    - null
    - null
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
    arxiv_id: '2506.20362'
    title: Self-Supervised Graph Learning via Spectral Bootstrapping and Laplacian-Based
      Augmentations
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8894
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0015
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SimMLP
    model_plain: SimMLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.17660'
    title: 'DAM-GT: Dual Positional Encoding-Based Attention Masking Graph Transformer
      for Node Classification'
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8892
    - null
    - null
    - null
    - null
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
    arxiv_id: '2406.19258'
    title: Leveraging Contrastive Learning for Enhanced Node Representations in Tokenized
      Graph Transformers
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.889
    - null
    - null
    - null
    - null
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
    - 0.889
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: RDF2Vec-SymCL
    model_plain: RDF2Vec-SymCL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.10738'
    title: Knowledge Graph Contrastive Learning based on Relation-Symmetrical Structure
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8889
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: Scattering GCN
    model_plain: Scattering GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: May 22, 2024
    date_iso: '2024-05-22'
    date_display: May 2024
    codebase_url: https://github.com/liun-online/WaveGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8883
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: ClusterSCL
    model_plain: ClusterSCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.19258'
    title: Leveraging Contrastive Learning for Enhanced Node Representations in Tokenized
      Graph Transformers
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8874
    - null
    - null
    - null
    - null
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
    arxiv_id: '2505.17660'
    title: 'DAM-GT: Dual Positional Encoding-Based Attention Masking Graph Transformer
      for Node Classification'
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8874
    - null
    - null
    - null
    - null
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
    arxiv_id: '2410.10241'
    title: Revisiting Graph Autoencoders as Implicit Contrastive Learners
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/EdisonLeeeee/lrGAE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.887
    - null
    - null
    - null
    - null
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
    arxiv_id: '2505.17660'
    title: 'DAM-GT: Dual Positional Encoding-Based Attention Masking Graph Transformer
      for Node Classification'
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8869
    - null
    - null
    - null
    - null
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
    arxiv_id: '2305.06142'
    title: arXiv:2305.06142
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/sajqavril/Feature-Extension-Graph-Neural-Networks.git
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8866
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0008
    - null
    - null
    - null
    - null
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
    - 0.8855
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: HAT-GAE(full)
    model_plain: HAT-GAE(full)
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
    - 0.8855
    - null
    - null
    - null
    - null
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
    - 0.8854
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: RDF2Vec
    model_plain: RDF2Vec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1703.06103'
    title: Modeling Relational Data with Graph Convolutional Networks
    date: Mar 2017
    date_iso: 2017-03
    date_display: Mar 2017
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8833
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: APPNP
    model_plain: APPNP
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
    - 0.8832
    - null
    - null
    - null
    - null
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
    - 0.8832
    - null
    - null
    - null
    - null
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
    arxiv_id: '2410.10241'
    title: Revisiting Graph Autoencoders as Implicit Contrastive Learners
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/EdisonLeeeee/lrGAE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.883
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: SeeGera
    model_plain: SeeGera
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10241'
    title: Revisiting Graph Autoencoders as Implicit Contrastive Learners
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/EdisonLeeeee/lrGAE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.883
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: WaveShrink-ChebNet
    model_plain: WaveShrink-ChebNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: May 22, 2024
    date_iso: '2024-05-22'
    date_display: May 2024
    codebase_url: https://github.com/liun-online/WaveGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.882
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: GCN+P+D
    model_plain: GCN+P+D
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.19258'
    title: Leveraging Contrastive Learning for Enhanced Node Representations in Tokenized
      Graph Transformers
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8806
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: ChebNet
    model_plain: ChebNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.06142'
    title: arXiv:2305.06142
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/sajqavril/Feature-Extension-Graph-Neural-Networks.git
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8792
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: RDF2Vec
    model_plain: RDF2Vec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.10738'
    title: Knowledge Graph Contrastive Learning based on Relation-Symmetrical Structure
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8788
    - null
    - null
    - null
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
    - 0.878
    - null
    - null
    - null
    - null
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
    - 0.8776
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: HAT-GAE-TC
    model_plain: HAT-GAE-TC
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
    - 0.8769
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: HAT-GAE-HM
    model_plain: HAT-GAE-HM
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
    - 0.8767
    - null
    - null
    - null
    - null
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
    - 0.8763
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: GNN-LF
    model_plain: GNN-LF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.06142'
    title: arXiv:2305.06142
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/sajqavril/Feature-Extension-Graph-Neural-Networks.git
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8763
    - null
    - null
    - null
    - null
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
    - 0.8752
    - null
    - null
    - null
    - null
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
    - 0.8741
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: HAT-GAE-AM
    model_plain: HAT-GAE-AM
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
    - 0.8741
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0003
    - null
    - null
    - null
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
    arxiv_id: '2305.06142'
    title: arXiv:2305.06142
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/sajqavril/Feature-Extension-Graph-Neural-Networks.git
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8738
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0015
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: WL
    model_plain: WL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1703.06103'
    title: Modeling Relational Data with Graph Convolutional Networks
    date: Mar 2017
    date_iso: 2017-03
    date_display: Mar 2017
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8737
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: GRACE
    model_plain: GRACE
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
    - 0.872
    - null
    - null
    - null
    - null
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
    arxiv_id: '2202.04139'
    title: Simplified Graph Convolution with Heterophily
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8714
    - null
    - null
    - null
    - null
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
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_iso: '2025-01-30'
    date_display: Jan 2025
    codebase_url: https://github.com/Zehong-Wang/GPM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8698
    - null
    - null
    - null
    - null
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
    - 0.8697
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0056
    - null
    - null
    - null
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
    - 0.8696
    - null
    - null
    - null
    - null
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
    - 0.8694
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: GNN-HF
    model_plain: GNN-HF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.06142'
    title: arXiv:2305.06142
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/sajqavril/Feature-Extension-Graph-Neural-Networks.git
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8694
    - null
    - null
    - null
    - null
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
    - 0.869
    - null
    - null
    - null
    - null
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
    arxiv_id: '2410.10241'
    title: Revisiting Graph Autoencoders as Implicit Contrastive Learners
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/EdisonLeeeee/lrGAE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.869
    - null
    - null
    - null
    - null
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
    - 0.8681
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: ASGC
    model_plain: ASGC
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.04139'
    title: Simplified Graph Convolution with Heterophily
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8672
    - null
    - null
    - null
    - null
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
    - 0.8671
    - null
    - null
    - null
    - null
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
    - 0.867
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: Supervised GCN
    model_plain: Supervised GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.20362'
    title: Self-Supervised Graph Learning via Spectral Bootstrapping and Laplacian-Based
      Augmentations
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8651
    - null
    - null
    - null
    - null
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
    - 0.864
    - null
    - null
    - null
    - null
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
    arxiv_id: '2410.10241'
    title: Revisiting Graph Autoencoders as Implicit Contrastive Learners
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/EdisonLeeeee/lrGAE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.864
    - null
    - null
    - null
    - null
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
    - 0.863
    - null
    - null
    - null
    - null
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
    arxiv_id: '2210.08792'
    title: Unifying Graph Contrastive Learning with Flexible Contextual Scopes
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: https://github.com/zyzisastudyreallyhardguy/UGCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.863
    - null
    - null
    - null
    - null
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
    arxiv_id: '2506.20362'
    title: Self-Supervised Graph Learning via Spectral Bootstrapping and Laplacian-Based
      Augmentations
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8628
    - null
    - null
    - null
    - null
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
    arxiv_id: '2305.15747'
    title: Union Subgraph Neural Networks
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/AngusMonroe/UnionSNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8626
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0056
    - null
    - null
    - null
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
    arxiv_id: '2410.10241'
    title: Revisiting Graph Autoencoders as Implicit Contrastive Learners
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/EdisonLeeeee/lrGAE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.862
    - null
    - null
    - null
    - null
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
    arxiv_id: '2305.06142'
    title: arXiv:2305.06142
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/sajqavril/Feature-Extension-Graph-Neural-Networks.git
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8607
    - null
    - null
    - null
    - null
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
    arxiv_id: '2305.06142'
    title: arXiv:2305.06142
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/sajqavril/Feature-Extension-Graph-Neural-Networks.git
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8588
    - null
    - null
    - null
    - null
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
    - 0.857
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: Scattering
    model_plain: Scattering
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: May 22, 2024
    date_iso: '2024-05-22'
    date_display: May 2024
    codebase_url: https://github.com/liun-online/WaveGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8568
    - null
    - null
    - null
    - null
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
    - 0.8568
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: UGMAE
    model_plain: UGMAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.20362'
    title: Self-Supervised Graph Learning via Spectral Bootstrapping and Laplacian-Based
      Augmentations
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8568
    - null
    - null
    - null
    - null
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
    arxiv_id: '2406.19258'
    title: Leveraging Contrastive Learning for Enhanced Node Representations in Tokenized
      Graph Transformers
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8547
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0144
    - null
    - null
    - null
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
    arxiv_id: '2110.09443'
    title: Beltrami Flow and Neural Diffusion on Graphs
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: https://github.com/twitter-research/graph-neural-pde
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.854
    - null
    - null
    - null
    - null
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
    - 0.853
    - null
    - null
    - null
    - null
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
    - 0.852
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: SGWT
    model_plain: SGWT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: May 22, 2024
    date_iso: '2024-05-22'
    date_display: May 2024
    codebase_url: https://github.com/liun-online/WaveGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8519
    - null
    - null
    - null
    - null
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
    arxiv_id: '2406.19258'
    title: Leveraging Contrastive Learning for Enhanced Node Representations in Tokenized
      Graph Transformers
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8519
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0226
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AP-GCN
    model_plain: AP-GCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.10306'
    title: Adaptive Propagation Graph Convolutional Network
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: https://github.com/spindro/AP-GCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8518
    - null
    - null
    - null
    - null
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
    - null
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
    - 0.85
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.05
    - null
    - null
    - null
    - null
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
    - 0.849
    - null
    - null
    - null
    - null
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
    arxiv_id: '2305.06142'
    title: arXiv:2305.06142
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/sajqavril/Feature-Extension-Graph-Neural-Networks.git
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8475
    - null
    - null
    - null
    - null
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
    - 0.847
    - null
    - null
    - null
    - null
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
    - 0.847
    - null
    - null
    - null
    - null
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
    - 0.8458
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: IGNN-Solver (AA)
    model_plain: IGNN-Solver (AA)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.08524'
    title: 'IGNN-Solver: A Graph Neural Solver for Implicit Graph Neural Networks'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/landrarwolf/IGNN-Solver
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.845
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: POT
    model_plain: POT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.13944'
    title: Provable Training for Graph Contrastive Learning
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: https://github.com/VoidHaruhi/POT-GCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.845
    - null
    - null
    - null
    - null
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
    - 0.844
    - null
    - null
    - null
    - null
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
    arxiv_id: '2410.08524'
    title: 'IGNN-Solver: A Graph Neural Solver for Implicit Graph Neural Networks'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/landrarwolf/IGNN-Solver
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8432
    - null
    - null
    - null
    - null
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
    - null
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
    - 0.843
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: IGNN-Solver (NN)
    model_plain: IGNN-Solver (NN)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.08524'
    title: 'IGNN-Solver: A Graph Neural Solver for Implicit Graph Neural Networks'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/landrarwolf/IGNN-Solver
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8413
    - null
    - null
    - null
    - null
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
    - 0.8411
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
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
    is_best: false
    metric_values:
    - 0.841
    - null
    - null
    - null
    - null
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
    arxiv_id: '2210.08792'
    title: Unifying Graph Contrastive Learning with Flexible Contextual Scopes
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: https://github.com/zyzisastudyreallyhardguy/UGCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.841
    - null
    - null
    - null
    - null
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.841
    - null
    - null
    - null
    - null
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
    - 0.841
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: DEMO-Net
    model_plain: DEMO-Net
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.08524'
    title: 'IGNN-Solver: A Graph Neural Solver for Implicit Graph Neural Networks'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/landrarwolf/IGNN-Solver
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8408
    - null
    - null
    - null
    - null
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
    - 0.8404
    - null
    - null
    - null
    - null
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
    arxiv_id: '2410.08524'
    title: 'IGNN-Solver: A Graph Neural Solver for Implicit Graph Neural Networks'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/landrarwolf/IGNN-Solver
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.839
    - null
    - null
    - null
    - null
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
    - 0.838
    - null
    - null
    - null
    - null
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
    - 0.8373
    - null
    - null
    - null
    - null
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
    arxiv_id: '2410.08524'
    title: 'IGNN-Solver: A Graph Neural Solver for Implicit Graph Neural Networks'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/landrarwolf/IGNN-Solver
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8368
    - null
    - null
    - null
    - null
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.836
    - null
    - null
    - null
    - null
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
    - 0.8354
    - null
    - null
    - null
    - null
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
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_iso: '2023-05-27'
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.835
    - null
    - null
    - null
    - null
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
    - 0.835
    - null
    - null
    - null
    - null
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
    - 0.835
    - null
    - null
    - null
    - null
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
    - 0.8341
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: UGNN
    model_plain: UGNN
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
    - 0.834
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: simple Teacher-Free Graph Self-Distillation (TGS) framework
    model_plain: simple Teacher-Free Graph Self-Distillation (TGS) framework
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.03483'
    title: A Teacher-Free Graph Knowledge Distillation Framework with Dual Self-Distillation
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: https://github.com/LirongWu/TGS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.834
    - null
    - null
    - null
    - null
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
    - 0.8336
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0015
    - null
    - null
    - null
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
    arxiv_id: '2406.19258'
    title: Leveraging Contrastive Learning for Enhanced Node Representations in Tokenized
      Graph Transformers
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8317
    - null
    - null
    - null
    - null
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
    arxiv_id: '2202.04139'
    title: Simplified Graph Convolution with Heterophily
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8311
    - null
    - null
    - null
    - null
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
    arxiv_id: '2010.01777'
    title: A Unified View on Graph Neural Networks as Graph Signal Denoising
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: https://github.com/alge24/ADA-UGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8299
    - null
    - null
    - null
    - null
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
    - 0.829
    - null
    - null
    - null
    - null
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
    arxiv_id: '2202.04139'
    title: Simplified Graph Convolution with Heterophily
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.829
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: MH-Aug (w/ Reg)
    model_plain: MH-Aug (w/ Reg)
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
    - 0.828
    - null
    - null
    - null
    - null
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
    arxiv_id: '2309.13944'
    title: Provable Training for Graph Contrastive Learning
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: https://github.com/VoidHaruhi/POT-GCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.828
    - null
    - null
    - null
    - null
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
    - 0.8271
    - null
    - null
    - null
    - null
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
    - 0.8268
    - null
    - null
    - null
    - null
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
    arxiv_id: '2305.06142'
    title: arXiv:2305.06142
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/sajqavril/Feature-Extension-Graph-Neural-Networks.git
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8262
    - null
    - null
    - null
    - null
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
    arxiv_id: '1811.05868'
    title: Pitfalls of Graph Neural Network Evaluation
    date: Nov 2018
    date_iso: 2018-11
    date_display: Nov 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.826
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: GCN-Cheby
    model_plain: GCN-Cheby
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.04139'
    title: Simplified Graph Convolution with Heterophily
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8241
    - null
    - null
    - null
    - null
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
    - 0.824
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: SAGE-mean
    model_plain: SAGE-mean
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
    - 0.824
    - null
    - null
    - null
    - null
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
    arxiv_id: '2506.20362'
    title: Self-Supervised Graph Learning via Spectral Bootstrapping and Laplacian-Based
      Augmentations
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8221
    - null
    - null
    - null
    - null
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
    - 0.8221
    - null
    - null
    - null
    - null
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
    - 0.821
    - null
    - null
    - null
    - null
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
    - 0.821
    - null
    - null
    - null
    - null
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
    - 0.82
    - null
    - null
    - null
    - null
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.819
    - null
    - null
    - null
    - null
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
    arxiv_id: '2406.19258'
    title: Leveraging Contrastive Learning for Enhanced Node Representations in Tokenized
      Graph Transformers
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8186
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0382
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AM-GCN
    model_plain: AM-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.08524'
    title: 'IGNN-Solver: A Graph Neural Solver for Implicit Graph Neural Networks'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/landrarwolf/IGNN-Solver
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
    arxiv_id: '2411.02279'
    title: arXiv:2411.02279
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/huangJC0429/label-utilize-GCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8182
    - null
    - null
    - null
    - null
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
    arxiv_id: '2210.08792'
    title: Unifying Graph Contrastive Learning with Flexible Contextual Scopes
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: https://github.com/zyzisastudyreallyhardguy/UGCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.818
    - null
    - null
    - null
    - null
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
    - 0.8163
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0135
    - null
    - null
    - null
    - null
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
    - 0.8153
    - null
    - null
    - null
    - null
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
    - 0.8134
    - null
    - null
    - null
    - null
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
    - 0.8126
    - null
    - null
    - null
    - null
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
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_iso: '2023-05-27'
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.812
    - null
    - null
    - null
    - null
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
    arxiv_id: '2309.13944'
    title: Provable Training for Graph Contrastive Learning
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: https://github.com/VoidHaruhi/POT-GCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.812
    - null
    - null
    - null
    - null
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
    - 0.8116
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: Although Graph Neural Networks
    model_plain: Although Graph Neural Networks
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.18758'
    title: Task-Equivariant Graph Few-shot Learning
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/sung-won-kim/TEG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8077
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0332
    - null
    - null
    - null
    - null
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
    arxiv_id: '2002.10306'
    title: Adaptive Propagation Graph Convolutional Network
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: https://github.com/spindro/AP-GCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8075
    - null
    - null
    - null
    - null
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
    - 0.804
    - null
    - null
    - null
    - null
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
    - 0.8035
    - null
    - null
    - null
    - null
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
    - 0.803
    - null
    - null
    - null
    - null
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
    - 0.802
    - null
    - null
    - null
    - null
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
    - 0.802
    - null
    - null
    - null
    - null
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
    arxiv_id: '2002.10306'
    title: Adaptive Propagation Graph Convolutional Network
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: https://github.com/spindro/AP-GCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8017
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: SupCon + DisamGCL
    model_plain: SupCon + DisamGCL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08824'
    title: Disambiguated Node Classification with Graph Neural Networks
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/TianxiangZhao/DisambiguatedGNN
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
    - 0.8002
    - null
    - null
    - null
    - null
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
    - 0.799
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: SAGE-maxpool
    model_plain: SAGE-maxpool
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
    - 0.799
    - null
    - null
    - null
    - null
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
    - 0.7987
    - null
    - null
    - null
    - null
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
    - 0.7963
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0252
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGI + DisamGCL
    model_plain: DGI + DisamGCL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08824'
    title: Disambiguated Node Classification with Graph Neural Networks
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/TianxiangZhao/DisambiguatedGNN
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
    arxiv_id: '2403.16358'
    title: 'ChebMixer: Efficient Graph Representation Learning with MLP Mixer'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7955
    - null
    - null
    - null
    - null
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
    arxiv_id: '2410.10241'
    title: Revisiting Graph Autoencoders as Implicit Contrastive Learners
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/EdisonLeeeee/lrGAE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.792
    - null
    - null
    - null
    - null
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
    arxiv_id: '2402.08824'
    title: Disambiguated Node Classification with Graph Neural Networks
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/TianxiangZhao/DisambiguatedGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.788
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: SupCon
    model_plain: SupCon
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08824'
    title: Disambiguated Node Classification with Graph Neural Networks
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/TianxiangZhao/DisambiguatedGNN
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
    arxiv_id: '2002.10306'
    title: Adaptive Propagation Graph Convolutional Network
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: https://github.com/spindro/AP-GCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7862
    - null
    - null
    - null
    - null
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
    - 0.785
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: CE + DisamGCL
    model_plain: CE + DisamGCL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08824'
    title: Disambiguated Node Classification with Graph Neural Networks
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/TianxiangZhao/DisambiguatedGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.783
    - null
    - null
    - null
    - null
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
    arxiv_id: '1811.05868'
    title: Pitfalls of Graph Neural Network Evaluation
    date: Nov 2018
    date_iso: 2018-11
    date_display: Nov 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.78
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.19
    - null
    - null
    - null
    - null
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
    arxiv_id: '2202.04139'
    title: Simplified Graph Convolution with Heterophily
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.778
    - null
    - null
    - null
    - null
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
    - 0.778
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: CE
    model_plain: CE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08824'
    title: Disambiguated Node Classification with Graph Neural Networks
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/TianxiangZhao/DisambiguatedGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.769
    - null
    - null
    - null
    - null
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
    arxiv_id: '2210.08792'
    title: Unifying Graph Contrastive Learning with Flexible Contextual Scopes
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: https://github.com/zyzisastudyreallyhardguy/UGCL
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
    - 0.7633
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: Raw
    model_plain: Raw
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.04139'
    title: Simplified Graph Convolution with Heterophily
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7607
    - null
    - null
    - null
    - null
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
    arxiv_id: '2305.18758'
    title: Task-Equivariant Graph Few-shot Learning
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/sung-won-kim/TEG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7552
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0106
    - null
    - null
    - null
    - null
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
    - 0.75
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.029
    - null
    - null
    - null
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
    arxiv_id: '2210.08792'
    title: Unifying Graph Contrastive Learning with Flexible Contextual Scopes
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: https://github.com/zyzisastudyreallyhardguy/UGCL
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
    arxiv_id: '2210.08792'
    title: Unifying Graph Contrastive Learning with Flexible Contextual Scopes
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: https://github.com/zyzisastudyreallyhardguy/UGCL
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
    - 0.7325
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0426
    - null
    - null
    - null
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
    arxiv_id: '2004.13970'
    title: Directed Graph Convolutional Network
    date: Apr 2020
    date_iso: 2020-04
    date_display: Apr 2020
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
    - 0.7276
    - null
    - null
    - null
    - null
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
    - 0.7229
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: GAE_f
    model_plain: GAE_f
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.10241'
    title: Revisiting Graph Autoencoders as Implicit Contrastive Learners
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/EdisonLeeeee/lrGAE
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
    - 0.708
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.081
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LabelProp
    model_plain: LabelProp
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
    - 0.708
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.081
    - null
    - null
    - null
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
    arxiv_id: '2202.04139'
    title: Simplified Graph Convolution with Heterophily
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7048
    - null
    - null
    - null
    - null
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
    arxiv_id: '2305.18758'
    title: Task-Equivariant Graph Few-shot Learning
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/sung-won-kim/TEG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7042
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0166
    - null
    - null
    - null
    - null
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
    uses_external_data: null
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
    - null
    - null
    - null
    - null
  - model: R-GCN
    model_plain: R-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.10738'
    title: Knowledge Graph Contrastive Learning based on Relation-Symmetrical Structure
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
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
    - null
    - null
    - null
    - null
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
    - 0.6945
    - null
    - null
    - null
    - null
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
    - 0.6878
    - null
    - null
    - null
    - null
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
    arxiv_id: '2208.10010'
    title: 'NOSMOG: Learning Noise-robust and Structure-aware MLPs on Graphs'
    date: Aug 2022
    date_iso: 2022-08
    date_display: Aug 2022
    codebase_url: https://github.com/meettyj/NOSMOG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6762
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0221
    - null
    - null
    - null
    - null
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
    arxiv_id: '1703.06103'
    title: Modeling Relational Data with Graph Convolutional Networks
    date: Mar 2017
    date_iso: 2017-03
    date_display: Mar 2017
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6666
    - null
    - null
    - null
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
    - 0.641
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.057
    - null
    - null
    - null
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
    arxiv_id: '2305.18758'
    title: Task-Equivariant Graph Few-shot Learning
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/sung-won-kim/TEG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6171
    - null
    - null
    - null
    - null
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
    arxiv_id: '2305.18758'
    title: Task-Equivariant Graph Few-shot Learning
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/sung-won-kim/TEG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6139
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: Bloom 1B
    model_plain: Bloom 1B
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.14134'
    title: Exploring the Potential of Large Language Models for Heterophilic Graphs
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5233
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: 7B-to-1B
    model_plain: 7B-to-1B
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.14134'
    title: Exploring the Potential of Large Language Models for Heterophilic Graphs
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5158
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: Vicuna-7B
    model_plain: Vicuna-7B
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.14134'
    title: Exploring the Potential of Large Language Models for Heterophilic Graphs
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5153
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: Bloom 560M
    model_plain: Bloom 560M
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.14134'
    title: Exploring the Potential of Large Language Models for Heterophilic Graphs
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5152
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: 7B-to-560M
    model_plain: 7B-to-560M
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.14134'
    title: Exploring the Potential of Large Language Models for Heterophilic Graphs
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5151
    - null
    - null
    - null
    - null
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
    arxiv_id: '2408.14134'
    title: Exploring the Potential of Large Language Models for Heterophilic Graphs
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4983
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: TAGA
    model_plain: TAGA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.16800'
    title: 'TAGA: Text-Attributed Graph Self-Supervised Learning by Synergizing Graph
      and Text Mutual Transformations'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.498
    - null
    - null
    - null
    - null
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
    arxiv_id: '2408.14134'
    title: Exploring the Potential of Large Language Models for Heterophilic Graphs
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4943
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: TAGA-rw
    model_plain: TAGA-rw
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.16800'
    title: 'TAGA: Text-Attributed Graph Self-Supervised Learning by Synergizing Graph
      and Text Mutual Transformations'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.494
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: OGNN
    model_plain: OGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.14134'
    title: Exploring the Potential of Large Language Models for Heterophilic Graphs
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4779
    - null
    - null
    - null
    - null
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
    arxiv_id: '2408.14134'
    title: Exploring the Potential of Large Language Models for Heterophilic Graphs
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4738
    - null
    - null
    - null
    - null
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
    arxiv_id: '2408.14134'
    title: Exploring the Potential of Large Language Models for Heterophilic Graphs
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4709
    - null
    - null
    - null
    - null
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
    arxiv_id: '2408.14134'
    title: Exploring the Potential of Large Language Models for Heterophilic Graphs
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4663
    - null
    - null
    - null
    - null
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
    arxiv_id: '2305.18758'
    title: Task-Equivariant Graph Few-shot Learning
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/sung-won-kim/TEG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.456
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0716
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: G2P2
    model_plain: G2P2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.16800'
    title: 'TAGA: Text-Attributed Graph Self-Supervised Learning by Synergizing Graph
      and Text Mutual Transformations'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
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
    - 0.449
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.058
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GBK-GNN
    model_plain: GBK-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.14134'
    title: Exploring the Potential of Large Language Models for Heterophilic Graphs
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.449
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: DisamGCL
    model_plain: DisamGCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.14134'
    title: Exploring the Potential of Large Language Models for Heterophilic Graphs
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.439
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
  - model: PLM
    model_plain: PLM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.16800'
    title: 'TAGA: Text-Attributed Graph Self-Supervised Learning by Synergizing Graph
      and Text Mutual Transformations'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.427
    - null
    - null
    - null
    - null
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
    - 0.4256
    - null
    - null
    - null
    - null
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
    - 0.4244
    - null
    - null
    - null
    - null
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
    arxiv_id: '2305.18758'
    title: Task-Equivariant Graph Few-shot Learning
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/sung-won-kim/TEG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4237
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0242
    - null
    - null
    - null
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
    - 0.4219
    - null
    - null
    - null
    - null
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
    - 0.4218
    - null
    - null
    - null
    - null
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
    - 0.4209
    - null
    - null
    - null
    - null
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
    - 0.4206
    - null
    - null
    - null
    - null
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
    - 0.4163
    - null
    - null
    - null
    - null
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
    - 0.4157
    - null
    - null
    - null
    - null
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
    - 0.4148
    - null
    - null
    - null
    - null
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
    - 0.4093
    - null
    - null
    - null
    - null
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
    - 0.4089
    - null
    - null
    - null
    - null
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
    - 0.4074
    - null
    - null
    - null
    - null
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
    - 0.4017
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.1558
    - null
    - null
    - null
    - null
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
    - 0.3953
    - null
    - null
    - null
    - null
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
    arxiv_id: '2408.14134'
    title: Exploring the Potential of Large Language Models for Heterophilic Graphs
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3933
    - null
    - null
    - null
    - null
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
    - 0.3717
    - null
    - null
    - null
    - null
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
    - 0.3549
    - null
    - null
    - null
    - null
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
    arxiv_id: '2408.14134'
    title: Exploring the Potential of Large Language Models for Heterophilic Graphs
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3512
    - null
    - null
    - null
    - null
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
    - 0.3464
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0994
    - null
    - null
    - null
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
    - 0.3345
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.1103
    - null
    - null
    - null
    - null
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
    - 0.3262
    - null
    - null
    - null
    - null
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
    - 0.3226
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0945
    - null
    - null
    - null
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
    - 0.314
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0723
    - null
    - null
    - null
    - null
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
    - 0.3133
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0795
    - null
    - null
    - null
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
    - 0.3036
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0968
    - null
    - null
    - null
    - null
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
    - 0.3007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.1185
    - null
    - null
    - null
    - null
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
    - 0.2946
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.1111
    - null
    - null
    - null
    - null
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
    - 0.283
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0763
    - null
    - null
    - null
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
    - 0.2761
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.095
    - null
    - null
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
    - 0.2707
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0664
    - null
    - null
    - null
    - null
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
    - 0.27
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0683
    - null
    - null
    - null
    - null
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
    - 0.2658
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0873
    - null
    - null
    - null
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
    - 0.2611
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0734
    - null
    - null
    - null
    - null
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
    - 0.2603
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.088
    - null
    - null
    - null
    - null
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
    - 0.2522
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0671
    - null
    - null
    - null
    - null
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
    - 0.2488
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0772
    - null
    - null
    - null
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
    - 0.2431
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0688
    - null
    - null
    - null
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
    - 0.2413
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0664
    - null
    - null
    - null
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
    - 0.2372
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.1019
    - null
    - null
    - null
    - null
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
    arxiv_id: '2405.16800'
    title: 'TAGA: Text-Attributed Graph Self-Supervised Learning by Synergizing Graph
      and Text Mutual Transformations'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.173
    - null
    - null
    - null
    - null
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
    arxiv_id: '2405.16800'
    title: 'TAGA: Text-Attributed Graph Self-Supervised Learning by Synergizing Graph
      and Text Mutual Transformations'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.169
    - null
    - null
    - null
    - null
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
    - 0.1398
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0553
    - null
    - null
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
    arxiv_id: '2405.16800'
    title: 'TAGA: Text-Attributed Graph Self-Supervised Learning by Synergizing Graph
      and Text Mutual Transformations'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.049
    - null
    - null
    - null
    - null
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
    arxiv_id: '2103.05872'
    title: 'Sampling methods for efficient training of graph convolutional networks:
      A survey'
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
    - null
    - null
    - null
    - 0.759
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.008
    - null
    - null
    - null
    - null
    - null
  - model: Parallelized Graph Sampling
    model_plain: Parallelized Graph Sampling
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.05872'
    title: 'Sampling methods for efficient training of graph convolutional networks:
      A survey'
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
    - null
    - null
    - null
    - 0.771
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.001
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAINT-EDGE
    model_plain: GraphSAINT-EDGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.05872'
    title: 'Sampling methods for efficient training of graph convolutional networks:
      A survey'
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
    - null
    - null
    - null
    - 0.807
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.001
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAINT + RWSE
    model_plain: GraphSAINT + RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.05872'
    title: 'Sampling methods for efficient training of graph convolutional networks:
      A survey'
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
    - null
    - null
    - null
    - 0.815
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.001
    - null
    - null
    - null
    - null
    - null
  - model: No Pre-train
    model_plain: No Pre-train
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.15437'
    title: 'GPT-GNN: Generative Pre-Training of Graph Neural Networks'
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/acbull/GPT-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.586
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
    - 0.074
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
    arxiv_id: '2006.15437'
    title: 'GPT-GNN: Generative Pre-Training of Graph Neural Networks'
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/acbull/GPT-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.61
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
    - 0.07
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE (unsp.)
    model_plain: GraphSAGE (unsp.)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.15437'
    title: 'GPT-GNN: Generative Pre-Training of Graph Neural Networks'
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/acbull/GPT-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.597
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
    - 0.065
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Graph Infomax
    model_plain: Graph Infomax
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.15437'
    title: 'GPT-GNN: Generative Pre-Training of Graph Neural Networks'
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/acbull/GPT-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.604
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
    - 0.063
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: The breakthroughs in graph neural networks (Attr)
    model_plain: The breakthroughs in graph neural networks (Attr)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.15437'
    title: 'GPT-GNN: Generative Pre-Training of Graph Neural Networks'
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/acbull/GPT-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.625
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
    - 0.055
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
    arxiv_id: '2010.15421'
    title: Scalable Graph Neural Networks via Bidirectional Propagation
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.915
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
    - 0.0001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LADIES
    model_plain: LADIES
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.15421'
    title: Scalable Graph Neural Networks via Bidirectional Propagation
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.915
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
    - 0.0001
    - null
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
    arxiv_id: '2010.15421'
    title: Scalable Graph Neural Networks via Bidirectional Propagation
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.915
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
    - 0.0001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAINT
    model_plain: GraphSAINT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.15421'
    title: Scalable Graph Neural Networks via Bidirectional Propagation
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.915
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
    - 0.0001
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
    arxiv_id: '2010.15421'
    title: Scalable Graph Neural Networks via Bidirectional Propagation
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.915
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
    - 0.0001
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
    - 0.8738
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
    - null
    - null
    - null
  - model: Node2Vec
    model_plain: Node2Vec
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
    - 0.8788
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
    - null
    - null
    - null
  - model: LINE
    model_plain: LINE
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
    - 0.7635
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
    - null
    - null
    - null
  - model: ANRL
    model_plain: ANRL
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
    - 0.896
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
    - null
    - null
    - null
  - model: MetaPath2Vec
    model_plain: MetaPath2Vec
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
    - 0.8748
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
    - null
    - null
    - null
  - model: PMNE-n
    model_plain: PMNE-n
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
    - 0.8937
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
    - null
    - null
    - null
  - model: PMNE-r
    model_plain: PMNE-r
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
    - 0.7967
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
    - null
    - null
    - null
  - model: PMNE-c
    model_plain: PMNE-c
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
    - 0.8642
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
    - 0.878
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
    - 0.8444
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
    - 0.9136
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
    - null
    - null
    - null
  - model: DGI
    model_plain: DGI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2009.06211'
    title: Implicit Graph Neural Networks
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: https://github.com/SwiftieH/IGNN
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
    - 0.881
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: GCN/GAT
    model_plain: GCN/GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2009.06211'
    title: Implicit Graph Neural Networks
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: https://github.com/SwiftieH/IGNN
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
    - 0.87
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: DeepWalk
    model_plain: DeepWalk
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2009.06211'
    title: Implicit Graph Neural Networks
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: https://github.com/SwiftieH/IGNN
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
    - 0.748
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: mGCN
    model_plain: mGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2009.06211'
    title: Implicit Graph Neural Networks
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: https://github.com/SwiftieH/IGNN
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
    - 0.86
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: HAN
    model_plain: HAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2009.06211'
    title: Implicit Graph Neural Networks
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: https://github.com/SwiftieH/IGNN
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
    - 0.879
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: DMGI
    model_plain: DMGI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2009.06211'
    title: Implicit Graph Neural Networks
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: https://github.com/SwiftieH/IGNN
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
    - 0.898
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: IGNN
    model_plain: IGNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2009.06211'
    title: Implicit Graph Neural Networks
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: https://github.com/SwiftieH/IGNN
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
    - 0.905
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2008.08692'
    title: Enhancing Graph Neural Network-based Fraud Detectors against Camouflaged
      Fraudsters
    date: Aug 2020
    date_iso: 2020-08
    date_display: Aug 2020
    codebase_url: https://github.com/YingtongDou/CARE-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.7444
    - null
    - null
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
    - null
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2008.08692'
    title: Enhancing Graph Neural Network-based Fraud Detectors against Camouflaged
      Fraudsters
    date: Aug 2020
    date_iso: 2020-08
    date_display: Aug 2020
    codebase_url: https://github.com/YingtongDou/CARE-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.7389
    - null
    - null
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
    - null
    - null
    - null
  - model: RGCN
    model_plain: RGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2008.08692'
    title: Enhancing Graph Neural Network-based Fraud Detectors against Camouflaged
      Fraudsters
    date: Aug 2020
    date_iso: 2020-08
    date_display: Aug 2020
    codebase_url: https://github.com/YingtongDou/CARE-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.7512
    - null
    - null
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
    - null
    - null
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2008.08692'
    title: Enhancing Graph Neural Network-based Fraud Detectors against Camouflaged
      Fraudsters
    date: Aug 2020
    date_iso: 2020-08
    date_display: Aug 2020
    codebase_url: https://github.com/YingtongDou/CARE-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.7071
    - null
    - null
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
    - null
    - null
    - null
  - model: GeniePath
    model_plain: GeniePath
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2008.08692'
    title: Enhancing Graph Neural Network-based Fraud Detectors against Camouflaged
      Fraudsters
    date: Aug 2020
    date_iso: 2020-08
    date_display: Aug 2020
    codebase_url: https://github.com/YingtongDou/CARE-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.7156
    - null
    - null
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
    - null
    - null
    - null
  - model: Player2Vec
    model_plain: Player2Vec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2008.08692'
    title: Enhancing Graph Neural Network-based Fraud Detectors against Camouflaged
      Fraudsters
    date: Aug 2020
    date_iso: 2020-08
    date_display: Aug 2020
    codebase_url: https://github.com/YingtongDou/CARE-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.7686
    - null
    - null
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
    - null
    - null
    - null
  - model: SemiGNN
    model_plain: SemiGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2008.08692'
    title: Enhancing Graph Neural Network-based Fraud Detectors against Camouflaged
      Fraudsters
    date: Aug 2020
    date_iso: 2020-08
    date_display: Aug 2020
    codebase_url: https://github.com/YingtongDou/CARE-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.7025
    - null
    - null
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
    - null
    - null
    - null
  - model: GraphConsis
    model_plain: GraphConsis
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2008.08692'
    title: Enhancing Graph Neural Network-based Fraud Detectors against Camouflaged
      Fraudsters
    date: Aug 2020
    date_iso: 2020-08
    date_display: Aug 2020
    codebase_url: https://github.com/YingtongDou/CARE-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.8546
    - null
    - null
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
    - null
    - null
    - null
  - model: CARE-Att
    model_plain: CARE-Att
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2008.08692'
    title: Enhancing Graph Neural Network-based Fraud Detectors against Camouflaged
      Fraudsters
    date: Aug 2020
    date_iso: 2020-08
    date_display: Aug 2020
    codebase_url: https://github.com/YingtongDou/CARE-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.8949
    - null
    - null
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
    - null
    - null
    - null
  - model: CARE-Weight
    model_plain: CARE-Weight
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2008.08692'
    title: Enhancing Graph Neural Network-based Fraud Detectors against Camouflaged
      Fraudsters
    date: Aug 2020
    date_iso: 2020-08
    date_display: Aug 2020
    codebase_url: https://github.com/YingtongDou/CARE-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.8936
    - null
    - null
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
    - null
    - null
    - null
  - model: CARE-Mean
    model_plain: CARE-Mean
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2008.08692'
    title: Enhancing Graph Neural Network-based Fraud Detectors against Camouflaged
      Fraudsters
    date: Aug 2020
    date_iso: 2020-08
    date_display: Aug 2020
    codebase_url: https://github.com/YingtongDou/CARE-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.8935
    - null
    - null
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
    - null
    - null
    - null
  - model: CARE-GNN
    model_plain: CARE-GNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2008.08692'
    title: Enhancing Graph Neural Network-based Fraud Detectors against Camouflaged
      Fraudsters
    date: Aug 2020
    date_iso: 2020-08
    date_display: Aug 2020
    codebase_url: https://github.com/YingtongDou/CARE-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.8954
    - null
    - null
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
    - null
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.00020'
    title: Partitioning Message Passing for Graph Fraud Detection
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: https://github.com/Xtra-Computing/PMP
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.8369
    - null
    - null
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
    - 0.0125
    - null
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
    arxiv_id: '2412.00020'
    title: Partitioning Message Passing for Graph Fraud Detection
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: https://github.com/Xtra-Computing/PMP
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.8102
    - null
    - null
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
    - 0.0179
    - null
    - null
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
    arxiv_id: '2412.00020'
    title: Partitioning Message Passing for Graph Fraud Detection
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: https://github.com/Xtra-Computing/PMP
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.9316
    - null
    - null
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
    - 0.0087
    - null
    - null
    - null
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
    arxiv_id: '2412.00020'
    title: Partitioning Message Passing for Graph Fraud Detection
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: https://github.com/Xtra-Computing/PMP
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.9372
    - null
    - null
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
    - 0.0068
    - null
    - null
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
    arxiv_id: '2412.00020'
    title: Partitioning Message Passing for Graph Fraud Detection
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: https://github.com/Xtra-Computing/PMP
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.95
    - null
    - null
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
    - 0.0081
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CARE-GNN
    model_plain: CARE-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.00020'
    title: Partitioning Message Passing for Graph Fraud Detection
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: https://github.com/Xtra-Computing/PMP
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.9067
    - null
    - null
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
    - 0.0149
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PHC-GNN
    model_plain: PHC-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.00020'
    title: Partitioning Message Passing for Graph Fraud Detection
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: https://github.com/Xtra-Computing/PMP
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.9586
    - null
    - null
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
    - 0.0014
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: H2-FDetector
    model_plain: H2-FDetector
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.00020'
    title: Partitioning Message Passing for Graph Fraud Detection
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: https://github.com/Xtra-Computing/PMP
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.9603
    - null
    - null
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
    - 0.0069
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: BWGNN
    model_plain: BWGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.00020'
    title: Partitioning Message Passing for Graph Fraud Detection
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: https://github.com/Xtra-Computing/PMP
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.9742
    - null
    - null
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
    - 0.0048
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GHRN
    model_plain: GHRN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.00020'
    title: Partitioning Message Passing for Graph Fraud Detection
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: https://github.com/Xtra-Computing/PMP
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.9707
    - null
    - null
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
    - 0.0073
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GDN
    model_plain: GDN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.00020'
    title: Partitioning Message Passing for Graph Fraud Detection
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: https://github.com/Xtra-Computing/PMP
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.9709
    - null
    - null
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
    - 0.0016
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GFD
    model_plain: GFD
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.00020'
    title: Partitioning Message Passing for Graph Fraud Detection
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: https://github.com/Xtra-Computing/PMP
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.9757
    - null
    - null
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
    - 0.0012
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: RawFeatures
    model_plain: RawFeatures
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.14863'
    title: Graph Communal Contrastive Learning
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
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
    - 0.7382
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0001
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
    arxiv_id: '2110.14863'
    title: Graph Communal Contrastive Learning
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
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
    - 0.8438
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0008
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
    arxiv_id: '2110.14863'
    title: Graph Communal Contrastive Learning
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
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
    - 0.8563
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0009
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
    arxiv_id: '2110.14863'
    title: Graph Communal Contrastive Learning
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
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
    - 0.8643
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0056
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
    arxiv_id: '2110.14863'
    title: Graph Communal Contrastive Learning
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
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
    - 0.8742
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0007
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
    arxiv_id: '2110.14863'
    title: Graph Communal Contrastive Learning
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
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
    - 0.8388
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.005
    - null
    - null
    - null
    - null
  - model: HDI
    model_plain: HDI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.14863'
    title: Graph Communal Contrastive Learning
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
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
    - 0.8543
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0013
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
    arxiv_id: '2110.14863'
    title: Graph Communal Contrastive Learning
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
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
    - 0.8518
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0021
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
    arxiv_id: '2110.14863'
    title: Graph Communal Contrastive Learning
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
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
    - 0.8644
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0025
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
    arxiv_id: '2110.14863'
    title: Graph Communal Contrastive Learning
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
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
    - 0.8767
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0049
    - null
    - null
    - null
    - null
  - model: gCooL_c
    model_plain: gCooL_c
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.14863'
    title: Graph Communal Contrastive Learning
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
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
    - 0.8885
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0014
    - null
    - null
    - null
    - null
  - model: gCooL_e
    model_plain: gCooL_e
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.14863'
    title: Graph Communal Contrastive Learning
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
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
    - 0.8874
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.0009
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
    arxiv_id: '2002.01633'
    title: Structural Deep Clustering Network
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
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
    - null
    - null
    - 0.4154
    - null
    - null
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
    - 0.0051
    - null
    - null
  - model: AE
    model_plain: AE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.01633'
    title: Structural Deep Clustering Network
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
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
    - null
    - null
    - 0.4969
    - null
    - null
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
    - 0.0029
    - null
    - null
  - model: DEC
    model_plain: DEC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.01633'
    title: Structural Deep Clustering Network
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
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
    - null
    - null
    - 0.475
    - null
    - null
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
    - 0.0034
    - null
    - null
  - model: IDEC
    model_plain: IDEC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.01633'
    title: Structural Deep Clustering Network
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
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
    - null
    - null
    - 0.5028
    - null
    - null
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
    - 0.0017
    - null
    - null
  - model: GAE
    model_plain: GAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.01633'
    title: Structural Deep Clustering Network
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
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
    - null
    - null
    - 0.2592
    - null
    - null
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
    - 0.0041
    - null
    - null
  - model: VGAE
    model_plain: VGAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.01633'
    title: Structural Deep Clustering Network
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
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
    - null
    - null
    - 0.2551
    - null
    - null
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
    - 0.0022
    - null
    - null
  - model: DAEGC
    model_plain: DAEGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.01633'
    title: Structural Deep Clustering Network
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
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
    - null
    - null
    - 0.3055
    - null
    - null
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
    - 0.0029
    - null
    - null
  - model: SDCN_Q
    model_plain: SDCN_Q
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.01633'
    title: Structural Deep Clustering Network
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
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
    - null
    - null
    - 0.5689
    - null
    - null
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
    - 0.0027
    - null
    - null
  - model: SDCN
    model_plain: SDCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.01633'
    title: Structural Deep Clustering Network
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
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
    - null
    - null
    - 0.5082
    - null
    - null
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
    - 0.0021
    - null
    - null
  - model: BiasMF
    model_plain: BiasMF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2303.07797'
    title: Automated Self-Supervised Learning for Recommendation
    date: Mar 2023
    date_iso: 2023-03
    date_display: Mar 2023
    codebase_url: https://github.com/HKUDS/AutoCF
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
    - null
    - null
    - null
    - null
    - 0.0324
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
    - null
    - null
    - null
  - model: NCF
    model_plain: NCF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2303.07797'
    title: Automated Self-Supervised Learning for Recommendation
    date: Mar 2023
    date_iso: 2023-03
    date_display: Mar 2023
    codebase_url: https://github.com/HKUDS/AutoCF
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
    - null
    - null
    - null
    - null
    - 0.0367
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
    - null
    - null
    - null
  - model: AutoR
    model_plain: AutoR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2303.07797'
    title: Automated Self-Supervised Learning for Recommendation
    date: Mar 2023
    date_iso: 2023-03
    date_display: Mar 2023
    codebase_url: https://github.com/HKUDS/AutoCF
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
    - null
    - null
    - null
    - null
    - 0.0525
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
    - null
    - null
    - null
  - model: PinSage
    model_plain: PinSage
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2303.07797'
    title: Automated Self-Supervised Learning for Recommendation
    date: Mar 2023
    date_iso: 2023-03
    date_display: Mar 2023
    codebase_url: https://github.com/HKUDS/AutoCF
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
    - null
    - null
    - null
    - null
    - 0.0486
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
    - null
    - null
    - null
  - model: STGCN
    model_plain: STGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2303.07797'
    title: Automated Self-Supervised Learning for Recommendation
    date: Mar 2023
    date_iso: 2023-03
    date_display: Mar 2023
    codebase_url: https://github.com/HKUDS/AutoCF
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
    - null
    - null
    - null
    - null
    - 0.0583
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
    - null
    - null
    - null
  - model: GC-MC
    model_plain: GC-MC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2303.07797'
    title: Automated Self-Supervised Learning for Recommendation
    date: Mar 2023
    date_iso: 2023-03
    date_display: Mar 2023
    codebase_url: https://github.com/HKUDS/AutoCF
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
    - null
    - null
    - null
    - null
    - 0.0837
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
    - null
    - null
    - null
  - model: NGCF
    model_plain: NGCF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2303.07797'
    title: Automated Self-Supervised Learning for Recommendation
    date: Mar 2023
    date_iso: 2023-03
    date_display: Mar 2023
    codebase_url: https://github.com/HKUDS/AutoCF
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
    - null
    - null
    - null
    - null
    - 0.0551
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
    - null
    - null
    - null
  - model: GCCF
    model_plain: GCCF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2303.07797'
    title: Automated Self-Supervised Learning for Recommendation
    date: Mar 2023
    date_iso: 2023-03
    date_display: Mar 2023
    codebase_url: https://github.com/HKUDS/AutoCF
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
    - null
    - null
    - null
    - null
    - 0.0772
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
    - null
    - null
    - null
  - model: LightGCN
    model_plain: LightGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2303.07797'
    title: Automated Self-Supervised Learning for Recommendation
    date: Mar 2023
    date_iso: 2023-03
    date_display: Mar 2023
    codebase_url: https://github.com/HKUDS/AutoCF
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
    - null
    - null
    - null
    - null
    - 0.0868
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
    - null
    - null
    - null
  - model: DGCF
    model_plain: DGCF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2303.07797'
    title: Automated Self-Supervised Learning for Recommendation
    date: Mar 2023
    date_iso: 2023-03
    date_display: Mar 2023
    codebase_url: https://github.com/HKUDS/AutoCF
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
    - null
    - null
    - null
    - null
    - 0.0617
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
    - null
    - null
    - null
  - model: SLRec
    model_plain: SLRec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2303.07797'
    title: Automated Self-Supervised Learning for Recommendation
    date: Mar 2023
    date_iso: 2023-03
    date_display: Mar 2023
    codebase_url: https://github.com/HKUDS/AutoCF
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
    - null
    - null
    - null
    - null
    - 0.0742
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
    - null
    - null
    - null
  - model: NCL
    model_plain: NCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2303.07797'
    title: Automated Self-Supervised Learning for Recommendation
    date: Mar 2023
    date_iso: 2023-03
    date_display: Mar 2023
    codebase_url: https://github.com/HKUDS/AutoCF
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
    - null
    - null
    - null
    - null
    - 0.0955
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
    - null
    - null
    - null
  - model: SGL
    model_plain: SGL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2303.07797'
    title: Automated Self-Supervised Learning for Recommendation
    date: Mar 2023
    date_iso: 2023-03
    date_display: Mar 2023
    codebase_url: https://github.com/HKUDS/AutoCF
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
    - null
    - null
    - null
    - null
    - 0.0874
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
    - null
    - null
    - null
  - model: HCCF
    model_plain: HCCF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2303.07797'
    title: Automated Self-Supervised Learning for Recommendation
    date: Mar 2023
    date_iso: 2023-03
    date_display: Mar 2023
    codebase_url: https://github.com/HKUDS/AutoCF
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
    - null
    - null
    - null
    - null
    - 0.0885
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
    - null
    - null
    - null
  - model: AutoCF
    model_plain: AutoCF
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2303.07797'
    title: Automated Self-Supervised Learning for Recommendation
    date: Mar 2023
    date_iso: 2023-03
    date_display: Mar 2023
    codebase_url: https://github.com/HKUDS/AutoCF
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
    - null
    - null
    - null
    - null
    - 0.1277
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
    - null
    - null
    - null
  - model: DGCNN
    model_plain: DGCNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.16716'
    title: 'GraphPro: Graph Pre-training and Prompt Learning for Recommendation'
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: https://github.com/HKUDS/GraphPro
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
    - null
    - null
    - null
    - 0.0158
    - null
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
    - null
    - null
    - null
  - model: GraphPrompt (LightGCN+)
    model_plain: GraphPrompt (LightGCN+)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.16716'
    title: 'GraphPro: Graph Pre-training and Prompt Learning for Recommendation'
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: https://github.com/HKUDS/GraphPro
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
    - null
    - null
    - null
    - 0.0191
    - null
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
    - null
    - null
    - null
  - model: GPF (LightGCN+)
    model_plain: GPF (LightGCN+)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.16716'
    title: 'GraphPro: Graph Pre-training and Prompt Learning for Recommendation'
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: https://github.com/HKUDS/GraphPro
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
    - null
    - null
    - null
    - 0.0174
    - null
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
    - null
    - null
    - null
  - model: EvolveGCN-H (LightGCN+)
    model_plain: EvolveGCN-H (LightGCN+)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.16716'
    title: 'GraphPro: Graph Pre-training and Prompt Learning for Recommendation'
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: https://github.com/HKUDS/GraphPro
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
    - null
    - null
    - null
    - 0.0157
    - null
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
    - null
    - null
    - null
  - model: ROLAND (LightGCN+)
    model_plain: ROLAND (LightGCN+)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.16716'
    title: 'GraphPro: Graph Pre-training and Prompt Learning for Recommendation'
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: https://github.com/HKUDS/GraphPro
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
    - null
    - null
    - null
    - 0.015
    - null
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
    - null
    - null
    - null
  - model: GraphPrompt (SGL+)
    model_plain: GraphPrompt (SGL+)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.16716'
    title: 'GraphPro: Graph Pre-training and Prompt Learning for Recommendation'
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: https://github.com/HKUDS/GraphPro
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
    - null
    - null
    - null
    - 0.0139
    - null
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
    - null
    - null
    - null
  - model: GPF (SGL+)
    model_plain: GPF (SGL+)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.16716'
    title: 'GraphPro: Graph Pre-training and Prompt Learning for Recommendation'
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: https://github.com/HKUDS/GraphPro
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
    - null
    - null
    - null
    - 0.0187
    - null
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
    - null
    - null
    - null
  - model: EvolveGCN-H (SGL+)
    model_plain: EvolveGCN-H (SGL+)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.16716'
    title: 'GraphPro: Graph Pre-training and Prompt Learning for Recommendation'
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: https://github.com/HKUDS/GraphPro
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
    - null
    - null
    - null
    - 0.0134
    - null
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
    - null
    - null
    - null
  - model: ROLAND (SGL+)
    model_plain: ROLAND (SGL+)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.16716'
    title: 'GraphPro: Graph Pre-training and Prompt Learning for Recommendation'
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: https://github.com/HKUDS/GraphPro
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
    - null
    - null
    - null
    - 0.0161
    - null
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
    - null
    - null
    - null
  - model: GraphPrompt (MixGCF+)
    model_plain: GraphPrompt (MixGCF+)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.16716'
    title: 'GraphPro: Graph Pre-training and Prompt Learning for Recommendation'
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: https://github.com/HKUDS/GraphPro
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
    - null
    - null
    - null
    - 0.0216
    - null
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
    - null
    - null
    - null
  - model: GPF (MixGCF+)
    model_plain: GPF (MixGCF+)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.16716'
    title: 'GraphPro: Graph Pre-training and Prompt Learning for Recommendation'
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: https://github.com/HKUDS/GraphPro
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
    - null
    - null
    - null
    - 0.0182
    - null
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
    - null
    - null
    - null
  - model: EvolveGCN-H (MixGCF+)
    model_plain: EvolveGCN-H (MixGCF+)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.16716'
    title: 'GraphPro: Graph Pre-training and Prompt Learning for Recommendation'
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: https://github.com/HKUDS/GraphPro
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
    - null
    - null
    - null
    - 0.0171
    - null
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
    - null
    - null
    - null
  - model: ROLAND (MixGCF+)
    model_plain: ROLAND (MixGCF+)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.16716'
    title: 'GraphPro: Graph Pre-training and Prompt Learning for Recommendation'
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: https://github.com/HKUDS/GraphPro
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
    - null
    - null
    - null
    - 0.0152
    - null
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
    - null
    - null
    - null
  - model: GPF (SimGCL+)
    model_plain: GPF (SimGCL+)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.16716'
    title: 'GraphPro: Graph Pre-training and Prompt Learning for Recommendation'
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: https://github.com/HKUDS/GraphPro
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
    - null
    - null
    - null
    - 0.0182
    - null
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
    - null
    - null
    - null
  - model: EvolveGCN-O (SimGCL+)
    model_plain: EvolveGCN-O (SimGCL+)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.16716'
    title: 'GraphPro: Graph Pre-training and Prompt Learning for Recommendation'
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: https://github.com/HKUDS/GraphPro
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
    - null
    - null
    - null
    - 0.0168
    - null
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
    - null
    - null
    - null
  - model: ROLAND (SimGCL+)
    model_plain: ROLAND (SimGCL+)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.16716'
    title: 'GraphPro: Graph Pre-training and Prompt Learning for Recommendation'
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: https://github.com/HKUDS/GraphPro
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
    - null
    - null
    - null
    - 0.0151
    - null
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
    - null
    - null
    - null
  - model: GraphPro (SimGCL+)
    model_plain: GraphPro (SimGCL+)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.16716'
    title: 'GraphPro: Graph Pre-training and Prompt Learning for Recommendation'
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: https://github.com/HKUDS/GraphPro
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
    - null
    - null
    - null
    - 0.0205
    - null
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
    - null
    - null
    - null
  - model: MLP
    model_plain: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.11749'
    title: Learning Feature Encoder with Synthetic Anomalies for Weakly Supervised
      Graph Anomaly Detection
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/yj-zhou/SAWGAD
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.903
    - null
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
    - 0.01
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
    arxiv_id: '2605.11749'
    title: Learning Feature Encoder with Synthetic Anomalies for Weakly Supervised
      Graph Anomaly Detection
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/yj-zhou/SAWGAD
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.822
    - null
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
    - 0.0
    - null
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
    arxiv_id: '2605.11749'
    title: Learning Feature Encoder with Synthetic Anomalies for Weakly Supervised
      Graph Anomaly Detection
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/yj-zhou/SAWGAD
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.894
    - null
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
    - 0.01
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
    arxiv_id: '2605.11749'
    title: Learning Feature Encoder with Synthetic Anomalies for Weakly Supervised
      Graph Anomaly Detection
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/yj-zhou/SAWGAD
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.918
    - null
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
    - 0.01
    - null
    - null
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
    arxiv_id: '2605.11749'
    title: Learning Feature Encoder with Synthetic Anomalies for Weakly Supervised
      Graph Anomaly Detection
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/yj-zhou/SAWGAD
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.91
    - null
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
    - 0.01
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PCGNN
    model_plain: PCGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.11749'
    title: Learning Feature Encoder with Synthetic Anomalies for Weakly Supervised
      Graph Anomaly Detection
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/yj-zhou/SAWGAD
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.907
    - null
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
    - 0.01
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: H2FD
    model_plain: H2FD
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.11749'
    title: Learning Feature Encoder with Synthetic Anomalies for Weakly Supervised
      Graph Anomaly Detection
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/yj-zhou/SAWGAD
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.87
    - null
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
    - 0.01
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: BWGNN
    model_plain: BWGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.11749'
    title: Learning Feature Encoder with Synthetic Anomalies for Weakly Supervised
      Graph Anomaly Detection
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/yj-zhou/SAWGAD
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.885
    - null
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
    - 0.02
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GHRN
    model_plain: GHRN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.11749'
    title: Learning Feature Encoder with Synthetic Anomalies for Weakly Supervised
      Graph Anomaly Detection
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/yj-zhou/SAWGAD
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.885
    - null
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
    - 0.02
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ConsisGAD
    model_plain: ConsisGAD
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.11749'
    title: Learning Feature Encoder with Synthetic Anomalies for Weakly Supervised
      Graph Anomaly Detection
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/yj-zhou/SAWGAD
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.952
    - null
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
    - 0.01
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CARE-GNN
    model_plain: CARE-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.11749'
    title: Learning Feature Encoder with Synthetic Anomalies for Weakly Supervised
      Graph Anomaly Detection
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/yj-zhou/SAWGAD
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.899
    - null
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
    - 0.01
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GATSep
    model_plain: GATSep
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.11749'
    title: Learning Feature Encoder with Synthetic Anomalies for Weakly Supervised
      Graph Anomaly Detection
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/yj-zhou/SAWGAD
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.937
    - null
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
    - 0.01
    - null
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
    arxiv_id: '2605.11749'
    title: Learning Feature Encoder with Synthetic Anomalies for Weakly Supervised
      Graph Anomaly Detection
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/yj-zhou/SAWGAD
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.909
    - null
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
    - 0.02
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: weakly supervised graph anomaly detection method
    model_plain: weakly supervised graph anomaly detection method
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.11749'
    title: Learning Feature Encoder with Synthetic Anomalies for Weakly Supervised
      Graph Anomaly Detection
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/yj-zhou/SAWGAD
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - 0.969
    - null
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
    - 0.01
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LightGCN
    model_plain: LightGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.16563'
    title: 'RDGCL: Reaction-Diffusion Graph Contrastive Learning for Recommendation'
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
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
    - null
    - null
    - null
    - null
    - 0.1804
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
    - null
    - null
    - null
  - model: LT-OCF
    model_plain: LT-OCF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.16563'
    title: 'RDGCL: Reaction-Diffusion Graph Contrastive Learning for Recommendation'
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
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
    - null
    - null
    - null
    - null
    - 0.1572
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
    - null
    - null
    - null
  - model: HMLET
    model_plain: HMLET
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.16563'
    title: 'RDGCL: Reaction-Diffusion Graph Contrastive Learning for Recommendation'
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
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
    - null
    - null
    - null
    - null
    - 0.1532
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
    - null
    - null
    - null
  - model: SGL
    model_plain: SGL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.16563'
    title: 'RDGCL: Reaction-Diffusion Graph Contrastive Learning for Recommendation'
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
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
    - null
    - null
    - null
    - null
    - 0.1778
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
    - null
    - null
    - null
  - model: SimGRACE
    model_plain: SimGRACE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.16563'
    title: 'RDGCL: Reaction-Diffusion Graph Contrastive Learning for Recommendation'
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
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
    - null
    - null
    - null
    - null
    - 0.116
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
    - null
    - null
    - null
  - model: GCA
    model_plain: GCA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.16563'
    title: 'RDGCL: Reaction-Diffusion Graph Contrastive Learning for Recommendation'
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
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
    - null
    - null
    - null
    - null
    - 0.151
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
    - null
    - null
    - null
  - model: HCCF
    model_plain: HCCF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.16563'
    title: 'RDGCL: Reaction-Diffusion Graph Contrastive Learning for Recommendation'
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
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
    - null
    - null
    - null
    - null
    - 0.0658
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
    - null
    - null
    - null
  - model: SHT
    model_plain: SHT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.16563'
    title: 'RDGCL: Reaction-Diffusion Graph Contrastive Learning for Recommendation'
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
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
    - null
    - null
    - null
    - null
    - 0.1309
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
    - null
    - null
    - null
  - model: XSimGCL
    model_plain: XSimGCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.16563'
    title: 'RDGCL: Reaction-Diffusion Graph Contrastive Learning for Recommendation'
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
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
    - null
    - null
    - null
    - null
    - 0.143
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
    - null
    - null
    - null
  - model: NCL
    model_plain: NCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.16563'
    title: 'RDGCL: Reaction-Diffusion Graph Contrastive Learning for Recommendation'
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
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
    - null
    - null
    - null
    - null
    - 0.1667
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
    - null
    - null
    - null
  - model: GF-CF
    model_plain: GF-CF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.16563'
    title: 'RDGCL: Reaction-Diffusion Graph Contrastive Learning for Recommendation'
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
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
    - null
    - null
    - null
    - null
    - 0.1394
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
    - null
    - null
    - null
  - model: BSPM
    model_plain: BSPM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.16563'
    title: 'RDGCL: Reaction-Diffusion Graph Contrastive Learning for Recommendation'
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
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
    - null
    - null
    - null
    - null
    - 0.1443
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
    - null
    - null
    - null
  - model: RGCL
    model_plain: RGCL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.16563'
    title: 'RDGCL: Reaction-Diffusion Graph Contrastive Learning for Recommendation'
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.1823
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
    - null
    - null
    - null
  - model: NCF
    model_plain: NCF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.16656'
    title: Graph Augmentation for Recommendation
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: https://github.com/HKUDS/GraphAug
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
    - null
    - null
    - null
    - null
    - 0.1032
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
    - null
    - null
    - null
  - model: AutoR
    model_plain: AutoR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.16656'
    title: Graph Augmentation for Recommendation
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: https://github.com/HKUDS/GraphAug
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
    - null
    - null
    - null
    - null
    - 0.1213
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
    - null
    - null
    - null
  - model: GC-MC
    model_plain: GC-MC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.16656'
    title: Graph Augmentation for Recommendation
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: https://github.com/HKUDS/GraphAug
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
    - null
    - null
    - null
    - null
    - 0.1646
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
    - null
    - null
    - null
  - model: PinSage
    model_plain: PinSage
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.16656'
    title: Graph Augmentation for Recommendation
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: https://github.com/HKUDS/GraphAug
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
    - null
    - null
    - null
    - null
    - 0.0917
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
    - null
    - null
    - null
  - model: NGCF
    model_plain: NGCF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.16656'
    title: Graph Augmentation for Recommendation
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: https://github.com/HKUDS/GraphAug
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
    - null
    - null
    - null
    - null
    - 0.1223
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
    - null
    - null
    - null
  - model: LightGCN
    model_plain: LightGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.16656'
    title: Graph Augmentation for Recommendation
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: https://github.com/HKUDS/GraphAug
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
    - null
    - null
    - null
    - null
    - 0.1775
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
    - null
    - null
    - null
  - model: GCCF
    model_plain: GCCF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.16656'
    title: Graph Augmentation for Recommendation
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: https://github.com/HKUDS/GraphAug
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
    - null
    - null
    - null
    - null
    - 0.1508
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
    - null
    - null
    - null
  - model: DisenGCN
    model_plain: DisenGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.16656'
    title: Graph Augmentation for Recommendation
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: https://github.com/HKUDS/GraphAug
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
    - null
    - null
    - null
    - null
    - 0.1206
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
    - null
    - null
    - null
  - model: DGCF
    model_plain: DGCF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.16656'
    title: Graph Augmentation for Recommendation
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: https://github.com/HKUDS/GraphAug
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
    - null
    - null
    - null
    - null
    - 0.1567
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
    - null
    - null
    - null
  - model: MHCN
    model_plain: MHCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.16656'
    title: Graph Augmentation for Recommendation
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: https://github.com/HKUDS/GraphAug
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
    - null
    - null
    - null
    - null
    - 0.1015
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
    - null
    - null
    - null
  - model: STGCN
    model_plain: STGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.16656'
    title: Graph Augmentation for Recommendation
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: https://github.com/HKUDS/GraphAug
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
    - null
    - null
    - null
    - null
    - 0.1158
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
    - null
    - null
    - null
  - model: SLRec
    model_plain: SLRec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.16656'
    title: Graph Augmentation for Recommendation
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: https://github.com/HKUDS/GraphAug
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
    - null
    - null
    - null
    - null
    - 0.1679
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
    - null
    - null
    - null
  - model: SGL
    model_plain: SGL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.16656'
    title: Graph Augmentation for Recommendation
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: https://github.com/HKUDS/GraphAug
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
    - null
    - null
    - null
    - null
    - 0.1856
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
    - null
    - null
    - null
  - model: DDGCL
    model_plain: DDGCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.16656'
    title: Graph Augmentation for Recommendation
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: https://github.com/HKUDS/GraphAug
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
    - null
    - null
    - null
    - null
    - 0.1675
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
    - null
    - null
    - null
  - model: HCCF
    model_plain: HCCF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.16656'
    title: Graph Augmentation for Recommendation
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: https://github.com/HKUDS/GraphAug
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
    - null
    - null
    - null
    - null
    - 0.1803
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
    - null
    - null
    - null
  - model: CGI
    model_plain: CGI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.16656'
    title: Graph Augmentation for Recommendation
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: https://github.com/HKUDS/GraphAug
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
    - null
    - null
    - null
    - null
    - 0.1819
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
    - null
    - null
    - null
  - model: NCL
    model_plain: NCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.16656'
    title: Graph Augmentation for Recommendation
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: https://github.com/HKUDS/GraphAug
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
    - null
    - null
    - null
    - null
    - 0.1907
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
    - null
    - null
    - null
  - model: GraphAug
    model_plain: GraphAug
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.16656'
    title: Graph Augmentation for Recommendation
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: https://github.com/HKUDS/GraphAug
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
    - null
    - null
    - null
    - null
    - 0.2019
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
    - null
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.12547'
    title: Geometry Contrastive Learning on Heterogeneous Graphs
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.636
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - 0.0095
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
    arxiv_id: '2206.12547'
    title: Geometry Contrastive Learning on Heterogeneous Graphs
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.5193
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - 0.0036
    - null
    - null
    - null
    - null
    - null
    - null
  - model: R-GCN
    model_plain: R-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.12547'
    title: Geometry Contrastive Learning on Heterogeneous Graphs
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.6401
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - 0.012
    - null
    - null
    - null
    - null
    - null
    - null
  - model: mGCN
    model_plain: mGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.12547'
    title: Geometry Contrastive Learning on Heterogeneous Graphs
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.6592
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - 0.0046
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
    arxiv_id: '2206.12547'
    title: Geometry Contrastive Learning on Heterogeneous Graphs
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.5343
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - 0.008
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
    arxiv_id: '2206.12547'
    title: Geometry Contrastive Learning on Heterogeneous Graphs
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.703
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - 0.0075
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
    arxiv_id: '2206.12547'
    title: Geometry Contrastive Learning on Heterogeneous Graphs
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.6631
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - 0.0079
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
    arxiv_id: '2206.12547'
    title: Geometry Contrastive Learning on Heterogeneous Graphs
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.6621
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - 0.0077
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
    arxiv_id: '2206.12547'
    title: Geometry Contrastive Learning on Heterogeneous Graphs
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.4028
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - 0.0141
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
    arxiv_id: '2206.12547'
    title: Geometry Contrastive Learning on Heterogeneous Graphs
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.6707
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - 0.0139
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
    arxiv_id: '2206.12547'
    title: Geometry Contrastive Learning on Heterogeneous Graphs
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.3838
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - 0.0135
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HDGI
    model_plain: HDGI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.12547'
    title: Geometry Contrastive Learning on Heterogeneous Graphs
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.4293
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - 0.0184
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DMGI
    model_plain: DMGI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.12547'
    title: Geometry Contrastive Learning on Heterogeneous Graphs
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.7469
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - 0.0112
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
    arxiv_id: '2206.12547'
    title: Geometry Contrastive Learning on Heterogeneous Graphs
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.765
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - 0.0122
    - null
    - null
    - null
    - null
    - null
    - null
  - model: IHGCL
    model_plain: IHGCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.17234'
    title: Intent-guided Heterogeneous Graph Contrastive Learning for Recommendation
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/wangyu0627/IHGCL
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
    - null
    - null
    - null
    - null
    - 0.167
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
    - null
    - null
    - null
  - model: LightGCN
    model_plain: LightGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.17234'
    title: Intent-guided Heterogeneous Graph Contrastive Learning for Recommendation
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/wangyu0627/IHGCL
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
    - null
    - null
    - null
    - null
    - 0.1574
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
    - null
    - null
    - null
  - model: SGL
    model_plain: SGL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.17234'
    title: Intent-guided Heterogeneous Graph Contrastive Learning for Recommendation
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/wangyu0627/IHGCL
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
    - null
    - null
    - null
    - null
    - 0.1646
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
    - null
    - null
    - null
  - model: XSimGCL
    model_plain: XSimGCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.17234'
    title: Intent-guided Heterogeneous Graph Contrastive Learning for Recommendation
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/wangyu0627/IHGCL
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
    - null
    - null
    - null
    - null
    - 0.1751
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
    - null
    - null
    - null
  - model: DisenHAN
    model_plain: DisenHAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.17234'
    title: Intent-guided Heterogeneous Graph Contrastive Learning for Recommendation
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/wangyu0627/IHGCL
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
    - null
    - null
    - null
    - null
    - 0.1508
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
    - null
    - null
    - null
  - model: DCCF
    model_plain: DCCF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.17234'
    title: Intent-guided Heterogeneous Graph Contrastive Learning for Recommendation
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/wangyu0627/IHGCL
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
    - null
    - null
    - null
    - null
    - 0.1705
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
    - null
    - null
    - null
  - model: BIGCF
    model_plain: BIGCF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.17234'
    title: Intent-guided Heterogeneous Graph Contrastive Learning for Recommendation
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/wangyu0627/IHGCL
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
    - null
    - null
    - null
    - null
    - 0.1758
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
    - null
    - null
    - null
  - model: HERec
    model_plain: HERec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.17234'
    title: Intent-guided Heterogeneous Graph Contrastive Learning for Recommendation
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/wangyu0627/IHGCL
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
    - null
    - null
    - null
    - null
    - 0.142
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
    - null
    - null
    - null
  - model: HAN
    model_plain: HAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.17234'
    title: Intent-guided Heterogeneous Graph Contrastive Learning for Recommendation
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/wangyu0627/IHGCL
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
    - null
    - null
    - null
    - null
    - 0.1385
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
    - null
    - null
    - null
  - model: HeCo
    model_plain: HeCo
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.17234'
    title: Intent-guided Heterogeneous Graph Contrastive Learning for Recommendation
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/wangyu0627/IHGCL
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
    - null
    - null
    - null
    - null
    - 0.1519
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
    - null
    - null
    - null
  - model: SMIN
    model_plain: SMIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.17234'
    title: Intent-guided Heterogeneous Graph Contrastive Learning for Recommendation
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/wangyu0627/IHGCL
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
    - null
    - null
    - null
    - null
    - 0.1569
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
    - null
    - null
    - null
  - model: CHEST
    model_plain: CHEST
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.06722'
    title: Curriculum Pre-Training Heterogeneous Subgraph Transformer for Top-$N$
      Recommendation
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.1765
    - null
    - null
    - null
    - 0.0844
    - null
    - null
    - null
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
    - null
    - null
    - null
  milestones:
  - value: 0.8929
    std: null
    model: R-GCN
    arxiv_id: '1703.06103'
    title: Modeling Relational Data with Graph Convolutional Networks
    date: 2017-03
  - value: 0.901
    std: 0.005
    model: UGCL
    arxiv_id: '2210.08792'
    title: Unifying Graph Contrastive Learning with Flexible Contextual Scopes
    date: 2022-10
  - value: 0.9655
    std: null
    model: COMPGCN-SymCL
    arxiv_id: '2211.10738'
    title: Knowledge Graph Contrastive Learning based on Relation-Symmetrical Structure
    date: 2022-11
  - value: 0.9801
    std: 0.0009
    model: CoE
    arxiv_id: '2505.20853'
    title: arXiv:2505.20853
    date: 2025-05
---

