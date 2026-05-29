---
title: Coauthor-Physics
slug: coauthor-physics
benchmark: Classic
task_type: node_classification
description: Co-authorship graph (Physics) node classification from the "Pitfalls
  of Graph Neural Network Evaluation" paper.
primary_metric: Accuracy
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.Coauthor.html
stats: null
result_count: 153
best_model:
  model: DAM-GT
  value: 0.974
  metric: Accuracy
  arxiv_id: '2505.17660'
  paper_title: 'DAM-GT: Dual Positional Encoding-Based Attention Masking Graph Transformer
    for Node Classification'
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
  - Hits@50
  rows:
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
    is_best: true
    metric_values:
    - 0.974
    - null
    metric_stds:
    - 0.0004
    - null
  - model: NAGphormer
    model_plain: NAGphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2303.06147'
    title: 'Exphormer: Sparse Transformers for Graphs'
    date: Mar 10, 2023
    date_iso: '2023-03-10'
    date_display: Mar 2023
    codebase_url: https://github.com/hamed1375/Exphormer
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9734
    - null
    metric_stds:
    - 0.0003
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
    is_best: true
    metric_values:
    - 0.9734
    - null
    metric_stds:
    - 0.0004
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
    - 0.9719
    - null
    metric_stds:
    - 0.0004
    - null
  - model: Exphormer
    model_plain: Exphormer
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2303.06147'
    title: 'Exphormer: Sparse Transformers for Graphs'
    date: Mar 10, 2023
    date_iso: '2023-03-10'
    date_display: Mar 2023
    codebase_url: https://github.com/hamed1375/Exphormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9716
    - null
    metric_stds:
    - 0.0013
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
    - 0.9694
    - null
    metric_stds:
    - 0.0006
    - null
  - model: GPRGNN
    model_plain: GPRGNN
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
    - 0.9685
    - null
    metric_stds:
    - 0.0008
    - null
  - model: GraphGPS
    model_plain: GraphGPS
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
    - 0.9677
    - null
    metric_stds:
    - 0.0006
    - null
  - model: SGFormer
    model_plain: SGFormer
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
    - 0.9671
    - null
    metric_stds:
    - 0.0006
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
    - 0.9655
    - null
    metric_stds:
    - 0.0007
    - null
  - model: APPNP
    model_plain: APPNP
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
    - 0.9654
    - null
    metric_stds:
    - 0.0007
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
    - 0.9647
    - null
    metric_stds:
    - 0.0004
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
    - 0.9643
    - null
    metric_stds:
    - 0.0005
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
    - 0.9633
    - null
    metric_stds:
    - 0.0013
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
    - 0.9629
    - null
    metric_stds:
    - 0.0004
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
    - 0.9627
    - null
    metric_stds:
    - 0.0003
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
    - 0.9625
    - null
    metric_stds:
    - 0.0005
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
    - 0.9623
    - null
    metric_stds:
    - 0.0001
    - null
  - model: GCN
    model_plain: GCN
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
    - 0.9618
    - null
    metric_stds:
    - 0.0007
    - null
  - model: GAT
    model_plain: GAT
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
    - 0.9617
    - null
    metric_stds:
    - 0.0008
    - null
  - model: GREET
    model_plain: GREET
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
    - 0.9605
    - null
    metric_stds:
    - 0.0012
    - null
  - model: rLap
    model_plain: rLap
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.04004'
    title: Randomized Schur Complement Views for Graph Contrastive Learning
    date: Jun 6, 2023
    date_iso: '2023-06-06'
    date_display: Jun 2023
    codebase_url: https://github.com/kvignesh1420/rlap
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.9583
    - null
    metric_stds:
    - 0.0044
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
    - 0.9581
    - null
    metric_stds:
    - 0.0006
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
    - 0.9581
    - null
    metric_stds:
    - 0.0005
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
    - 0.958
    - null
    metric_stds:
    - 0.001
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
    - 0.9578
    - null
    metric_stds:
    - 0.0011
    - null
  - model: GRACE
    model_plain: GRACE
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
    - 0.9574
    - null
    metric_stds:
    - 0.0006
    - null
  - model: Sp^2GCL + PiNGDA
    model_plain: Sp^2GCL + PiNGDA
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
    - 0.9574
    - null
    metric_stds:
    - 0.0004
    - null
  - model: SP^2GCL
    model_plain: SP^2GCL
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
    - 0.9573
    - null
    metric_stds:
    - 0.0004
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
    - 0.957
    - null
    metric_stds:
    - 0.002
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
    - 0.9564
    - null
    metric_stds:
    - 0.001
    - null
  - model: NodeDropping
    model_plain: NodeDropping
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.04004'
    title: Randomized Schur Complement Views for Graph Contrastive Learning
    date: Jun 6, 2023
    date_iso: '2023-06-06'
    date_display: Jun 2023
    codebase_url: https://github.com/kvignesh1420/rlap
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.9563
    - null
    metric_stds:
    - 0.0032
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
    - 0.9563
    - null
    metric_stds:
    - 0.001
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
    - 0.956
    - null
    metric_stds:
    - 0.003
    - null
  - model: EdgeDroppingEVC
    model_plain: EdgeDroppingEVC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.04004'
    title: Randomized Schur Complement Views for Graph Contrastive Learning
    date: Jun 6, 2023
    date_iso: '2023-06-06'
    date_display: Jun 2023
    codebase_url: https://github.com/kvignesh1420/rlap
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.956
    - null
    metric_stds:
    - 0.0037
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
    - 0.956
    - null
    metric_stds:
    - 0.002
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
    - 0.9557
    - null
    metric_stds:
    - 0.0021
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
    - 0.9557
    - null
    metric_stds:
    - 0.0021
    - null
  - model: EdgeAddition
    model_plain: EdgeAddition
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.04004'
    title: Randomized Schur Complement Views for Graph Contrastive Learning
    date: Jun 6, 2023
    date_iso: '2023-06-06'
    date_display: Jun 2023
    codebase_url: https://github.com/kvignesh1420/rlap
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.9553
    - null
    metric_stds:
    - 0.0035
    - null
  - model: GCA
    model_plain: GCA
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
    - 0.9552
    - null
    metric_stds:
    - 0.0021
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
    - 0.9551
    - null
    metric_stds:
    - 0.0008
    - null
  - model: EdgeDroppingPR
    model_plain: EdgeDroppingPR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.04004'
    title: Randomized Schur Complement Views for Graph Contrastive Learning
    date: Jun 6, 2023
    date_iso: '2023-06-06'
    date_display: Jun 2023
    codebase_url: https://github.com/kvignesh1420/rlap
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.9551
    - null
    metric_stds:
    - 0.0025
    - null
  - model: GAT
    model_plain: GAT
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
    - 0.9551
    - null
    metric_stds:
    - 0.0016
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
    - 0.955
    - null
    metric_stds:
    - 0.002
    - null
  - model: GCN
    model_plain: GCN
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
    - 0.955
    - null
    metric_stds:
    - 0.0024
    - null
  - model: BGRL
    model_plain: BGRL
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
    - 0.9548
    - null
    metric_stds:
    - 0.0008
    - null
  - model: EdgeDroppingDegree
    model_plain: EdgeDroppingDegree
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.04004'
    title: Randomized Schur Complement Views for Graph Contrastive Learning
    date: Jun 6, 2023
    date_iso: '2023-06-06'
    date_display: Jun 2023
    codebase_url: https://github.com/kvignesh1420/rlap
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.9547
    - null
    metric_stds:
    - 0.0038
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
    - 0.954
    - null
    metric_stds:
    - 0.001
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
    - 0.9538
    - null
    metric_stds:
    - 0.0006
    - null
  - model: SUGRL
    model_plain: SUGRL
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
    - 0.9538
    - null
    metric_stds:
    - 0.0011
    - null
  - model: MVGRL
    model_plain: MVGRL
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
    - 0.9533
    - null
    metric_stds:
    - 0.0003
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
    - 0.953
    - null
    metric_stds:
    - 0.003
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
    - 0.953
    - null
    metric_stds:
    - 0.0032
    - null
  - model: GRACE
    model_plain: GRACE
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
    - 0.9521
    - null
    metric_stds:
    - 0.001
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
    - 0.952
    - null
    metric_stds:
    - 0.002
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
    - 0.952
    - null
    metric_stds:
    - 0.001
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
    - 0.952
    - null
    metric_stds:
    - 0.001
    - null
  - model: MarkovDiffusion
    model_plain: MarkovDiffusion
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.04004'
    title: Randomized Schur Complement Views for Graph Contrastive Learning
    date: Jun 6, 2023
    date_iso: '2023-06-06'
    date_display: Jun 2023
    codebase_url: https://github.com/kvignesh1420/rlap
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.9513
    - null
    metric_stds:
    - 0.0043
    - null
  - model: RandomWalkSubgraph
    model_plain: RandomWalkSubgraph
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.04004'
    title: Randomized Schur Complement Views for Graph Contrastive Learning
    date: Jun 6, 2023
    date_iso: '2023-06-06'
    date_display: Jun 2023
    codebase_url: https://github.com/kvignesh1420/rlap
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.9512
    - null
    metric_stds:
    - 0.0033
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
    - 0.9512
    - null
    metric_stds:
    - 0.0027
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
    - 0.9512
    - null
    metric_stds:
    - 0.0015
    - null
  - model: PPRDiffusion
    model_plain: PPRDiffusion
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.04004'
    title: Randomized Schur Complement Views for Graph Contrastive Learning
    date: Jun 6, 2023
    date_iso: '2023-06-06'
    date_display: Jun 2023
    codebase_url: https://github.com/kvignesh1420/rlap
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.9509
    - null
    metric_stds:
    - 0.0034
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
    - 0.95
    - null
    metric_stds:
    - 0.001
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
    - 0.95
    - null
    metric_stds:
    - 0.004
    - null
  - model: GCA
    model_plain: GCA
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
    - 0.9496
    - null
    metric_stds:
    - 0.0025
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
    - 0.9493
    - null
    metric_stds:
    - 0.0021
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
    - 0.947
    - null
    metric_stds:
    - 0.004
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
    - 0.9469
    - null
    metric_stds:
    - 0.0015
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
    - 0.9456
    - null
    metric_stds:
    - 0.0006
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
    - 0.9454
    - null
    metric_stds:
    - 0.0059
    - null
  - model: DGI
    model_plain: DGI
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
    - 0.9451
    - null
    metric_stds:
    - 0.0052
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
    - 0.945
    - null
    metric_stds:
    - 0.003
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
    - 0.9443
    - null
    metric_stds:
    - 0.002
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
    - 0.9432
    - null
    metric_stds:
    - 0.0028
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
    - 0.943
    - null
    metric_stds:
    - 0.0038
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
    - 0.9428
    - null
    metric_stds:
    - 0.0043
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
    - 0.941
    - null
    metric_stds:
    - 0.003
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
    - 0.941
    - null
    metric_stds:
    - 0.0042
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
    - 0.941
    - null
    metric_stds:
    - 0.002
    - null
  - model: PushNet-TPP
    model_plain: PushNet-TPP
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2003.02228'
    title: 'PushNet: Efficient and Adaptive Neural Message Passing'
    date: Mar 2020
    date_iso: 2020-03
    date_display: Mar 2020
    codebase_url: https://github.com/buschju/pushnet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9409
    - null
    metric_stds:
    - 0.0047
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
    - 0.9401
    - null
    metric_stds:
    - 0.0025
    - null
  - model: PushNet
    model_plain: PushNet
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2003.02228'
    title: 'PushNet: Efficient and Adaptive Neural Message Passing'
    date: Mar 2020
    date_iso: 2020-03
    date_display: Mar 2020
    codebase_url: https://github.com/buschju/pushnet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9401
    - null
    metric_stds:
    - 0.0053
    - null
  - model: APPNP
    model_plain: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2003.02228'
    title: 'PushNet: Efficient and Adaptive Neural Message Passing'
    date: Mar 2020
    date_iso: 2020-03
    date_display: Mar 2020
    codebase_url: https://github.com/buschju/pushnet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9396
    - null
    metric_stds:
    - 0.0045
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
    - 0.9395
    - null
    metric_stds:
    - 0.0017
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
    - 0.9389
    - null
    metric_stds:
    - 0.0049
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
    - 0.9386
    - null
    metric_stds:
    - 0.001
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2003.02228'
    title: 'PushNet: Efficient and Adaptive Neural Message Passing'
    date: Mar 2020
    date_iso: 2020-03
    date_display: Mar 2020
    codebase_url: https://github.com/buschju/pushnet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9379
    - null
    metric_stds:
    - 0.0049
    - null
  - model: PushNet-PTP
    model_plain: PushNet-PTP
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2003.02228'
    title: 'PushNet: Efficient and Adaptive Neural Message Passing'
    date: Mar 2020
    date_iso: 2020-03
    date_display: Mar 2020
    codebase_url: https://github.com/buschju/pushnet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9367
    - null
    metric_stds:
    - 0.0055
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
    - 0.9358
    - null
    metric_stds:
    - 0.0041
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
    - 0.9352
    - null
    metric_stds:
    - 0.0041
    - null
  - model: GCNJK
    model_plain: GCNJK
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2003.02228'
    title: 'PushNet: Efficient and Adaptive Neural Message Passing'
    date: Mar 2020
    date_iso: 2020-03
    date_display: Mar 2020
    codebase_url: https://github.com/buschju/pushnet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9349
    - null
    metric_stds:
    - 0.0056
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
    - 0.9343
    - null
    metric_stds:
    - 0.0054
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
    - 0.934
    - null
    metric_stds:
    - 0.0123
    - null
  - model: JK-Net
    model_plain: JK-Net
    is_baseline: true
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
    - 0.933
    - null
    metric_stds:
    - 0.003
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
    - 0.9328
    - null
    metric_stds:
    - 0.0003
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
    - 0.9327
    - null
    metric_stds:
    - 0.0016
    - null
  - model: S^3-CL
    model_plain: S^3-CL
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
    - 0.9326
    - null
    metric_stds:
    - 0.0042
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
    - 0.93
    - null
    metric_stds:
    - 0.008
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
    - 0.928
    - null
    metric_stds:
    - 0.006
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
    - 0.928
    - null
    metric_stds:
    - 0.01
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
    - 0.928
    - null
    metric_stds:
    - 0.0062
    - null
  - model: SGC
    model_plain: SGC
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
    - 0.928
    - null
    metric_stds:
    - 0.0015
    - null
  - model: GloGNN
    model_plain: GloGNN
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
    - 0.9279
    - null
    metric_stds:
    - 0.0067
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
    - 0.9267
    - null
    metric_stds:
    - 0.0059
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
    - 0.926
    - null
    metric_stds:
    - 0.01
    - null
  - model: ChebNet
    model_plain: ChebNet
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
    - 0.925
    - null
    metric_stds:
    - 0.007
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
    - 0.925
    - null
    metric_stds:
    - 0.009
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
    - 0.925
    - null
    metric_stds:
    - 0.009
    - null
  - model: DeepWalk
    model_plain: DeepWalk
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
    - 0.9177
    - null
    metric_stds:
    - 0.0015
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
    - 0.916
    - null
    metric_stds:
    - 0.0049
    - null
  - model: Node2Vec
    model_plain: Node2Vec
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
    - 0.9123
    - null
    metric_stds:
    - 0.0007
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
    - 0.9089
    - null
    metric_stds:
    - 0.0024
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
    - 0.903
    - null
    metric_stds:
    - 0.012
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
    - 0.889
    - null
    metric_stds:
    - 0.011
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
    - 0.868
    - null
    metric_stds:
    - 0.014
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
    - 0.867
    - null
    metric_stds:
    - 0.015
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
    - 0.866
    - null
    metric_stds:
    - 0.02
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7673
    - null
    metric_stds:
    - 0.1068
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
    - 0.76
    - null
    metric_stds:
    - 0.0225
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7591
    - null
    metric_stds:
    - 0.073
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7526
    - null
    metric_stds:
    - 0.0475
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7507
    - null
    metric_stds:
    - 0.0705
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7409
    - null
    metric_stds:
    - 0.0802
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7401
    - null
    metric_stds:
    - 0.0617
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7391
    - null
    metric_stds:
    - 0.0733
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7263
    - null
    metric_stds:
    - 0.0788
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7199
    - null
    metric_stds:
    - 0.0993
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7033
    - null
    metric_stds:
    - 0.0487
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7
    - null
    metric_stds:
    - 0.0837
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.6534
    - null
    metric_stds:
    - 0.1102
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.6504
    - null
    metric_stds:
    - 0.1069
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.6395
    - null
    metric_stds:
    - 0.0939
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
    - 0.592
    - null
    metric_stds:
    - 0.1614
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.5858
    - null
    metric_stds:
    - 0.1135
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.5846
    - null
    metric_stds:
    - 0.1543
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.5719
    - null
    metric_stds:
    - 0.1909
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
    - 0.556
    - null
    metric_stds:
    - 0.007
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.5475
    - null
    metric_stds:
    - 0.1842
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
    - 0.5127
    - null
    metric_stds:
    - 0.1842
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.4484
    - null
    metric_stds:
    - 0.1442
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.3617
    - null
    metric_stds:
    - 0.0965
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.3192
    - null
    metric_stds:
    - 0.0978
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.3066
    - null
    metric_stds:
    - 0.0872
    - null
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
    - null
    - 0.6146
    metric_stds:
    - null
    - 0.0612
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
    - null
    - 0.7098
    metric_stds:
    - null
    - 0.0196
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
    - null
    - 0.7229
    metric_stds:
    - null
    - 0.0169
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
    - null
    - 0.7371
    metric_stds:
    - null
    - 0.0228
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
    - null
    - 0.741
    metric_stds:
    - null
    - 0.0251
  - model: SEAL
    model_plain: SEAL
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
    - null
    - 0.7427
    metric_stds:
    - null
    - 0.0258
  - model: Neo-GNN
    model_plain: Neo-GNN
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
    - null
    - 0.7228
    metric_stds:
    - null
    - 0.0233
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
    - null
    - 0.658
    metric_stds:
    - null
    - 0.0226
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
    - null
    - 0.7596
    metric_stds:
    - null
    - 0.0173
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
    - null
    - 0.7636
    metric_stds:
    - null
    - 0.014
  milestones:
  - value: 0.93
    std: 0.008
    model: GS-mean
    arxiv_id: '1811.05868'
    title: Pitfalls of Graph Neural Network Evaluation
    date: 2018-11
  - value: 0.9409
    std: 0.0047
    model: PushNet-TPP
    arxiv_id: '2003.02228'
    title: 'PushNet: Efficient and Adaptive Neural Message Passing'
    date: 2020-03
  - value: 0.956
    std: 0.003
    model: Unifying Graph Contrastive Learning
    arxiv_id: '2210.08792'
    title: Unifying Graph Contrastive Learning with Flexible Contextual Scopes
    date: 2022-10
  - value: 0.9633
    std: 0.0013
    model: Local-GCL
    arxiv_id: '2212.04604'
    title: Localized Graph Contrastive Learning
    date: 2022-12
  - value: 0.9734
    std: 0.0003
    model: NAGphormer
    arxiv_id: '2303.06147'
    title: 'Exphormer: Sparse Transformers for Graphs'
    date: '2023-03-10'
  - value: 0.974
    std: 0.0004
    model: DAM-GT
    arxiv_id: '2505.17660'
    title: 'DAM-GT: Dual Positional Encoding-Based Attention Masking Graph Transformer
      for Node Classification'
    date: 2025-05
---

