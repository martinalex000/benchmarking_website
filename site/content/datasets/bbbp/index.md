---
title: BBBP
slug: bbbp
benchmark: MoleculeNet
task_type: graph_classification
description: Binary classification — blood-brain barrier permeability of molecules.
primary_metric: ROC-AUC
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.MoleculeNet.html
stats: null
result_count: 203
best_model:
  model: Gode
  value: 0.948
  metric: ROC-AUC
  arxiv_id: '2306.01631'
  paper_title: Bi-level Contrastive Learning for Knowledge-Enhanced Molecule Representations
variants:
- slug: scaffold-split
  name: Scaffold split
  notes: ''
  is_standard: true
  primary_metric: ROC-AUC
  higher_is_better: true
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - ROC-AUC
  rows:
  - model: Gode
    model_plain: Gode
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.01631'
    title: Bi-level Contrastive Learning for Knowledge-Enhanced Molecule Representations
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: ''
    uses_external_data: true
    is_best: true
    metric_values:
    - 0.948
    metric_stds:
    - 0.019
  - model: SGLB
    model_plain: SGLB
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.07633'
    title: SE(3)-Invariant Multiparameter Persistent Homology for Chiral-Sensitive
      Molecular Property Prediction
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.94
    metric_stds:
    - 0.021
  - model: MoLFormer-XL
    model_plain: MoLFormer-XL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.09553'
    title: How Much Structural Information Large Scale Molecular Language Representations
      Can Capture?
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/IBM/molformer
    uses_external_data: true
    is_best: true
    metric_values:
    - 0.937
    metric_stds:
    - null
  - model: KANO_GTrans
    model_plain: KANO_GTrans
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.01631'
    title: Bi-level Contrastive Learning for Knowledge-Enhanced Molecule Representations
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: ''
    uses_external_data: true
    is_best: true
    metric_values:
    - 0.937
    metric_stds:
    - 0.023
  - model: Masking Node + Supervised
    model_plain: Masking Node + Supervised
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.06010'
    title: Does GNN Pretraining Help Molecular Representation?
    date: Jul 2022
    date_iso: 2022-07
    date_display: Jul 2022
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9343
    metric_stds:
    - 0.025
  - model: KANO_CMPNN
    model_plain: KANO_CMPNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.01631'
    title: Bi-level Contrastive Learning for Knowledge-Enhanced Molecule Representations
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: ''
    uses_external_data: true
    is_best: true
    metric_values:
    - 0.926
    metric_stds:
    - 0.018
  - model: ECFP-4 + RF
    model_plain: ECFP-4 + RF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.07633'
    title: SE(3)-Invariant Multiparameter Persistent Homology for Chiral-Sensitive
      Molecular Property Prediction
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.924
    metric_stds:
    - 0.024
  - model: KGE_NFM_w_MolKG
    model_plain: KGE_NFM_w_MolKG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.01631'
    title: Bi-level Contrastive Learning for Knowledge-Enhanced Molecule Representations
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: ''
    uses_external_data: true
    is_best: true
    metric_values:
    - 0.924
    metric_stds:
    - 0.024
  - model: Context Prediction + Supervised
    model_plain: Context Prediction + Supervised
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.06010'
    title: Does GNN Pretraining Help Molecular Representation?
    date: Jul 2022
    date_iso: 2022-07
    date_display: Jul 2022
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9227
    metric_stds:
    - 0.0157
  - model: No Pre-train
    model_plain: No Pre-train
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.06010'
    title: Does GNN Pretraining Help Molecular Representation?
    date: Jul 2022
    date_iso: 2022-07
    date_display: Jul 2022
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9223
    metric_stds:
    - 0.0307
  - model: 10% ZINC + 100% PubChem
    model_plain: 10% ZINC + 100% PubChem
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.09553'
    title: How Much Structural Information Large Scale Molecular Language Representations
      Can Capture?
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/IBM/molformer
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.922
    metric_stds:
    - null
  - model: ProtoS-L2
    model_plain: ProtoS-L2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.04804'
    title: Optimal Transport Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.92
    metric_stds:
    - 0.01
  - model: ProtoW-L2 (no reg.)
    model_plain: ProtoW-L2 (no reg.)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.04804'
    title: Optimal Transport Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.92
    metric_stds:
    - 0.01
  - model: ProtoW-Dot (no reg.)
    model_plain: ProtoW-Dot (no reg.)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.04804'
    title: Optimal Transport Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.919
    metric_stds:
    - 0.009
  - model: ProtoW-Dot
    model_plain: ProtoW-Dot
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.04804'
    title: Optimal Transport Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.919
    metric_stds:
    - 0.009
  - model: Supervised
    model_plain: Supervised
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.06010'
    title: Does GNN Pretraining Help Molecular Representation?
    date: Jul 2022
    date_iso: 2022-07
    date_display: Jul 2022
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9165
    metric_stds:
    - 0.0211
  - model: 10% Zinc + 10% Pub
    model_plain: 10% Zinc + 10% Pub
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.09553'
    title: How Much Structural Information Large Scale Molecular Language Representations
      Can Capture?
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/IBM/molformer
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.915
    metric_stds:
    - null
  - model: D-MPNN
    model_plain: D-MPNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.04804'
    title: Optimal Transport Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.915
    metric_stds:
    - 0.01
  - model: Node-MPN
    model_plain: Node-MPN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.07633'
    title: SE(3)-Invariant Multiparameter Persistent Homology for Chiral-Sensitive
      Molecular Property Prediction
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.913
    metric_stds:
    - 0.041
  - model: MPNN
    model_plain: MPNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.01631'
    title: Bi-level Contrastive Learning for Knowledge-Enhanced Molecule Representations
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.913
    metric_stds:
    - 0.041
  - model: N-GRAM
    model_plain: N-GRAM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.01631'
    title: Bi-level Contrastive Learning for Knowledge-Enhanced Molecule Representations
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.912
    metric_stds:
    - 0.013
  - model: D-MPNN+TopK Pool
    model_plain: D-MPNN+TopK Pool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.04804'
    title: Optimal Transport Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.912
    metric_stds:
    - 0.032
  - model: MLP-Fingerprint
    model_plain: MLP-Fingerprint
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.04804'
    title: Optimal Transport Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.911
    metric_stds:
    - 0.005
  - model: MoLFormer-Base
    model_plain: MoLFormer-Base
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.09553'
    title: How Much Structural Information Large Scale Molecular Language Representations
      Can Capture?
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/IBM/molformer
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.909
    metric_stds:
    - null
  - model: D-MPNN+SAG Pool
    model_plain: D-MPNN+SAG Pool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.04804'
    title: Optimal Transport Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.901
    metric_stds:
    - 0.034
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.04804'
    title: Optimal Transport Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9
    metric_stds:
    - 0.014
  - model: 100% Zinc
    model_plain: 100% Zinc
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.09553'
    title: How Much Structural Information Large Scale Molecular Language Representations
      Can Capture?
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/IBM/molformer
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.899
    metric_stds:
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.04804'
    title: Optimal Transport Graph Neural Networks
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.888
    metric_stds:
    - 0.015
  - model: GraphCON
    model_plain: GraphCON
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.07633'
    title: SE(3)-Invariant Multiparameter Persistent Homology for Chiral-Sensitive
      Molecular Property Prediction
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.877
    metric_stds:
    - 0.036
  - model: GROVER_Large_GTrans
    model_plain: GROVER_Large_GTrans
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.01631'
    title: Bi-level Contrastive Learning for Knowledge-Enhanced Molecule Representations
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.862
    metric_stds:
    - 0.039
  - model: IA-GPL
    model_plain: IA-GPL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17676'
    title: Instance-Aware Graph Prompt Learning
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8562
    metric_stds:
    - 0.0052
  - model: mGCN
    model_plain: mGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.01631'
    title: Bi-level Contrastive Learning for Knowledge-Enhanced Molecule Representations
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.85
    metric_stds:
    - 0.064
  - model: SchNet
    model_plain: SchNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.01631'
    title: Bi-level Contrastive Learning for Knowledge-Enhanced Molecule Representations
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.848
    metric_stds:
    - 0.022
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17676'
    title: Instance-Aware Graph Prompt Learning
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8397
    metric_stds:
    - 0.0086
  - model: Weave
    model_plain: Weave
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.07633'
    title: SE(3)-Invariant Multiparameter Persistent Homology for Chiral-Sensitive
      Molecular Property Prediction
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.837
    metric_stds:
    - 0.065
  - model: GPF-plus
    model_plain: GPF-plus
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17676'
    title: Instance-Aware Graph Prompt Learning
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8308
    metric_stds:
    - 0.0157
  - model: GPF
    model_plain: GPF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17676'
    title: Instance-Aware Graph Prompt Learning
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8286
    metric_stds:
    - 0.0198
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17676'
    title: Instance-Aware Graph Prompt Learning
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8072
    metric_stds:
    - 0.0137
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17676'
    title: Instance-Aware Graph Prompt Learning
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.802
    metric_stds:
    - 0.017
  - model: Linear Probing
    model_plain: Linear Probing
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17676'
    title: Instance-Aware Graph Prompt Learning
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7967
    metric_stds:
    - 0.0131
  - model: unified method
    model_plain: unified method
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.08806'
    title: Unified 2D and 3D Pre-Training of Molecular Representations
    date: Jul 2022
    date_iso: 2022-07
    date_display: Jul 2022
    codebase_url: https://github.com/teslacool/UnifiedMolPretrain
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.774
    metric_stds:
    - 0.006
  - model: LLaMA3-3B <SO>G_k>
    model_plain: LLaMA3-3B G_k>
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.01771'
    title: '<SO$ _k$>: One LLM Token for Explicit Graph Structural Understanding'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: https://github.com/Jingyao-Wu/SOG
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.769
    metric_stds:
    - 0.031
  - model: MolCLR_GTrans
    model_plain: MolCLR_GTrans
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.01631'
    title: Bi-level Contrastive Learning for Knowledge-Enhanced Molecule Representations
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.767
    metric_stds:
    - 0.022
  - model: DeMol
    model_plain: DeMol
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00568'
    title: Enhancing Molecular Property Predictions by Learning from Bond Modelling
      and Interactions
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.751
    metric_stds:
    - 0.006
  - model: Context Prediction
    model_plain: Context Prediction
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.06010'
    title: Does GNN Pretraining Help Molecular Representation?
    date: Jul 2022
    date_iso: 2022-07
    date_display: Jul 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.741
    metric_stds:
    - 0.0022
  - model: agg + I
    model_plain: agg + I
    is_baseline: true
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
    - 0.7408
    metric_stds:
    - 0.0
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
    - 0.7388
    metric_stds:
    - 0.011
  - model: LEMON
    model_plain: LEMON
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00568'
    title: Enhancing Molecular Property Predictions by Learning from Bond Modelling
      and Interactions
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.737
    metric_stds:
    - 0.011
  - model: Motif Prediction
    model_plain: Motif Prediction
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.06010'
    title: Does GNN Pretraining Help Molecular Representation?
    date: Jul 2022
    date_iso: 2022-07
    date_display: Jul 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7365
    metric_stds:
    - 0.0036
  - model: Node Prediction
    model_plain: Node Prediction
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.06010'
    title: Does GNN Pretraining Help Molecular Representation?
    date: Jul 2022
    date_iso: 2022-07
    date_display: Jul 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7345
    metric_stds:
    - 0.0027
  - model: Contrastive learning
    model_plain: Contrastive learning
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.06010'
    title: Does GNN Pretraining Help Molecular Representation?
    date: Jul 2022
    date_iso: 2022-07
    date_display: Jul 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7332
    metric_stds:
    - 0.0238
  - model: MolCLR
    model_plain: MolCLR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.01631'
    title: Bi-level Contrastive Learning for Knowledge-Enhanced Molecule Representations
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.733
    metric_stds:
    - 0.01
  - model: MoleBlend
    model_plain: MoleBlend
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00568'
    title: Enhancing Molecular Property Predictions by Learning from Bond Modelling
      and Interactions
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.73
    metric_stds:
    - 0.008
  - model: Uni-Mol
    model_plain: Uni-Mol
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00568'
    title: Enhancing Molecular Property Predictions by Learning from Bond Modelling
      and Interactions
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.729
    metric_stds:
    - 0.006
  - model: UGMAE
    model_plain: UGMAE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08023'
    title: 'UGMAE: A Unified Framework for Graph Masked Autoencoders'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.728
    metric_stds:
    - 0.004
  - model: MoAMa
    model_plain: MoAMa
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.04589'
    title: Motif-aware Attribute Masking for Molecular Graph Pre-training
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.728
    metric_stds:
    - 0.009
  - model: D-SLA
    model_plain: D-SLA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.04589'
    title: Motif-aware Attribute Masking for Molecular Graph Pre-training
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.726
    metric_stds:
    - 0.008
  - model: G-Tuning
    model_plain: G-Tuning
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.13583'
    title: Fine-tuning Graph Neural Networks by Preserving Graph Generative Patterns
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/zjunet/G-Tuning
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.7259
    metric_stds:
    - 0.0032
  - model: GraphLoG
    model_plain: GraphLoG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.04589'
    title: Motif-aware Attribute Masking for Molecular Graph Pre-training
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.725
    metric_stds:
    - 0.008
  - model: GEM
    model_plain: GEM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00568'
    title: Enhancing Molecular Property Predictions by Learning from Bond Modelling
      and Interactions
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.724
    metric_stds:
    - 0.004
  - model: GraphMAE
    model_plain: GraphMAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.04589'
    title: Motif-aware Attribute Masking for Molecular Graph Pre-training
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.72
    metric_stds:
    - 0.006
  - model: Mole-BERT
    model_plain: Mole-BERT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.04589'
    title: Motif-aware Attribute Masking for Molecular Graph Pre-training
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.719
    metric_stds:
    - 0.016
  - model: MoleculeSDE
    model_plain: MoleculeSDE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00568'
    title: Enhancing Molecular Property Predictions by Learning from Bond Modelling
      and Interactions
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.718
    metric_stds:
    - 0.007
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.01631'
    title: Bi-level Contrastive Learning for Knowledge-Enhanced Molecule Representations
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.718
    metric_stds:
    - 0.009
  - model: VGAE-Tuning
    model_plain: VGAE-Tuning
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.13583'
    title: Fine-tuning Graph Neural Networks by Preserving Graph Generative Patterns
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/zjunet/G-Tuning
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.7169
    metric_stds:
    - 0.0051
  - model: GCL
    model_plain: GCL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.03506'
    title: Subgraph Networks Based Contrastive Learning
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.716
    metric_stds:
    - 0.008
  - model: Galformer
    model_plain: Galformer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00568'
    title: Enhancing Molecular Property Predictions by Learning from Bond Modelling
      and Interactions
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.716
    metric_stds:
    - 0.009
  - model: MCM
    model_plain: MCM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.04589'
    title: Motif-aware Attribute Masking for Molecular Graph Pre-training
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.716
    metric_stds:
    - 0.006
  - model: RGCL
    model_plain: RGCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.03506'
    title: Subgraph Networks Based Contrastive Learning
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.714
    metric_stds:
    - 0.007
  - model: EQuAD
    model_plain: EQuAD
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.11083'
    title: arXiv:2407.11083
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/tianyao-aka/EQuAD
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7122
    metric_stds:
    - 0.0147
  - model: Graphormer
    model_plain: Graphormer
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1802.00543'
    title: Modeling polypharmacy side effects with graph convolutional networks
    date: Feb 2, 2018
    date_iso: '2018-02-02'
    date_display: Feb 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.712
    metric_stds:
    - 0.008
  - model: AttrMask & ContextPred
    model_plain: AttrMask & ContextPred
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.08806'
    title: Unified 2D and 3D Pre-Training of Molecular Representations
    date: Jul 2022
    date_iso: 2022-07
    date_display: Jul 2022
    codebase_url: https://github.com/teslacool/UnifiedMolPretrain
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.712
    metric_stds:
    - 0.009
  - model: ContextPred
    model_plain: ContextPred
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.13315'
    title: 3D Molecular Geometry Analysis with 2D Graphs
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.712
    metric_stds:
    - 0.009
  - model: stark20213d
    model_plain: stark20213d
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.08806'
    title: Unified 2D and 3D Pre-Training of Molecular Representations
    date: Jul 2022
    date_iso: 2022-07
    date_display: Jul 2022
    codebase_url: https://github.com/teslacool/UnifiedMolPretrain
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.711
    metric_stds:
    - 0.02
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
    - 0.7107
    metric_stds:
    - 0.0113
  - model: IGM
    model_plain: IGM
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.10988'
    title: Graph Invariant Learning with Subgraph Co-mixup for Out-Of-Distribution
      Generalization
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/BUPT-GAMMA/IGM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7103
    metric_stds:
    - 0.0079
  - model: D-MPNN
    model_plain: D-MPNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.09885'
    title: 'ChemBERTa: Large-Scale Self-Supervised Pretraining for Molecular Property
      Prediction'
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: https://huggingface.co/seyonec/ChemBERTa-zinc-base-v1
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.708
    metric_stds:
    - null
  - model: HU. et.al
    model_plain: HU. et.al
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.01631'
    title: Bi-level Contrastive Learning for Knowledge-Enhanced Molecule Representations
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.708
    metric_stds:
    - 0.015
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
    - 0.7072
    metric_stds:
    - 0.0153
  - model: MGSSL
    model_plain: MGSSL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.01631'
    title: Bi-level Contrastive Learning for Knowledge-Enhanced Molecule Representations
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.705
    metric_stds:
    - 0.011
  - model: GROVER
    model_plain: GROVER
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.08806'
    title: Unified 2D and 3D Pre-Training of Molecular Representations
    date: Jul 2022
    date_iso: 2022-07
    date_display: Jul 2022
    codebase_url: https://github.com/teslacool/UnifiedMolPretrain
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.703
    metric_stds:
    - 0.016
  - model: G-Contextual
    model_plain: G-Contextual
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.13315'
    title: 3D Molecular Geometry Analysis with 2D Graphs
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.703
    metric_stds:
    - 0.016
  - model: GAP-EMPNN
    model_plain: GAP-EMPNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.13315'
    title: 3D Molecular Geometry Analysis with 2D Graphs
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.703
    metric_stds:
    - 0.002
  - model: JOAO
    model_plain: JOAO
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.03506'
    title: Subgraph Networks Based Contrastive Learning
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.702
    metric_stds:
    - 0.01
  - model: SVM
    model_plain: SVM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.09885'
    title: 'ChemBERTa: Large-Scale Self-Supervised Pretraining for Molecular Property
      Prediction'
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: https://huggingface.co/seyonec/ChemBERTa-zinc-base-v1
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.702
    metric_stds:
    - null
  - model: AttrMask
    model_plain: AttrMask
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.13315'
    title: 3D Molecular Geometry Analysis with 2D Graphs
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.702
    metric_stds:
    - 0.005
  - model: GTOT-Tuning
    model_plain: GTOT-Tuning
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.13583'
    title: Fine-tuning Graph Neural Networks by Preserving Graph Generative Patterns
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/zjunet/G-Tuning
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.7004
    metric_stds:
    - 0.0148
  - model: GROVER_base
    model_plain: GROVER_base
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.06462'
    title: Invariant-Based Diagnostics for Graph Benchmarks
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.7
    metric_stds:
    - 0.001
  - model: AD-GCL
    model_plain: AD-GCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.03506'
    title: Subgraph Networks Based Contrastive Learning
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7
    metric_stds:
    - 0.011
  - model: GIN+Pretrain
    model_plain: GIN+Pretrain
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2304.02806'
    title: 'Graph Mixture of Experts: Learning on Large-Scale Graphs with Explicit
      Diversity Modeling'
    date: Apr 2023
    date_iso: 2023-04
    date_display: Apr 2023
    codebase_url: https://github.com/VITA-Group/Graph-Mixture-of-Experts
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.6994
    metric_stds:
    - 0.0092
  - model: MoleOOD
    model_plain: MoleOOD
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.11083'
    title: arXiv:2407.11083
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/tianyao-aka/EQuAD
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6984
    metric_stds:
    - 0.0184
  - model: DIR
    model_plain: DIR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.10988'
    title: Graph Invariant Learning with Subgraph Co-mixup for Out-Of-Distribution
      Generalization
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/BUPT-GAMMA/IGM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6973
    metric_stds:
    - 0.0154
  - model: N-Gram_RF
    model_plain: N-Gram_RF
    is_baseline: true
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
    - 0.697
    metric_stds:
    - 0.006
  - model: GraphCL
    model_plain: GraphCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.03506'
    title: Subgraph Networks Based Contrastive Learning
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.697
    metric_stds:
    - 0.007
  - model: GREA
    model_plain: GREA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.11083'
    title: arXiv:2407.11083
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/tianyao-aka/EQuAD
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.697
    metric_stds:
    - 0.0128
  - model: CIGA
    model_plain: CIGA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.10988'
    title: Graph Invariant Learning with Subgraph Co-mixup for Out-Of-Distribution
      Generalization
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/BUPT-GAMMA/IGM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6965
    metric_stds:
    - 0.0132
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
    - 0.6959
    metric_stds:
    - 0.0134
  - model: MoNet
    model_plain: MoNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.10657'
    title: Generalizing Graph Neural Networks on Out-Of-Distribution Graphs
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: https://github.com/googlebaba/StableGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6952
    metric_stds:
    - 0.0046
  - model: GROVER_large
    model_plain: GROVER_large
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.06462'
    title: Invariant-Based Diagnostics for Graph Benchmarks
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.695
    metric_stds:
    - 0.001
  - model: StochNorm
    model_plain: StochNorm
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.13583'
    title: Fine-tuning Graph Neural Networks by Preserving Graph Generative Patterns
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/zjunet/G-Tuning
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.6927
    metric_stds:
    - 0.0167
  - model: GraphMVP
    model_plain: GraphMVP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.08005'
    title: Evaluating Self-Supervised Learning for Molecular Graph Embeddings
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/hansen7/MolGraphEval
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.692
    metric_stds:
    - 0.018
  - model: InfoGraph
    model_plain: InfoGraph
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.13315'
    title: 3D Molecular Geometry Analysis with 2D Graphs
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.692
    metric_stds:
    - 0.008
  - model: IRM
    model_plain: IRM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.10988'
    title: Graph Invariant Learning with Subgraph Co-mixup for Out-Of-Distribution
      Generalization
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/BUPT-GAMMA/IGM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6913
    metric_stds:
    - 0.0145
  - model: N-Gram_XGB
    model_plain: N-Gram_XGB
    is_baseline: true
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
    - 0.691
    metric_stds:
    - 0.008
  - model: 3D Infomax
    model_plain: 3D Infomax
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.07633'
    title: SE(3)-Invariant Multiparameter Persistent Homology for Chiral-Sensitive
      Molecular Property Prediction
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.691
    metric_stds:
    - 0.011
  - model: Vanilla Tuning
    model_plain: Vanilla Tuning
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.13583'
    title: Fine-tuning Graph Neural Networks by Preserving Graph Generative Patterns
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/zjunet/G-Tuning
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.6899
    metric_stds:
    - 0.0313
  - model: StableGCN
    model_plain: StableGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.10657'
    title: Generalizing Graph Neural Networks on Out-Of-Distribution Graphs
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: https://github.com/googlebaba/StableGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6882
    metric_stds:
    - 0.0387
  - model: Infomax
    model_plain: Infomax
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08023'
    title: 'UGMAE: A Unified Framework for Graph Masked Autoencoders'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.688
    metric_stds:
    - 0.008
  - model: PretrainGNN
    model_plain: PretrainGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.06462'
    title: Invariant-Based Diagnostics for Graph Benchmarks
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.687
    metric_stds:
    - 0.013
  - model: Manifold-Mixup
    model_plain: Manifold-Mixup
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.10988'
    title: Graph Invariant Learning with Subgraph Co-mixup for Out-Of-Distribution
      Generalization
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/BUPT-GAMMA/IGM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6867
    metric_stds:
    - 0.0138
  - model: GMoE-GIN+Pretrain
    model_plain: GMoE-GIN+Pretrain
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2304.02806'
    title: 'Graph Mixture of Experts: Learning on Large-Scale Graphs with Explicit
      Diversity Modeling'
    date: Apr 2023
    date_iso: 2023-04
    date_display: Apr 2023
    codebase_url: https://github.com/VITA-Group/Graph-Mixture-of-Experts
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.6862
    metric_stds:
    - 0.0102
  - model: StableSAGE
    model_plain: StableSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.10657'
    title: Generalizing Graph Neural Networks on Out-Of-Distribution Graphs
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: https://github.com/googlebaba/StableGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6847
    metric_stds:
    - 0.0247
  - model: G-Mixup
    model_plain: G-Mixup
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.10988'
    title: Graph Invariant Learning with Subgraph Co-mixup for Out-Of-Distribution
      Generalization
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/BUPT-GAMMA/IGM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6844
    metric_stds:
    - 0.0208
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
    - 0.6828
    metric_stds:
    - 0.0147
  - model: RF
    model_plain: RF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.09885'
    title: 'ChemBERTa: Large-Scale Self-Supervised Pretraining for Molecular Property
      Prediction'
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: https://huggingface.co/seyonec/ChemBERTa-zinc-base-v1
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.681
    metric_stds:
    - null
  - model: BSS
    model_plain: BSS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.13583'
    title: Fine-tuning Graph Neural Networks by Preserving Graph Generative Patterns
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/zjunet/G-Tuning
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.6802
    metric_stds:
    - 0.0276
  - model: ContextPred
    model_plain: ContextPred
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.03506'
    title: Subgraph Networks Based Contrastive Learning
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.68
    metric_stds:
    - 0.02
  - model: GraphLoG
    model_plain: GraphLoG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.13315'
    title: 3D Molecular Geometry Analysis with 2D Graphs
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.678
    metric_stds:
    - 0.017
  - model: DELTA
    model_plain: DELTA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.13583'
    title: Fine-tuning Graph Neural Networks by Preserving Graph Generative Patterns
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/zjunet/G-Tuning
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.6779
    metric_stds:
    - 0.0076
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.10657'
    title: Generalizing Graph Neural Networks on Out-Of-Distribution Graphs
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: https://github.com/googlebaba/StableGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6772
    metric_stds:
    - 0.0189
  - model: L2_SP
    model_plain: L2_SP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.13583'
    title: Fine-tuning Graph Neural Networks by Preserving Graph Generative Patterns
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/zjunet/G-Tuning
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.677
    metric_stds:
    - 0.0321
  - model: InfoGraph
    model_plain: InfoGraph
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00568'
    title: Enhancing Molecular Property Predictions by Learning from Bond Modelling
      and Interactions
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.675
    metric_stds:
    - 0.001
  - model: VIB-GSL
    model_plain: VIB-GSL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15745'
    title: Robust Ante-hoc Graph Explainer using Bilevel Optimization
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.675
    metric_stds:
    - 0.019
  - model: AI
    model_plain: AI
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.05481'
    title: A Molecular Multimodal Foundation Model Associating Molecule Graphs with
      Natural Language
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: https://github.com/BingSu12/MoMu
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.673
    metric_stds:
    - 0.012
  - model: MVGRL
    model_plain: MVGRL
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
    - 0.6724
    metric_stds:
    - 0.0139
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.10657'
    title: Generalizing Graph Neural Networks on Out-Of-Distribution Graphs
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: https://github.com/googlebaba/StableGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6717
    metric_stds:
    - 0.0049
  - model: EGNN
    model_plain: EGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1802.00543'
    title: Modeling polypharmacy side effects with graph convolutional networks
    date: Feb 2, 2018
    date_iso: '2018-02-02'
    date_display: Feb 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.671
    metric_stds:
    - 0.01
  - model: RAGE
    model_plain: RAGE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15745'
    title: Robust Ante-hoc Graph Explainer using Bilevel Optimization
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.671
    metric_stds:
    - 0.021
  - model: GROVER
    model_plain: GROVER
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.08005'
    title: Evaluating Self-Supervised Learning for Molecular Graph Embeddings
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/hansen7/MolGraphEval
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.67
    metric_stds:
    - 0.003
  - model: GMoE-GCN
    model_plain: GMoE-GCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2304.02806'
    title: 'Graph Mixture of Experts: Learning on Large-Scale Graphs with Explicit
      Diversity Modeling'
    date: Apr 2023
    date_iso: 2023-04
    date_display: Apr 2023
    codebase_url: https://github.com/VITA-Group/Graph-Mixture-of-Experts
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6693
    metric_stds:
    - 0.0172
  - model: ERM
    model_plain: ERM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.10988'
    title: Graph Invariant Learning with Subgraph Co-mixup for Out-Of-Distribution
      Generalization
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/BUPT-GAMMA/IGM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6693
    metric_stds:
    - 0.0231
  - model: GIN0
    model_plain: GIN0
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.10657'
    title: Generalizing Graph Neural Networks on Out-Of-Distribution Graphs
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: https://github.com/googlebaba/StableGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6665
    metric_stds:
    - 0.0132
  - model: MolCLR
    model_plain: MolCLR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00568'
    title: Enhancing Molecular Property Predictions by Learning from Bond Modelling
      and Interactions
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.666
    metric_stds:
    - 0.018
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
    - 0.6651
    metric_stds:
    - 0.008
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.10657'
    title: Generalizing Graph Neural Networks on Out-Of-Distribution Graphs
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: https://github.com/googlebaba/StableGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6647
    metric_stds:
    - 0.009
  - model: LLaMA2-7B <SO>G_k</SO>
    model_plain: LLaMA2-7B G_k
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.01771'
    title: '<SO$ _k$>: One LLM Token for Explicit Graph Structural Understanding'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: https://github.com/Jingyao-Wu/SOG
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.664
    metric_stds:
    - 0.027
  - model: G-Motif
    model_plain: G-Motif
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.13315'
    title: 3D Molecular Geometry Analysis with 2D Graphs
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.664
    metric_stds:
    - 0.034
  - model: DimeNet++
    model_plain: DimeNet++
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1802.00543'
    title: Modeling polypharmacy side effects with graph convolutional networks
    date: Feb 2, 2018
    date_iso: '2018-02-02'
    date_display: Feb 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.662
    metric_stds:
    - 0.009
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.10657'
    title: Generalizing Graph Neural Networks on Out-Of-Distribution Graphs
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: https://github.com/googlebaba/StableGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6616
    metric_stds:
    - 0.0097
  - model: JOAO
    model_plain: JOAO
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.08005'
    title: Evaluating Self-Supervised Learning for Molecular Graph Embeddings
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/hansen7/MolGraphEval
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.661
    metric_stds:
    - 0.008
  - model: Galactica-120B
    model_plain: Galactica-120B
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.01771'
    title: '<SO$ _k$>: One LLM Token for Explicit Graph Structural Understanding'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: https://github.com/Jingyao-Wu/SOG
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.661
    metric_stds:
    - null
  - model: GISST
    model_plain: GISST
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.02719'
    title: 'Beyond Topological Self-Explainable GNNs: A Formal Explainability Perspective'
    date: Feb 4, 2025
    date_iso: '2025-02-04'
    date_display: Feb 2025
    codebase_url: https://github.com/steveazzolin/beyond-topo-segnns
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.66
    metric_stds:
    - 0.03
  - model: MGNN
    model_plain: MGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.02719'
    title: 'Beyond Topological Self-Explainable GNNs: A Formal Explainability Perspective'
    date: Feb 4, 2025
    date_iso: '2025-02-04'
    date_display: Feb 2025
    codebase_url: https://github.com/steveazzolin/beyond-topo-segnns
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.66
    metric_stds:
    - 0.03
  - model: InfoGraph
    model_plain: InfoGraph
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.08005'
    title: Evaluating Self-Supervised Learning for Molecular Graph Embeddings
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/hansen7/MolGraphEval
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.659
    metric_stds:
    - 0.006
  - model: Supervised
    model_plain: Supervised
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.13583'
    title: Fine-tuning Graph Neural Networks by Preserving Graph Generative Patterns
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/zjunet/G-Tuning
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.6584
    metric_stds:
    - 0.0451
  - model: PNA
    model_plain: PNA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1802.00543'
    title: Modeling polypharmacy side effects with graph convolutional networks
    date: Feb 2, 2018
    date_iso: '2018-02-02'
    date_display: Feb 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.658
    metric_stds:
    - 0.011
  - model: No Pre-train
    model_plain: No Pre-train
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.03506'
    title: Subgraph Networks Based Contrastive Learning
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.658
    metric_stds:
    - 0.045
  - model: GSAT
    model_plain: GSAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15745'
    title: Robust Ante-hoc Graph Explainer using Bilevel Optimization
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.658
    metric_stds:
    - 0.022
  - model: GMT
    model_plain: GMT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15745'
    title: Robust Ante-hoc Graph Explainer using Bilevel Optimization
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.658
    metric_stds:
    - 0.019
  - model: EIIL
    model_plain: EIIL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.10988'
    title: Graph Invariant Learning with Subgraph Co-mixup for Out-Of-Distribution
      Generalization
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/BUPT-GAMMA/IGM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6577
    metric_stds:
    - 0.0336
  - model: JK-Net
    model_plain: JK-Net
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.10657'
    title: Generalizing Graph Neural Networks on Out-Of-Distribution Graphs
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: https://github.com/googlebaba/StableGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6562
    metric_stds:
    - 0.0077
  - model: Uni-Mol
    model_plain: Uni-Mol
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.04589'
    title: Motif-aware Attribute Masking for Molecular Graph Pre-training
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.654
    metric_stds:
    - 0.01
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.05481'
    title: A Molecular Multimodal Foundation Model Associating Molecule Graphs with
      Natural Language
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: https://github.com/BingSu12/MoMu
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.652
    metric_stds:
    - 0.014
  - model: DC-GISST
    model_plain: DC-GISST
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.02719'
    title: 'Beyond Topological Self-Explainable GNNs: A Formal Explainability Perspective'
    date: Feb 4, 2025
    date_iso: '2025-02-04'
    date_display: Feb 2025
    codebase_url: https://github.com/steveazzolin/beyond-topo-segnns
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.65
    metric_stds:
    - 0.02
  - model: DC-GSAT
    model_plain: DC-GSAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.02719'
    title: 'Beyond Topological Self-Explainable GNNs: A Formal Explainability Perspective'
    date: Feb 4, 2025
    date_iso: '2025-02-04'
    date_display: Feb 2025
    codebase_url: https://github.com/steveazzolin/beyond-topo-segnns
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.65
    metric_stds:
    - 0.03
  - model: DC-SMGNN
    model_plain: DC-SMGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.02719'
    title: 'Beyond Topological Self-Explainable GNNs: A Formal Explainability Perspective'
    date: Feb 4, 2025
    date_iso: '2025-02-04'
    date_display: Feb 2025
    codebase_url: https://github.com/steveazzolin/beyond-topo-segnns
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.65
    metric_stds:
    - 0.05
  - model: DC-DIR
    model_plain: DC-DIR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.02719'
    title: 'Beyond Topological Self-Explainable GNNs: A Formal Explainability Perspective'
    date: Feb 4, 2025
    date_iso: '2025-02-04'
    date_display: Feb 2025
    codebase_url: https://github.com/steveazzolin/beyond-topo-segnns
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.65
    metric_stds:
    - 0.02
  - model: V-REx
    model_plain: V-REx
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.10988'
    title: Graph Invariant Learning with Subgraph Co-mixup for Out-Of-Distribution
      Generalization
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/BUPT-GAMMA/IGM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6486
    metric_stds:
    - 0.0213
  - model: GraphCL
    model_plain: GraphCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.08005'
    title: Evaluating Self-Supervised Learning for Molecular Graph Embeddings
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/hansen7/MolGraphEval
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.647
    metric_stds:
    - 0.017
  - model: EdgePred
    model_plain: EdgePred
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.13315'
    title: 3D Molecular Geometry Analysis with 2D Graphs
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.645
    metric_stds:
    - 0.031
  - model: GPT-GNN
    model_plain: GPT-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.13315'
    title: 3D Molecular Geometry Analysis with 2D Graphs
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.645
    metric_stds:
    - 0.011
  - model: Dir-GNN
    model_plain: Dir-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15745'
    title: Robust Ante-hoc Graph Explainer using Bilevel Optimization
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.644
    metric_stds:
    - 0.029
  - model: AttentiveFP
    model_plain: AttentiveFP
    is_baseline: true
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
    - 0.643
    metric_stds:
    - 0.018
  - model: AttrMasking
    model_plain: AttrMasking
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.03506'
    title: Subgraph Networks Based Contrastive Learning
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.643
    metric_stds:
    - 0.028
  - model: ChemBERTa 10M
    model_plain: ChemBERTa 10M
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.09885'
    title: 'ChemBERTa: Large-Scale Self-Supervised Pretraining for Molecular Property
      Prediction'
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: https://huggingface.co/seyonec/ChemBERTa-zinc-base-v1
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.643
    metric_stds:
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1802.00543'
    title: Modeling polypharmacy side effects with graph convolutional networks
    date: Feb 2, 2018
    date_iso: '2018-02-02'
    date_display: Feb 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.641
    metric_stds:
    - 0.015
  - model: Deepseek-R1
    model_plain: Deepseek-R1
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.01771'
    title: '<SO$ _k$>: One LLM Token for Explicit Graph Structural Understanding'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: https://github.com/Jingyao-Wu/SOG
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.636
    metric_stds:
    - null
  - model: MolCA-GS
    model_plain: MolCA-GS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.01771'
    title: '<SO$ _k$>: One LLM Token for Explicit Graph Structural Understanding'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: https://github.com/Jingyao-Wu/SOG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.636
    metric_stds:
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1802.00543'
    title: Modeling polypharmacy side effects with graph convolutional networks
    date: Feb 2, 2018
    date_iso: '2018-02-02'
    date_display: Feb 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.635
    metric_stds:
    - 0.012
  - model: ChebNet
    model_plain: ChebNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.05481'
    title: A Molecular Multimodal Foundation Model Associating Molecule Graphs with
      Natural Language
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: https://github.com/BingSu12/MoMu
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.635
    metric_stds:
    - 0.017
  - model: DiffPool
    model_plain: DiffPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.10657'
    title: Generalizing Graph Neural Networks on Out-Of-Distribution Graphs
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: https://github.com/googlebaba/StableGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6335
    metric_stds:
    - 0.0221
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
    - 0.6284
    metric_stds:
    - 0.0036
  - model: AttrMask
    model_plain: AttrMask
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.08005'
    title: Evaluating Self-Supervised Learning for Molecular Graph Embeddings
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/hansen7/MolGraphEval
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.627
    metric_stds:
    - 0.027
  - model: MolCA-S
    model_plain: MolCA-S
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.01771'
    title: '<SO$ _k$>: One LLM Token for Explicit Graph Structural Understanding'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: https://github.com/Jingyao-Wu/SOG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.625
    metric_stds:
    - null
  - model: GPT-GNN
    model_plain: GPT-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.08005'
    title: Evaluating Self-Supervised Learning for Molecular Graph Embeddings
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/hansen7/MolGraphEval
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.62
    metric_stds:
    - 0.009
  - model: MLP
    model_plain: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.05481'
    title: A Molecular Multimodal Foundation Model Associating Molecule Graphs with
      Natural Language
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: https://github.com/BingSu12/MoMu
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.612
    metric_stds:
    - 0.019
  - model: SGC
    model_plain: SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.10657'
    title: Generalizing Graph Neural Networks on Out-Of-Distribution Graphs
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: https://github.com/googlebaba/StableGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6117
    metric_stds:
    - 0.0291
  - model: GraphSAGE
    model_plain: GraphSAGE
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
    - 0.6078
    metric_stds:
    - 0.0243
  - model: Galactica-125M
    model_plain: Galactica-125M
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.13089'
    title: 'gimlet: A Unified Graph-Text Model for Instruction-Based Molecule Zero-Shot
      Learning'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/zhao-ht/GIMLET
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.6052
    metric_stds:
    - null
  - model: Feature Map
    model_plain: Feature Map
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.13583'
    title: Fine-tuning Graph Neural Networks by Preserving Graph Generative Patterns
    date: Dec 2023
    date_iso: 2023-12
    date_display: Dec 2023
    codebase_url: https://github.com/zjunet/G-Tuning
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.6042
    metric_stds:
    - 0.0078
  - model: KVPLM
    model_plain: KVPLM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.13089'
    title: 'gimlet: A Unified Graph-Text Model for Instruction-Based Molecule Zero-Shot
      Learning'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/zhao-ht/GIMLET
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.602
    metric_stds:
    - null
  - model: Llama-7b
    model_plain: Llama-7b
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.01771'
    title: '<SO$ _k$>: One LLM Token for Explicit Graph Structural Understanding'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: https://github.com/Jingyao-Wu/SOG
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.601
    metric_stds:
    - null
  - model: CIGA
    model_plain: CIGA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.10657'
    title: Generalizing Graph Neural Networks on Out-Of-Distribution Graphs
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: https://github.com/googlebaba/StableGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6006
    metric_stds:
    - 0.0566
  - model: Gimlet
    model_plain: Gimlet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.01771'
    title: '<SO$ _k$>: One LLM Token for Explicit Graph Structural Understanding'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: https://github.com/Jingyao-Wu/SOG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.594
    metric_stds:
    - null
  - model: Gimlet
    model_plain: Gimlet
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.13089'
    title: 'gimlet: A Unified Graph-Text Model for Instruction-Based Molecule Zero-Shot
      Learning'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/zhao-ht/GIMLET
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.5939
    metric_stds:
    - null
  - model: GPF-AttrMasking
    model_plain: GPF-AttrMasking
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.01771'
    title: '<SO$ _k$>: One LLM Token for Explicit Graph Structural Understanding'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: https://github.com/Jingyao-Wu/SOG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.588
    metric_stds:
    - null
  - model: GraphMAE
    model_plain: GraphMAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.08005'
    title: Evaluating Self-Supervised Learning for Molecular Graph Embeddings
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/hansen7/MolGraphEval
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.586
    metric_stds:
    - 0.023
  - model: GPT-4o
    model_plain: GPT-4o
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.01771'
    title: '<SO$ _k$>: One LLM Token for Explicit Graph Structural Understanding'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: https://github.com/Jingyao-Wu/SOG
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.57
    metric_stds:
    - null
  - model: GPF-GCL
    model_plain: GPF-GCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.01771'
    title: '<SO$ _k$>: One LLM Token for Explicit Graph Structural Understanding'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: https://github.com/Jingyao-Wu/SOG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.565
    metric_stds:
    - null
  - model: Cont. Pred
    model_plain: Cont. Pred
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.08005'
    title: Evaluating Self-Supervised Learning for Molecular Graph Embeddings
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/hansen7/MolGraphEval
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.555
    metric_stds:
    - 0.02
  - model: LLaMA3-3B LoRA SFT
    model_plain: LLaMA3-3B LoRA SFT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.01771'
    title: '<SO$ _k$>: One LLM Token for Explicit Graph Structural Understanding'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: https://github.com/Jingyao-Wu/SOG
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.55
    metric_stds:
    - 0.008
  - model: DIR
    model_plain: DIR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2111.10657'
    title: Generalizing Graph Neural Networks on Out-Of-Distribution Graphs
    date: Nov 2021
    date_iso: 2021-11
    date_display: Nov 2021
    codebase_url: https://github.com/googlebaba/StableGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5465
    metric_stds:
    - 0.0808
  - model: EdgePred
    model_plain: EdgePred
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.08005'
    title: Evaluating Self-Supervised Learning for Molecular Graph Embeddings
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/hansen7/MolGraphEval
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.542
    metric_stds:
    - 0.01
  - model: Galactica-1.3B
    model_plain: Galactica-1.3B
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.13089'
    title: 'gimlet: A Unified Graph-Text Model for Instruction-Based Molecule Zero-Shot
      Learning'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/zhao-ht/GIMLET
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.5394
    metric_stds:
    - null
  - model: LLaMA3-3B Soft Prompt
    model_plain: LLaMA3-3B Soft Prompt
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.01771'
    title: '<SO$ _k$>: One LLM Token for Explicit Graph Structural Understanding'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: https://github.com/Jingyao-Wu/SOG
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.537
    metric_stds:
    - 0.008
  - model: LLaMA3-3B Few-shot (Morgan Sim)
    model_plain: LLaMA3-3B Few-shot (Morgan Sim)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.01771'
    title: '<SO$ _k$>: One LLM Token for Explicit Graph Structural Understanding'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: https://github.com/Jingyao-Wu/SOG
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.513
    metric_stds:
    - 0.008
  - model: Random
    model_plain: Random
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.08005'
    title: Evaluating Self-Supervised Learning for Molecular Graph Embeddings
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/hansen7/MolGraphEval
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.507
    metric_stds:
    - 0.025
  - model: LLaMA3-3B Zero-shot
    model_plain: LLaMA3-3B Zero-shot
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.01771'
    title: '<SO$ _k$>: One LLM Token for Explicit Graph Structural Understanding'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: https://github.com/Jingyao-Wu/SOG
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.5
    metric_stds:
    - 0.0
  - model: MoMu
    model_plain: MoMu
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.13089'
    title: 'gimlet: A Unified Graph-Text Model for Instruction-Based Molecule Zero-Shot
      Learning'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/zhao-ht/GIMLET
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.4981
    metric_stds:
    - null
  - model: All-In-One
    model_plain: All-In-One
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17676'
    title: Instance-Aware Graph Prompt Learning
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4949
    metric_stds:
    - 0.0532
  - model: LLaMA3-3B Few-shot (Random)
    model_plain: LLaMA3-3B Few-shot (Random)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.01771'
    title: '<SO$ _k$>: One LLM Token for Explicit Graph Structural Understanding'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: https://github.com/Jingyao-Wu/SOG
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.494
    metric_stds:
    - 0.006
  - model: Fine Tuning
    model_plain: Fine Tuning
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17676'
    title: Instance-Aware Graph Prompt Learning
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4888
    metric_stds:
    - 0.0068
  - model: CLAMP
    model_plain: CLAMP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.13089'
    title: 'gimlet: A Unified Graph-Text Model for Instruction-Based Molecule Zero-Shot
      Learning'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/zhao-ht/GIMLET
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.4788
    metric_stds:
    - null
  milestones:
  - value: 0.712
    std: 0.008
    model: Graphormer
    arxiv_id: '1802.00543'
    title: Modeling polypharmacy side effects with graph convolutional networks
    date: '2018-02-02'
  - value: 0.92
    std: 0.01
    model: ProtoS-L2
    arxiv_id: '2006.04804'
    title: Optimal Transport Graph Neural Networks
    date: 2020-06
  - value: 0.937
    std: null
    model: MoLFormer-XL
    arxiv_id: '2106.09553'
    title: How Much Structural Information Large Scale Molecular Language Representations
      Can Capture?
    date: 2021-06
  - value: 0.948
    std: 0.019
    model: Gode
    arxiv_id: '2306.01631'
    title: Bi-level Contrastive Learning for Knowledge-Enhanced Molecule Representations
    date: 2023-06
---

