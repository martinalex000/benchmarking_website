---
title: Graph Learning via Logic-Based Weisfeiler--Leman Variants and Tabularization
arxiv_id: '2508.10651'
authors: []
published_date: Aug 2025
abstract: We present a novel approach for graph classification based on tabularizing
  graph data via new variants of the Weisfeiler–Leman algorithm and then applying
  methods for tabular data. We investigate a comprehensive class of versions of the
  Weisfeiler–Leman algorithm obtained by modifying the underlying logical framework
  and establish a precise theoretical characterization of their expressive power.
  We then test selected versions on 14 benchmark datasets that span a range of application
  domains. The experiments demonstrate that our approach generally achieves better
  predictive performance than graph neural networks and matches that of graph transformers,
  while being 40--60$ $ faster and requiring neither a GPU nor extensive hyperparameter
  tuning.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
proposed_models:
- Full
- Plain
- Maj.
- Int.
- Hyb.
- Q-WL-RF (Ours) Full
- Q-WL-RF (Ours) Plain
- Q-WL-RF (Ours) Maj.
- Q-WL-RF (Ours) Int.
- Q-WL-RF (Ours) Hyb.
mrr: 0.025
results:
- &id002
  dataset: ClinTox
  rows:
  - model: Supervised
    value: 0.8814
    std: 0.0251
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23345'
    title: Graph Positional Autoencoders as Self-supervised Learners
    date: May 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: GraphGPS
    value: 0.859
    std: 0.04
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 2
    is_best: true
  - model: GraphFP_CP
    value: 0.847
    std: 0.058
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    codebase_url: ''
    uses_external_data: true
    is_global_top: true
    global_rank: 3
    is_best: true
  - model: GraphMAE
    value: 0.8269
    std: 0.0339
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23345'
    title: Graph Positional Autoencoders as Self-supervised Learners
    date: May 2025
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 4
    is_best: true
  - model: Q-WL-RF (Ours) Plain
    value: 0.718
    std: 0.02
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 25
    is_best: false
  - model: Q-WL-RF (Ours) Maj.
    value: 0.706
    std: 0.033
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 28
    is_best: false
  - model: Q-WL-RF (Ours) Int.
    value: 0.695
    std: 0.03
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 31
    is_best: false
  - model: Q-WL-RF (Ours) Hyb.
    value: 0.68
    std: 0.022
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 32
    is_best: false
  - model: Q-WL-RF (Ours) Full
    value: 0.656
    std: 0.013
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 37
    is_best: false
  - model: GIN
    value: 0.64
    std: 0.047
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 41
    is_best: false
  - model: GCN
    value: 0.591
    std: 0.021
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 1
    source_ref: this paper
    global_rank: 13
    is_best: false
  - model: Kern. WL
    value: 0.537
    std: 0.041
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 46
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id001
  dataset: Peptides-func
  rows:
  - model: LightGBM (ECFP)
    value: 0.746
    std: null
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: '2025-01-29'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: Random Forest (ECFP)
    value: 0.7355
    std: 0.001
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: '2025-01-29'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: false
  - model: LightGBM (TT)
    value: 0.7318
    std: null
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: '2025-01-29'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: Full
    value: 0.705
    std: 0.003
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 40
    is_best: false
  - model: Hyb.
    value: 0.705
    std: 0.003
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 41
    is_best: false
  - model: WL-GK
    value: 0.671
    std: null
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 125
    is_best: false
  - model: GraphGPS
    value: 0.654
    std: 0.01
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 162
    is_best: false
  - model: GIN
    value: 0.594
    std: 0.012
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 39
    is_best: false
  - model: GCN
    value: 0.541
    std: 0.007
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 1
    source_ref: this paper
    global_rank: 9
    is_best: false
  - model: Plain
    value: 0.306
    std: 0.001
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 304
    is_best: false
  - model: Maj.
    value: 0.306
    std: 0.001
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 305
    is_best: false
  - model: Int.
    value: 0.306
    std: 0.001
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 306
    is_best: false
  metric: AP
  higher_is_better: true
results_grouped:
- benchmark: LRGB
  datasets:
  - *id001
- benchmark: MoleculeNet
  datasets:
  - *id002
main_figure: /figures/2508.10651/main_figure.png
---

