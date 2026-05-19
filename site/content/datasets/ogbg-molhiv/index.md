---
title: ogbg-molhiv
slug: ogbg-molhiv
benchmark: OGB
task_type: graph_classification
description: 'Binary graph classification on HIV inhibition (molecules). Highly imbalanced
  dataset: only ~3.5% of molecules are active (HIV inhibitors). Evaluated with ROC-AUC
  to account for class imbalance.'
primary_metric: ROC-AUC
higher_is_better: true
pyg_url: https://ogb.stanford.edu/docs/leader_graphprop/#ogbg-molhiv
stats:
  num_graphs: 41127
  avg_nodes: 25.5
  avg_edges: 27.5
  num_classes: 2
result_count: 251
best_model:
  model: MLP
  value: 0.9685
  metric: ROC-AUC
variants:
- slug: standard-split
  name: Standard split
  notes: 'Scaffold split. Metric: ROC-AUC.'
  is_standard: true
  primary_metric: ROC-AUC
  higher_is_better: true
  metrics:
  - ROC-AUC
  - AUROC
  rows:
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
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9685
    - null
    metric_stds:
    - 0.0001
    - null
  - model: GAT
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
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9682
    - null
    metric_stds:
    - 0.0003
    - null
  - model: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.02379'
    title: 'No Metric to Rule Them All: Toward Principled Evaluations of Graph-Learning
      Datasets'
    date: '2025-02-04'
    date_iso: '2025-02-04'
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.968
    - null
    metric_stds:
    - 0.002
    - null
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2502.02379'
    title: 'No Metric to Rule Them All: Toward Principled Evaluations of Graph-Learning
      Datasets'
    date: '2025-02-04'
    date_iso: '2025-02-04'
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.967
    - null
    metric_stds:
    - 0.002
    - null
  - model: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.02379'
    title: 'No Metric to Rule Them All: Toward Principled Evaluations of Graph-Learning
      Datasets'
    date: '2025-02-04'
    date_iso: '2025-02-04'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.962
    - null
    metric_stds:
    - 0.003
    - null
  - model: SigGate-GT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.17324'
    title: 'SigGate-GT: Taming Over-Smoothing in Graph Transformers via Sigmoid-Gated
      Attention'
    date: Apr 2026
    date_iso: 2026-04
    codebase_url: https://github.com/bettyguo/SigGate-GT
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8247
    - null
    metric_stds:
    - 0.0063
    - null
  - model: G1
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.17324'
    title: 'SigGate-GT: Taming Over-Smoothing in Graph Transformers via Sigmoid-Gated
      Attention'
    date: Apr 2026
    date_iso: 2026-04
    codebase_url: https://github.com/bettyguo/SigGate-GT
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8247
    - null
    metric_stds:
    - null
    - null
  - model: Per-head
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.17324'
    title: 'SigGate-GT: Taming Over-Smoothing in Graph Transformers via Sigmoid-Gated
      Attention'
    date: Apr 2026
    date_iso: 2026-04
    codebase_url: https://github.com/bettyguo/SigGate-GT
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8247
    - null
    metric_stds:
    - null
    - null
  - model: HyMN (GatedGCN, T=2)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.03113'
    title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs with Walk-Based
      Centrality'
    date: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8107
    - null
    metric_stds:
    - 0.0021
    - null
  - model: Exphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.17324'
    title: 'SigGate-GT: Taming Over-Smoothing in Graph Transformers via Sigmoid-Gated
      Attention'
    date: Apr 2026
    date_iso: 2026-04
    codebase_url: https://github.com/bettyguo/SigGate-GT
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8075
    - null
    metric_stds:
    - 0.009399999999999999
    - null
  - model: GSAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.12136'
    title: Molecular Topological Profile (MOLTOP) - Simple and Strong Baseline for
      Molecular Graph Classification
    date: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.8067
    - null
    metric_stds:
    - 0.0095
    - null
  - model: CIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.03561'
    title: 'CIN++: Enhancing Topological Message Passing'
    date: Jun 2023
    date_iso: 2023-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8063
    - null
    metric_stds:
    - 0.0094
    - null
  - model: EGT (pre-trained)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09263'
    title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks? Simple Architectures
      Meet Excellence
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.806
    - null
    metric_stds:
    - 0.0065
    - null
  - model: Shared
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.17324'
    title: 'SigGate-GT: Taming Over-Smoothing in Graph Transformers via Sigmoid-Gated
      Attention'
    date: Apr 2026
    date_iso: 2026-04
    codebase_url: https://github.com/bettyguo/SigGate-GT
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8058
    - null
    metric_stds:
    - null
    - null
  - model: Graphormer (pre-trained)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09263'
    title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks? Simple Architectures
      Meet Excellence
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.8051
    - null
    metric_stds:
    - 0.0053
    - null
  - model: Graphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: '2023-06-09'
    date_iso: '2023-06-09'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8051
    - null
    metric_stds:
    - 0.0053
    - null
  - model: MOLTOP
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.12136'
    title: Molecular Topological Profile (MOLTOP) - Simple and Strong Baseline for
      Molecular Graph Classification
    date: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.8042
    - null
    metric_stds:
    - 0.0025
    - null
  - model: P-WL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.12136'
    title: Molecular Topological Profile (MOLTOP) - Simple and Strong Baseline for
      Molecular Graph Classification
    date: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.8039
    - null
    metric_stds:
    - 0.004
    - null
  - model: Directional GSN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.19285'
    title: Facilitating Graph Neural Networks with Random Walk on Simplicial Complexes
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8039
    - null
    metric_stds:
    - 0.009
    - null
  - model: GSN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.04941'
    title: Distance-Restricted Folklore Weisfeiler-Leman GNNs with Provable Cycle
      Counting Power
    date: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8039
    - null
    metric_stds:
    - 0.009
    - null
  - model: HyMN (GIN, T=2)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.03113'
    title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs with Walk-Based
      Centrality'
    date: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8036
    - null
    metric_stds:
    - 0.0123
    - null
  - model: GSSC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09263'
    title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks? Simple Architectures
      Meet Excellence
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8035
    - null
    metric_stds:
    - 0.0142
    - null
  - model: GatedGCN + CSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.03113'
    title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs with Walk-Based
      Centrality'
    date: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8033
    - null
    metric_stds:
    - 0.0056
    - null
  - model: PST
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 1.0
    arxiv_id: '2405.02795'
    title: Graph as Point Set
    date: '2024-05-05'
    date_iso: '2024-05-05'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8032
    - null
    metric_stds:
    - 0.0071
    - null
  - model: CIN (small)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.1
    arxiv_id: '2306.03561'
    title: 'CIN++: Enhancing Topological Message Passing'
    date: Jun 2023
    date_iso: 2023-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8026
    - null
    metric_stds:
    - 0.0102
    - null
  - model: GPS + RandAlign
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.09774'
    title: 'RandAlign: A Parameter-Free Method for Regularizing Graph Convolutional
      Networks'
    date: Apr 2024
    date_iso: 2024-04
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8021
    - null
    metric_stds:
    - 0.0305
    - null
  - model: GPS+Hodge1Lap
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.19285'
    title: Facilitating Graph Neural Networks with Random Walk on Simplicial Complexes
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8021
    - null
    metric_stds:
    - 0.0154
    - null
  - model: G2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.17324'
    title: 'SigGate-GT: Taming Over-Smoothing in Graph Transformers via Sigmoid-Gated
      Attention'
    date: Apr 2026
    date_iso: 2026-04
    codebase_url: https://github.com/bettyguo/SigGate-GT
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8012
    - null
    metric_stds:
    - null
    - null
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2502.09263'
    title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks? Simple Architectures
      Meet Excellence
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8012
    - null
    metric_stds:
    - 0.0124
    - null
  - model: SUN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08450'
    title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via Graph
      Products'
    date: Feb 2024
    date_iso: 2024-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8003
    - null
    metric_stds:
    - 0.0055
    - null
  - model: SUN (EGO)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.04941'
    title: Distance-Restricted Folklore Weisfeiler-Leman GNNs with Provable Cycle
      Counting Power
    date: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8003
    - null
    metric_stds:
    - 0.0055
    - null
  - model: GINE-MLP-Mixer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.03113'
    title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs with Walk-Based
      Centrality'
    date: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7997
    - null
    metric_stds:
    - 0.0102
    - null
  - model: G-MLPMixer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.02795'
    title: Graph as Point Set
    date: '2024-05-05'
    date_iso: '2024-05-05'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7997
    - null
    metric_stds:
    - 0.0102
    - null
  - model: Graph MLP-Mixer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.17311'
    title: Probabilistic Graph Rewiring via Virtual Nodes
    date: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.799
    - null
    metric_stds:
    - 0.01
    - null
  - model: A_2^Ngbh
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.03380'
    title: On the Theoretical Expressive Power and the Design Space of Higher-Order
      Graph Transformers
    date: '2024-04-04'
    date_iso: '2024-04-04'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7981
    - null
    metric_stds:
    - 0.0097
    - null
  - model: AS_0:1^SN+VS
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.03380'
    title: On the Theoretical Expressive Power and the Design Space of Higher-Order
      Graph Transformers
    date: '2024-04-04'
    date_iso: '2024-04-04'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7981
    - null
    metric_stds:
    - 0.0114
    - null
  - model: GECO
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09263'
    title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks? Simple Architectures
      Meet Excellence
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.798
    - null
    metric_stds:
    - 0.02
    - null
  - model: DGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.03561'
    title: 'CIN++: Enhancing Topological Message Passing'
    date: Jun 2023
    date_iso: 2023-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.797
    - null
    metric_stds:
    - 0.0097
    - null
  - model: HyMN (GIN, T=2) no CSE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.03113'
    title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs with Walk-Based
      Centrality'
    date: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7962
    - null
    metric_stds:
    - 0.0114
    - null
  - model: GNN (a)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08450'
    title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via Graph
      Products'
    date: Feb 2024
    date_iso: 2024-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7961
    - null
    metric_stds:
    - 0.0119
    - null
  - model: GIN-AK+
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.19285'
    title: Facilitating Graph Neural Networks with Random Walk on Simplicial Complexes
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7961
    - null
    metric_stds:
    - 0.011
    - null
  - model: GNNAK+
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.04941'
    title: Distance-Restricted Folklore Weisfeiler-Leman GNNs with Provable Cycle
      Counting Power
    date: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7961
    - null
    metric_stds:
    - 0.0119
    - null
  - model: SSWL+
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.02795'
    title: Graph as Point Set
    date: '2024-05-05'
    date_iso: '2024-05-05'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7958
    - null
    metric_stds:
    - 0.0035
    - null
  - model: GNN-SSWL+
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08450'
    title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via Graph
      Products'
    date: Feb 2024
    date_iso: 2024-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7958
    - null
    metric_stds:
    - 0.0035
    - null
  - model: PR-MPNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.17311'
    title: Probabilistic Graph Rewiring via Virtual Nodes
    date: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.795
    - null
    metric_stds:
    - 0.009
    - null
  - model: PR-MPNN_Sim
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.02156'
    title: Probabilistically Rewired Message-Passing Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.795
    - null
    metric_stds:
    - 0.009
    - null
  - model: Subgraphormer
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08450'
    title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via Graph
      Products'
    date: Feb 2024
    date_iso: 2024-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7948
    - null
    metric_stds:
    - 0.0128
    - null
  - model: Original Graph
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.22100'
    title: 'SHAKE-GNN: Scalable Hierarchical Kirchhoff-Forest Graph Neural Network'
    date: Sep 2025
    date_iso: 2025-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.794
    - null
    metric_stds:
    - null
    - null
  - model: EGP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.07966'
    title: Higher-Order Expander Graph Propagation
    date: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7934
    - null
    metric_stds:
    - 0.0035
    - null
  - model: BiScale-GTR (Molecule)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.06336'
    title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale Molecular
      Representation Learning'
    date: Apr 2026
    date_iso: 2026-04
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.792
    - null
    metric_stds:
    - 0.006
    - null
  - model: PathNN-SP (K=2)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: '2023-06-09'
    date_iso: '2023-06-09'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7917
    - null
    metric_stds:
    - 0.0109
    - null
  - model: GatedGCN+PE+VN_G
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13526'
    title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    date: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.791
    - null
    metric_stds:
    - 0.0086
    - null
  - model: CS-GNN (T = 2)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.03113'
    title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs with Walk-Based
      Centrality'
    date: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7909
    - null
    metric_stds:
    - 0.009
    - null
  - model: PNA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.03561'
    title: 'CIN++: Enhancing Topological Message Passing'
    date: Jun 2023
    date_iso: 2023-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7905
    - null
    metric_stds:
    - 0.0132
    - null
  - model: HyMN (GatedGCN, T=2) w/out CSE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.03113'
    title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs with Walk-Based
      Centrality'
    date: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7902
    - null
    metric_stds:
    - 0.0091
    - null
  - model: A_2^LN+VT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.03380'
    title: On the Theoretical Expressive Power and the Design Space of Higher-Order
      Graph Transformers
    date: '2024-04-04'
    date_iso: '2024-04-04'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7901
    - null
    metric_stds:
    - 0.0082
    - null
  - model: GCN (Ric_F)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.11390'
    title: A Remedy for Over-Squashing in Graph Learning via Forman‐Ricci Curvature
      based Graph-to-Hypergraph Structural Lifting
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.79
    - null
    metric_stds:
    - 0.13
    - null
  - model: AST (Ric_F)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.11390'
    title: A Remedy for Over-Squashing in Graph Learning via Forman‐Ricci Curvature
      based Graph-to-Hypergraph Structural Lifting
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.79
    - null
    metric_stds:
    - 0.19
    - null
  - model: GIN + CGP
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.03424'
    title: Cayley Graph Propagation
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7899
    - null
    metric_stds:
    - 0.009
    - null
  - model: GPS+EdgeRWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.19285'
    title: Facilitating Graph Neural Networks with Random Walk on Simplicial Complexes
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7891
    - null
    metric_stds:
    - 0.0118
    - null
  - model: SpecFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.19285'
    title: Facilitating Graph Neural Networks with Random Walk on Simplicial Complexes
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7889
    - null
    metric_stds:
    - 0.0124
    - null
  - model: PathNN-AP (K=2)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: '2023-06-09'
    date_iso: '2023-06-09'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7884
    - null
    metric_stds:
    - 0.0146
    - null
  - model: IPR-MPNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.17311'
    title: Probabilistic Graph Rewiring via Virtual Nodes
    date: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.788
    - null
    metric_stds:
    - 0.006
    - null
  - model: GraphGPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09263'
    title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks? Simple Architectures
      Meet Excellence
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.788
    - null
    metric_stds:
    - 0.0101
    - null
  - model: WIRE Performer
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
    - 0.788
    - null
    metric_stds:
    - 0.001
    - null
  - model: Softmax transformer
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
    - 0.788
    - null
    metric_stds:
    - 0.001
    - null
  - model: GPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.02156'
    title: Probabilistically Rewired Message-Passing Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.788
    - null
    metric_stds:
    - 0.01
    - null
  - model: HIMP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.03561'
    title: 'CIN++: Enhancing Topological Message Passing'
    date: Jun 2023
    date_iso: 2023-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.788
    - null
    metric_stds:
    - 0.0082
    - null
  - model: GraphGPS baseline
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.17324'
    title: 'SigGate-GT: Taming Over-Smoothing in Graph Transformers via Sigmoid-Gated
      Attention'
    date: Apr 2026
    date_iso: 2026-04
    codebase_url: https://github.com/bettyguo/SigGate-GT
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7879999999999999
    - null
    metric_stds:
    - null
    - null
  - model: Coarsened Graph
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.22100'
    title: 'SHAKE-GNN: Scalable Hierarchical Kirchhoff-Forest Graph Neural Network'
    date: Sep 2025
    date_iso: 2025-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.787
    - null
    metric_stds:
    - null
    - null
  - model: I$^2$GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.04941'
    title: Distance-Restricted Folklore Weisfeiler-Leman GNNs with Provable Cycle
      Counting Power
    date: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7868
    - null
    metric_stds:
    - 0.0093
    - null
  - model: SEM-IL (GCN)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.18777'
    title: Improving Compositional Generalization using - Iterated Learning and Simplicial
      Embeddings
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7861
    - null
    metric_stds:
    - 0.0073
    - null
  - model: DeeperGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.09774'
    title: 'RandAlign: A Parameter-Free Method for Regularizing Graph Convolutional
      Networks'
    date: Apr 2024
    date_iso: 2024-04
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7858
    - null
    metric_stds:
    - 0.0117
    - null
  - model: GraphCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.785
    - null
    metric_stds:
    - 0.012
    - null
  - model: POLICY-LEARN (T = 2)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.03113'
    title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs with Walk-Based
      Centrality'
    date: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7849
    - null
    metric_stds:
    - 0.0101
    - null
  - model: k=3 Ramanujan Expander
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.07966'
    title: Higher-Order Expander Graph Propagation
    date: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7848
    - null
    metric_stds:
    - 0.0135
    - null
  - model: GWNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: '2023-06-09'
    date_iso: '2023-06-09'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7838
    - null
    metric_stds:
    - 0.0099
    - null
  - model: GRIT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09263'
    title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks? Simple Architectures
      Meet Excellence
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7835
    - null
    metric_stds:
    - 0.0054
    - null
  - model: Exphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09263'
    title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks? Simple Architectures
      Meet Excellence
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7834
    - null
    metric_stds:
    - 0.0044
    - null
  - model: NGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08450'
    title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via Graph
      Products'
    date: Feb 2024
    date_iso: 2024-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7834
    - null
    metric_stds:
    - 0.0186
    - null
  - model: Nested-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.04941'
    title: Distance-Restricted Folklore Weisfeiler-Leman GNNs with Provable Cycle
      Counting Power
    date: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7834
    - null
    metric_stds:
    - 0.0186
    - null
  - model: AgentNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: '2023-06-09'
    date_iso: '2023-06-09'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7833
    - null
    metric_stds:
    - 0.0069
    - null
  - model: GatedGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    arxiv_id: '2405.13526'
    title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    date: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7827
    - null
    metric_stds:
    - 0.0111
    - null
  - model: SEM-only (GCN)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.18777'
    title: Improving Compositional Generalization using - Iterated Learning and Simplicial
      Embeddings
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7821
    - null
    metric_stds:
    - 0.0078
    - null
  - model: Mole-BERT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.06336'
    title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale Molecular
      Representation Learning'
    date: Apr 2026
    date_iso: 2026-04
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.782
    - null
    metric_stds:
    - 0.008
    - null
  - model: DRFWL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    arxiv_id: '2405.02795'
    title: Graph as Point Set
    date: '2024-05-05'
    date_iso: '2024-05-05'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7818
    - null
    metric_stds:
    - 0.0219
    - null
  - model: d-DRFWL(2) GNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.04941'
    title: Distance-Restricted Folklore Weisfeiler-Leman GNNs with Provable Cycle
      Counting Power
    date: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7818
    - null
    metric_stds:
    - 0.0219
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.78
    - null
    metric_stds:
    - 0.01
    - null
  - model: SimSGT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.06336'
    title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale Molecular
      Representation Learning'
    date: Apr 2026
    date_iso: 2026-04
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.78
    - null
    metric_stds:
    - 0.019
    - null
  - model: AST
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.11390'
    title: A Remedy for Over-Squashing in Graph Learning via Forman‐Ricci Curvature
      based Graph-to-Hypergraph Structural Lifting
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.78
    - null
    metric_stds:
    - 0.2
    - null
  - model: UniGNN2
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.11390'
    title: A Remedy for Over-Squashing in Graph Learning via Forman‐Ricci Curvature
      based Graph-to-Hypergraph Structural Lifting
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.78
    - null
    metric_stds:
    - 0.15
    - null
  - model: EDGNN (Ric_F)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.11390'
    title: A Remedy for Over-Squashing in Graph Learning via Forman‐Ricci Curvature
      based Graph-to-Hypergraph Structural Lifting
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.78
    - null
    metric_stds:
    - 0.16
    - null
  - model: UniGNN2 (Ric_F)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.11390'
    title: A Remedy for Over-Squashing in Graph Learning via Forman‐Ricci Curvature
      based Graph-to-Hypergraph Structural Lifting
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.78
    - null
    metric_stds:
    - 0.16
    - null
  - model: GraphFP_CP
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.78
    - null
    metric_stds:
    - 0.015
    - null
  - model: ESAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: '2023-06-09'
    date_iso: '2023-06-09'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.78
    - null
    metric_stds:
    - 0.0142
    - null
  - model: ExpC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.09774'
    title: 'RandAlign: A Parameter-Free Method for Regularizing Graph Convolutional
      Networks'
    date: Apr 2024
    date_iso: 2024-04
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7799
    - null
    metric_stds:
    - 0.0082
    - null
  - model: GSN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.03561'
    title: 'CIN++: Enhancing Topological Message Passing'
    date: Jun 2023
    date_iso: 2023-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7799
    - null
    metric_stds:
    - 0.01
    - null
  - model: G3
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.17324'
    title: 'SigGate-GT: Taming Over-Smoothing in Graph Transformers via Sigmoid-Gated
      Attention'
    date: Apr 2026
    date_iso: 2026-04
    codebase_url: https://github.com/bettyguo/SigGate-GT
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7795000000000001
    - null
    metric_stds:
    - null
    - null
  - model: GCN + CGP
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.03424'
    title: Cayley Graph Propagation
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7794
    - null
    metric_stds:
    - 0.0122
    - null
  - model: GINE-ViT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.03113'
    title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs with Walk-Based
      Centrality'
    date: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7792
    - null
    metric_stds:
    - 0.0142
    - null
  - model: Graph ViT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.17311'
    title: Probabilistic Graph Rewiring via Virtual Nodes
    date: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.779
    - null
    metric_stds:
    - 0.015
    - null
  - model: BiScale-GTR (Fragment)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.06336'
    title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale Molecular
      Representation Learning'
    date: Apr 2026
    date_iso: 2026-04
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.779
    - null
    metric_stds:
    - 0.011
    - null
  - model: SAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.19285'
    title: Facilitating Graph Neural Networks with Random Walk on Simplicial Complexes
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.7785
    - null
    metric_stds:
    - 0.247
    - null
  - model: GraphGPS+LAC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.06336'
    title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale Molecular
      Representation Learning'
    date: Apr 2026
    date_iso: 2026-04
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.776
    - null
    metric_stds:
    - null
    - null
  - model: JOAOv2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.775
    - null
    metric_stds:
    - 0.012
    - null
  - model: Base
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.02156'
    title: Probabilistically Rewired Message-Passing Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.775
    - null
    metric_stds:
    - 0.011
    - null
  - model: GIN+CSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.03113'
    title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs with Walk-Based
      Centrality'
    date: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7744
    - null
    metric_stds:
    - 0.0187
    - null
  - model: PR-MPNN_Imle
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.02156'
    title: Probabilistically Rewired Message-Passing Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.774
    - null
    metric_stds:
    - 0.015
    - null
  - model: EGP (GCN)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.03424'
    title: Cayley Graph Propagation
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7731
    - null
    metric_stds:
    - 0.0081
    - null
  - model: RANDOM (T = 2)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.03113'
    title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs with Walk-Based
      Centrality'
    date: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.773
    - null
    metric_stds:
    - 0.0256
    - null
  - model: ContextPred
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.773
    - null
    metric_stds:
    - 0.01
    - null
  - model: AttrMasking
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.772
    - null
    metric_stds:
    - 0.011
    - null
  - model: Deep LRP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.04941'
    title: Distance-Restricted Folklore Weisfeiler-Leman GNNs with Provable Cycle
      Counting Power
    date: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7719
    - null
    metric_stds:
    - 0.014
    - null
  - model: GIN + FA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.03424'
    title: Cayley Graph Propagation
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7718
    - null
    metric_stds:
    - 0.0147
    - null
  - model: MAG-GNN (T = 2)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.03113'
    title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs with Walk-Based
      Centrality'
    date: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7712
    - null
    metric_stds:
    - 0.0113
    - null
  - model: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.771
    - null
    metric_stds:
    - 0.011
    - null
  - model: E-SPN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: '2023-06-09'
    date_iso: '2023-06-09'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.771
    - null
    metric_stds:
    - 0.012
    - null
  - model: GINE + VN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13526'
    title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    date: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7707
    - null
    metric_stds:
    - 0.0149
    - null
  - model: GCN + virtual node
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.19285'
    title: Facilitating Graph Neural Networks with Random Walk on Simplicial Complexes
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7707
    - null
    metric_stds:
    - 0.0149
    - null
  - model: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.03561'
    title: 'CIN++: Enhancing Topological Message Passing'
    date: Jun 2023
    date_iso: 2023-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7707
    - null
    metric_stds:
    - 0.0149
    - null
  - model: Baseline (GINE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.18777'
    title: Improving Compositional Generalization using - Iterated Learning and Simplicial
      Embeddings
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7701
    - null
    metric_stds:
    - 0.0094
    - null
  - model: MORE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.06336'
    title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale Molecular
      Representation Learning'
    date: Apr 2026
    date_iso: 2026-04
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.77
    - null
    metric_stds:
    - 0.007
    - null
  - model: GAT (Ric_F)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.11390'
    title: A Remedy for Over-Squashing in Graph Learning via Forman‐Ricci Curvature
      based Graph-to-Hypergraph Structural Lifting
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.77
    - null
    metric_stds:
    - 0.17
    - null
  - model: GraphMAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.06336'
    title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale Molecular
      Representation Learning'
    date: Apr 2026
    date_iso: 2026-04
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.768
    - null
    metric_stds:
    - 0.006
    - null
  - model: GCN+PE+VN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13526'
    title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    date: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7678
    - null
    metric_stds:
    - 0.0111
    - null
  - model: DSS-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08450'
    title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via Graph
      Products'
    date: Feb 2024
    date_iso: 2024-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7678
    - null
    metric_stds:
    - 0.0166
    - null
  - model: GatedGCN + VN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13526'
    title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    date: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7676
    - null
    metric_stds:
    - 0.0172
    - null
  - model: JOAO
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.767
    - null
    metric_stds:
    - 0.012
    - null
  - model: GraphFP
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.767
    - null
    metric_stds:
    - 0.01
    - null
  - model: CP, alpha=0.1
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.767
    - null
    metric_stds:
    - 0.013
    - null
  - model: Full
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.03113'
    title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs with Walk-Based
      Centrality'
    date: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7654
    - null
    metric_stds:
    - 0.0137
    - null
  - model: GCN+FLAG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: '2023-06-09'
    date_iso: '2023-06-09'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7654
    - null
    metric_stds:
    - 0.0114
    - null
  - model: GatedGCN with PairNorm
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13526'
    title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    date: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7645
    - null
    metric_stds:
    - 0.0128
    - null
  - model: GINE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.505
    arxiv_id: '2405.17311'
    title: Probabilistic Graph Rewiring via Virtual Nodes
    date: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.764
    - null
    metric_stds:
    - 0.01
    - null
  - model: Base w. PE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.02156'
    title: Probabilistically Rewired Message-Passing Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.764
    - null
    metric_stds:
    - 0.018
    - null
  - model: Reconstr. GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.03113'
    title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs with Walk-Based
      Centrality'
    date: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7632
    - null
    metric_stds:
    - 0.014
    - null
  - model: Recon. GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08450'
    title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via Graph
      Products'
    date: Feb 2024
    date_iso: 2024-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7632
    - null
    metric_stds:
    - 0.014
    - null
  - model: G-Contextual
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.763
    - null
    metric_stds:
    - 0.015
    - null
  - model: FAGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.03424'
    title: Cayley Graph Propagation
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7628
    - null
    metric_stds:
    - 0.0191
    - null
  - model: GIN + PM_at (Summation-MLP)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.07966'
    title: Higher-Order Expander Graph Propagation
    date: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7614
    - null
    metric_stds:
    - 0.0056
    - null
  - model: GCN + Master Node
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.03424'
    title: Cayley Graph Propagation
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7608
    - null
    metric_stds:
    - 0.0134
    - null
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2306.03561'
    title: 'CIN++: Enhancing Topological Message Passing'
    date: Jun 2023
    date_iso: 2023-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7606
    - null
    metric_stds:
    - 0.0097
    - null
  - model: TopK
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.09821'
    title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    date: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.76
    - null
    metric_stds:
    - 0.01
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.76
    - null
    metric_stds:
    - 0.01
    - null
  - model: EGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.11390'
    title: A Remedy for Over-Squashing in Graph Learning via Forman‐Ricci Curvature
      based Graph-to-Hypergraph Structural Lifting
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.76
    - null
    metric_stds:
    - 0.17
    - null
  - model: PR-MPNN_Gmb
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.02156'
    title: Probabilistically Rewired Message-Passing Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.76
    - null
    metric_stds:
    - 0.025
    - null
  - model: GCN + VN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13526'
    title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    date: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7599
    - null
    metric_stds:
    - 0.0119
    - null
  - model: GatedGCN + mean
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13526'
    title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    date: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7594
    - null
    metric_stds:
    - 0.0096
    - null
  - model: MGSSL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.757
    - null
    metric_stds:
    - 0.013
    - null
  - model: Plain GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.07966'
    title: Higher-Order Expander Graph Propagation
    date: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7558
    - null
    metric_stds:
    - 0.014
    - null
  - model: GIN + PM (Summation)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.07966'
    title: Higher-Order Expander Graph Propagation
    date: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7538
    - null
    metric_stds:
    - 0.015
    - null
  - model: EGP (GIN)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.03424'
    title: Cayley Graph Propagation
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7537
    - null
    metric_stds:
    - 0.0076
    - null
  - model: RWPT (Walk, k=16, l=2)
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7524
    - null
    metric_stds:
    - null
    - null
  - model: GIN + PM_sp (Summation-MLP)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.07966'
    title: Higher-Order Expander Graph Propagation
    date: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7524
    - null
    metric_stds:
    - 0.0206
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7515
    - null
    metric_stds:
    - 0.0239
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7515
    - null
    metric_stds:
    - null
    - null
  - model: RWPT (Walk, k=4, l=4)
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7514
    - null
    metric_stds:
    - null
    - null
  - model: GIN + RM (Learn-Features)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.07966'
    title: Higher-Order Expander Graph Propagation
    date: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7511
    - null
    metric_stds:
    - 0.0133
    - null
  - model: GIN_C (Vocab 200)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.751
    - null
    metric_stds:
    - 0.013
    - null
  - model: GIN + PM (Learnt)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.07966'
    title: Higher-Order Expander Graph Propagation
    date: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7503
    - null
    metric_stds:
    - 0.0201
    - null
  - model: SEP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.09821'
    title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    date: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.75
    - null
    metric_stds:
    - 0.0
    - null
  - model: PSDS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.02795'
    title: Graph as Point Set
    date: '2024-05-05'
    date_iso: '2024-05-05'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7492
    - null
    metric_stds:
    - 0.0118
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7485
    - null
    metric_stds:
    - null
    - null
  - model: GraphMVP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.748
    - null
    metric_stds:
    - 0.014
    - null
  - model: GIN + RM (Masking)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.07966'
    title: Higher-Order Expander Graph Propagation
    date: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7439
    - null
    metric_stds:
    - 0.0219
    - null
  - model: RWPT (Pre-Train w/ three)
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7403
    - null
    metric_stds:
    - null
    - null
  - model: --
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.09821'
    title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    date: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.74
    - null
    metric_stds:
    - 0.02
    - null
  - model: Graclus
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.09821'
    title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    date: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.74
    - null
    metric_stds:
    - 0.03
    - null
  - model: ECPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.09821'
    title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    date: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.74
    - null
    metric_stds:
    - 0.01
    - null
  - model: KMIS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.09821'
    title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    date: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.74
    - null
    metric_stds:
    - 0.02
    - null
  - model: EigenPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.09821'
    title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    date: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.74
    - null
    metric_stds:
    - 0.02
    - null
  - model: HOSC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.09821'
    title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    date: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.74
    - null
    metric_stds:
    - 0.02
    - null
  - model: G-Motif
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.738
    - null
    metric_stds:
    - 0.012
    - null
  - model: GraphLoG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.737
    - null
    metric_stds:
    - 0.009
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7357
    - null
    metric_stds:
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7346
    - null
    metric_stds:
    - null
    - null
  - model: RWPT (Full attn. mask)
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7342
    - null
    metric_stds:
    - 0.0343
    - null
  - model: RWPT (Edge feat. input)
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7315
    - null
    metric_stds:
    - 0.0295
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.73
    - null
    metric_stds:
    - 0.02
    - null
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.73
    - null
    metric_stds:
    - 0.037
    - null
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.73
    - null
    metric_stds:
    - 0.048
    - null
  - model: GraphFP-JT_C
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.73
    - null
    metric_stds:
    - 0.019
    - null
  - model: RWPT (Neighbor, [4,4,2])
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7281
    - null
    metric_stds:
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
    - 0.7267
    - null
    metric_stds:
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.7
    - null
    metric_stds:
    - 0.04
    - null
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.7
    - null
    metric_stds:
    - 0.04
    - null
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.69
    - null
    metric_stds:
    - 0.034
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.68
    - null
    metric_stds:
    - 0.052
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
    - 0.6686
    - null
    metric_stds:
    - null
    - null
  - model: MLP
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
    - 0.6637
    - null
    metric_stds:
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
    - 0.6554
    - null
    metric_stds:
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
    - 0.6544
    - null
    metric_stds:
    - null
    - null
  - model: GPT-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.652
    - null
    metric_stds:
    - 0.021
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
    - 0.6484
    - null
    metric_stds:
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
    - 0.6395
    - null
    metric_stds:
    - null
    - null
  - model: K-SG SAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.02156'
    title: Probabilistically Rewired Message-Passing Networks
    date: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.613
    - null
    metric_stds:
    - 0.01
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
    - 0.6104
    - null
    metric_stds:
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
    - 0.5962
    - null
    metric_stds:
    - null
    - null
  - model: D-MPNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.06462'
    title: Invariant-Based Diagnostics for Graph Benchmarks
    date: May 2026
    date_iso: 2026-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.7709999999999999
    metric_stds:
    - null
    - 0.005
  - model: AttentiveFP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.06462'
    title: Invariant-Based Diagnostics for Graph Benchmarks
    date: May 2026
    date_iso: 2026-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.757
    metric_stds:
    - null
    - 0.013999999999999999
  - model: N-Gram_RF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.06462'
    title: Invariant-Based Diagnostics for Graph Benchmarks
    date: May 2026
    date_iso: 2026-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.772
    metric_stds:
    - null
    - 0.001
  - model: N-Gram_XGB
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.06462'
    title: Invariant-Based Diagnostics for Graph Benchmarks
    date: May 2026
    date_iso: 2026-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.787
    metric_stds:
    - null
    - 0.004
  - model: PretrainGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.06462'
    title: Invariant-Based Diagnostics for Graph Benchmarks
    date: May 2026
    date_iso: 2026-05
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - 0.799
    metric_stds:
    - null
    - 0.006999999999999999
  - model: GROVER_base
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.06462'
    title: Invariant-Based Diagnostics for Graph Benchmarks
    date: May 2026
    date_iso: 2026-05
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - 0.625
    metric_stds:
    - null
    - 0.009000000000000001
  - model: GROVER_large
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.06462'
    title: Invariant-Based Diagnostics for Graph Benchmarks
    date: May 2026
    date_iso: 2026-05
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - 0.682
    metric_stds:
    - null
    - 0.011000000000000001
  - model: GraphMVP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.06462'
    title: Invariant-Based Diagnostics for Graph Benchmarks
    date: May 2026
    date_iso: 2026-05
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - 0.77
    metric_stds:
    - null
    - 0.012
  - model: MolCLR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.06462'
    title: Invariant-Based Diagnostics for Graph Benchmarks
    date: May 2026
    date_iso: 2026-05
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - 0.7809999999999999
    metric_stds:
    - null
    - 0.005
  - model: GEM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.06462'
    title: Invariant-Based Diagnostics for Graph Benchmarks
    date: May 2026
    date_iso: 2026-05
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - 0.8059999999999999
    metric_stds:
    - null
    - 0.009000000000000001
  - model: Uni-Mol
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.06462'
    title: Invariant-Based Diagnostics for Graph Benchmarks
    date: May 2026
    date_iso: 2026-05
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - 0.8079999999999999
    metric_stds:
    - null
    - 0.003
  - model: agg + I
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.06462'
    title: Invariant-Based Diagnostics for Graph Benchmarks
    date: May 2026
    date_iso: 2026-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.7695000000000001
    metric_stds:
    - null
    - 0.0034000000000000002
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2502.00282'
    title: 'GraphMinNet: Learning Dependencies in Graphs with Light Complexity Minimal
      Architecture'
    date: '2025-02-01'
    date_iso: '2025-02-01'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.7599
    metric_stds:
    - null
    - 0.0119
  - model: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.00282'
    title: 'GraphMinNet: Learning Dependencies in Graphs with Light Complexity Minimal
      Architecture'
    date: '2025-02-01'
    date_iso: '2025-02-01'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.7707
    metric_stds:
    - null
    - 0.0149
  - model: SAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.00282'
    title: 'GraphMinNet: Learning Dependencies in Graphs with Light Complexity Minimal
      Architecture'
    date: '2025-02-01'
    date_iso: '2025-02-01'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.7785
    metric_stds:
    - null
    - 0.0247
  - model: GraphGPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.00282'
    title: 'GraphMinNet: Learning Dependencies in Graphs with Light Complexity Minimal
      Architecture'
    date: '2025-02-01'
    date_iso: '2025-02-01'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.788
    metric_stds:
    - null
    - 0.0101
  - model: Exphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.00282'
    title: 'GraphMinNet: Learning Dependencies in Graphs with Light Complexity Minimal
      Architecture'
    date: '2025-02-01'
    date_iso: '2025-02-01'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.7879
    metric_stds:
    - null
    - 0.0131
  - model: Graph-Mamba
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.00282'
    title: 'GraphMinNet: Learning Dependencies in Graphs with Light Complexity Minimal
      Architecture'
    date: '2025-02-01'
    date_iso: '2025-02-01'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.7823
    metric_stds:
    - null
    - 0.0121
  - model: GSSC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.00282'
    title: 'GraphMinNet: Learning Dependencies in Graphs with Light Complexity Minimal
      Architecture'
    date: '2025-02-01'
    date_iso: '2025-02-01'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.8035
    metric_stds:
    - null
    - 0.0142
  - model: Ours
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.00282'
    title: 'GraphMinNet: Learning Dependencies in Graphs with Light Complexity Minimal
      Architecture'
    date: '2025-02-01'
    date_iso: '2025-02-01'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.8086
    metric_stds:
    - null
    - 0.0056
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.7599
    metric_stds:
    - null
    - 0.0119
  - model: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.7707
    metric_stds:
    - null
    - 0.0149
  - model: CIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.8094
    metric_stds:
    - null
    - 0.0057
  - model: PR-MPNN_Sim
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.795
    metric_stds:
    - null
    - 0.009
  - model: GPS+rand
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.621
    metric_stds:
    - null
    - 0.0444
  - model: GPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.7798
    metric_stds:
    - null
    - 0.0077
  - model: GPS+LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.7736
    metric_stds:
    - null
    - 0.0097
  - model: GPS+RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.788
    metric_stds:
    - null
    - 0.0101
  - model: GPS + (RWSE/LapPE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.7719
    metric_stds:
    - null
    - 0.0129
  - model: GPS+AllPSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.7645
    metric_stds:
    - null
    - 0.0236
  - model: GPSE + GPS
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.7815
    metric_stds:
    - null
    - 0.0133
  - model: Self-supervised pre-trained
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - 0.773
    metric_stds:
    - null
    - 0.01
  - model: GraphLOG pretrained
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - 0.785
    metric_stds:
    - null
    - 0.012
  - model: InfoGraph pretrained
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - 0.702
    metric_stds:
    - null
    - 0.006
  - model: JOAOv2 pre-trained
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - 0.684
    metric_stds:
    - null
    - 0.005
  - model: GraphMAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - 0.772
    metric_stds:
    - null
    - 0.01
  - model: GraphLoG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - 0.778
    metric_stds:
    - null
    - 0.008
  - model: No augmentation
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.753
    metric_stds:
    - null
    - 0.019
  - model: GraphLoG augmented
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.744
    metric_stds:
    - null
    - 0.015
  - model: LapPE augmented
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.756
    metric_stds:
    - null
    - 0.011
  - model: RWSE augmented
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.781
    metric_stds:
    - null
    - 0.015
  - model: AllPSE augmented
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.754
    metric_stds:
    - null
    - 0.015
  - model: GPSE augmented
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.772
    metric_stds:
    - null
    - 0.015
  - model: GPS+GPSE (LapPE & EigVals excluded)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.7849
    metric_stds:
    - null
    - 0.0067
  - model: GPS+GPSE (ElstaticPE excluded)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.7681
    metric_stds:
    - null
    - 0.0146
  - model: GPS+GPSE (RWSE excluded)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.7771
    metric_stds:
    - null
    - 0.0105
  - model: GPS+GPSE (HKdiagSE excluded)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.7787
    metric_stds:
    - null
    - 0.0198
  - model: GPS+GPSE (CycleSE excluded)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.7739
    metric_stds:
    - null
    - 0.024
  - model: No pre-training
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.753
    metric_stds:
    - null
    - 0.019
  - model: SSL InfoMax pre-trained
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - 0.76
    metric_stds:
    - null
    - 0.007
  - model: SSL EdgePred pre-trained
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - 0.763
    metric_stds:
    - null
    - 0.01
  - model: SSL AttrMasking pre-trained
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - 0.772
    metric_stds:
    - null
    - 0.011
  - model: SSL ContextPred pre-trained
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - 0.773
    metric_stds:
    - null
    - 0.01
  milestones:
  - value: 0.8094
    std: 0.0057
    model: CIN
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: '2023-06-09'
  - value: 0.8107
    std: 0.0021
    model: HyMN (GatedGCN, T=2)
    arxiv_id: '2501.03113'
    title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs with Walk-Based
      Centrality'
    date: 2025-01
  - value: 0.968
    std: 0.002
    model: GIN
    arxiv_id: '2502.02379'
    title: 'No Metric to Rule Them All: Toward Principled Evaluations of Graph-Learning
      Datasets'
    date: '2025-02-04'
  - value: 0.9685
    std: 0.0001
    model: MLP
    arxiv_id: '2511.16767'
    title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed Graphs as
      Effectively as We Expected'
    date: 2025-11
---

