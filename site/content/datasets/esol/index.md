---
title: ESOL
slug: esol
benchmark: MoleculeNet
task_type: graph_regression
description: Aqueous solubility regression (log mol/L) on 1,128 molecules.
primary_metric: RMSE
higher_is_better: false
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.MoleculeNet.html
stats: null
result_count: 98
best_model:
  model: 10% Zinc + 10% Pub
  value: 0.2775
  metric: RMSE
  arxiv_id: '2106.09553'
  paper_title: How Much Structural Information Large Scale Molecular Language Representations
    Can Capture?
variants:
- slug: scaffold-split
  name: Scaffold split
  notes: ''
  is_standard: true
  primary_metric: RMSE
  higher_is_better: false
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - RMSE
  - AUC
  rows:
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
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.2775
    - null
    metric_stds:
    - null
    - null
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2787
    - null
    metric_stds:
    - null
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2798
    - null
    metric_stds:
    - null
    - null
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
    is_best: true
    metric_values:
    - 0.28
    - null
    metric_stds:
    - 0.01
    - null
  - model: SphereNet
    model_plain: SphereNet
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
    - 0.29
    - null
    metric_stds:
    - 0.01
    - null
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3023
    - null
    metric_stds:
    - null
    - null
  - model: DimeNet++
    model_plain: DimeNet++
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
    - 0.32
    - null
    metric_stds:
    - 0.02
    - null
  - model: Graphormer-SPIS
    model_plain: Graphormer-SPIS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.13987'
    title: On Structural Expressive Power of Graph Transformers
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.484
    - null
    metric_stds:
    - 0.005
    - null
  - model: A-FP
    model_plain: A-FP
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.503
    - null
    metric_stds:
    - null
    - null
  - model: Neural FPs + neural net
    model_plain: Neural FPs + neural net
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1509.09292'
    title: Convolutional Networks on Graphs for Learning Molecular Fingerprints
    date: Sep 2015
    date_iso: 2015-09
    date_display: Sep 2015
    codebase_url: https://github.com/HIPS/neural-fingerprint
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.52
    - null
    metric_stds:
    - 0.07
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.13987'
    title: On Structural Expressive Power of Graph Transformers
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.552
    - null
    metric_stds:
    - 0.007
    - null
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
    - 0.555
    - null
    metric_stds:
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.13987'
    title: On Structural Expressive Power of Graph Transformers
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.564
    - null
    metric_stds:
    - 0.015
    - null
  - model: GeomGCL
    model_plain: GeomGCL
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.575
    - null
    metric_stds:
    - null
    - null
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
    - 0.578
    - null
    metric_stds:
    - null
    - null
  - model: PNA
    model_plain: PNA
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
    - 0.58
    - null
    metric_stds:
    - 0.03
    - null
  - model: MPNN
    model_plain: MPNN
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.58
    - null
    metric_stds:
    - null
    - null
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
    - 0.589
    - null
    metric_stds:
    - null
    - null
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
    - 0.594
    - null
    metric_stds:
    - 0.031
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
    is_best: false
    metric_values:
    - 0.605
    - null
    metric_stds:
    - 0.029
    - null
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
    - 0.608
    - null
    metric_stds:
    - 0.029
    - null
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
    is_best: false
    metric_values:
    - 0.612
    - null
    metric_stds:
    - 0.083
    - null
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
    is_best: false
    metric_values:
    - 0.616
    - null
    metric_stds:
    - 0.028
    - null
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
    - 0.624
    - null
    metric_stds:
    - null
    - null
  - model: GCN
    model_plain: GCN
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
    - 0.63
    - null
    metric_stds:
    - 0.05
    - null
  - model: DimeNet++
    model_plain: DimeNet++
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.633
    - null
    metric_stds:
    - null
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
    - 0.635
    - null
    metric_stds:
    - 0.027
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
    - 0.65
    - null
    metric_stds:
    - 0.06
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
    - 0.6532
    - null
    metric_stds:
    - null
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
    - 0.654
    - null
    metric_stds:
    - 0.028
    - null
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
    - 0.665
    - null
    metric_stds:
    - 0.026
    - null
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
    is_best: false
    metric_values:
    - 0.673
    - null
    metric_stds:
    - 0.087
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
    is_best: false
    metric_values:
    - 0.674
    - null
    metric_stds:
    - 0.034
    - null
  - model: GAT
    model_plain: GAT
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.697
    - null
    metric_stds:
    - null
    - null
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
    - 0.701
    - null
    metric_stds:
    - null
    - null
  - model: GIN
    model_plain: GIN
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.724
    - null
    metric_stds:
    - null
    - null
  - model: MoLlama, ours
    model_plain: MoLlama, ours
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.12638'
    title: 'NExT-Mol: 3D Diffusion Meets 1D Language Modeling for 3D Molecule Generation'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/acharkq/NExT-Mol
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.74
    - null
    metric_stds:
    - 0.01
    - null
  - model: GCN
    model_plain: GCN
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.742
    - null
    metric_stds:
    - null
    - null
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
    - 0.746
    - null
    metric_stds:
    - 0.128
    - null
  - model: Neural FPs + linear layer
    model_plain: Neural FPs + linear layer
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1509.09292'
    title: Convolutional Networks on Graphs for Learning Molecular Fingerprints
    date: Sep 2015
    date_iso: 2015-09
    date_display: Sep 2015
    codebase_url: https://github.com/HIPS/neural-fingerprint
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.77
    - null
    metric_stds:
    - 0.11
    - null
  - model: Graphormer
    model_plain: Graphormer
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7725
    - null
    metric_stds:
    - null
    - null
  - model: MolPROP
    model_plain: MolPROP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.12638'
    title: 'NExT-Mol: 3D Diffusion Meets 1D Language Modeling for 3D Molecule Generation'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/acharkq/NExT-Mol
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.777
    - null
    metric_stds:
    - 0.02
    - null
  - model: GEM
    model_plain: GEM
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.798
    - null
    metric_stds:
    - null
    - null
  - model: ChemBERTa
    model_plain: ChemBERTa
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.12638'
    title: 'NExT-Mol: 3D Diffusion Meets 1D Language Modeling for 3D Molecule Generation'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/acharkq/NExT-Mol
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.889
    - null
    metric_stds:
    - 0.0
    - null
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
    - 0.894
    - null
    metric_stds:
    - 0.028
    - null
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
    - 0.902
    - null
    metric_stds:
    - 0.104
    - null
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
    - 0.914
    - null
    metric_stds:
    - null
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
    - 0.914
    - null
    metric_stds:
    - 0.092
    - null
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
    - 0.922
    - null
    metric_stds:
    - 0.017
    - null
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
    - 0.934
    - null
    metric_stds:
    - null
    - null
  - model: GraphCL
    model_plain: GraphCL
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
    - 0.959
    - null
    metric_stds:
    - 0.047
    - null
  - model: GC
    model_plain: GC
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.97
    - null
    metric_stds:
    - null
    - null
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
    - 0.982
    - null
    metric_stds:
    - 0.109
    - null
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
    - 1.027
    - null
    metric_stds:
    - 0.201
    - null
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
    - 1.028
    - null
    metric_stds:
    - 0.145
    - null
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
    - 1.045
    - null
    metric_stds:
    - 0.064
    - null
  - model: D-MPNN
    model_plain: D-MPNN
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
    - 1.05
    - null
    metric_stds:
    - 0.008
    - null
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
    - 1.068
    - null
    metric_stds:
    - 0.05
    - null
  - model: RF
    model_plain: RF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.12638'
    title: 'NExT-Mol: 3D Diffusion Meets 1D Language Modeling for 3D Molecule Generation'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/acharkq/NExT-Mol
    uses_external_data: false
    is_best: false
    metric_values:
    - 1.07
    - null
    metric_stds:
    - 0.19
    - null
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
    - 1.1
    - null
    metric_stds:
    - 0.16
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
    - 1.1
    - null
    metric_stds:
    - 0.006
    - null
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
    - 1.113
    - null
    metric_stds:
    - 0.023
    - null
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
    - 1.158
    - null
    metric_stds:
    - 0.055
    - null
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
    is_best: false
    metric_values:
    - 1.167
    - null
    metric_stds:
    - 0.43
    - null
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
    - 1.167
    - null
    metric_stds:
    - 0.43
    - null
  - model: GIN+Pretrain
    model_plain: GIN+Pretrain
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.12638'
    title: 'NExT-Mol: 3D Diffusion Meets 1D Language Modeling for 3D Molecule Generation'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/acharkq/NExT-Mol
    uses_external_data: false
    is_best: false
    metric_values:
    - 1.22
    - null
    metric_stds:
    - 0.02
    - null
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
    - 1.266
    - null
    metric_stds:
    - 0.147
    - null
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
    - 1.329
    - null
    metric_stds:
    - null
    - null
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 1.394
    - null
    metric_stds:
    - 0.12
    - null
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
    is_best: false
    metric_values:
    - 1.399
    - null
    metric_stds:
    - 0.177
    - null
  - model: Circular FPs + neural net
    model_plain: Circular FPs + neural net
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1509.09292'
    title: Convolutional Networks on Graphs for Learning Molecular Fingerprints
    date: Sep 2015
    date_iso: 2015-09
    date_display: Sep 2015
    codebase_url: https://github.com/HIPS/neural-fingerprint
    uses_external_data: false
    is_best: false
    metric_values:
    - 1.4
    - null
    metric_stds:
    - 0.13
    - null
  - model: GATv2
    model_plain: GATv2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.12638'
    title: 'NExT-Mol: 3D Diffusion Meets 1D Language Modeling for 3D Molecule Generation'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/acharkq/NExT-Mol
    uses_external_data: false
    is_best: false
    metric_values:
    - 1.41
    - null
    metric_stds:
    - 0.0
    - null
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
    - 1.43
    - null
    metric_stds:
    - 0.05
    - null
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 1.438
    - null
    metric_stds:
    - 0.12
    - null
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
    - 1.452
    - null
    metric_stds:
    - 0.02
    - null
  - model: AttrMask
    model_plain: AttrMask
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
    - 1.486
    - null
    metric_stds:
    - 0.12
    - null
  - model: SVM
    model_plain: SVM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.12638'
    title: 'NExT-Mol: 3D Diffusion Meets 1D Language Modeling for 3D Molecule Generation'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/acharkq/NExT-Mol
    uses_external_data: false
    is_best: false
    metric_values:
    - 1.5
    - null
    metric_stds:
    - 0.0
    - null
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 1.507
    - null
    metric_stds:
    - 0.13
    - null
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 1.51
    - null
    metric_stds:
    - 0.09
    - null
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 1.538
    - null
    metric_stds:
    - 0.13
    - null
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 1.553
    - null
    metric_stds:
    - 0.11
    - null
  - model: ContextPred
    model_plain: ContextPred
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
    - 1.597
    - null
    metric_stds:
    - 0.14
    - null
  - model: No Pre-train
    model_plain: No Pre-train
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
    - 1.605
    - null
    metric_stds:
    - 0.08
    - null
  - model: JOAO
    model_plain: JOAO
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
    - 1.64
    - null
    metric_stds:
    - 0.09
    - null
  - model: Circular FPs + linear layer
    model_plain: Circular FPs + linear layer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1509.09292'
    title: Convolutional Networks on Graphs for Learning Molecular Fingerprints
    date: Sep 2015
    date_iso: 2015-09
    date_display: Sep 2015
    codebase_url: https://github.com/HIPS/neural-fingerprint
    uses_external_data: false
    is_best: false
    metric_values:
    - 1.71
    - null
    metric_stds:
    - 0.13
    - null
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
    - 1.717
    - null
    metric_stds:
    - 0.08
    - null
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
    - 1.742
    - null
    metric_stds:
    - 0.05
    - null
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
    - 2.5
    - null
    metric_stds:
    - 0.193
    - null
  - model: GCN
    model_plain: GCN
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 2.64
    - null
    metric_stds:
    - 0.239
    - null
  - model: GROVER
    model_plain: GROVER
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
    - 3.107
    - null
    metric_stds:
    - 1.39
    - null
  - model: Predict mean
    model_plain: Predict mean
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1509.09292'
    title: Convolutional Networks on Graphs for Learning Molecular Fingerprints
    date: Sep 2015
    date_iso: 2015-09
    date_display: Sep 2015
    codebase_url: https://github.com/HIPS/neural-fingerprint
    uses_external_data: false
    is_best: false
    metric_values:
    - 4.29
    - null
    metric_stds:
    - 0.4
    - null
  - model: GNNExplainer
    model_plain: GNNExplainer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.02025'
    title: arXiv:2603.02025
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.518
    metric_stds:
    - null
    - null
  - model: PGExplainer
    model_plain: PGExplainer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.02025'
    title: arXiv:2603.02025
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.779
    metric_stds:
    - null
    - null
  - model: ProtGNN
    model_plain: ProtGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.02025'
    title: arXiv:2603.02025
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.562
    metric_stds:
    - null
    - null
  - model: VGIB
    model_plain: VGIB
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.02025'
    title: arXiv:2603.02025
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.675
    metric_stds:
    - null
    - null
  - model: PGIB
    model_plain: PGIB
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.02025'
    title: arXiv:2603.02025
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.65
    metric_stds:
    - null
    - null
  - model: GCFExplainer
    model_plain: GCFExplainer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.02025'
    title: arXiv:2603.02025
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.805
    metric_stds:
    - null
    - null
  - model: GCBM
    model_plain: GCBM
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.02025'
    title: arXiv:2603.02025
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.912
    metric_stds:
    - null
    - null
  milestones:
  - value: 0.52
    std: 0.07
    model: Neural FPs + neural net
    arxiv_id: '1509.09292'
    title: Convolutional Networks on Graphs for Learning Molecular Fingerprints
    date: 2015-09
  - value: 0.2775
    std: null
    model: 10% Zinc + 10% Pub
    arxiv_id: '2106.09553'
    title: How Much Structural Information Large Scale Molecular Language Representations
      Can Capture?
    date: 2021-06
---

