---
title: Peptides-struct
slug: peptides-struct
benchmark: LRGB
task_type: graph_regression
description: Multi-task graph regression on peptide structural properties (11 targets).
primary_metric: MAE
higher_is_better: false
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.LRGBDataset.html
stats:
  num_graphs: 15535
  avg_nodes: 150.94
  avg_edges: 307.3
  num_classes: 11
result_count: 368
best_model:
  model: ESA
  value: 0.2393
  metric: MAE
  arxiv_id: '2402.10793'
  paper_title: An end-to-end attention-based approach for learning on graphs
variants:
- slug: standard-split
  name: Standard split
  notes: 'Official random split (80/10/10). Metric: MAE (lower is better).'
  is_standard: true
  primary_metric: MAE
  higher_is_better: false
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - MAE
  rows:
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
    is_best: true
    metric_values:
    - 0.2393
    metric_stds:
    - 0.0004
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
    is_best: true
    metric_values:
    - 0.2416
    metric_stds:
    - 0.0026
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
    - 0.2421
    metric_stds:
    - 0.0016
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
    - 0.2422
    metric_stds:
    - 0.0014
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
    - 0.2422
    metric_stds:
    - 0.0007
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
    - 0.2422
    metric_stds:
    - 0.0007
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
    - 0.2424
    metric_stds:
    - 0.001
  - model: + SigGate + DropEdge
    model_plain: + SigGate + DropEdge
    is_baseline: true
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
    - 0.2428
    metric_stds:
    - 0.001
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
    - 0.2429
    metric_stds:
    - 0.0019
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
    - 0.243
    metric_stds:
    - 0.0013
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
    - 0.243
    metric_stds:
    - 0.0013
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
    - 0.2431
    metric_stds:
    - 0.0012
  - model: + SigGate
    model_plain: + SigGate
    is_baseline: true
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
    - 0.2431
    metric_stds:
    - 0.0012
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
    - 0.2431
    metric_stds:
    - 0.002
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
    - 0.2432
    metric_stds:
    - 0.0013
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
    is_best: false
    metric_values:
    - 0.2432
    metric_stds:
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
    - 0.2433
    metric_stds:
    - 0.0001
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2433
    metric_stds:
    - 0.0011
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
    - 0.2435
    metric_stds:
    - 0.0007
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
    - 0.2436
    metric_stds:
    - 0.0022
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
    - 0.2436
    metric_stds:
    - 0.0018
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
    - 0.2437
    metric_stds:
    - 0.0006
  - model: Ours
    model_plain: Ours
    is_baseline: false
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.2438
    metric_stds:
    - 0.0014
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
    - 0.2438
    metric_stds:
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
    - 0.2438
    metric_stds:
    - 0.0014
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
    - 0.244
    metric_stds:
    - 0.0001
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
    - 0.2442
    metric_stds:
    - 0.0002
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
    - 0.2446
    metric_stds:
    - 0.0026
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
    - 0.2447
    metric_stds:
    - 0.0007
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
    - 0.2449
    metric_stds:
    - 0.0018
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
    - 0.2449
    metric_stds:
    - 0.0016
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
    - 0.245
    metric_stds:
    - 0.0011
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
    - 0.245
    metric_stds:
    - 0.0017
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
    - 0.2451
    metric_stds:
    - 0.0006
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
    - 0.2452
    metric_stds:
    - 0.0018
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
    - 0.2453
    metric_stds:
    - 0.0009
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
    - 0.2453
    metric_stds:
    - 0.0025
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
    - 0.2453
    metric_stds:
    - 0.0025
  - model: ESA (3/4)
    model_plain: ESA (3/4)
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
    - 0.245329301
    metric_stds:
    - 0.000297453
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
    - 0.2454
    metric_stds:
    - 0.0003
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
    - 0.2455
    metric_stds:
    - 0.0013
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
    - 0.2455
    metric_stds:
    - 0.0013
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
    - 0.2456
    metric_stds:
    - 0.001
  - model: GCN+PE+VN
    model_plain: GCN+PE+VN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13526'
    title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2456
    metric_stds:
    - 0.001
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
    - 0.2456
    metric_stds:
    - 0.0017
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
    - 0.2457
    metric_stds:
    - 0.0013
  - model: GatedGCN+PE+VN_G
    model_plain: GatedGCN+PE+VN_G
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13526'
    title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2458
    metric_stds:
    - 0.0006
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
    - 0.2458
    metric_stds:
    - 0.0017
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
    - 0.2459
    metric_stds:
    - 0.002
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
    - 0.2459
    metric_stds:
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
    - 0.2459
    metric_stds:
    - 0.0002
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
    - 0.2459
    metric_stds:
    - 0.0007
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
    - 0.246
    metric_stds:
    - 0.0007
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
    - 0.246
    metric_stds:
    - 0.0012
  - model: GCN (6/6)
    model_plain: GCN (6/6)
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
    - 0.246
    metric_stds:
    - 0.0007
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
    - 0.2461
    metric_stds:
    - 0.0024
  - model: IPR-MPNN
    model_plain: IPR-MPNN
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
    - 0.2462
    metric_stds:
    - 0.0007
  - model: LR-GWN
    model_plain: LR-GWN
    is_baseline: false
    is_overridden: true
    override_reason: Peptides-struct MAE was reported on a x100 scale in extraction;
      corrected to the benchmark scale.
    params_millions: null
    arxiv_id: '2509.06743'
    title: Long-Range Graph Wavelet Networks
    date: Sep 2025
    date_iso: 2025-09
    date_display: Sep 2025
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.2463
    metric_stds:
    - 0.07
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
    - 0.2463
    metric_stds:
    - 0.0005
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
    - 0.2463
    metric_stds:
    - 0.0012
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
    - 0.2464
    metric_stds:
    - 0.0013
  - model: GPSE + GPS
    model_plain: GPSE + GPS
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
    - 0.2464
    metric_stds:
    - 0.0025
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
    - 0.2464
    metric_stds:
    - 0.0009
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
    - 0.2464
    metric_stds:
    - 0.0024
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
    - 0.2465
    metric_stds:
    - 0.002
  - model: GatedGCN+PE-ViT
    model_plain: GatedGCN+PE-ViT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13526'
    title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2465
    metric_stds:
    - 0.0015
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
    - 0.2466
    metric_stds:
    - 0.0012
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
    - 0.2466
    metric_stds:
    - 0.001
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
    - 0.2467
    metric_stds:
    - 0.0003
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
    - 0.2467
    metric_stds:
    - 0.0019
  - model: R-method
    model_plain: R-method
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
    - 0.247
    metric_stds:
    - 0.001
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
    - 0.247
    metric_stds:
    - 0.0015
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
    - 0.2471
    metric_stds:
    - 0.0003
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
    - 0.2471
    metric_stds:
    - 0.0007
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
    - 0.2472
    metric_stds:
    - 0.0008
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
    - 0.2472
    metric_stds:
    - 0.0009
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
    - 0.2472
    metric_stds:
    - 0.0014
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
    - 0.2473
    metric_stds:
    - 0.0017
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
    - 0.2473
    metric_stds:
    - 0.0025
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
    - 0.2473
    metric_stds:
    - 0.0013
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
    - 0.2473
    metric_stds:
    - 0.0017
  - model: GIN (10/8)
    model_plain: GIN (10/8)
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
    - 0.2473
    metric_stds:
    - 0.0017
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
    - 0.2475
    metric_stds:
    - 0.0011
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
    - 0.2475
    metric_stds:
    - 0.0015
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
    - 0.2475
    metric_stds:
    - 0.0015
  - model: Subgraphormer
    model_plain: Subgraphormer
    is_baseline: true
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
    - 0.2475
    metric_stds:
    - 0.0007
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
    - 0.2475
    metric_stds:
    - 0.0015
  - model: Graph MLP-Mixer
    model_plain: Graph MLP-Mixer
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
    - 0.2475
    metric_stds:
    - 0.0015
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.2476
    metric_stds:
    - 0.0002
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
    - 0.2477
    metric_stds:
    - 0.0009
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
    - 0.2477
    metric_stds:
    - 0.0007
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
    - 0.2477
    metric_stds:
    - 0.001
  - model: PR-MPNN
    model_plain: PR-MPNN
    is_baseline: false
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
    - 0.2477
    metric_stds:
    - 0.0005
  - model: GatedGCN+GPSE
    model_plain: GatedGCN+GPSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13526'
    title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2477
    metric_stds:
    - 0.0009
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
    - 0.2478
    metric_stds:
    - 0.0016
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
    - 0.2478
    metric_stds:
    - 0.0017
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
    - 0.2478
    metric_stds:
    - 0.0016
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
    - 0.2479
    metric_stds:
    - 0.0011
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
    - 0.248
    metric_stds:
    - 0.0025
  - model: B-method
    model_plain: B-method
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
    - 0.248
    metric_stds:
    - 0.001
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
    - 0.248
    metric_stds:
    - 0.001
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
    - 0.2481
    metric_stds:
    - 0.0013
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
    - 0.2481
    metric_stds:
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
    - 0.2482
    metric_stds:
    - 0.0019
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
    - 0.2482
    metric_stds:
    - 0.001
  - model: M
    model_plain: M
    is_baseline: false
    is_overridden: true
    override_reason: Peptides-struct MAE was reported on a x100 scale in extraction;
      corrected to the benchmark scale.
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
    date_iso: '2024-05-22'
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.2483
    metric_stds:
    - 0.11
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
    - 0.2484
    metric_stds:
    - 0.0034
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
    - 0.2485
    metric_stds:
    - 0.0015
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
    - 0.2485
    metric_stds:
    - 0.0017
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
    - 0.2485
    metric_stds:
    - 0.0009
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
    - 0.2486
    metric_stds:
    - 0.0012
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
    - 0.2486
    metric_stds:
    - 0.0007
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
    - 0.2486
    metric_stds:
    - 0.0007
  - model: GPSE + GCN
    model_plain: GPSE + GCN
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
    - 0.2487
    metric_stds:
    - 0.0011
  - model: GPS + projection
    model_plain: GPS + projection
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13526'
    title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2487
    metric_stds:
    - 0.0011
  - model: Ours(567k)
    model_plain: Ours(567k)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01704'
    title: Transformers are efficient hierarchical chemical graph learners
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2487
    metric_stds:
    - 0.0009
  - model: + DropEdge
    model_plain: + DropEdge
    is_baseline: true
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
    - 0.2488
    metric_stds:
    - 0.0015
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
    - 0.2488
    metric_stds:
    - 0.0018
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
    - 0.2488
    metric_stds:
    - 0.0017
  - model: GCN + VN
    model_plain: GCN + VN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13526'
    title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2488
    metric_stds:
    - 0.0021
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
    - 0.24888524548573923
    metric_stds:
    - 0.0013272721664974406
  - model: TokenGT (10/10)
    model_plain: TokenGT (10/10)
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
    - 0.24888524548573923
    metric_stds:
    - 0.0013272721664974406
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
    - 0.2489
    metric_stds:
    - 0.0011
  - model: + PairNorm
    model_plain: + PairNorm
    is_baseline: true
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
    - 0.2491
    metric_stds:
    - 0.0011
  - model: GraphGPS (w/ Positional Encoding, 0.01 CE)
    model_plain: GraphGPS (w/ Positional Encoding, 0.01 CE)
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
    - 0.2491
    metric_stds:
    - 0.0024
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
    - 0.2492
    metric_stds:
    - 0.0019
  - model: WaveGC
    model_plain: WaveGC
    is_baseline: true
    is_overridden: true
    override_reason: Peptides-struct MAE was reported on a x100 scale in extraction;
      corrected to the benchmark scale.
    params_millions: null
    arxiv_id: '2509.06743'
    title: Long-Range Graph Wavelet Networks
    date: Sep 2025
    date_iso: 2025-09
    date_display: Sep 2025
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.2495
    metric_stds:
    - 0.07
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
    - 0.2496
    metric_stds:
    - 0.0013
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
    - 0.2497
    metric_stds:
    - 0.0007
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
    - 0.2498
    metric_stds:
    - 0.0015
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
    - 0.2498
    metric_stds:
    - 0.0008
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
    - 0.2499
    metric_stds:
    - 0.001
  - model: GraphGPS (w/ Positional Encoding, No Reg)
    model_plain: GraphGPS (w/ Positional Encoding, No Reg)
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
    - 0.2499
    metric_stds:
    - 0.0003
  - model: Baseline (no modification)
    model_plain: Baseline (no modification)
    is_baseline: true
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
    - 0.25
    metric_stds:
    - 0.0012
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
    - 0.25
    metric_stds:
    - 0.0005
  - model: GraphGPS (w/ Positional Encoding, w/out backprop cut-off 0.01 CE)
    model_plain: GraphGPS (w/ Positional Encoding, w/out backprop cut-off 0.01 CE)
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
    - 0.25
    metric_stds:
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
    - 0.25
    metric_stds:
    - 0.0027
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
    - 0.25
    metric_stds:
    - 0.0005
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
    - 0.25
    metric_stds:
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
    - 0.2501
    metric_stds:
    - 0.0012
  - model: GRED
    model_plain: GRED
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    arxiv_id: '2312.01538'
    title: Recurrent Distance Filtering for Graph Representation Learning
    date: '2023-12-03'
    date_iso: '2023-12-03'
    date_display: Dec 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2503
    metric_stds:
    - 0.0019
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
    - 0.2503
    metric_stds:
    - 0.0016
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
    - 0.2505
    metric_stds:
    - 0.0023
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
    - 0.2505
    metric_stds:
    - 0.0014
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
    - 0.2506
    metric_stds:
    - 0.0022
  - model: GPSE + GPS
    model_plain: GPSE + GPS
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
    - 0.2506
    metric_stds:
    - 0.001
  - model: DEFT
    model_plain: DEFT
    is_baseline: true
    is_overridden: true
    override_reason: Peptides-struct MAE was reported on a x100 scale in extraction;
      corrected to the benchmark scale.
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
    date_iso: '2024-05-22'
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.2506
    metric_stds:
    - 0.13
  - model: GatedGCN+PE-Mixer
    model_plain: GatedGCN+PE-Mixer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13526'
    title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2508
    metric_stds:
    - 0.0007
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
    - 0.2509
    metric_stds:
    - 0.0014
  - model: GPS
    model_plain: GPS
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
    - 0.2509
    metric_stds:
    - 0.0014
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
    - 0.2509
    metric_stds:
    - 0.0008
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
    - 0.2509
    metric_stds:
    - 0.0014
  - model: GPS (8/6)
    model_plain: GPS (8/6)
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
    - 0.2509
    metric_stds:
    - 0.0014
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
    - 0.251
    metric_stds:
    - 0.0008
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
    - 0.251
    metric_stds:
    - 0.001
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
    - 0.251
    metric_stds:
    - 0.003
  - model: nsqure~
    model_plain: nsqure~
    is_baseline: false
    is_overridden: true
    override_reason: Peptides-struct MAE was reported on a x100 scale in extraction;
      corrected to the benchmark scale.
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.2512
    metric_stds:
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
    - 0.2512
    metric_stds:
    - 0.0025
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
    - 0.2518
    metric_stds:
    - 0.0012
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
    - 0.2519
    metric_stds:
    - 0.0033
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
    - 0.252
    metric_stds:
    - 0.003
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
    - 0.252
    metric_stds:
    - 0.003
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
    - 0.252
    metric_stds:
    - 0.003
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
    - 0.2521
    metric_stds:
    - 0.001
  - model: GatedGCN + VN
    model_plain: GatedGCN + VN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13526'
    title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2523
    metric_stds:
    - 0.0016
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
    - 0.2523
    metric_stds:
    - 0.0013
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
    - 0.2524
    metric_stds:
    - 0.0009
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
    - 0.2524
    metric_stds:
    - 0.0009
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
    - 0.2529
    metric_stds:
    - 0.0016
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
    - 0.2529
    metric_stds:
    - 0.0016
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
    - 0.2529
    metric_stds:
    - 0.0009
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
    - 0.2529
    metric_stds:
    - 0.0023
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
    - 0.2529
    metric_stds:
    - 0.0016
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
    - 0.2529
    metric_stds:
    - 0.0016
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
    - 0.253
    metric_stds:
    - 0.001
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
    - 0.253
    metric_stds:
    - 0.003
  - model: Drew-GIN
    model_plain: Drew-GIN
    is_baseline: true
    is_overridden: true
    override_reason: Peptides-struct MAE was reported on a x100 scale in extraction;
      corrected to the benchmark scale.
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.2536
    metric_stds:
    - null
  - model: DRew-GCN+LapPE
    model_plain: DRew-GCN+LapPE
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
    - 0.2536
    metric_stds:
    - 0.0015
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
    - 0.2536
    metric_stds:
    - 0.0015
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
    - 0.2536
    metric_stds:
    - 0.0015
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
    - 0.2539
    metric_stds:
    - 0.0011
  - model: SGWT
    model_plain: SGWT
    is_baseline: true
    is_overridden: true
    override_reason: Peptides-struct MAE was reported on a x100 scale in extraction;
      corrected to the benchmark scale.
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
    date_iso: '2024-05-22'
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.2539
    metric_stds:
    - 0.21
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
    - 0.2539
    metric_stds:
    - 0.0007
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
    - 0.254
    metric_stds:
    - 0.002
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
    - 0.254
    metric_stds:
    - 0.003
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
    - 0.254
    metric_stds:
    - 0.004
  - model: PathNN-SP
    model_plain: PathNN-SP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: '2023-06-09'
    date_iso: '2023-06-09'
    date_display: Jun 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.254
    metric_stds:
    - 0.0046
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
    - 0.2542
    metric_stds:
    - 0.003
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
    - 0.2545
    metric_stds:
    - 0.0012
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
    - 0.2545
    metric_stds:
    - 0.0032
  - model: SAN
    model_plain: SAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01704'
    title: Transformers are efficient hierarchical chemical graph learners
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2545
    metric_stds:
    - 0.0012
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
    - 0.2547
    metric_stds:
    - 0.0009
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
    - 0.255
    metric_stds:
    - 0.004
  - model: BNPool
    model_plain: BNPool
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.255
    metric_stds:
    - 0.001
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
    - 0.255
    metric_stds:
    - 0.0014
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
    - 0.2553
    metric_stds:
    - 0.0005
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
    - 0.2559
    metric_stds:
    - null
  - model: RWPT (Walk, k=4, l=4)
    model_plain: RWPT (Walk, k=4, l=4)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.14098'
    title: 'Toward a Graph Foundation Model: Pre-Training Transformers With Random
      Walks'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2561
    metric_stds:
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
    - 0.2562
    metric_stds:
    - 0.0037
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
    - 0.2563
    metric_stds:
    - 0.002
  - model: SEA-GWNN
    model_plain: SEA-GWNN
    is_baseline: true
    is_overridden: true
    override_reason: Peptides-struct MAE was reported on a x100 scale in extraction;
      corrected to the benchmark scale.
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
    date_iso: '2024-05-22'
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.2564
    metric_stds:
    - 0.31
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
    - 0.2564
    metric_stds:
    - 0.012
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
    - 0.2566
    metric_stds:
    - 0.0019
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
    - 0.2568
    metric_stds:
    - 0.0005
  - model: PathNN-AP
    model_plain: PathNN-AP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: '2023-06-09'
    date_iso: '2023-06-09'
    date_display: Jun 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2569
    metric_stds:
    - 0.003
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
    - 0.257
    metric_stds:
    - 0.003
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
    - 0.257
    metric_stds:
    - 0.0006
  - model: Baseline (w/out Positional Encoding)
    model_plain: Baseline (w/out Positional Encoding)
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
    - 0.257
    metric_stds:
    - 0.0015
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
    - 0.2574
    metric_stds:
    - 0.002
  - model: R-GCN (RWSE)
    model_plain: R-GCN (RWSE)
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
    - 0.2574
    metric_stds:
    - 0.002
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
    - 0.258
    metric_stds:
    - 0.003
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
    - 0.258
    metric_stds:
    - 0.003
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
    - 0.2584
    metric_stds:
    - 0.0015
  - model: GINE + VN
    model_plain: GINE + VN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13526'
    title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2584
    metric_stds:
    - 0.0011
  - model: WaveNet
    model_plain: WaveNet
    is_baseline: true
    is_overridden: true
    override_reason: Peptides-struct MAE was reported on a x100 scale in extraction;
      corrected to the benchmark scale.
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
    - 0.2588
    metric_stds:
    - 0.01
  - model: NPQ_W-P-SV
    model_plain: NPQ_W-P-SV
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.09660'
    title: Neural Priority Queues for Graph Neural Networks
    date: '2023-07-18'
    date_iso: '2023-07-18'
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2589
    metric_stds:
    - 0.0031
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
    - 0.2594
    metric_stds:
    - 0.0038
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
    - 0.2599
    metric_stds:
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
    - 0.2606
    metric_stds:
    - 0.0014
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
    - 0.2612
    metric_stds:
    - 0.0013
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
    - 0.2612
    metric_stds:
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
    - 0.2614
    metric_stds:
    - 0.0023
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
    - 0.2616
    metric_stds:
    - 0.0018
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
    - 0.2618
    metric_stds:
    - 0.0058
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
    - 0.262
    metric_stds:
    - 0.003
  - model: ECPool
    model_plain: ECPool
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.262
    metric_stds:
    - 0.006
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
    - 0.2621
    metric_stds:
    - 0.0036
  - model: BiScale-GTR (Molecule)
    model_plain: BiScale-GTR (Molecule)
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
    - 0.2621
    metric_stds:
    - 0.0022
  - model: Graph BPE (with validity/OOV handling)
    model_plain: Graph BPE (with validity/OOV handling)
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
    - 0.2621
    metric_stds:
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
    - 0.263
    metric_stds:
    - 0.003
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.263
    metric_stds:
    - 0.001
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
    - 0.2632
    metric_stds:
    - 0.0008
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
    - 0.2634
    metric_stds:
    - 0.0019
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.264
    metric_stds:
    - 0.001
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.264
    metric_stds:
    - 0.001
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
    - 0.2643
    metric_stds:
    - 0.0008
  - model: Scattering GCN
    model_plain: Scattering GCN
    is_baseline: true
    is_overridden: true
    override_reason: Peptides-struct MAE was reported on a x100 scale in extraction;
      corrected to the benchmark scale.
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
    date_iso: '2024-05-22'
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.2643
    metric_stds:
    - 0.2
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
    - 0.2645
    metric_stds:
    - 0.0023
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
    - 0.265
    metric_stds:
    - 0.003
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.265
    metric_stds:
    - 0.003
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
    - 0.2656
    metric_stds:
    - 0.0009
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
    - 0.266
    metric_stds:
    - 0.002
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.266
    metric_stds:
    - 0.0
  - model: NPQ_W
    model_plain: NPQ_W
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.09660'
    title: Neural Priority Queues for Graph Neural Networks
    date: '2023-07-18'
    date_iso: '2023-07-18'
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.267
    metric_stds:
    - 0.0009
  - model: Scattering
    model_plain: Scattering
    is_baseline: true
    is_overridden: true
    override_reason: Peptides-struct MAE was reported on a x100 scale in extraction;
      corrected to the benchmark scale.
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
    date_iso: '2024-05-22'
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.2677
    metric_stds:
    - 0.11
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
    - 0.2679
    metric_stds:
    - 0.0015
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
    - 0.2683
    metric_stds:
    - 0.0043
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
    - 0.2683
    metric_stds:
    - 0.0043
  - model: SAN
    model_plain: SAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    arxiv_id: '2405.02795'
    title: Graph as Point Set
    date: '2024-05-05'
    date_iso: '2024-05-05'
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2683
    metric_stds:
    - 0.0043
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
    - 0.2687
    metric_stds:
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
    - 0.2699
    metric_stds:
    - 0.0018
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
    - 0.2701
    metric_stds:
    - 0.0007
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
    - 0.2703
    metric_stds:
    - 0.0015
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
    - 0.2705
    metric_stds:
    - 0.0045
  - model: GWNN
    model_plain: GWNN
    is_baseline: true
    is_overridden: true
    override_reason: Peptides-struct MAE was reported on a x100 scale in extraction;
      corrected to the benchmark scale.
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
    date_iso: '2024-05-22'
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.2734
    metric_stds:
    - 0.04
  - model: GNN (a)
    model_plain: GNN (a)
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
    - 0.274
    metric_stds:
    - 0.0
  - model: WaveShrink-ChebNet
    model_plain: WaveShrink-ChebNet
    is_baseline: true
    is_overridden: true
    override_reason: Peptides-struct MAE was reported on a x100 scale in extraction;
      corrected to the benchmark scale.
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
    date_iso: '2024-05-22'
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.2745
    metric_stds:
    - 0.06
  - model: UFGConvS
    model_plain: UFGConvS
    is_baseline: true
    is_overridden: true
    override_reason: Peptides-struct MAE was reported on a x100 scale in extraction;
      corrected to the benchmark scale.
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: '2024-05-22'
    date_iso: '2024-05-22'
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.275
    metric_stds:
    - 0.21
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.276
    metric_stds:
    - 0.018
  - model: EigenPool
    model_plain: EigenPool
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.276
    metric_stds:
    - 0.002
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
    - 0.2775
    metric_stds:
    - 0.0057
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
    - 0.2778
    metric_stds:
    - 0.0018
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
    - 0.2781
    metric_stds:
    - 0.0028
  - model: HGP-SL (GCN)
    model_plain: HGP-SL (GCN)
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
    - 0.2786
    metric_stds:
    - 0.0018
  - model: HGP-SL (SAGE)
    model_plain: HGP-SL (SAGE)
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
    - 0.2794
    metric_stds:
    - 0.0058
  - model: Drew-GIN
    model_plain: Drew-GIN
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
    - 0.2799
    metric_stds:
    - 0.0016
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.28
    metric_stds:
    - 0.001
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.283
    metric_stds:
    - 0.001
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
    - 0.2842
    metric_stds:
    - 0.013
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
    - 0.2851
    metric_stds:
    - 0.0112
  - model: DBGNN
    model_plain: DBGNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.127
    arxiv_id: '2407.12419'
    title: Dirac--Bianconi Graph Neural Networks -- Enabling Non-Diffusive Long-Range
      Graph Predictions
    date: '2024-07-17'
    date_iso: '2024-07-17'
    date_display: Jul 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2864
    metric_stds:
    - 0.0046
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
    - 0.2874
    metric_stds:
    - 0.0021
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
    - 0.2921
    metric_stds:
    - 0.0023
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.295
    metric_stds:
    - 0.007
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
    - 0.2966
    metric_stds:
    - 0.0024
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
    - 0.2971
    metric_stds:
    - 0.0037
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
    - 0.2986
    metric_stds:
    - 0.0013
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
    - 0.2995
    metric_stds:
    - 0.0005
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
    - 0.3004
    metric_stds:
    - 0.0032
  - model: VIB-GSL (GCN)
    model_plain: VIB-GSL (GCN)
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
    - 0.3032
    metric_stds:
    - 0.0011
  - model: NPQ_M
    model_plain: NPQ_M
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.09660'
    title: Neural Priority Queues for Graph Neural Networks
    date: '2023-07-18'
    date_iso: '2023-07-18'
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3037
    metric_stds:
    - 0.054
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
    - 0.3043
    metric_stds:
    - 0.0019
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
    - 0.305
    metric_stds:
    - 0.002
  - model: VIB-GSL (SAGE)
    model_plain: VIB-GSL (SAGE)
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
    - 0.3063
    metric_stds:
    - 0.0014
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
    - 0.3065
    metric_stds:
    - 0.0019
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
    - 0.3074
    metric_stds:
    - 0.0029
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
    - 0.3078
    metric_stds:
    - 0.0026
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
    - 0.3078
    metric_stds:
    - 0.0026
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
    - 0.3137
    metric_stds:
    - 0.0019
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
    - 0.3137
    metric_stds:
    - 0.0019
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
    - 0.3138
    metric_stds:
    - 0.0041
  - model: NPQ_M-P
    model_plain: NPQ_M-P
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.09660'
    title: Neural Priority Queues for Graph Neural Networks
    date: '2023-07-18'
    date_iso: '2023-07-18'
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3141
    metric_stds:
    - 0.0049
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
    - 0.3162
    metric_stds:
    - 0.0032
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
    - 0.3173
    metric_stds:
    - 0.0007
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
    - 0.318
    metric_stds:
    - 0.01
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
    - 0.318
    metric_stds:
    - 0.01
  - model: GCN
    model_plain: GCN
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
    - 0.3234
    metric_stds:
    - 0.0006
  - model: GCN+LapPE
    model_plain: GCN+LapPE
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
    - 0.325
    metric_stds:
    - 0.018
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
    - 0.3272
    metric_stds:
    - 0.0001
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
    - 0.3297
    metric_stds:
    - 0.0085
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
    - 0.335
    metric_stds:
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
    - 0.3357
    metric_stds:
    - 0.0006
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
    - 0.3357
    metric_stds:
    - 0.0006
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
    - 0.3357
    metric_stds:
    - 0.0006
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
    - 0.3357
    metric_stds:
    - 0.0006
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
    - 0.3369
    metric_stds:
    - 0.0026
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
    - 0.3374
    metric_stds:
    - 0.0011
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
    - 0.3382
    metric_stds:
    - 0.0019
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
    - 0.339
    metric_stds:
    - 0.007
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
    - 0.3394
    metric_stds:
    - 0.0012
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
    - 0.3404
    metric_stds:
    - 0.0015
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
    - 0.3408
    metric_stds:
    - 0.0011
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
    - 0.3418
    metric_stds:
    - 0.0015
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
    - 0.342
    metric_stds:
    - 0.0013
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
    - 0.3422
    metric_stds:
    - 0.0008
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
    - 0.344
    metric_stds:
    - 0.009
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
    - 0.3471
    metric_stds:
    - 0.001
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
    - 0.3471
    metric_stds:
    - 0.001
  - model: GCN + FoSR
    model_plain: GCN + FoSR
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
    - 0.3473
    metric_stds:
    - 0.0007
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
    - 0.3478
    metric_stds:
    - 0.0013
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
    - 0.348
    metric_stds:
    - 0.0007
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
    - 0.3493
    metric_stds:
    - 0.0007
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
    - 0.3496
    metric_stds:
    - 0.0013
  - model: None
    model_plain: None
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
    - 0.3496
    metric_stds:
    - 0.0013
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.35
    metric_stds:
    - 0.002
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
    - 0.3506
    metric_stds:
    - 0.0011
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
    - 0.3514
    metric_stds:
    - 0.0009
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.352
    metric_stds:
    - 0.017
  - model: Baseline
    model_plain: Baseline
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.09660'
    title: Neural Priority Queues for Graph Neural Networks
    date: '2023-07-18'
    date_iso: '2023-07-18'
    date_display: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.353
    metric_stds:
    - 0.0019
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.354
    metric_stds:
    - 0.019
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
    - 0.3547
    metric_stds:
    - 0.0045
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
    - 0.3547
    metric_stds:
    - 0.0045
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: '2023-06-09'
    date_iso: '2023-06-09'
    date_display: Jun 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3547
    metric_stds:
    - 0.0045
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
    - 0.355
    metric_stds:
    - 0.005
  - model: GatedGCN + PairNorm
    model_plain: GatedGCN + PairNorm
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13526'
    title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3551
    metric_stds:
    - 0.0008
  - model: GatedGCN with PairNorm
    model_plain: GatedGCN with PairNorm
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13526'
    title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3551
    metric_stds:
    - 0.0008
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.356
    metric_stds:
    - 0.014
  - model: GCN + Pairnorm
    model_plain: GCN + Pairnorm
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13526'
    title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3562
    metric_stds:
    - 0.0007
  - model: GatedGCN + mean
    model_plain: GatedGCN + mean
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13526'
    title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3566
    metric_stds:
    - 0.0007
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
    - 0.3566
    metric_stds:
    - 0.0014
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.36
    metric_stds:
    - 0.016
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.361
    metric_stds:
    - 0.022
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
    - 0.3618
    metric_stds:
    - 0.001
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.364
    metric_stds:
    - 0.021
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
    - 0.3647
    metric_stds:
    - 0.0028
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
    - 0.366
    metric_stds:
    - null
  - model: Energy GNN (edge-wise)
    model_plain: Energy GNN (edge-wise)
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
    - 0.367
    metric_stds:
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.368
    metric_stds:
    - 0.023
  - model: SAGE
    model_plain: SAGE
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
    - 0.3716
    metric_stds:
    - 0.0011
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
    - 0.375
    metric_stds:
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.375
    metric_stds:
    - 0.02
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.379
    metric_stds:
    - 0.013
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.387
    metric_stds:
    - 0.023
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.509
    arxiv_id: '2512.15549'
    title: Photonics-Enhanced Graph Convolutional Networks
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.395
    metric_stds:
    - 0.0017
  - model: VIB-GSL (GAT)
    model_plain: VIB-GSL (GAT)
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
    - 0.3992
    metric_stds:
    - 0.0129
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
    - 0.402
    metric_stds:
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
    - 0.4231
    metric_stds:
    - 0.0049
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
    - 0.426
    metric_stds:
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
    - 0.4345
    metric_stds:
    - 0.0026
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
    - 0.4347
    metric_stds:
    - 0.0033
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
    - 0.4351
    metric_stds:
    - 0.0008
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
    - 0.4374
    metric_stds:
    - 0.005
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
    - 0.4375
    metric_stds:
    - 0.0036
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
    - 0.4492
    metric_stds:
    - 0.0002
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
    - 0.454
    metric_stds:
    - 0.027
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
    - 0.4541
    metric_stds:
    - 0.0005
  - model: GINE
    model_plain: GINE
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
    - 0.6346
    metric_stds:
    - 0.0071
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
    - 0.6473
    metric_stds:
    - 0.0849
  milestones:
  - value: 0.2529
    std: 0.0016
    model: Transformer+LapPE
    arxiv_id: '2206.08164'
    title: LRGB
    date: 2022-06
  - value: 0.2481
    std: null
    model: Exphormer
    arxiv_id: '2306.02866'
    title: Learning Probabilistic Symmetrization for Architecture Agnostic Equivariance
    date: 2023-06
  - value: 0.2453
    std: 0.0025
    model: MGT+WavePE
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: 2023-08
  - value: 0.2424
    std: 0.001
    model: NBA-GCN+LapPE
    arxiv_id: '2310.07430'
    title: Non-backtracking Graph Neural Networks
    date: 2023-10
  - value: 0.2416
    std: 0.0026
    model: GRPE-FFGT
    arxiv_id: '2311.04653'
    title: Hybrid Focal and Full-Range Attention Based Graph Transformers
    date: 2023-11
  - value: 0.2393
    std: 0.0004
    model: ESA
    arxiv_id: '2402.10793'
    title: An end-to-end attention-based approach for learning on graphs
    date: 2024-02
---

