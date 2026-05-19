---
title: ogbg-molpcba
slug: ogbg-molpcba
benchmark: OGB
task_type: graph_classification
description: Multi-label classification (128 tasks) on PubChem BioAssay.
primary_metric: AP
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.OGBDataset.html
stats: null
result_count: 90
best_model:
  model: GatedGCN + VN
  value: 0.3141
  metric: AP
variants:
- slug: standard-split
  name: Standard split
  notes: 'Scaffold split. Metric: AP (Average Precision).'
  is_standard: true
  primary_metric: AP
  higher_is_better: true
  metrics:
  - AP
  - ACC
  - Accuracy
  - ROC-AUC
  rows:
  - model: GatedGCN + VN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.11951'
    title: 'Distinguished In Uniform: - Self-Attention Vs. Virtual Nodes'
    date: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.3141
    - null
    - null
    - null
    metric_stds:
    - 0.0019
    - null
    - null
    - null
  - model: NeuralWalker
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.03386'
    title: Learning Long Range Dependencies on Graphs - via Random Walks
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3086
    - 0.7888
    - null
    - null
    metric_stds:
    - 0.0031
    - 0.0059
    - null
    - null
  - model: GatedGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    arxiv_id: '2405.11951'
    title: 'Distinguished In Uniform: - Self-Attention Vs. Virtual Nodes'
    date: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3066
    - null
    - null
    - null
    metric_stds:
    - 0.0013
    - null
    - null
    - null
  - model: LGI-GT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.11951'
    title: 'Distinguished In Uniform: - Self-Attention Vs. Virtual Nodes'
    date: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.304
    - null
    - null
    - null
    metric_stds:
    - 0.0029
    - null
    - null
    - null
  - model: CRaWl
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
    - 0.2986
    - null
    - null
    - null
    metric_stds:
    - 0.0025
    - null
    - null
    - null
  - model: CRaWI
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
    - 0.2986
    - null
    - null
    - null
    metric_stds:
    - 0.0025
    - null
    - null
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.2984
    - null
    - null
    - null
    metric_stds:
    - 0.0031
    - null
    - null
    - null
  - model: GatedGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    arxiv_id: '2502.09263'
    title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks? Simple Architectures
      Meet Excellence
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2981
    - null
    - 0.8258
    - null
    metric_stds:
    - 0.0024
    - null
    - 0.0055
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
    - 0.2972
    - null
    - null
    - null
    metric_stds:
    - 0.0023
    - null
    - null
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
    - 0.2961
    - null
    - null
    - null
    metric_stds:
    - 0.0024
    - null
    - null
    - null
  - model: GECO
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.12059'
    title: A Scalable and Effective Alternative to Graph Transformers
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2961
    - null
    - null
    - null
    metric_stds:
    - 0.0008
    - null
    - null
    - null
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
    - 0.2939
    - null
    - null
    - null
    metric_stds:
    - 0.0016
    - null
    - null
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
    - 0.2937
    - null
    - null
    - null
    metric_stds:
    - 0.0023
    - null
    - null
    - null
  - model: GPS+EdgeRWSE
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
    - 0.2934
    - null
    - null
    - null
    metric_stds:
    - 0.0025
    - null
    - null
    - null
  - model: Subgraphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.24293'
    title: 'Latent-Hysteresis Graph ODEs: Modeling Coupled Topology-Feature Evolution
      via Continuous Phase Transitions'
    date: Apr 2026
    date_iso: 2026-04
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.293
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
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
    - 0.293
    - null
    - null
    - null
    metric_stds:
    - 0.0044
    - null
    - null
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
    - 0.293
    - null
    - null
    - null
    metric_stds:
    - 0.0044
    - null
    - null
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
    - 0.292
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
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
    - 0.2917
    - null
    - null
    - null
    metric_stds:
    - 0.0027
    - null
    - null
    - null
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
    - 0.2911
    - null
    - null
    - null
    metric_stds:
    - 0.0036
    - null
    - null
    - null
  - model: GraphGPS
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
    - 0.2907
    - null
    - null
    - null
    metric_stds:
    - 0.0028
    - null
    - null
    - null
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
    - 0.2907
    - null
    - null
    - null
    metric_stds:
    - 0.0028
    - null
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
    - 0.2902
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
  - model: DGN
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
    - 0.2885
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
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
    - 0.2869
    - null
    - null
    - null
    metric_stds:
    - 0.0012
    - null
    - null
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
    - 0.2866
    - null
    - null
    - null
    metric_stds:
    - 0.0016
    - null
    - null
    - null
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
    - 0.2854
    - null
    - null
    - null
    metric_stds:
    - 0.0029
    - null
    - null
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
    - 0.2849
    - null
    - null
    - null
    metric_stds:
    - 0.0025
    - null
    - null
    - null
  - model: PNA
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
    - 0.2838
    - null
    - null
    - null
    metric_stds:
    - 0.0035
    - null
    - null
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
    - 0.2832
    - null
    - null
    - null
    metric_stds:
    - 0.0041
    - null
    - null
    - null
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
    - 0.2826
    - null
    - null
    - null
    metric_stds:
    - 0.0001
    - null
    - null
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
    - 0.2823
    - null
    - null
    - null
    metric_stds:
    - 0.0026
    - null
    - null
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
    - 0.2802
    - null
    - null
    - null
    metric_stds:
    - 0.0061
    - null
    - null
    - null
  - model: DeeperGCN
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
    - 0.2781
    - null
    - null
    - null
    metric_stds:
    - 0.0038
    - null
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
    - 0.278
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
  - model: VANILLA-FFGT
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
    - 0.2779
    - null
    - null
    - null
    metric_stds:
    - 0.0049
    - null
    - null
    - null
  - model: SAN+LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.531
    arxiv_id: '2311.04653'
    title: Hybrid Focal and Full-Range Attention Based Graph Transformers -
    date: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2765
    - null
    - null
    - null
    metric_stds:
    - 0.0042
    - null
    - null
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
    is_best: false
    metric_values:
    - 0.2765
    - null
    - null
    - null
    metric_stds:
    - 0.0042
    - null
    - null
    - null
  - model: GraphTrans (GCN-Virtual)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.12059'
    title: A Scalable and Effective Alternative to Graph Transformers
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2761
    - null
    - null
    - null
    metric_stds:
    - 0.0029
    - null
    - null
    - null
  - model: GraphTrans
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.03386'
    title: Learning Long Range Dependencies on Graphs - via Random Walks
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2761
    - null
    - null
    - null
    metric_stds:
    - 0.0029
    - null
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
    - 0.2721
    - null
    - 0.8077
    - null
    metric_stds:
    - 0.0046
    - null
    - 0.0041
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
    - 0.2714
    - null
    - null
    - null
    metric_stds:
    - 0.0014
    - null
    - null
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
    - 0.2703
    - null
    - null
    - null
    metric_stds:
    - 0.0023
    - null
    - null
    - null
  - model: GINE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.505
    arxiv_id: '2405.11951'
    title: 'Distinguished In Uniform: - Self-Attention Vs. Virtual Nodes'
    date: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2703
    - null
    - null
    - null
    metric_stds:
    - 0.0023
    - null
    - null
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
    - 0.2703
    - null
    - null
    - null
    metric_stds:
    - 0.0023
    - null
    - null
    - null
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
    - 0.2703
    - null
    - null
    - null
    metric_stds:
    - 0.0023
    - null
    - null
    - null
  - model: GatedGCN+LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    arxiv_id: '2406.12059'
    title: A Scalable and Effective Alternative to Graph Transformers
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.267
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
  - model: GatedGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    arxiv_id: '2311.04653'
    title: Hybrid Focal and Full-Range Attention Based Graph Transformers -
    date: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.267
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
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
    - 0.2621
    - null
    - null
    - null
    metric_stds:
    - 0.0026
    - null
    - null
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
    - 0.2566
    - null
    - null
    - null
    metric_stds:
    - 0.0047
    - null
    - null
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
    - 0.2538
    - null
    - null
    - null
    metric_stds:
    - 0.0019
    - null
    - null
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
    - 0.2481
    - null
    - null
    - null
    metric_stds:
    - 0.0032
    - null
    - null
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
    - 0.2424
    - null
    - null
    - null
    metric_stds:
    - 0.0034
    - null
    - null
    - null
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
    - 0.2424
    - null
    - null
    - null
    metric_stds:
    - 0.0034
    - null
    - null
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
    - 0.2362
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
  - model: ExpC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.12059'
    title: A Scalable and Effective Alternative to Graph Transformers
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2342
    - null
    - null
    - null
    metric_stds:
    - 0.0029
    - null
    - null
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
    - 0.2291
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
  - model: GIN
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
    - 0.2266
    - null
    - null
    - null
    metric_stds:
    - 0.0028
    - null
    - null
    - null
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2405.13526'
    title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    date: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.202
    - null
    - null
    - null
    metric_stds:
    - 0.0024
    - null
    - null
    - null
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
    - 0.0753
    - null
    - null
    - null
    metric_stds:
    - 0.0045
    - null
    - null
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
    - null
    - null
    - null
    - 0.767
    metric_stds:
    - null
    - null
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
    - null
    - null
    - null
    - 0.744
    metric_stds:
    - null
    - null
    - null
    - null
  - model: GT
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
    - null
    - null
    - 0.6454
    - null
    metric_stds:
    - null
    - null
    - 0.0033
    - null
  - model: SAT
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
    - null
    - null
    - 0.7522
    - null
    metric_stds:
    - null
    - null
    - 0.0056
    - null
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2410.03424'
    title: Cayley Graph Propagation
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.5483
    - null
    metric_stds:
    - null
    - null
    - 0.0209
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
    - null
    - null
    - 0.6069
    - null
    metric_stds:
    - null
    - null
    - 0.0062
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
    - null
    - null
    - 0.6821
    - null
    metric_stds:
    - null
    - null
    - 0.0045
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
    - null
    - null
    - 0.6782
    - null
    metric_stds:
    - null
    - null
    - 0.0066
    - null
  - model: GIN
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
    - null
    - null
    - 0.5888
    - null
    metric_stds:
    - null
    - null
    - 0.0441
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
    - null
    - null
    - 0.6533
    - null
    metric_stds:
    - null
    - null
    - 0.119
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
    - null
    - null
    - 0.6562
    - null
    metric_stds:
    - null
    - null
    - 0.0147
    - null
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2407.02758'
    title: Differential Encoding for Improved Representation Learning over Graphs
    date: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.6839
    - null
    metric_stds:
    - null
    - null
    - 0.0084
    - null
  - model: GCN + virtual node
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.02758'
    title: Differential Encoding for Improved Representation Learning over Graphs
    date: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.7037
    - null
    metric_stds:
    - null
    - null
    - 0.0107
    - null
  - model: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.02758'
    title: Differential Encoding for Improved Representation Learning over Graphs
    date: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.6892
    - null
    metric_stds:
    - null
    - null
    - 0.01
    - null
  - model: DeeperGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.02758'
    title: Differential Encoding for Improved Representation Learning over Graphs
    date: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.7712
    - null
    metric_stds:
    - null
    - null
    - 0.0071
    - null
  - model: ExpC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.02758'
    title: Differential Encoding for Improved Representation Learning over Graphs
    date: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.7976
    - null
    metric_stds:
    - null
    - null
    - 0.0072
    - null
  - model: K-Subtree SAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.02758'
    title: Differential Encoding for Improved Representation Learning over Graphs
    date: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.7522
    - null
    metric_stds:
    - null
    - null
    - 0.0056
    - null
  - model: GPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.02758'
    title: Differential Encoding for Improved Representation Learning over Graphs
    date: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.8015
    - null
    metric_stds:
    - null
    - null
    - 0.0033
    - null
  - model: Ours
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.02758'
    title: Differential Encoding for Improved Representation Learning over Graphs
    date: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.8096
    - null
    metric_stds:
    - null
    - null
    - 0.0029
    - null
  - model: SAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.03386'
    title: Learning Long Range Dependencies on Graphs - via Random Walks
    date: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.7522
    - null
    - null
    metric_stds:
    - null
    - 0.0056
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
    - null
    - null
    - null
    - 0.723
    metric_stds:
    - null
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
    - null
    - null
    - null
    - 0.7132
    metric_stds:
    - null
    - null
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
    - null
    - null
    - null
    - 0.7012
    metric_stds:
    - null
    - null
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
    - null
    - null
    - null
    - 0.7269
    metric_stds:
    - null
    - null
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
    - null
    - null
    - null
    - 0.6331
    metric_stds:
    - null
    - null
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
    - null
    - null
    - null
    - 0.6709
    metric_stds:
    - null
    - null
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
    - null
    - null
    - null
    - 0.633
    metric_stds:
    - null
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
    - null
    - null
    - null
    - 0.6149
    metric_stds:
    - null
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
    - null
    - null
    - null
    - 0.779
    metric_stds:
    - null
    - null
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
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.8103
    metric_stds:
    - null
    - null
    - null
    - null
  milestones:
  - value: 0.2986
    std: 0.0025
    model: CRaWI
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
  - value: 0.3141
    std: 0.0019
    model: GatedGCN + VN
    arxiv_id: '2405.11951'
    title: 'Distinguished In Uniform: - Self-Attention Vs. Virtual Nodes'
    date: 2024-05
---

