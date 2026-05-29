---
title: SIDER
slug: sider
benchmark: MoleculeNet
task_type: graph_classification
description: Multi-label classification of marketed drug side effects (27 tasks).
primary_metric: ROC-AUC
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.MoleculeNet.html
stats:
  num_graphs: null
  avg_nodes: null
  avg_edges: null
  num_classes: 27
result_count: 110
best_model:
  model: MoLFormer-XL
  value: 0.69
  metric: ROC-AUC
  arxiv_id: '2106.09553'
  paper_title: How Much Structural Information Large Scale Molecular Language Representations
    Can Capture?
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
    - 0.69
    metric_stds:
    - null
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
    is_best: true
    metric_values:
    - 0.69
    metric_stds:
    - null
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
    is_best: true
    metric_values:
    - 0.685
    metric_stds:
    - 0.008
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.684
    metric_stds:
    - 0.003
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
    - 0.674
    metric_stds:
    - 0.005
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
    - 0.674
    metric_stds:
    - 0.01
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
    is_best: false
    metric_values:
    - 0.674
    metric_stds:
    - 0.014
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.672
    metric_stds:
    - 0.004
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
    - 0.668
    metric_stds:
    - null
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
  - model: Graphormer
    model_plain: Graphormer
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
    - 0.661
    metric_stds:
    - 0.011
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.659
    metric_stds:
    - 0.013
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
  - model: SAN
    model_plain: SAN
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
    - 0.658
    metric_stds:
    - 0.012
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
    is_best: false
    metric_values:
    - 0.655
    metric_stds:
    - 0.016
  - model: PatchGT-DeeperGCN
    model_plain: PatchGT-DeeperGCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.14425'
    title: 'PatchGT: Transformer over Non-trainable Clusters for Learning Graph Representations'
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: https://github.com/tufts-ml/PatchGT
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6546
    metric_stds:
    - 0.0103
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
    is_best: false
    metric_values:
    - 0.653
    metric_stds:
    - 0.014
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.649
    metric_stds:
    - 0.003
  - model: PatchGT-GCN
    model_plain: PatchGT-GCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.14425'
    title: 'PatchGT: Transformer over Non-trainable Clusters for Learning Graph Representations'
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: https://github.com/tufts-ml/PatchGT
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.649
    metric_stds:
    - 0.0092
  - model: GROVER
    model_plain: GROVER
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.648
    metric_stds:
    - 0.006
  - model: GeomGCL
    model_plain: GeomGCL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2109.11730'
    title: 'GeomGCL: Geometric Graph Contrastive Learning for Molecular Property Prediction'
    date: Sep 2021
    date_iso: 2021-09
    date_display: Sep 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.648
    metric_stds:
    - null
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
    - 0.648
    metric_stds:
    - null
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
    - 0.646
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
    - 0.646
    metric_stds:
    - 0.005
  - model: DGN
    model_plain: DGN
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
    - 0.645
    metric_stds:
    - 0.016
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.643
    metric_stds:
    - 0.005
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.643
    metric_stds:
    - 0.009
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
  - model: 3D Infomax
    model_plain: 3D Infomax
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.641
    metric_stds:
    - 0.001
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
    - 0.641
    metric_stds:
    - 0.015
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
    - 0.641
    metric_stds:
    - 0.007
  - model: GraphMVP
    model_plain: GraphMVP
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
    - 0.639
    metric_stds:
    - 0.012
  - model: GeomMPNN
    model_plain: GeomMPNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2109.11730'
    title: 'GeomGCL: Geometric Graph Contrastive Learning for Molecular Property Prediction'
    date: Sep 2021
    date_iso: 2021-09
    date_display: Sep 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.638
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
    is_best: false
    metric_values:
    - 0.638
    metric_stds:
    - 0.012
  - model: D-MPNN
    model_plain: D-MPNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2109.11730'
    title: 'GeomGCL: Geometric Graph Contrastive Learning for Molecular Property Prediction'
    date: Sep 2021
    date_iso: 2021-09
    date_display: Sep 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.637
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
    - 0.633
    metric_stds:
    - 0.008
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
    - 0.633
    metric_stds:
    - 0.025
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
    is_best: false
    metric_values:
    - 0.6321
    metric_stds:
    - 0.0149
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
    - 0.632
    metric_stds:
    - 0.005
  - model: MoCL
    model_plain: MoCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2109.11730'
    title: 'GeomGCL: Geometric Graph Contrastive Learning for Molecular Property Prediction'
    date: Sep 2021
    date_iso: 2021-09
    date_display: Sep 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.629
    metric_stds:
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
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
    - 0.628
    metric_stds:
    - 0.011
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.628
    metric_stds:
    - 0.011
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
    - 0.627
    metric_stds:
    - 0.008
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
    is_best: false
    metric_values:
    - 0.6268
    metric_stds:
    - 0.0182
  - model: CoMPT
    model_plain: CoMPT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2109.11730'
    title: 'GeomGCL: Geometric Graph Contrastive Learning for Molecular Property Prediction'
    date: Sep 2021
    date_iso: 2021-09
    date_display: Sep 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.626
    metric_stds:
    - null
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
    - 0.6245
    metric_stds:
    - 0.0125
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
    - 0.623
    metric_stds:
    - 0.009
  - model: ContextPred
    model_plain: ContextPred
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.622
    metric_stds:
    - 0.005
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
    is_best: false
    metric_values:
    - 0.6214
    metric_stds:
    - 0.0113
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
    is_best: false
    metric_values:
    - 0.6192
    metric_stds:
    - 0.0089
  - model: MAT
    model_plain: MAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2109.11730'
    title: 'GeomGCL: Geometric Graph Contrastive Learning for Molecular Property Prediction'
    date: Sep 2021
    date_iso: 2021-09
    date_display: Sep 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.619
    metric_stds:
    - null
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
    - 0.6165
    metric_stds:
    - 0.0077
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
    - 0.6162
    metric_stds:
    - 0.0112
  - model: MGSSL
    model_plain: MGSSL
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
    - 0.616
    metric_stds:
    - 0.01
  - model: DimeNet++
    model_plain: DimeNet++
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2109.11730'
    title: 'GeomGCL: Geometric Graph Contrastive Learning for Molecular Property Prediction'
    date: Sep 2021
    date_iso: 2021-09
    date_display: Sep 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.615
    metric_stds:
    - null
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
    - 0.614
    metric_stds:
    - 0.006
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
    - 0.6122
    metric_stds:
    - 0.012
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.612
    metric_stds:
    - 0.011
  - model: AttrMask
    model_plain: AttrMask
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.612
    metric_stds:
    - 0.001
  - model: Nested GIN
    model_plain: Nested GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.14425'
    title: 'PatchGT: Transformer over Non-trainable Clusters for Learning Graph Representations'
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: https://github.com/tufts-ml/PatchGT
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.612
    metric_stds:
    - 0.0115
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
    - 0.612
    metric_stds:
    - 0.036
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
    - 0.612
    metric_stds:
    - 0.011
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
    - 0.61
    metric_stds:
    - 0.007
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
    - 0.609
    metric_stds:
    - 0.006
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.608
    metric_stds:
    - 0.003
  - model: MGNN
    model_plain: MGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2109.11730'
    title: 'GeomGCL: Geometric Graph Contrastive Learning for Molecular Property Prediction'
    date: Sep 2021
    date_iso: 2021-09
    date_display: Sep 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.607
    metric_stds:
    - null
  - model: GraphMVP
    model_plain: GraphMVP
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2212.10789'
    title: Multi-modal Molecule Structure-text Model for Text-based Retrieval and
      Editing
    date: Dec 2022
    date_iso: 2022-12
    date_display: Dec 2022
    codebase_url: https://huggingface.co/datasets/chao1224/MoleculeSTM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6064
    metric_stds:
    - 0.0013
  - model: AttentiveFP
    model_plain: AttentiveFP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2109.11730'
    title: 'GeomGCL: Geometric Graph Contrastive Learning for Molecular Property Prediction'
    date: Sep 2021
    date_iso: 2021-09
    date_display: Sep 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.605
    metric_stds:
    - null
  - model: EdgePred
    model_plain: EdgePred
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
    - 0.604
    metric_stds:
    - 0.007
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
    - 0.604
    metric_stds:
    - 0.006
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
    - 0.603
    metric_stds:
    - 0.011
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
    - 0.602
    metric_stds:
    - 0.011
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
    - 0.6
    metric_stds:
    - 0.008
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
    - 0.599
    metric_stds:
    - 0.017
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.599
    metric_stds:
    - 0.003
  - model: GCN-VN
    model_plain: GCN-VN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.14425'
    title: 'PatchGT: Transformer over Non-trainable Clusters for Learning Graph Representations'
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: https://github.com/tufts-ml/PatchGT
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5984
    metric_stds:
    - 0.0154
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
    - 0.595
    metric_stds:
    - 0.009
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
    is_best: false
    metric_values:
    - 0.595
    metric_stds:
    - 0.03
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
    - 0.586
    metric_stds:
    - 0.004
  - model: InfoGraph
    model_plain: InfoGraph
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2109.11730'
    title: 'GeomGCL: Geometric Graph Contrastive Learning for Molecular Property Prediction'
    date: Sep 2021
    date_iso: 2021-09
    date_display: Sep 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.585
    metric_stds:
    - null
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
    - 0.584
    metric_stds:
    - 0.008
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
    - 0.583
    metric_stds:
    - 0.015
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
    - 0.583
    metric_stds:
    - 0.003
  - model: GIN-VN
    model_plain: GIN-VN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.14425'
    title: 'PatchGT: Transformer over Non-trainable Clusters for Learning Graph Representations'
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: https://github.com/tufts-ml/PatchGT
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5775
    metric_stds:
    - 0.0114
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.577
    metric_stds:
    - 0.003
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
    - 0.576
    metric_stds:
    - 0.016
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
    - 0.573
    metric_stds:
    - 0.016
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
    - 0.573
    metric_stds:
    - 0.05
  - model: GIN
    model_plain: GIN
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
    - 0.573
    metric_stds:
    - 0.016
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
    - 0.572
    metric_stds:
    - 0.01
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
    - 0.571
    metric_stds:
    - 0.005
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
    - 0.57
    metric_stds:
    - 0.018
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
    - 0.561
    metric_stds:
    - 0.001
  - model: STGCN
    model_plain: STGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2109.11730'
    title: 'GeomGCL: Geometric Graph Contrastive Learning for Molecular Property Prediction'
    date: Sep 2021
    date_iso: 2021-09
    date_display: Sep 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.56
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
    - 0.553
    metric_stds:
    - 0.008
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
    - 0.552
    metric_stds:
    - 0.018
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
    - 0.545
    metric_stds:
    - 0.038
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
    - 0.536
    metric_stds:
    - 0.003
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
    - 0.532
    metric_stds:
    - 0.011
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
    - 0.5285
    metric_stds:
    - 0.0084
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
    - 0.5261
    metric_stds:
    - 0.0039
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
    - 0.5244
    metric_stds:
    - 0.0083
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
    - 0.5224
    metric_stds:
    - 0.0016
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
    - 0.5211
    metric_stds:
    - 0.0151
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
    - 0.513
    metric_stds:
    - 0.0221
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
    - 0.5124
    metric_stds:
    - 0.0206
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
    - 0.4914
    metric_stds:
    - 0.0119
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
    - 0.4854
    metric_stds:
    - 0.0075
  milestones:
  - value: 0.685
    std: 0.008
    model: Graphormer
    arxiv_id: '1802.00543'
    title: Modeling polypharmacy side effects with graph convolutional networks
    date: '2018-02-02'
  - value: 0.69
    std: null
    model: MoLFormer-XL
    arxiv_id: '2106.09553'
    title: How Much Structural Information Large Scale Molecular Language Representations
      Can Capture?
    date: 2021-06
---

