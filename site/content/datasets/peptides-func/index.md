---
title: Peptides-func
slug: peptides-func
benchmark: LRGB
task_type: graph_classification
description: Multi-label graph classification on peptide molecules (10 classes).
primary_metric: AP
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.LRGBDataset.html
stats:
  num_graphs: 15535
  avg_nodes: 150.94
  avg_edges: 307.3
  num_classes: 10
result_count: 367
best_model:
  model: LightGBM (ECFP)
  value: 0.746
  metric: AP
  arxiv_id: '2501.17901'
  paper_title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
variants:
- slug: standard-split
  name: Standard split
  notes: 'Official random split (80/10/10). Metric: AP (Average Precision).'
  is_standard: true
  primary_metric: AP
  higher_is_better: true
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - AP
  - Accuracy
  - MAE
  rows:
  - model: LightGBM (ECFP)
    model_plain: LightGBM (ECFP)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: '2025-01-29'
    date_iso: '2025-01-29'
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.746
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: Random Forest (ECFP)
    model_plain: Random Forest (ECFP)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: '2025-01-29'
    date_iso: '2025-01-29'
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7355
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
  - model: LightGBM (TT)
    model_plain: LightGBM (TT)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: '2025-01-29'
    date_iso: '2025-01-29'
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7318
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: S2GCN+PE
    model_plain: S2GCN+PE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.17311'
    title: Probabilistic Graph Rewiring via Virtual Nodes
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7311
    - null
    - null
    metric_stds:
    - 0.0066
    - null
    - null
  - model: LightGBM (RDKit)
    model_plain: LightGBM (RDKit)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: '2025-01-29'
    date_iso: '2025-01-29'
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7311
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: S4G
    model_plain: S4G
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08678'
    title: 'Graph Mamba: Towards Learning on Graphs with State Space Models'
    date: '2024-02-13'
    date_iso: '2024-02-13'
    date_display: Feb 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7293
    - null
    - null
    metric_stds:
    - 0.0004
    - null
    - null
  - model: BuNN
    model_plain: BuNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.15540'
    title: Bundle Neural Networks for message diffusion on graphs
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7276
    - null
    - null
    metric_stds:
    - 0.0065
    - null
    - null
  - model: S2GCN
    model_plain: S2GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.17311'
    title: Probabilistic Graph Rewiring via Virtual Nodes
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7275
    - null
    - null
    metric_stds:
    - 0.0066
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09263'
    title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks? Simple Architectures
      Meet Excellence
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7261
    - null
    - null
    metric_stds:
    - 0.0067
    - null
    - null
  - model: LR-GWN (TC)
    model_plain: LR-GWN (TC)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.06743'
    title: Long-Range Graph Wavelet Networks
    date: Sep 2025
    date_iso: 2025-09
    date_display: Sep 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7216
    - null
    - null
    metric_stds:
    - 0.0040999999999999995
    - null
    - null
  - model: kGCN-SSM
    model_plain: kGCN-SSM
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.10818'
    title: 'On Vanishing Gradients, Over-Smoothing, and Over-Squashing in GNNs: Bridging
      Recurrent and Graph Learning'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7212
    - null
    - null
    metric_stds:
    - 0.0027
    - null
    - null
  - model: IPR-MPNN
    model_plain: IPR-MPNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.16560'
    title: Algorithmic Graph Tasks
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/nec-research/Adaptive-Message-Passing
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.721
    - null
    - null
    metric_stds:
    - 0.0039
    - null
    - null
  - model: 2VN2S
    model_plain: 2VN2S
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.17311'
    title: Probabilistic Graph Rewiring via Virtual Nodes
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.721
    - null
    - null
    metric_stds:
    - 0.0039
    - null
    - null
  - model: NBA
    model_plain: NBA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.16560'
    title: Algorithmic Graph Tasks
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/nec-research/Adaptive-Message-Passing
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7207
    - null
    - null
    metric_stds:
    - 0.0028
    - null
    - null
  - model: Extremely Randomized Trees (ECFP)
    model_plain: Extremely Randomized Trees (ECFP)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: '2025-01-29'
    date_iso: '2025-01-29'
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7198
    - null
    - null
    metric_stds:
    - 0.0008
    - null
    - null
  - model: GraphMinNet
    model_plain: GraphMinNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.00282'
    title: 'GraphMinNet: Learning Dependencies in Graphs with Light Complexity Minimal
      Architecture'
    date: '2025-02-01'
    date_iso: '2025-02-01'
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7182
    - null
    - null
    metric_stds:
    - 0.0024
    - null
    - null
  - model: GatedGCN + VN + HOPE-WavePE
    model_plain: GatedGCN + VN + HOPE-WavePE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.19117'
    title: 'Range-aware Positional Encoding via High-order Pretraining: Theory and
      Practice'
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7171
    - null
    - null
    metric_stds:
    - 0.0023
    - null
    - null
  - model: Random Forest
    model_plain: Random Forest
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: '2025-01-29'
    date_iso: '2025-01-29'
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7166
    - null
    - null
    metric_stds:
    - 0.0009
    - null
    - null
  - model: AMP
    model_plain: AMP
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.16560'
    title: Algorithmic Graph Tasks
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/nec-research/Adaptive-Message-Passing
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7161
    - null
    - null
    metric_stds:
    - 0.0047
    - null
    - null
  - model: GraphGPS + HDSE
    model_plain: GraphGPS + HDSE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7156
    - null
    - null
    metric_stds:
    - 0.0058
    - null
    - null
  - model: DRew+LapPE
    model_plain: DRew+LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.01538'
    title: Recurrent Distance Filtering for Graph Representation Learning
    date: '2023-12-03'
    date_iso: '2023-12-03'
    date_display: Dec 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.715
    - null
    - null
    metric_stds:
    - 0.0044
    - null
    - null
  - model: DRew
    model_plain: DRew
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.715
    - null
    - null
    metric_stds:
    - 0.0044
    - null
    - null
  - model: Random Forest (RDKit)
    model_plain: Random Forest (RDKit)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: '2025-01-29'
    date_iso: '2025-01-29'
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7148
    - null
    - null
    metric_stds:
    - 0.0013
    - null
    - null
  - model: 2VN1S
    model_plain: 2VN1S
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.17311'
    title: Probabilistic Graph Rewiring via Virtual Nodes
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7146
    - null
    - null
    metric_stds:
    - 0.0055
    - null
    - null
  - model: 2VN4S
    model_plain: 2VN4S
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.17311'
    title: Probabilistic Graph Rewiring via Virtual Nodes
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7145
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
  - model: GENs
    model_plain: GENs
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7142
    - null
    - null
    metric_stds:
    - 0.0071
    - null
    - null
  - model: GENs+LapPE
    model_plain: GENs+LapPE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7142
    - null
    - null
    metric_stds:
    - 0.0071
    - null
    - null
  - model: HGODE
    model_plain: HGODE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.24293'
    title: 'Latent-Hysteresis Graph ODEs: Modeling Coupled Topology-Feature Evolution
      via Continuous Phase Transitions'
    date: Apr 2026
    date_iso: 2026-04
    date_display: Apr 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.714
    - null
    - null
    metric_stds:
    - 0.022
    - null
    - null
  - model: GRED
    model_plain: GRED
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09263'
    title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks? Simple Architectures
      Meet Excellence
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7133
    - null
    - null
    metric_stds:
    - 0.0011
    - null
    - null
  - model: GRED+LapPE
    model_plain: GRED+LapPE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.01538'
    title: Recurrent Distance Filtering for Graph Representation Learning
    date: '2023-12-03'
    date_iso: '2023-12-03'
    date_display: Dec 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7133
    - null
    - null
    metric_stds:
    - 0.0011
    - null
    - null
  - model: DRew-GCN+LapPE
    model_plain: DRew-GCN+LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.02156'
    title: Probabilistically Rewired Message-Passing Neural Networks
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7126
    - null
    - null
    metric_stds:
    - 0.0045
    - null
    - null
  - model: NeuralWalker
    model_plain: NeuralWalker
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.03386'
    title: Learning Long Range Dependencies on Graphs via Random Walks
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7096
    - null
    - null
    metric_stds:
    - 0.0078
    - null
    - null
  - model: GRAMA
    model_plain: GRAMA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.7093
    - null
    - null
    metric_stds:
    - 0.0078
    - null
    - null
  - model: GENs+RWSE
    model_plain: GENs+RWSE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7087
    - null
    - null
    metric_stds:
    - 0.0103
    - null
    - null
  - model: GSSC
    model_plain: GSSC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09263'
    title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks? Simple Architectures
      Meet Excellence
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7081
    - null
    - null
    metric_stds:
    - 0.0062
    - null
    - null
  - model: CRaWl
    model_plain: CRaWl
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.16560'
    title: Algorithmic Graph Tasks
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/nec-research/Adaptive-Message-Passing
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7074
    - null
    - null
    metric_stds:
    - 0.0032
    - null
    - null
  - model: GMN
    model_plain: GMN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7071
    - null
    - null
    metric_stds:
    - 0.0083
    - null
    - null
  - model: NBA-GCN+LapPE
    model_plain: NBA-GCN+LapPE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.07430'
    title: Non-backtracking Graph Neural Networks
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7071
    - null
    - null
    metric_stds:
    - 0.0067
    - null
    - null
  - model: ESA
    model_plain: ESA
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.10793'
    title: An end-to-end attention-based approach for learning on graphs
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7071
    - null
    - null
    metric_stds:
    - 0.0015
    - null
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09263'
    title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks? Simple Architectures
      Meet Excellence
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7059
    - null
    - null
    metric_stds:
    - 0.0089
    - null
    - null
  - model: Full
    model_plain: Full
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.10651'
    title: Graph Learning via Logic-Based Weisfeiler--Leman Variants and Tabularization
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.705
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
  - model: Hyb.
    model_plain: Hyb.
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.10651'
    title: Graph Learning via Logic-Based Weisfeiler--Leman Variants and Tabularization
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.705
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
  - model: GRED
    model_plain: GRED
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.16560'
    title: Algorithmic Graph Tasks
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/nec-research/Adaptive-Message-Passing
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7041
    - null
    - null
    metric_stds:
    - 0.0049
    - null
    - null
  - model: 1VN - FC
    model_plain: 1VN - FC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.17311'
    title: Probabilistic Graph Rewiring via Virtual Nodes
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7039
    - null
    - null
    metric_stds:
    - 0.0046
    - null
    - null
  - model: Stable-ChebNet
    model_plain: Stable-ChebNet
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7032
    - null
    - null
    metric_stds:
    - 0.0026
    - null
    - null
  - model: Tango_GPS
    model_plain: Tango_GPS
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.05070'
    title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential Flows'
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7021
    - null
    - null
    metric_stds:
    - 0.0043
    - null
    - null
  - model: DAGNN
    model_plain: DAGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7021
    - null
    - null
    metric_stds:
    - 0.0075
    - null
    - null
  - model: PH-DGN
    model_plain: PH-DGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.16560'
    title: Algorithmic Graph Tasks
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/nec-research/Adaptive-Message-Passing
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7012
    - null
    - null
    metric_stds:
    - 0.0045
    - null
    - null
  - model: GatedGCN
    model_plain: GatedGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09263'
    title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks? Simple Architectures
      Meet Excellence
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7006
    - null
    - null
    metric_stds:
    - 0.0033
    - null
    - null
  - model: DRew
    model_plain: DRew
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.01538'
    title: Recurrent Distance Filtering for Graph Representation Learning
    date: '2023-12-03'
    date_iso: '2023-12-03'
    date_display: Dec 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6996
    - null
    - null
    metric_stds:
    - 0.0076
    - null
    - null
  - model: Drew-GIN
    model_plain: Drew-GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6996
    - null
    - null
    metric_stds:
    - 0.0076
    - null
    - null
  - model: MP-SSM
    model_plain: MP-SSM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.6993
    - null
    - null
    metric_stds:
    - 0.0052
    - null
    - null
  - model: CO-GNN
    model_plain: CO-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.16560'
    title: Algorithmic Graph Tasks
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/nec-research/Adaptive-Message-Passing
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.699
    - null
    - null
    metric_stds:
    - 0.0093
    - null
    - null
  - model: GRIT
    model_plain: GRIT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6988
    - null
    - null
    metric_stds:
    - 0.0082
    - null
    - null
  - model: Extremely Randomized Trees (TT)
    model_plain: Extremely Randomized Trees (TT)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: '2025-01-29'
    date_iso: '2025-01-29'
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6986
    - null
    - null
    metric_stds:
    - 0.0008
    - null
    - null
  - model: PST
    model_plain: PST
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 1.0
    arxiv_id: '2405.02795'
    title: Graph as Point Set
    date: '2024-05-05'
    date_iso: '2024-05-05'
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6984
    - null
    - null
    metric_stds:
    - 0.0051
    - null
    - null
  - model: GatedGCN+LapPE
    model_plain: GatedGCN+LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.07430'
    title: Non-backtracking Graph Neural Networks
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6982
    - null
    - null
    metric_stds:
    - 0.0014
    - null
    - null
  - model: DRew-GatedGCN+LapPE
    model_plain: DRew-GatedGCN+LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.02156'
    title: Probabilistically Rewired Message-Passing Neural Networks
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6977
    - null
    - null
    metric_stds:
    - 0.0026
    - null
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
    - 0.6975
    - null
    - null
    metric_stds:
    - 0.0025
    - null
    - null
  - model: WaveGC
    model_plain: WaveGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.06743'
    title: Long-Range Graph Wavelet Networks
    date: Sep 2025
    date_iso: 2025-09
    date_display: Sep 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6973
    - null
    - null
    metric_stds:
    - 0.0043
    - null
    - null
  - model: M
    model_plain: M
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
    date_iso: '2024-05-22'
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6973
    - null
    - null
    metric_stds:
    - 0.0043
    - null
    - null
  - model: GraphMLPMixer
    model_plain: GraphMLPMixer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.01538'
    title: Recurrent Distance Filtering for Graph Representation Learning
    date: '2023-12-03'
    date_iso: '2023-12-03'
    date_display: Dec 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.697
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
  - model: HOD-GNN
    model_plain: HOD-GNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.02565'
    title: On The Expressive Power of GNN Derivatives
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6968000000000001
    - null
    - null
    metric_stds:
    - 0.005600000000000001
    - null
    - null
  - model: Graph-ViT + GFSA
    model_plain: Graph-ViT + GFSA
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.04234'
    title: Graph Convolutions Enrich the Self-Attention in Transformers!
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.6964
    - null
    - null
    metric_stds:
    - 0.0025
    - null
    - null
  - model: NBA-GIN
    model_plain: NBA-GIN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.07430'
    title: Non-backtracking Graph Neural Networks
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6961
    - null
    - null
    metric_stds:
    - 0.0045
    - null
    - null
  - model: PPGT
    model_plain: PPGT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2504.12588'
    title: Plain Transformers Can be Powerful Graph Learners
    date: Apr 2025
    date_iso: 2025-04
    date_display: Apr 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6961
    - null
    - null
    metric_stds:
    - 0.0062
    - null
    - null
  - model: GRPE-FFGT
    model_plain: GRPE-FFGT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.04653'
    title: Hybrid Focal and Full-Range Attention Based Graph Transformers
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6956
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
  - model: GPNN
    model_plain: GPNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09263'
    title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks? Simple Architectures
      Meet Excellence
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6955
    - null
    - null
    metric_stds:
    - 0.0057
    - null
    - null
  - model: NBA-GCN
    model_plain: NBA-GCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.07430'
    title: Non-backtracking Graph Neural Networks
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6951
    - null
    - null
    metric_stds:
    - 0.0024
    - null
    - null
  - model: HyMN (GIN, T=2)
    model_plain: HyMN (GIN, T=2)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.03113'
    title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs with Walk-Based
      Centrality'
    date: Jan 2025
    date_iso: 2025-01
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6948
    - null
    - null
    metric_stds:
    - 0.0052
    - null
    - null
  - model: SigGate-GT
    model_plain: SigGate-GT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.17324'
    title: 'SigGate-GT: Taming Over-Smoothing in Graph Transformers via Sigmoid-Gated
      Attention'
    date: Apr 2026
    date_iso: 2026-04
    date_display: Apr 2026
    codebase_url: https://github.com/bettyguo/SigGate-GT
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6947
    - null
    - null
    metric_stds:
    - 0.0037
    - null
    - null
  - model: GRIT-SPSE
    model_plain: GRIT-SPSE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09365'
    title: Simple Path Structural Encoding for Graph Transformers
    date: '2025-02-13'
    date_iso: '2025-02-13'
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6945
    - null
    - null
    metric_stds:
    - 0.0113
    - null
    - null
  - model: Graph ViT
    model_plain: Graph ViT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.04653'
    title: Hybrid Focal and Full-Range Attention Based Graph Transformers
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6942
    - null
    - null
    metric_stds:
    - 0.0075
    - null
    - null
  - model: SortMPNN
    model_plain: SortMPNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.06984'
    title: On the Stability of Multiset and Graph Neural Networks
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.694
    - null
    - null
    metric_stds:
    - 0.0049
    - null
    - null
  - model: Extremely Randomized Trees (RDKit)
    model_plain: Extremely Randomized Trees (RDKit)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: '2025-01-29'
    date_iso: '2025-01-29'
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6938
    - null
    - null
    metric_stds:
    - 0.0006
    - null
    - null
  - model: AdaptMPNN
    model_plain: AdaptMPNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.06984'
    title: On the Stability of Multiset and Graph Neural Networks
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6934
    - null
    - null
    metric_stds:
    - 0.0099
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6924
    - null
    - null
    metric_stds:
    - 0.0044
    - null
    - null
  - model: G-MLPMixer
    model_plain: G-MLPMixer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.16560'
    title: Algorithmic Graph Tasks
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/nec-research/Adaptive-Message-Passing
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6921
    - null
    - null
    metric_stds:
    - 0.0054
    - null
    - null
  - model: GINE-MLP-Mixer
    model_plain: GINE-MLP-Mixer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.03113'
    title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs with Walk-Based
      Centrality'
    date: Jan 2025
    date_iso: 2025-01
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6921
    - null
    - null
    metric_stds:
    - 0.0054
    - null
    - null
  - model: MixHop
    model_plain: MixHop
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.692
    - null
    - null
    metric_stds:
    - 0.0037
    - null
    - null
  - model: Graph MLP-Mixer
    model_plain: Graph MLP-Mixer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.692
    - null
    - null
    metric_stds:
    - 0.0054
    - null
    - null
  - model: VANILLA-FFGT
    model_plain: VANILLA-FFGT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.04653'
    title: Hybrid Focal and Full-Range Attention Based Graph Transformers
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6914
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
  - model: HyMN (GCN, T=1)
    model_plain: HyMN (GCN, T=1)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.03113'
    title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs with Walk-Based
      Centrality'
    date: Jan 2025
    date_iso: 2025-01
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6912
    - null
    - null
    metric_stds:
    - 0.017
    - null
    - null
  - model: GQT
    model_plain: GQT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.13798'
    title: Learning Graph Quantized Tokenizers
    date: '2024-10-17'
    date_iso: '2024-10-17'
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6903
    - null
    - null
    metric_stds:
    - 0.0085
    - null
    - null
  - model: Tango_GatedGCN
    model_plain: Tango_GatedGCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.05070'
    title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential Flows'
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6892
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
  - model: GEN w/o EA
    model_plain: GEN w/o EA
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6889
    - null
    - null
    metric_stds:
    - 0.0092
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
    date: '2024-05-22'
    date_iso: '2024-05-22'
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6875
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
  - model: agg + I
    model_plain: agg + I
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.06462'
    title: Invariant-Based Diagnostics for Graph Benchmarks
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6874
    - null
    - null
    metric_stds:
    - 0.0022
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.00367'
    title: Where Did the Gap Go? Reassessing the Long-Range Graph Benchmark
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: https://github.com/toenshoff/LRGB
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.686
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
  - model: R-GCN (RWSE)
    model_plain: R-GCN (RWSE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.03113'
    title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs with Walk-Based
      Centrality'
    date: Jan 2025
    date_iso: 2025-01
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.686
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
  - model: HyMN
    model_plain: HyMN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.02565'
    title: On The Expressive Power of GNN Derivatives
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6857
    - null
    - null
    metric_stds:
    - 0.0055000000000000005
    - null
    - null
  - model: GEN w/o HA
    model_plain: GEN w/o HA
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6847
    - null
    - null
    metric_stds:
    - 0.0089
    - null
    - null
  - model: MixHop-GCN+LapPE
    model_plain: MixHop-GCN+LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.02156'
    title: Probabilistically Rewired Message-Passing Neural Networks
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6843
    - null
    - null
    metric_stds:
    - 0.0049
    - null
    - null
  - model: GRPE
    model_plain: GRPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.04653'
    title: Hybrid Focal and Full-Range Attention Based Graph Transformers
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6836
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
  - model: Graph-Mamba (Node Level Permutation + Degree Prioritization)
    model_plain: Graph-Mamba (Node Level Permutation + Degree Prioritization)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.00789'
    title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling with Selective
      State Spaces'
    date: '2024-02-01'
    date_iso: '2024-02-01'
    date_display: Feb 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6834
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: SIMPLE
    model_plain: SIMPLE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.18917'
    title: 'GraIP: A Benchmarking Framework For Neural Graph Inverse Problems'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.683
    - null
    - null
    metric_stds:
    - 0.009
    - null
    - null
  - model: DIGL+MPNN+LapPE
    model_plain: DIGL+MPNN+LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.02156'
    title: Probabilistically Rewired Message-Passing Neural Networks
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.683
    - null
    - null
    metric_stds:
    - 0.0026
    - null
    - null
  - model: PR-MPNN
    model_plain: PR-MPNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6825
    - null
    - null
    metric_stds:
    - 0.0086
    - null
    - null
  - model: GatedGCN+PE+VN_G
    model_plain: GatedGCN+PE+VN_G
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.17311'
    title: Probabilistic Graph Rewiring via Virtual Nodes
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6822
    - null
    - null
    metric_stds:
    - 0.0052
    - null
    - null
  - model: IM-GCN
    model_plain: IM-GCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: '2025-05-29'
    date_iso: '2025-05-29'
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6822
    - null
    - null
    metric_stds:
    - 0.0088
    - null
    - null
  - model: Graph-Mamba (Node Level Permutation)
    model_plain: Graph-Mamba (Node Level Permutation)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.00789'
    title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling with Selective
      State Spaces'
    date: '2024-02-01'
    date_iso: '2024-02-01'
    date_display: Feb 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6821
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: ChebNet
    model_plain: ChebNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.6819
    - null
    - null
    metric_stds:
    - 0.0027
    - null
    - null
  - model: MGT
    model_plain: MGT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.04653'
    title: Hybrid Focal and Full-Range Attention Based Graph Transformers
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6817
    - null
    - null
    metric_stds:
    - 0.0064
    - null
    - null
  - model: MGT+WavePE
    model_plain: MGT+WavePE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6817
    - null
    - null
    metric_stds:
    - 0.0064
    - null
    - null
  - model: PathNN
    model_plain: PathNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.07430'
    title: Non-backtracking Graph Neural Networks
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6816
    - null
    - null
    metric_stds:
    - 0.0026
    - null
    - null
  - model: GCN + CSE
    model_plain: GCN + CSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.03113'
    title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs with Walk-Based
      Centrality'
    date: Jan 2025
    date_iso: 2025-01
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6812
    - null
    - null
    metric_stds:
    - 0.0037
    - null
    - null
  - model: Tango-NON-ENERGY_GatedGCN
    model_plain: Tango-NON-ENERGY_GatedGCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.05070'
    title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential Flows'
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6807
    - null
    - null
    metric_stds:
    - 0.0045000000000000005
    - null
    - null
  - model: GRIT-RWSE
    model_plain: GRIT-RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09365'
    title: Simple Path Structural Encoding for Graph Transformers
    date: '2025-02-13'
    date_iso: '2025-02-13'
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6803
    - null
    - null
    metric_stds:
    - 0.0085
    - null
    - null
  - model: Tango-NON-TANGENT_GatedGCN
    model_plain: Tango-NON-TANGENT_GatedGCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.05070'
    title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential Flows'
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6801
    - null
    - null
    metric_stds:
    - 0.0052
    - null
    - null
  - model: HyMN (GatedGCN, T=2)
    model_plain: HyMN (GatedGCN, T=2)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.03113'
    title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs with Walk-Based
      Centrality'
    date: Jan 2025
    date_iso: 2025-01
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6788
    - null
    - null
    metric_stds:
    - 0.0052
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.03815'
    title: k-Maximum Inner Product Attention for Graph Transformers and the Expressive
      Power of GraphGPS
    date: Apr 2026
    date_iso: 2026-04
    date_display: Apr 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6787000000000001
    - null
    - null
    metric_stds:
    - 0.005600000000000001
    - null
    - null
  - model: GatedGCN
    model_plain: GatedGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.00367'
    title: Where Did the Gap Go? Reassessing the Long-Range Graph Benchmark
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: https://github.com/toenshoff/LRGB
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6765
    - null
    - null
    metric_stds:
    - 0.0047
    - null
    - null
  - model: Tango-NON-ENERGY_GPS
    model_plain: Tango-NON-ENERGY_GPS
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.05070'
    title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential Flows'
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6758
    - null
    - null
    metric_stds:
    - 0.0039000000000000003
    - null
    - null
  - model: HyMN (GIN, T=1) w/out CSE
    model_plain: HyMN (GIN, T=1) w/out CSE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.03113'
    title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs with Walk-Based
      Centrality'
    date: Jan 2025
    date_iso: 2025-01
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6758
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
  - model: SWAN
    model_plain: SWAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.6751
    - null
    - null
    metric_stds:
    - 0.0039
    - null
    - null
  - model: IM-GINE
    model_plain: IM-GINE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: '2025-05-29'
    date_iso: '2025-05-29'
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6745
    - null
    - null
    metric_stds:
    - 0.0022
    - null
    - null
  - model: Graph Mamba-1
    model_plain: Graph Mamba-1
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.07430'
    title: Non-backtracking Graph Neural Networks
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6739
    - null
    - null
    metric_stds:
    - 0.0087
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.03113'
    title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs with Walk-Based
      Centrality'
    date: Jan 2025
    date_iso: 2025-01
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6739
    - null
    - null
    metric_stds:
    - 0.0024
    - null
    - null
  - model: Graph-Mamba
    model_plain: Graph-Mamba
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.07430'
    title: Non-backtracking Graph Neural Networks
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6739
    - null
    - null
    metric_stds:
    - 0.0087
    - null
    - null
  - model: GRASS
    model_plain: GRASS
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    arxiv_id: '2407.05649'
    title: 'Greener GRASS: Enhancing GNNs with Encoding, Rewiring, and Attention'
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6737
    - null
    - null
    metric_stds:
    - 0.0064
    - null
    - null
  - model: Tango-NON-TANGENT_GPS
    model_plain: Tango-NON-TANGENT_GPS
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.05070'
    title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential Flows'
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6733
    - null
    - null
    metric_stds:
    - 0.0059
    - null
    - null
  - model: DRew(GatedGCN)
    model_plain: DRew(GatedGCN)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.02156'
    title: Probabilistically Rewired Message-Passing Neural Networks
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6733
    - null
    - null
    metric_stds:
    - 0.0094
    - null
    - null
  - model: + ReHub-FC
    model_plain: + ReHub-FC
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.01519'
    title: 'ReHub: Linear Complexity Graph Transformers with Adaptive Hub-Spoke Reassignment'
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6732
    - null
    - null
    metric_stds:
    - 0.0107
    - null
    - null
  - model: SUN
    model_plain: SUN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.04653'
    title: Hybrid Focal and Full-Range Attention Based Graph Transformers
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.673
    - null
    - null
    metric_stds:
    - 0.0078
    - null
    - null
  - model: HyMN (GatedGCN, T=2) w/out CSE
    model_plain: HyMN (GatedGCN, T=2) w/out CSE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.03113'
    title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs with Walk-Based
      Centrality'
    date: Jan 2025
    date_iso: 2025-01
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6723
    - null
    - null
    metric_stds:
    - 0.0079
    - null
    - null
  - model: BiScale-GTR
    model_plain: BiScale-GTR
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.06336'
    title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale Molecular
      Representation Learning'
    date: Apr 2026
    date_iso: 2026-04
    date_display: Apr 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6717
    - null
    - null
    metric_stds:
    - 0.0107
    - null
    - null
  - model: IM-GatedGCN
    model_plain: IM-GatedGCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: '2025-05-29'
    date_iso: '2025-05-29'
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6713
    - null
    - null
    metric_stds:
    - 0.0051
    - null
    - null
  - model: WL-GK
    model_plain: WL-GK
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.10651'
    title: Graph Learning via Logic-Based Weisfeiler--Leman Variants and Tabularization
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.671
    - null
    - null
    metric_stds:
    - 0.0
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
    date: '2024-05-22'
    date_iso: '2024-05-22'
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6695
    - null
    - null
    metric_stds:
    - 0.0063
    - null
    - null
  - model: FragFormer
    model_plain: FragFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.06336'
    title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale Molecular
      Representation Learning'
    date: Apr 2026
    date_iso: 2026-04
    date_display: Apr 2026
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.6693
    - null
    - null
    metric_stds:
    - 0.0154
    - null
    - null
  - model: GPSE + GPS
    model_plain: GPSE + GPS
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6688
    - null
    - null
    metric_stds:
    - 0.0151
    - null
    - null
  - model: GPSE-noabs
    model_plain: GPSE-noabs
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6687
    - null
    - null
    metric_stds:
    - 0.0119
    - null
    - null
  - model: SpecFormer
    model_plain: SpecFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.6686
    - null
    - null
    metric_stds:
    - 0.0064
    - null
    - null
  - model: + ReHub
    model_plain: + ReHub
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.01519'
    title: 'ReHub: Linear Complexity Graph Transformers with Adaptive Hub-Spoke Reassignment'
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6685
    - null
    - null
    metric_stds:
    - 0.0074
    - null
    - null
  - model: GatedGCN+RWSE
    model_plain: GatedGCN+RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.19117'
    title: 'Range-aware Positional Encoding via High-order Pretraining: Theory and
      Practice'
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6685
    - null
    - null
    metric_stds:
    - 0.0062
    - null
    - null
  - model: TIGT
    model_plain: TIGT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09263'
    title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks? Simple Architectures
      Meet Excellence
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6679
    - null
    - null
    metric_stds:
    - 0.0074
    - null
    - null
  - model: VANILLA
    model_plain: VANILLA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.04653'
    title: Hybrid Focal and Full-Range Attention Based Graph Transformers
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6648
    - null
    - null
    metric_stds:
    - 0.0087
    - null
    - null
  - model: GPSE-SignNet
    model_plain: GPSE-SignNet
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6647
    - null
    - null
    metric_stds:
    - 0.0093
    - null
    - null
  - model: GPS + RandAlign
    model_plain: GPS + RandAlign
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.09774'
    title: 'RandAlign: A Parameter-Free Method for Regularizing Graph Convolutional
      Networks'
    date: Apr 2024
    date_iso: 2024-04
    date_display: Apr 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.663
    - null
    - null
    metric_stds:
    - 0.0005
    - null
    - null
  - model: GPS + k-MIP
    model_plain: GPS + k-MIP
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.03815'
    title: k-Maximum Inner Product Attention for Graph Transformers and the Expressive
      Power of GraphGPS
    date: Apr 2026
    date_iso: 2026-04
    date_display: Apr 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6627
    - null
    - null
    metric_stds:
    - 0.0044
    - null
    - null
  - model: GPS+EdgeRWSE
    model_plain: GPS+EdgeRWSE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.19285'
    title: Facilitating Graph Neural Networks with Random Walk on Simplicial Complexes
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6625
    - null
    - null
    metric_stds:
    - 0.0042
    - null
    - null
  - model: GPS + Mamba
    model_plain: GPS + Mamba
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08678'
    title: 'Graph Mamba: Towards Learning on Graphs with State Space Models'
    date: '2024-02-13'
    date_iso: '2024-02-13'
    date_display: Feb 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6624
    - null
    - null
    metric_stds:
    - 0.0079
    - null
    - null
  - model: GINE
    model_plain: GINE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.00367'
    title: Where Did the Gap Go? Reassessing the Long-Range Graph Benchmark
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: https://github.com/toenshoff/LRGB
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6621
    - null
    - null
    metric_stds:
    - 0.0067
    - null
    - null
  - model: GIN + RWSE
    model_plain: GIN + RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.03113'
    title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs with Walk-Based
      Centrality'
    date: Jan 2025
    date_iso: 2025-01
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6621
    - null
    - null
    metric_stds:
    - 0.0067
    - null
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.10793'
    title: An end-to-end attention-based approach for learning on graphs
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6621
    - null
    - null
    metric_stds:
    - 0.0067
    - null
    - null
  - model: GIN+CSE
    model_plain: GIN+CSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.03113'
    title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs with Walk-Based
      Centrality'
    date: Jan 2025
    date_iso: 2025-01
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6619
    - null
    - null
    metric_stds:
    - 0.0077
    - null
    - null
  - model: GPSE-signinvar
    model_plain: GPSE-signinvar
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6619
    - null
    - null
    metric_stds:
    - 0.0097
    - null
    - null
  - model: GatedGCN + CSE
    model_plain: GatedGCN + CSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.03113'
    title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs with Walk-Based
      Centrality'
    date: Jan 2025
    date_iso: 2025-01
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6611
    - null
    - null
    metric_stds:
    - 0.0058
    - null
    - null
  - model: Subgraphormer
    model_plain: Subgraphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.24293'
    title: 'Latent-Hysteresis Graph ODEs: Modeling Coupled Topology-Feature Evolution
      via Continuous Phase Transitions'
    date: Apr 2026
    date_iso: 2026-04
    date_display: Apr 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.661
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
  - model: Ours
    model_plain: Ours
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.02758'
    title: Differential Encoding for Improved Representation Learning over Graphs
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6608
    - null
    - null
    metric_stds:
    - 0.0046
    - null
    - null
  - model: GPS + Performer
    model_plain: GPS + Performer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.03815'
    title: k-Maximum Inner Product Attention for Graph Transformers and the Expressive
      Power of GraphGPS
    date: Apr 2026
    date_iso: 2026-04
    date_display: Apr 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6606000000000001
    - null
    - null
    metric_stds:
    - 0.0064
    - null
    - null
  - model: CSA-SPSE
    model_plain: CSA-SPSE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09365'
    title: Simple Path Structural Encoding for Graph Transformers
    date: '2025-02-13'
    date_iso: '2025-02-13'
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6605
    - null
    - null
    metric_stds:
    - 0.0096
    - null
    - null
  - model: GPS + GFSA
    model_plain: GPS + GFSA
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.04234'
    title: Graph Convolutions Enrich the Self-Attention in Transformers!
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.6593
    - null
    - null
    metric_stds:
    - 0.0094
    - null
    - null
  - model: MixHop-GCN
    model_plain: MixHop-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.02156'
    title: Probabilistically Rewired Message-Passing Neural Networks
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6592
    - null
    - null
    metric_stds:
    - 0.0036
    - null
    - null
  - model: + NeuralAtoms
    model_plain: + NeuralAtoms
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.01519'
    title: 'ReHub: Linear Complexity Graph Transformers with Adaptive Hub-Spoke Reassignment'
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6591
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
  - model: GatedGCN + Neural Atoms
    model_plain: GatedGCN + Neural Atoms
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.01276'
    title: 'Neural Atoms: Propagating Long-range Interaction in Molecular Graphs through
      Efficient Communication Channel'
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6591
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
  - model: I-MLE
    model_plain: I-MLE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.18917'
    title: 'GraIP: A Benchmarking Framework For Neural Graph Inverse Problems'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.659
    - null
    - null
    metric_stds:
    - 0.012
    - null
    - null
  - model: GPS+Hodge1Lap
    model_plain: GPS+Hodge1Lap
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.19285'
    title: Facilitating Graph Neural Networks with Random Walk on Simplicial Complexes
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6584
    - null
    - null
    metric_stds:
    - 0.0033
    - null
    - null
  - model: GPSE-abs (default)
    model_plain: GPSE-abs (default)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6584
    - null
    - null
    metric_stds:
    - 0.0042
    - null
    - null
  - model: Graph-Mamba
    model_plain: Graph-Mamba
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.285
    arxiv_id: '2402.00789'
    title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling with Selective
      State Spaces'
    date: '2024-02-01'
    date_iso: '2024-02-01'
    date_display: Feb 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6581
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: ViT-PS
    model_plain: ViT-PS
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.02866'
    title: Learning Probabilistic Symmetrization for Architecture Agnostic Equivariance
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.6575
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: 7-ℓGIN
    model_plain: 7-ℓGIN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.13749'
    title: 'Weisfeiler and Leman Go Loopy: A New Hierarchy for Graph Representational
      Learning'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.657
    - null
    - 0.2513
    metric_stds:
    - 0.006
    - null
    - 0.0021
  - model: 7-\ell{}GIN
    model_plain: 7-\ell{}GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.13749'
    title: 'Weisfeiler and Leman Go Loopy: A New Hierarchy for Graph Representational
      Learning'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.657
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
  - model: CIN
    model_plain: CIN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.03561'
    title: 'CIN++: Enhancing Topological Message Passing'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6569
    - null
    - null
    metric_stds:
    - 0.0117
    - null
    - null
  - model: GatedGCN
    model_plain: GatedGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.03113'
    title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs with Walk-Based
      Centrality'
    date: Jan 2025
    date_iso: 2025-01
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6558
    - null
    - null
    metric_stds:
    - 0.0068
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
    date: '2024-05-22'
    date_iso: '2024-05-22'
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6547
    - null
    - null
    metric_stds:
    - 0.0048
    - null
    - null
  - model: MAGNA
    model_plain: MAGNA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6541
    - null
    - null
    metric_stds:
    - 0.0038
    - null
    - null
  - model: GPS w/ Transformer
    model_plain: GPS w/ Transformer
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
    - 0.6535
    - null
    - null
    metric_stds:
    - 0.0041
    - null
    - null
  - model: GPS
    model_plain: GPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.19285'
    title: Facilitating Graph Neural Networks with Random Walk on Simplicial Complexes
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6535
    - null
    - null
    metric_stds:
    - 0.0041
    - null
    - null
  - model: GraphGPS+LapPE
    model_plain: GraphGPS+LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.02156'
    title: Probabilistically Rewired Message-Passing Neural Networks
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6535
    - null
    - null
    metric_stds:
    - 0.0041
    - null
    - null
  - model: GPS + (RWSE/LapPE)
    model_plain: GPS + (RWSE/LapPE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6535
    - null
    - null
    metric_stds:
    - 0.0041
    - null
    - null
  - model: GraphGPS
    model_plain: GraphGPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.02866'
    title: Learning Probabilistic Symmetrization for Architecture Agnostic Equivariance
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6535
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: Graph transformer
    model_plain: Graph transformer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.03815'
    title: k-Maximum Inner Product Attention for Graph Transformers and the Expressive
      Power of GraphGPS
    date: Apr 2026
    date_iso: 2026-04
    date_display: Apr 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6534
    - null
    - null
    metric_stds:
    - 0.0091
    - null
    - null
  - model: GPS+LapPE
    model_plain: GPS+LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.05649'
    title: 'Greener GRASS: Enhancing GNNs with Encoding, Rewiring, and Attention'
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6534
    - null
    - null
    metric_stds:
    - 0.0091
    - null
    - null
  - model: GPS + k-MIP (k=1)
    model_plain: GPS + k-MIP (k=1)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.03815'
    title: k-Maximum Inner Product Attention for Graph Transformers and the Expressive
      Power of GraphGPS
    date: Apr 2026
    date_iso: 2026-04
    date_display: Apr 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6529
    - null
    - null
    metric_stds:
    - 0.0034000000000000002
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
    date: '2024-05-22'
    date_iso: '2024-05-22'
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6529
    - null
    - null
    metric_stds:
    - 0.0082
    - null
    - null
  - model: Exphormer
    model_plain: Exphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.02866'
    title: Learning Probabilistic Symmetrization for Architecture Agnostic Equivariance
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6527
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: Graphormer-AnchorGT-SPD
    model_plain: Graphormer-AnchorGT-SPD
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.03481'
    title: 'AnchorGT: Efficient and Flexible Attention Architecture for Scalable Graph
      Transformers'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.652
    - null
    - null
    metric_stds:
    - 0.0264
    - null
    - null
  - model: PST-onelayer
    model_plain: PST-onelayer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.02795'
    title: Graph as Point Set
    date: '2024-05-05'
    date_iso: '2024-05-05'
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6517
    - null
    - null
    metric_stds:
    - 0.0076
    - null
    - null
  - model: CSA-RWSE
    model_plain: CSA-RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09365'
    title: Simple Path Structural Encoding for Graph Transformers
    date: '2025-02-13'
    date_iso: '2025-02-13'
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6513
    - null
    - null
    metric_stds:
    - 0.0061
    - null
    - null
  - model: Random rewire
    model_plain: Random rewire
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.18917'
    title: 'GraIP: A Benchmarking Framework For Neural Graph Inverse Problems'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.651
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
  - model: GCN-LASER
    model_plain: GCN-LASER
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01668'
    title: Locality-Aware Graph Rewiring in GNNs
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6489
    - null
    - null
    metric_stds:
    - 0.0074
    - null
    - null
  - model: AS_0:1^SN+VS
    model_plain: AS_0:1^SN+VS
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.03380'
    title: On the Theoretical Expressive Power and the Design Space of Higher-Order
      Graph Transformers
    date: '2024-04-04'
    date_iso: '2024-04-04'
    date_display: Apr 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6486
    - null
    - null
    metric_stds:
    - 0.0063
    - null
    - null
  - model: \mathcal {AS}_{0:1}^{\mathsf {SN}}
    model_plain: \mathcal {AS}_{0:1}^{\mathsf {SN}}
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.03380'
    title: On the Theoretical Expressive Power and the Design Space of Higher-Order
      Graph Transformers
    date: '2024-04-04'
    date_iso: '2024-04-04'
    date_display: Apr 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6486
    - null
    - null
    metric_stds:
    - 0.0063
    - null
    - null
  - model: GEAET
    model_plain: GEAET
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09263'
    title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks? Simple Architectures
      Meet Excellence
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6485
    - null
    - null
    metric_stds:
    - 0.0035
    - null
    - null
  - model: GPS + BigBird
    model_plain: GPS + BigBird
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.03815'
    title: k-Maximum Inner Product Attention for Graph Transformers and the Expressive
      Power of GraphGPS
    date: Apr 2026
    date_iso: 2026-04
    date_display: Apr 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6483
    - null
    - null
    metric_stds:
    - 0.0073
    - null
    - null
  - model: 0.01 L1
    model_plain: 0.01 L1
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.11730'
    title: Stronger Graph Transformer with Regularized Attention Scores
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6477
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: DIGL+MPNN
    model_plain: DIGL+MPNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.02156'
    title: Probabilistically Rewired Message-Passing Neural Networks
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6469
    - null
    - null
    metric_stds:
    - 0.0019
    - null
    - null
  - model: 0.05 L1
    model_plain: 0.05 L1
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.11730'
    title: Stronger Graph Transformer with Regularized Attention Scores
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6468
    - null
    - null
    metric_stds:
    - 0.002
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
    - 0.6467
    - null
    - null
    metric_stds:
    - 0.0124
    - null
    - null
  - model: SAGE-LASER
    model_plain: SAGE-LASER
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01668'
    title: Locality-Aware Graph Rewiring in GNNs
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6464
    - null
    - null
    metric_stds:
    - 0.0032
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
    date: '2024-05-22'
    date_iso: '2024-05-22'
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6463
    - null
    - null
    metric_stds:
    - 0.0027
    - null
    - null
  - model: GraphGPS-AnchorGT
    model_plain: GraphGPS-AnchorGT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.03481'
    title: 'AnchorGT: Efficient and Flexible Attention Architecture for Scalable Graph
      Transformers'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.646
    - null
    - null
    metric_stds:
    - 0.0031
    - null
    - null
  - model: Policy-Learn
    model_plain: Policy-Learn
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.02565'
    title: On The Expressive Power of GNN Derivatives
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6459
    - null
    - null
    metric_stds:
    - 0.0018
    - null
    - null
  - model: MOLTOP
    model_plain: MOLTOP
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.12136'
    title: Molecular Topological Profile (MOLTOP) - Simple and Strong Baseline for
      Molecular Graph Classification
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6459
    - null
    - null
    metric_stds:
    - 0.0005
    - null
    - null
  - model: Graphormer
    model_plain: Graphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.03481'
    title: 'AnchorGT: Efficient and Flexible Attention Architecture for Scalable Graph
      Transformers'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6453
    - null
    - null
    metric_stds:
    - 0.0121
    - null
    - null
  - model: AS_0:1+attn.bias+RWSE
    model_plain: AS_0:1+attn.bias+RWSE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.03380'
    title: On the Theoretical Expressive Power and the Design Space of Higher-Order
      Graph Transformers
    date: '2024-04-04'
    date_iso: '2024-04-04'
    date_display: Apr 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6445
    - null
    - null
    metric_stds:
    - 0.0082
    - null
    - null
  - model: \mathcal {AS}_{0:1}-dense+attn.bias
    model_plain: \mathcal {AS}_{0:1}-dense+attn.bias
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.03380'
    title: On the Theoretical Expressive Power and the Design Space of Higher-Order
      Graph Transformers
    date: '2024-04-04'
    date_iso: '2024-04-04'
    date_display: Apr 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6445
    - null
    - null
    metric_stds:
    - 0.0082
    - null
    - null
  - model: LASER
    model_plain: LASER
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01668'
    title: Locality-Aware Graph Rewiring in GNNs
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.644
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
  - model: SAN+RWSE
    model_plain: SAN+RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.468
    arxiv_id: '2206.08164'
    title: LRGB
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/vijaydwivedi75/lrgb
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6439
    - null
    - null
    metric_stds:
    - 0.0075
    - null
    - null
  - model: SAN
    model_plain: SAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.16560'
    title: Algorithmic Graph Tasks
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/nec-research/Adaptive-Message-Passing
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6439
    - null
    - null
    metric_stds:
    - 0.0075
    - null
    - null
  - model: PST-gc
    model_plain: PST-gc
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.02795'
    title: Graph as Point Set
    date: '2024-05-05'
    date_iso: '2024-05-05'
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6439
    - null
    - null
    metric_stds:
    - 0.0342
    - null
    - null
  - model: Baseline
    model_plain: Baseline
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.11730'
    title: Stronger Graph Transformer with Regularized Attention Scores
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6435
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: NBA-GatedGCN
    model_plain: NBA-GatedGCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.07430'
    title: Non-backtracking Graph Neural Networks
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6429
    - null
    - null
    metric_stds:
    - 0.0062
    - null
    - null
  - model: GPS+RWSE
    model_plain: GPS+RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.04765'
    title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6427
    - null
    - null
    metric_stds:
    - 0.0035
    - null
    - null
  - model: 0.01 CE
    model_plain: 0.01 CE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.11730'
    title: Stronger Graph Transformer with Regularized Attention Scores
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6423
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: A_2^Ngbh
    model_plain: A_2^Ngbh
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.03380'
    title: On the Theoretical Expressive Power and the Design Space of Higher-Order
      Graph Transformers
    date: '2024-04-04'
    date_iso: '2024-04-04'
    date_display: Apr 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6419
    - null
    - null
    metric_stds:
    - 0.0108
    - null
    - null
  - model: Eigenformer
    model_plain: Eigenformer
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.17791'
    title: Graph Transformers without Positional Encodings
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6414
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: GPS+AllPSE
    model_plain: GPS+AllPSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6397
    - null
    - null
    metric_stds:
    - 0.0092
    - null
    - null
  - model: LASER - Not Equivariant
    model_plain: LASER - Not Equivariant
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01668'
    title: Locality-Aware Graph Rewiring in GNNs
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6385
    - null
    - null
    metric_stds:
    - 0.0048
    - null
    - null
  - model: SAN+LapPE
    model_plain: SAN+LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.531
    arxiv_id: '2206.08164'
    title: LRGB
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/vijaydwivedi75/lrgb
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6384
    - null
    - null
    metric_stds:
    - 0.0121
    - null
    - null
  - model: SAT
    model_plain: SAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6384
    - null
    - null
    metric_stds:
    - 0.0121
    - null
    - null
  - model: Subgraphormer
    model_plain: Subgraphormer
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.293
    arxiv_id: '2402.08450'
    title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via Graph
      Products'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6373
    - null
    - null
    metric_stds:
    - 0.011
    - null
    - null
  - model: MOSE
    model_plain: MOSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.02565'
    title: On The Expressive Power of GNN Derivatives
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.635
    - null
    - null
    metric_stds:
    - 0.011000000000000001
    - null
    - null
  - model: GT+MoSE_S
    model_plain: GT+MoSE_S
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.18676'
    title: Homomorphism Counts as Structural Encodings for Graph Learning
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.635
    - null
    - null
    metric_stds:
    - 0.011
    - null
    - null
  - model: A_3(connected)
    model_plain: A_3(connected)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.03380'
    title: On the Theoretical Expressive Power and the Design Space of Higher-Order
      Graph Transformers
    date: '2024-04-04'
    date_iso: '2024-04-04'
    date_display: Apr 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6329
    - null
    - null
    metric_stds:
    - 0.0117
    - null
    - null
  - model: Transformer+LapPE
    model_plain: Transformer+LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.501
    arxiv_id: '2206.08164'
    title: LRGB
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/vijaydwivedi75/lrgb
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6326
    - null
    - null
    metric_stds:
    - 0.0126
    - null
    - null
  - model: Transformer
    model_plain: Transformer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.16560'
    title: Algorithmic Graph Tasks
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/nec-research/Adaptive-Message-Passing
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6326
    - null
    - null
    metric_stds:
    - 0.0126
    - null
    - null
  - model: Transf.+LapPE
    model_plain: Transf.+LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08450'
    title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via Graph
      Products'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6326
    - null
    - null
    metric_stds:
    - 0.0126
    - null
    - null
  - model: GT
    model_plain: GT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6326
    - null
    - null
    metric_stds:
    - 0.0126
    - null
    - null
  - model: Eigenformer (feat.)
    model_plain: Eigenformer (feat.)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.17791'
    title: Graph Transformers without Positional Encodings
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6317
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: GPSE + GCN
    model_plain: GPSE + GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6316
    - null
    - null
    metric_stds:
    - 0.0085
    - null
    - null
  - model: SignNet
    model_plain: SignNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.02565'
    title: On The Expressive Power of GNN Derivatives
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6314
    - null
    - null
    metric_stds:
    - 0.0059
    - null
    - null
  - model: GT+MoSE_Omega
    model_plain: GT+MoSE_Omega
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.18676'
    title: Homomorphism Counts as Structural Encodings for Graph Learning
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.629
    - null
    - null
    metric_stds:
    - 0.011
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
    date: '2024-05-22'
    date_iso: '2024-05-22'
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6287
    - null
    - null
    metric_stds:
    - 0.0064
    - null
    - null
  - model: GAT-LASER
    model_plain: GAT-LASER
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01668'
    title: Locality-Aware Graph Rewiring in GNNs
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6271
    - null
    - null
    metric_stds:
    - 0.0052
    - null
    - null
  - model: GraphFP
    model_plain: GraphFP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.06336'
    title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale Molecular
      Representation Learning'
    date: Apr 2026
    date_iso: 2026-04
    date_display: Apr 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6267
    - null
    - null
    metric_stds:
    - 0.0073
    - null
    - null
  - model: GraphFP_CP
    model_plain: GraphFP_CP
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6267
    - null
    - null
    metric_stds:
    - 0.0073
    - null
    - null
  - model: TokenGT
    model_plain: TokenGT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.10793'
    title: An end-to-end attention-based approach for learning on graphs
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6263
    - null
    - null
    metric_stds:
    - 0.0117
    - null
    - null
  - model: Exphormer
    model_plain: Exphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.13798'
    title: Learning Graph Quantized Tokenizers
    date: '2024-10-17'
    date_iso: '2024-10-17'
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6258
    - null
    - null
    metric_stds:
    - 0.0092
    - null
    - null
  - model: GDT (RWSE)
    model_plain: GDT (RWSE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.18676'
    title: Homomorphism Counts as Structural Encodings for Graph Learning
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.625
    - null
    - null
    metric_stds:
    - 0.012
    - null
    - null
  - model: GPS
    model_plain: GPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6231
    - null
    - null
    metric_stds:
    - 0.0252
    - null
    - null
  - model: FloydNet
    model_plain: FloydNet
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.19094'
    title: 'FloydNet: A Learning Paradigm for Global Relational Reasoning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6224
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: GIN + Laplacian PE
    model_plain: GIN + Laplacian PE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.02565'
    title: On The Expressive Power of GNN Derivatives
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6218
    - null
    - null
    metric_stds:
    - 0.0055000000000000005
    - null
    - null
  - model: GCN+LapPE
    model_plain: GCN+LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6218
    - null
    - null
    metric_stds:
    - 0.0055
    - null
    - null
  - model: GPS (EN H-19-RWPE)
    model_plain: GPS (EN H-19-RWPE)
    is_baseline: false
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
    - 0.617
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
  - model: GIN-SDRF-R
    model_plain: GIN-SDRF-R
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01668'
    title: Locality-Aware Graph Rewiring in GNNs
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6131
    - null
    - null
    metric_stds:
    - 0.0084
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
    date: '2024-05-22'
    date_iso: '2024-05-22'
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6112
    - null
    - null
    metric_stds:
    - 0.0053
    - null
    - null
  - model: No-PE 0.1 L1
    model_plain: No-PE 0.1 L1
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.11730'
    title: Stronger Graph Transformer with Regularized Attention Scores
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6096
    - null
    - null
    metric_stds:
    - 0.00185
    - null
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6092
    - null
    - null
    metric_stds:
    - 0.0088
    - null
    - null
  - model: GPS (LCP-ORC)
    model_plain: GPS (LCP-ORC)
    is_baseline: false
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
    - 0.609
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
  - model: GatedGCN
    model_plain: GatedGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.16560'
    title: Algorithmic Graph Tasks
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/nec-research/Adaptive-Message-Passing
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6069
    - null
    - null
    metric_stds:
    - 0.0035
    - null
    - null
  - model: Gated + RWSE
    model_plain: Gated + RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.02758'
    title: Differential Encoding for Improved Representation Learning over Graphs
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6069
    - null
    - null
    metric_stds:
    - 0.0035
    - null
    - null
  - model: GatedGCN+LapPE
    model_plain: GatedGCN+LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.02156'
    title: Probabilistically Rewired Message-Passing Neural Networks
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6069
    - null
    - null
    metric_stds:
    - 0.0035
    - null
    - null
  - model: GatedGCN+RWSE
    model_plain: GatedGCN+RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.02866'
    title: Learning Probabilistic Symmetrization for Architecture Agnostic Equivariance
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6069
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: GatedGCN+GPSE
    model_plain: GatedGCN+GPSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.02156'
    title: Probabilistically Rewired Message-Passing Neural Networks
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6069
    - null
    - null
    metric_stds:
    - 0.0035
    - null
    - null
  - model: GIN + RWSE
    model_plain: GIN + RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.02565'
    title: On The Expressive Power of GNN Derivatives
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6067
    - null
    - null
    metric_stds:
    - 0.0069
    - null
    - null
  - model: R-GCN (RWSE)
    model_plain: R-GCN (RWSE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    date_iso: '2023-07-14'
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6067
    - null
    - null
    metric_stds:
    - 0.0069
    - null
    - null
  - model: GCN (Norm. H-20-LAPE)
    model_plain: GCN (Norm. H-20-LAPE)
    is_baseline: false
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
    - 0.604
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
  - model: GPS (LCP-FRC)
    model_plain: GPS (LCP-FRC)
    is_baseline: false
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
    - 0.604
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
  - model: GCN + PANDA
    model_plain: GCN + PANDA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.06777'
    title: Asynchronous Message Passing for Addressing Oversquashing in Graph Neural
      Networks
    date: Sep 2025
    date_iso: 2025-09
    date_display: Sep 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6028
    - null
    - null
    metric_stds:
    - 0.0031
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
    date: '2024-05-22'
    date_iso: '2024-05-22'
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6023
    - null
    - null
    metric_stds:
    - 0.0027
    - null
    - null
  - model: GraphCON
    model_plain: GraphCON
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.6022
    - null
    - null
    metric_stds:
    - 0.0068
    - null
    - null
  - model: GCN (Hodge H-20-LAPE)
    model_plain: GCN (Hodge H-20-LAPE)
    is_baseline: false
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
    - 0.602
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
  - model: BORF
    model_plain: BORF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01668'
    title: Locality-Aware Graph Rewiring in GNNs
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6012
    - null
    - null
    metric_stds:
    - 0.0031
    - null
    - null
  - model: GatedGCN+EdgeRWSE
    model_plain: GatedGCN+EdgeRWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.19285'
    title: Facilitating Graph Neural Networks with Random Walk on Simplicial Complexes
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6002
    - null
    - null
    metric_stds:
    - 0.0048
    - null
    - null
  - model: GCN + Neural Atoms
    model_plain: GCN + Neural Atoms
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.01276'
    title: 'Neural Atoms: Propagating Long-range Interaction in Molecular Graphs through
      Efficient Communication Channel'
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5996
    - null
    - null
    metric_stds:
    - 0.0033
    - null
    - null
  - model: GCN + BORF
    model_plain: GCN + BORF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.06777'
    title: Asynchronous Message Passing for Addressing Oversquashing in Graph Neural
      Networks
    date: Sep 2025
    date_iso: 2025-09
    date_display: Sep 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5993999999999999
    - null
    - null
    metric_stds:
    - 0.0037
    - null
    - null
  - model: GPS (20-LAPE)
    model_plain: GPS (20-LAPE)
    is_baseline: false
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
    - 0.599
    - null
    - null
    metric_stds:
    - 0.011
    - null
    - null
  - model: A-DGN
    model_plain: A-DGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.5975
    - null
    - null
    metric_stds:
    - 0.0044
    - null
    - null
  - model: SAGE
    model_plain: SAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01668'
    title: Locality-Aware Graph Rewiring in GNNs
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5971
    - null
    - null
    metric_stds:
    - 0.0041
    - null
    - null
  - model: PSDS
    model_plain: PSDS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.02795'
    title: Graph as Point Set
    date: '2024-05-05'
    date_iso: '2024-05-05'
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5965
    - null
    - null
    metric_stds:
    - 0.0064
    - null
    - null
  - model: d-DRFWL(2) GNN
    model_plain: d-DRFWL(2) GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.04941'
    title: Distance-Restricted Folklore Weisfeiler-Leman GNNs with Provable Cycle
      Counting Power
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5953
    - null
    - null
    metric_stds:
    - 0.0048
    - null
    - null
  - model: GCN + FoSR
    model_plain: GCN + FoSR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.06777'
    title: Asynchronous Message Passing for Addressing Oversquashing in Graph Neural
      Networks
    date: Sep 2025
    date_iso: 2025-09
    date_display: Sep 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5947
    - null
    - null
    metric_stds:
    - 0.0034999999999999996
    - null
    - null
  - model: SDRF
    model_plain: SDRF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01668'
    title: Locality-Aware Graph Rewiring in GNNs
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5947
    - null
    - null
    metric_stds:
    - 0.0035
    - null
    - null
  - model: FOSR
    model_plain: FOSR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01668'
    title: Locality-Aware Graph Rewiring in GNNs
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5947
    - null
    - null
    metric_stds:
    - 0.0027
    - null
    - null
  - model: GPS (19-RWPE)
    model_plain: GPS (19-RWPE)
    is_baseline: false
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
    - 0.594
    - null
    - null
    metric_stds:
    - 0.011
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
    - 0.593
    - null
    - null
    metric_stds:
    - 0.009
    - null
    - null
  - model: Kipf et al.
    model_plain: Kipf et al.
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.13749'
    title: 'Weisfeiler and Leman Go Loopy: A New Hierarchy for Graph Representational
      Learning'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.593
    - null
    - 0.3496
    metric_stds:
    - 0.0023
    - null
    - 0.0013
  - model: Hu et al.
    model_plain: Hu et al.
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.13749'
    title: 'Weisfeiler and Leman Go Loopy: A New Hierarchy for Graph Representational
      Learning'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.593
    - null
    - 0.3496
    metric_stds:
    - 0.0023
    - null
    - 0.0013
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.02866'
    title: Learning Probabilistic Symmetrization for Architecture Agnostic Equivariance
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.593
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: Kipf et al. (GCN)
    model_plain: Kipf et al. (GCN)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.13749'
    title: 'Weisfeiler and Leman Go Loopy: A New Hierarchy for Graph Representational
      Learning'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.593
    - null
    - null
    metric_stds:
    - 0.0023
    - null
    - null
  - model: Hu et al. (Graphormer-like/Strategies)
    model_plain: Hu et al. (Graphormer-like/Strategies)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.13749'
    title: 'Weisfeiler and Leman Go Loopy: A New Hierarchy for Graph Representational
      Learning'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.593
    - null
    - null
    metric_stds:
    - 0.0023
    - null
    - null
  - model: GatedGCN+Hodge1Lap
    model_plain: GatedGCN+Hodge1Lap
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.19285'
    title: Facilitating Graph Neural Networks with Random Walk on Simplicial Complexes
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5926
    - null
    - null
    metric_stds:
    - 0.0059
    - null
    - null
  - model: SAGE-SDRF-R
    model_plain: SAGE-SDRF-R
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01668'
    title: Locality-Aware Graph Rewiring in GNNs
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5892
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
  - model: GINE + LapPE
    model_plain: GINE + LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.07430'
    title: Non-backtracking Graph Neural Networks
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5877
    - null
    - null
    metric_stds:
    - 0.0044
    - null
    - null
  - model: AS_0:1^SN
    model_plain: AS_0:1^SN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.03380'
    title: On the Theoretical Expressive Power and the Design Space of Higher-Order
      Graph Transformers
    date: '2024-04-04'
    date_iso: '2024-04-04'
    date_display: Apr 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5876
    - null
    - null
    metric_stds:
    - 0.0079
    - null
    - null
  - model: BS-KAGCN
    model_plain: BS-KAGCN
    is_baseline: false
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
    - 0.5871
    - null
    - null
    metric_stds:
    - 0.0102
    - null
    - null
  - model: No-PE Baseline
    model_plain: No-PE Baseline
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.11730'
    title: Stronger Graph Transformer with Regularized Attention Scores
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5866
    - null
    - null
    metric_stds:
    - 0.0184
    - null
    - null
  - model: Bresson et al.
    model_plain: Bresson et al.
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.13749'
    title: 'Weisfeiler and Leman Go Loopy: A New Hierarchy for Graph Representational
      Learning'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5864
    - null
    - 0.342
    metric_stds:
    - 0.0077
    - null
    - 0.0013
  - model: GatedGCN
    model_plain: GatedGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.02866'
    title: Learning Probabilistic Symmetrization for Architecture Agnostic Equivariance
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5864
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: GPS + BigBird
    model_plain: GPS + BigBird
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08678'
    title: 'Graph Mamba: Towards Learning on Graphs with State Space Models'
    date: '2024-02-13'
    date_iso: '2024-02-13'
    date_display: Feb 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5854
    - null
    - null
    metric_stds:
    - 0.0079
    - null
    - null
  - model: GCN + SDRF
    model_plain: GCN + SDRF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01668'
    title: Locality-Aware Graph Rewiring in GNNs
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5851
    - null
    - null
    metric_stds:
    - 0.0033
    - null
    - null
  - model: GNN-SSWL+
    model_plain: GNN-SSWL+
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.387
    arxiv_id: '2402.08450'
    title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via Graph
      Products'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5847
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5831
    - null
    - null
    metric_stds:
    - 0.0028
    - null
    - null
  - model: GatedGCN+RWSE
    model_plain: GatedGCN+RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.506
    arxiv_id: '2206.08164'
    title: LRGB
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/vijaydwivedi75/lrgb
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5812
    - null
    - null
    metric_stds:
    - 0.0053
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01668'
    title: Locality-Aware Graph Rewiring in GNNs
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.58
    - null
    - null
    metric_stds:
    - 0.0061
    - null
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01668'
    title: Locality-Aware Graph Rewiring in GNNs
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5799
    - null
    - null
    metric_stds:
    - 0.0006
    - null
    - null
  - model: GRAND
    model_plain: GRAND
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.5789
    - null
    - null
    metric_stds:
    - 0.0062
    - null
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
    - 0.5768
    - null
    - null
    metric_stds:
    - 0.0205
    - null
    - null
  - model: GAT-SDRF-R
    model_plain: GAT-SDRF-R
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01668'
    title: Locality-Aware Graph Rewiring in GNNs
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5756
    - null
    - null
    metric_stds:
    - 0.0037
    - null
    - null
  - model: Gumbel
    model_plain: Gumbel
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.18917'
    title: 'GraIP: A Benchmarking Framework For Neural Graph Inverse Problems'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.573
    - null
    - null
    metric_stds:
    - 0.012
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
    date: '2024-05-22'
    date_iso: '2024-05-22'
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.568
    - null
    - null
    metric_stds:
    - 0.0038
    - null
    - null
  - model: GCN + SDRF
    model_plain: GCN + SDRF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.07419'
    title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5670000000000001
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
  - model: GIN-SDRF-R
    model_plain: GIN-SDRF-R
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.07419'
    title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5670000000000001
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
  - model: + CAMP
    model_plain: + CAMP
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.06777'
    title: Asynchronous Message Passing for Addressing Oversquashing in Graph Neural
      Networks
    date: Sep 2025
    date_iso: 2025-09
    date_display: Sep 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5667
    - null
    - null
    metric_stds:
    - 0.0076
    - null
    - null
  - model: GCN (LCP-FRC)
    model_plain: GCN (LCP-FRC)
    is_baseline: false
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
    - 0.559
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
  - model: GCN (LCP-ORC)
    model_plain: GCN (LCP-ORC)
    is_baseline: false
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
    - 0.559
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
  - model: GCNII
    model_plain: GCNII
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.492
    arxiv_id: '2206.08164'
    title: LRGB
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/vijaydwivedi75/lrgb
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5543
    - null
    - null
    metric_stds:
    - 0.0078
    - null
    - null
  - model: GCN2
    model_plain: GCN2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.01519'
    title: 'ReHub: Linear Complexity Graph Transformers with Adaptive Hub-Spoke Reassignment'
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5543
    - null
    - null
    metric_stds:
    - 0.0078
    - null
    - null
  - model: GCN + PANDA
    model_plain: GCN + PANDA
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.03671'
    title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    date: '2024-06-06'
    date_iso: '2024-06-06'
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.554
    - null
    - null
    metric_stds:
    - 0.016
    - null
    - null
  - model: HGP-SL (GCN)
    model_plain: HGP-SL (GCN)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.553
    - null
    - null
    metric_stds:
    - 0.0088
    - null
    - null
  - model: Baseline (GINE)
    model_plain: Baseline (GINE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.18917'
    title: 'GraIP: A Benchmarking Framework For Neural Graph Inverse Problems'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.55
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
  - model: GIN (GINE)
    model_plain: GIN (GINE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.03481'
    title: 'AnchorGT: Efficient and Flexible Attention Architecture for Scalable Graph
      Transformers'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5498
    - null
    - null
    metric_stds:
    - 0.0079
    - null
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5498
    - null
    - null
    metric_stds:
    - 0.0079
    - null
    - null
  - model: GINE
    model_plain: GINE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.02866'
    title: Learning Probabilistic Symmetrization for Architecture Agnostic Equivariance
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5498
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: GCN (EE H-19-RWPE)
    model_plain: GCN (EE H-19-RWPE)
    is_baseline: false
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
    - 0.549
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
  - model: VIB-GSL (SAGE)
    model_plain: VIB-GSL (SAGE)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5411
    - null
    - null
    metric_stds:
    - 0.0074
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.10651'
    title: Graph Learning via Logic-Based Weisfeiler--Leman Variants and Tabularization
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.541
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
  - model: GCN (19-RWPE)
    model_plain: GCN (19-RWPE)
    is_baseline: false
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
    - 0.538
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
  - model: HGP-SL (SAGE)
    model_plain: HGP-SL (SAGE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5348
    - null
    - null
    metric_stds:
    - 0.0071
    - null
    - null
  - model: GCN (20-LAPE)
    model_plain: GCN (20-LAPE)
    is_baseline: false
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
    - 0.534
    - null
    - null
    metric_stds:
    - 0.006
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
    - 0.532
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
  - model: GTR
    model_plain: GTR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01668'
    title: Locality-Aware Graph Rewiring in GNNs
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5075
    - null
    - null
    metric_stds:
    - 0.0029
    - null
    - null
  - model: GatedGCN
    model_plain: GatedGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    arxiv_id: '2206.08164'
    title: LRGB
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/vijaydwivedi75/lrgb
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5073
    - null
    - null
    metric_stds:
    - 0.0036
    - null
    - null
  - model: GINE
    model_plain: GINE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.505
    arxiv_id: '2206.08164'
    title: LRGB
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/vijaydwivedi75/lrgb
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5003
    - null
    - null
    metric_stds:
    - 0.0042
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2206.08164'
    title: LRGB
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/vijaydwivedi75/lrgb
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4894
    - null
    - null
    metric_stds:
    - 0.0039
    - null
    - null
  - model: GCN+PhotPE
    model_plain: GCN+PhotPE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.501066
    arxiv_id: '2512.15549'
    title: Photonics-Enhanced Graph Convolutional Networks
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4886
    - null
    - null
    metric_stds:
    - 0.0052
    - null
    - null
  - model: GIN-FOSR-R
    model_plain: GIN-FOSR-R
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01668'
    title: Locality-Aware Graph Rewiring in GNNs
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4864
    - null
    - null
    metric_stds:
    - 0.0054
    - null
    - null
  - model: Random
    model_plain: Random
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01668'
    title: Locality-Aware Graph Rewiring in GNNs
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4796
    - null
    - null
    metric_stds:
    - 0.0067
    - null
    - null
  - model: GCN+LapPE
    model_plain: GCN+LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.501066
    arxiv_id: '2512.15549'
    title: Photonics-Enhanced Graph Convolutional Networks
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4776
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
  - model: VIB-GSL (GCN)
    model_plain: VIB-GSL (GCN)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4761
    - null
    - null
    metric_stds:
    - 0.0093
    - null
    - null
  - model: SAGE-FOSR-R
    model_plain: SAGE-FOSR-R
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01668'
    title: Locality-Aware Graph Rewiring in GNNs
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4678
    - null
    - null
    metric_stds:
    - 0.0068
    - null
    - null
  - model: GCN + FoSR
    model_plain: GCN + FoSR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01668'
    title: Locality-Aware Graph Rewiring in GNNs
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4629
    - null
    - null
    metric_stds:
    - 0.0071
    - null
    - null
  - model: GCN + BORF
    model_plain: GCN + BORF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.03671'
    title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    date: '2024-06-06'
    date_iso: '2024-06-06'
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.456
    - null
    - null
    metric_stds:
    - 0.015
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4559
    - null
    - null
    metric_stds:
    - 0.0035
    - null
    - null
  - model: GAT-FOSR-R
    model_plain: GAT-FOSR-R
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01668'
    title: Locality-Aware Graph Rewiring in GNNs
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4515
    - null
    - null
    metric_stds:
    - 0.0044
    - null
    - null
  - model: GT-E
    model_plain: GT-E
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.18676'
    title: Homomorphism Counts as Structural Encodings for Graph Learning
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.447
    - null
    - null
    metric_stds:
    - 0.017
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.03671'
    title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    date: '2024-06-06'
    date_iso: '2024-06-06'
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.442
    - null
    - null
    metric_stds:
    - 0.015
    - null
    - null
  - model: GCN + SDRF
    model_plain: GCN + SDRF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.03671'
    title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    date: '2024-06-06'
    date_iso: '2024-06-06'
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.439
    - null
    - null
    metric_stds:
    - 0.016
    - null
    - null
  - model: EGP (GIN)
    model_plain: EGP (GIN)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.07419'
    title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.429
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
  - model: VIB-GSL (GAT)
    model_plain: VIB-GSL (GAT)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4264
    - null
    - null
    metric_stds:
    - 0.0033
    - null
    - null
  - model: GraphMLPMixer
    model_plain: GraphMLPMixer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.04765'
    title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4225
    - null
    - null
    metric_stds:
    - 0.0095
    - null
    - null
  - model: MLP
    model_plain: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.03561'
    title: 'CIN++: Enhancing Topological Message Passing'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.406
    - null
    - null
    metric_stds:
    - 0.0021
    - null
    - null
  - model: Exphormer
    model_plain: Exphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.04765'
    title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4003
    - null
    - null
    metric_stds:
    - 0.0058
    - null
    - null
  - model: APPNP
    model_plain: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.04765'
    title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3964
    - null
    - null
    metric_stds:
    - 0.0022
    - null
    - null
  - model: Energy GNN + attention
    model_plain: Energy GNN + attention
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.00494'
    title: Graph Neural Networks Gone Hogwild
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.381
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: DIFFormer
    model_plain: DIFFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.04765'
    title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.381
    - null
    - null
    metric_stds:
    - 0.0013
    - null
    - null
  - model: SGFormer
    model_plain: SGFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.04765'
    title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3726
    - null
    - null
    metric_stds:
    - 0.0018
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.04765'
    title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3719
    - null
    - null
    metric_stds:
    - 0.0041
    - null
    - null
  - model: Graph transformer
    model_plain: Graph transformer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.04765'
    title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3622
    - null
    - null
    metric_stds:
    - 0.0036
    - null
    - null
  - model: GCN (5 layer)
    model_plain: GCN (5 layer)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.00494'
    title: Graph Neural Networks Gone Hogwild
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.362
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
    arxiv_id: '2506.04765'
    title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3614
    - null
    - null
    metric_stds:
    - 0.0036
    - null
    - null
  - model: GAT (5 layer)
    model_plain: GAT (5 layer)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.00494'
    title: Graph Neural Networks Gone Hogwild
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.355
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: Energy GNN (edge-wise)
    model_plain: Energy GNN (edge-wise)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.00494'
    title: Graph Neural Networks Gone Hogwild
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.348
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: GSD GNN
    model_plain: GSD GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.00494'
    title: Graph Neural Networks Gone Hogwild
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.343
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: Plain
    model_plain: Plain
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.10651'
    title: Graph Learning via Logic-Based Weisfeiler--Leman Variants and Tabularization
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.306
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
  - model: Maj.
    model_plain: Maj.
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.10651'
    title: Graph Learning via Logic-Based Weisfeiler--Leman Variants and Tabularization
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.306
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
  - model: Int.
    model_plain: Int.
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.10651'
    title: Graph Learning via Logic-Based Weisfeiler--Leman Variants and Tabularization
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.306
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
  - model: Graph-JEPA
    model_plain: Graph-JEPA
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 19.22
    arxiv_id: '2309.16014'
    title: Graph-level Representation Learning with Joint-Embedding Predictive Architectures
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.263
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
  - model: SAT
    model_plain: SAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.03481'
    title: 'AnchorGT: Efficient and Flexible Attention Architecture for Scalable Graph
      Transformers'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2601
    - null
    - null
    metric_stds:
    - 0.0248
    - null
    - null
  - model: Graph-JEPA \dagger
    model_plain: Graph-JEPA \dagger
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.16014'
    title: Graph-level Representation Learning with Joint-Embedding Predictive Architectures
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.252
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
  - model: IGNN (1 layer)
    model_plain: IGNN (1 layer)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.00494'
    title: Graph Neural Networks Gone Hogwild
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.211
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: GCN (NO)
    model_plain: GCN (NO)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.14864'
    title: Effective Structural Encodings via Local Curvature Profiles
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.407
    - null
    metric_stds:
    - null
    - 0.02
    - null
  - model: GCN (LA)
    model_plain: GCN (LA)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.14864'
    title: Effective Structural Encodings via Local Curvature Profiles
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.435
    - null
    metric_stds:
    - null
    - 0.018
    - null
  - model: GCN (RW)
    model_plain: GCN (RW)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.14864'
    title: Effective Structural Encodings via Local Curvature Profiles
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.432
    - null
    metric_stds:
    - null
    - 0.021
    - null
  - model: GCN (SUB)
    model_plain: GCN (SUB)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.14864'
    title: Effective Structural Encodings via Local Curvature Profiles
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.426
    - null
    metric_stds:
    - null
    - 0.02
    - null
  - model: GCN (LCP)
    model_plain: GCN (LCP)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.14864'
    title: Effective Structural Encodings via Local Curvature Profiles
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.444
    - null
    metric_stds:
    - null
    - 0.022
    - null
  - model: GIN (NO)
    model_plain: GIN (NO)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.14864'
    title: Effective Structural Encodings via Local Curvature Profiles
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.462
    - null
    metric_stds:
    - null
    - 0.022
    - null
  - model: GIN (LA)
    model_plain: GIN (LA)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.14864'
    title: Effective Structural Encodings via Local Curvature Profiles
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.488
    - null
    metric_stds:
    - null
    - 0.016
    - null
  - model: GIN (RW)
    model_plain: GIN (RW)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.14864'
    title: Effective Structural Encodings via Local Curvature Profiles
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.48
    - null
    metric_stds:
    - null
    - 0.021
    - null
  - model: GIN (SUB)
    model_plain: GIN (SUB)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.14864'
    title: Effective Structural Encodings via Local Curvature Profiles
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.473
    - null
    metric_stds:
    - null
    - 0.024
    - null
  - model: GIN (LCP)
    model_plain: GIN (LCP)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.14864'
    title: Effective Structural Encodings via Local Curvature Profiles
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.496
    - null
    metric_stds:
    - null
    - 0.022
    - null
  - model: AFR-3
    model_plain: AFR-3
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.09384'
    title: Mitigating Over-Smoothing and Over-Squashing using Augmentations of Forman-Ricci
      Curvature
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.448
    - null
    metric_stds:
    - null
    - 0.028
    - null
  - model: AFR-4
    model_plain: AFR-4
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.09384'
    title: Mitigating Over-Smoothing and Over-Squashing using Augmentations of Forman-Ricci
      Curvature
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.436
    - null
    metric_stds:
    - null
    - 0.025
    - null
  - model: BORF
    model_plain: BORF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.09384'
    title: Mitigating Over-Smoothing and Over-Squashing using Augmentations of Forman-Ricci
      Curvature
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.443
    - null
    metric_stds:
    - null
    - 0.028
    - null
  - model: None
    model_plain: None
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.09384'
    title: Mitigating Over-Smoothing and Over-Squashing using Augmentations of Forman-Ricci
      Curvature
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.405
    - null
    metric_stds:
    - null
    - 0.021
    - null
  milestones:
  - value: 0.6439
    std: 0.0075
    model: SAN+RWSE
    arxiv_id: '2206.08164'
    title: LRGB
    date: 2022-06
  - value: 0.6575
    std: null
    model: ViT-PS
    arxiv_id: '2306.02866'
    title: Learning Probabilistic Symmetrization for Architecture Agnostic Equivariance
    date: 2023-06
  - value: 0.6996
    std: 0.0076
    model: Drew-GIN
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
  - value: 0.7156
    std: 0.0058
    model: GraphGPS + HDSE
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: 2023-08
  - value: 0.721
    std: 0.0039
    model: IPR-MPNN
    arxiv_id: '2312.16560'
    title: Algorithmic Graph Tasks
    date: 2023-12
  - value: 0.7293
    std: 0.0004
    model: S4G
    arxiv_id: '2402.08678'
    title: 'Graph Mamba: Towards Learning on Graphs with State Space Models'
    date: '2024-02-13'
  - value: 0.7311
    std: 0.0066
    model: S2GCN+PE
    arxiv_id: '2405.17311'
    title: Probabilistic Graph Rewiring via Virtual Nodes
    date: 2024-05
  - value: 0.746
    std: null
    model: LightGBM (ECFP)
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: '2025-01-29'
---

