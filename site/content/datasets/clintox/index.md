---
title: ClinTox
slug: clintox
benchmark: MoleculeNet
task_type: graph_classification
description: Clinical toxicity prediction — FDA-approved vs. failed drugs (2 tasks).
primary_metric: ROC-AUC
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.MoleculeNet.html
stats:
  num_graphs: null
  avg_nodes: null
  avg_edges: null
  num_classes: 2
result_count: 142
best_model:
  model: SGLB
  value: 0.993
  metric: ROC-AUC
  arxiv_id: '2312.07633'
  paper_title: SE(3)-Invariant Multiparameter Persistent Homology for Chiral-Sensitive
    Molecular Property Prediction
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
    - 0.993
    metric_stds:
    - 0.004
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
    - 0.954
    metric_stds:
    - 0.011
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
    is_best: false
    metric_values:
    - 0.948
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
    is_best: false
    metric_values:
    - 0.947
    metric_stds:
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
    - 0.947
    metric_stds:
    - 0.029
  - model: LLaMA2-7B <SOG_k>
    model_plain: LLaMA2-7B
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.943
    metric_stds:
    - 0.001
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
    - 0.936
    metric_stds:
    - 0.007
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
    - 0.929
    metric_stds:
    - 0.011
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
    - 0.926
    metric_stds:
    - 0.007
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
    - 0.919
    metric_stds:
    - 0.018
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
    - 0.919
    metric_stds:
    - null
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
    - 0.906
    metric_stds:
    - null
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
    - 0.901
    metric_stds:
    - 0.013
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
    - 0.9
    metric_stds:
    - null
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
    - 0.898
    metric_stds:
    - 0.012
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
    - 0.898
    metric_stds:
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
    - 0.898
    metric_stds:
    - 0.027
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
    - 0.893
    metric_stds:
    - 0.031
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
    - 0.8902
    metric_stds:
    - 0.0121
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
    - 0.886
    metric_stds:
    - null
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
    - 0.8855
    metric_stds:
    - 0.0209
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
    - 0.879
    metric_stds:
    - 0.054
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
    - 0.879
    metric_stds:
    - 0.054
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
    - 0.877
    metric_stds:
    - 0.011
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
    - 0.877
    metric_stds:
    - null
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
    - 0.876
    metric_stds:
    - 0.007
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
    - 0.875
    metric_stds:
    - 0.027
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
    - 0.873
    metric_stds:
    - 0.02
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
    - 0.87
    metric_stds:
    - 0.005
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
    - 0.8675
    metric_stds:
    - 0.0104
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
    - 0.8635
    metric_stds:
    - 0.0127
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.861
    metric_stds:
    - 0.009
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
    - 0.859
    metric_stds:
    - 0.032
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
    - 0.859
    metric_stds:
    - 0.023
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
    - 0.858
    metric_stds:
    - 0.042
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
    - 0.855
    metric_stds:
    - 0.037
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.855
    metric_stds:
    - 0.037
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
    - 0.854
    metric_stds:
    - 0.008
  - model: GraphMVP
    model_plain: GraphMVP
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
    - 0.854
    metric_stds:
    - 0.008
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
    - 0.853
    metric_stds:
    - 0.022
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
    - 0.847
    metric_stds:
    - 0.009
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
    - 0.845
    metric_stds:
    - 0.01
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
    - 0.845
    metric_stds:
    - 0.051
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
    - 0.843
    metric_stds:
    - 0.027
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
    - 0.8406
    metric_stds:
    - 0.0384
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.834
    metric_stds:
    - 0.009
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
    - 0.833
    metric_stds:
    - null
  - model: SphereNet
    model_plain: SphereNet
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
    - 0.831
    metric_stds:
    - 0.01
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.826
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
    - 0.825
    metric_stds:
    - 0.012
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
    - 0.825
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
    - 0.824
    metric_stds:
    - 0.013
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
    - 0.823
    metric_stds:
    - 0.012
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
    - 0.823
    metric_stds:
    - 0.017
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
    - 0.823
    metric_stds:
    - 0.023
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
    - 0.823
    metric_stds:
    - 0.012
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
    - 0.822
    metric_stds:
    - null
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.813
    metric_stds:
    - 0.025
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
    - 0.812
    metric_stds:
    - 0.015
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
    - 0.812
    metric_stds:
    - 0.015
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
    - 0.812
    metric_stds:
    - 0.017
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
    - 0.808
    metric_stds:
    - null
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
    - 0.807
    metric_stds:
    - 0.021
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
    - 0.802
    metric_stds:
    - 0.015
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.798
    metric_stds:
    - 0.035
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
    - 0.795
    metric_stds:
    - 0.018
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
    - 0.795
    metric_stds:
    - 0.06
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
    - 0.791
    metric_stds:
    - 0.024
  - model: GraphCL
    model_plain: GraphCL
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
    - 0.789
    metric_stds:
    - 0.042
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
    - 0.789
    metric_stds:
    - 0.03
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
    - 0.789
    metric_stds:
    - 0.015
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
    - 0.788
    metric_stds:
    - 0.02
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
    - 0.782
    metric_stds:
    - 0.021
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
    - 0.781
    metric_stds:
    - null
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
    - 0.778
    metric_stds:
    - 0.02
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
    - 0.778
    metric_stds:
    - 0.02
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
    - 0.775
    metric_stds:
    - 0.042
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
    - 0.767
    metric_stds:
    - 0.033
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
    - 0.765
    metric_stds:
    - 0.01
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
    - 0.765
    metric_stds:
    - 0.019
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
    - 0.76
    metric_stds:
    - null
  - model: Infomax + S2PGNN
    model_plain: Infomax + S2PGNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06960'
    title: Search to Fine-tune Pre-trained Graph Neural Networks for Graph-level Tasks
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/zwangeo/icde2024
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.748
    metric_stds:
    - 0.038
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
    - 0.747
    metric_stds:
    - 0.044
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7464
    metric_stds:
    - 0.043
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
    - 0.745
    metric_stds:
    - 0.0076
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
    - 0.739
    metric_stds:
    - null
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
    - 0.7385
    metric_stds:
    - 0.0215
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
    - 0.737
    metric_stds:
    - 0.04
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
    - 0.737
    metric_stds:
    - 0.04
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.735
    metric_stds:
    - 0.043
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
    - 0.7331
    metric_stds:
    - 0.0408
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
    - 0.733
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
    - 0.726
    metric_stds:
    - 0.015
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7211
    metric_stds:
    - 0.0306
  - model: EdgePred + S2PGNN
    model_plain: EdgePred + S2PGNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06960'
    title: Search to Fine-tune Pre-trained Graph Neural Networks for Graph-level Tasks
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/zwangeo/icde2024
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.719
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.718
    metric_stds:
    - 0.041
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7177
    metric_stds:
    - 0.0538
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
    - 0.717
    metric_stds:
    - 0.042
  - model: Infomax
    model_plain: Infomax
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.06960'
    title: Search to Fine-tune Pre-trained Graph Neural Networks for Graph-level Tasks
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: https://github.com/zwangeo/icde2024
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.713
    metric_stds:
    - 0.026
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7075
    metric_stds:
    - 0.0498
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
    - 0.7033
    metric_stds:
    - 0.0376
  - model: InfoGraph
    model_plain: InfoGraph
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.699
    metric_stds:
    - 0.03
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
    - 0.693
    metric_stds:
    - null
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6863
    metric_stds:
    - 0.013
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6812
    metric_stds:
    - 0.0377
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
    - 0.68
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
    - 0.674
    metric_stds:
    - 0.043
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6592
    metric_stds:
    - 0.0378
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6553
    metric_stds:
    - 0.0425
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
    - 0.654
    metric_stds:
    - 0.05
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
    - 0.653
    metric_stds:
    - 0.061
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
    - 0.65
    metric_stds:
    - 0.064
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
    - 0.647
    metric_stds:
    - 0.005
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6405
    metric_stds:
    - 0.034
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
    - 0.634
    metric_stds:
    - 0.042
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
    - 0.631
    metric_stds:
    - 0.023
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
    - 0.625
    metric_stds:
    - 0.028
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
    - 0.62
    metric_stds:
    - 0.018
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
    - 0.619
    metric_stds:
    - 0.064
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
    - 0.614
    metric_stds:
    - 0.048
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
    - 0.613
    metric_stds:
    - null
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
    - 0.608
    metric_stds:
    - 0.03
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
    - 0.599
    metric_stds:
    - 0.082
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
    - 0.5957
    metric_stds:
    - 0.024
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
    - 0.594
    metric_stds:
    - 0.032
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
    - 0.594
    metric_stds:
    - 0.032
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.593
    metric_stds:
    - 0.037
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
    - 0.587
    metric_stds:
    - 0.019
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5806
    metric_stds:
    - 0.0442
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
    - 0.58
    metric_stds:
    - 0.044
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
    - 0.58
    metric_stds:
    - 0.044
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
    - 0.5778
    metric_stds:
    - 0.0403
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
    - 0.5765
    metric_stds:
    - 0.1111
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.568
    metric_stds:
    - 0.063
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
    - 0.55
    metric_stds:
    - 0.051
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.518
    metric_stds:
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
    - 0.511
    metric_stds:
    - 0.055
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.503
    metric_stds:
    - 0.017
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.497
    metric_stds:
    - 0.047
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.488
    metric_stds:
    - null
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.482
    metric_stds:
    - null
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.44
    metric_stds:
    - 0.026
  milestones:
  - value: 0.854
    std: 0.008
    model: Graphormer
    arxiv_id: '1802.00543'
    title: Modeling polypharmacy side effects with graph convolutional networks
    date: '2018-02-02'
  - value: 0.906
    std: null
    model: D-MPNN
    arxiv_id: '2010.09885'
    title: 'ChemBERTa: Large-Scale Self-Supervised Pretraining for Molecular Property
      Prediction'
    date: 2020-10
  - value: 0.948
    std: null
    model: MoLFormer-XL
    arxiv_id: '2106.09553'
    title: How Much Structural Information Large Scale Molecular Language Representations
      Can Capture?
    date: 2021-06
  - value: 0.954
    std: 0.011
    model: unified method
    arxiv_id: '2207.08806'
    title: Unified 2D and 3D Pre-Training of Molecular Representations
    date: 2022-07
  - value: 0.993
    std: 0.004
    model: SGLB
    arxiv_id: '2312.07633'
    title: SE(3)-Invariant Multiparameter Persistent Homology for Chiral-Sensitive
      Molecular Property Prediction
    date: 2023-12
---

