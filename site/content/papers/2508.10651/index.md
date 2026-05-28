---
title: Graph Learning via Logic-Based Weisfeiler--Leman Variants and Tabularization
arxiv_id: '2508.10651'
source_url: ''
authors: []
published_date: Aug 2025
published_date_iso: 2025-08
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
paper_type: method
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
mrr: 0.0238
adjusted_mrr: 0.0079
mrr_dataset_count: 1
benchmark_categories:
- LRGB
- OGB
- MoleculeNet
task_categories:
- graph_classification
experiment_scopes:
- graph-level
results:
- &id003
  dataset: ClinTox
  rows:
  - model: Supervised
    model_key: supervised
    model_plain: Supervised
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
    date_display: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.8814
    sort_std: 0.0251
    is_best: true
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.859
    std: 0.04
    paper_value: 0.859
    paper_std: 0.04
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to clintox (score=90)'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 3
    true_value: 0.859
    true_std: 0.04
    value_gap_source_arxiv: '2508.10651'
    value_gap_source_title: Graph Learning via Logic-Based Weisfeiler--Leman Variants
      and Tabularization
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.859
    sort_std: 0.04
    is_best: true
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.859
    std: 0.04
    paper_value: 0.859
    paper_std: 0.04
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 2
    true_value: 0.859
    true_std: 0.04
    value_gap_source_arxiv: '2508.10651'
    value_gap_source_title: Graph Learning via Logic-Based Weisfeiler--Leman Variants
      and Tabularization
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.859
    sort_std: 0.04
    is_best: true
  - model: GraphFP_CP
    model_key: graphfp_cp
    model_plain: GraphFP_CP
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
    date_display: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: true
    is_global_top: true
    global_rank: 4
    sort_value: 0.847
    sort_std: 0.058
    is_best: true
  - model: CP, \(α = 0.1\)
    model_key: cp, \(α = 0.1\)
    model_plain: CP, \(α = 0.1\)
    value: 0.847
    std: 0.088
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    sort_value: 0.847
    sort_std: 0.088
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.591
    std: 0.021
    paper_value: 0.591
    paper_std: 0.021
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to clintox (score=90)'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 16
    true_value: 0.781
    true_std: 0.058
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.19000000000000006
    value_note: ''
    paper_rank: 50
    rank_delta: 34
    rank_delta_abs: 34
    rank_delta_direction: worse
    sort_value: 0.781
    sort_std: 0.058
    is_best: false
  - model: Q-WL-RF (Ours) Plain
    model_key: q-wl-rf (ours) plain
    model_plain: Q-WL-RF (Ours) Plain
    value: 0.718
    std: 0.02
    paper_value: 0.718
    paper_std: 0.02
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 28
    true_value: 0.718
    true_std: 0.02
    value_gap_source_arxiv: '2508.10651'
    value_gap_source_title: Graph Learning via Logic-Based Weisfeiler--Leman Variants
      and Tabularization
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 28
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.718
    sort_std: 0.02
    is_best: false
  - model: Q-WL-RF (Plain)
    model_key: q-wl-rf (plain)
    model_plain: Q-WL-RF (Plain)
    value: 0.718
    std: 0.02
    paper_value: 0.718
    paper_std: 0.02
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to clintox (score=90)'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 31
    true_value: 0.718
    true_std: 0.02
    value_gap_source_arxiv: '2508.10651'
    value_gap_source_title: Graph Learning via Logic-Based Weisfeiler--Leman Variants
      and Tabularization
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.718
    sort_std: 0.02
    is_best: false
  - model: Q-WL-RF (Ours) Maj.
    model_key: q-wl-rf (ours) maj.
    model_plain: Q-WL-RF (Ours) Maj.
    value: 0.706
    std: 0.033
    paper_value: 0.706
    paper_std: 0.033
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 32
    true_value: 0.706
    true_std: 0.033
    value_gap_source_arxiv: '2508.10651'
    value_gap_source_title: Graph Learning via Logic-Based Weisfeiler--Leman Variants
      and Tabularization
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.706
    sort_std: 0.033
    is_best: false
  - model: Q-WL-RF (Maj.)
    model_key: q-wl-rf (maj.)
    model_plain: Q-WL-RF (Maj.)
    value: 0.706
    std: 0.033
    paper_value: 0.706
    paper_std: 0.033
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to clintox (score=90)'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 33
    true_value: 0.706
    true_std: 0.033
    value_gap_source_arxiv: '2508.10651'
    value_gap_source_title: Graph Learning via Logic-Based Weisfeiler--Leman Variants
      and Tabularization
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.706
    sort_std: 0.033
    is_best: false
  - model: Q-WL-RF (Ours) Int.
    model_key: q-wl-rf (ours) int.
    model_plain: Q-WL-RF (Ours) Int.
    value: 0.695
    std: 0.03
    paper_value: 0.695
    paper_std: 0.03
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 36
    true_value: 0.695
    true_std: 0.03
    value_gap_source_arxiv: '2508.10651'
    value_gap_source_title: Graph Learning via Logic-Based Weisfeiler--Leman Variants
      and Tabularization
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 36
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.695
    sort_std: 0.03
    is_best: false
  - model: Q-WL-RF (Int.)
    model_key: q-wl-rf (int.)
    model_plain: Q-WL-RF (Int.)
    value: 0.695
    std: 0.03
    paper_value: 0.695
    paper_std: 0.03
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to clintox (score=90)'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 37
    true_value: 0.695
    true_std: 0.03
    value_gap_source_arxiv: '2508.10651'
    value_gap_source_title: Graph Learning via Logic-Based Weisfeiler--Leman Variants
      and Tabularization
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 37
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.695
    sort_std: 0.03
    is_best: false
  - model: Q-WL-RF (Ours) Hyb.
    model_key: q-wl-rf (ours) hyb.
    model_plain: Q-WL-RF (Ours) Hyb.
    value: 0.68
    std: 0.022
    paper_value: 0.68
    paper_std: 0.022
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 38
    true_value: 0.68
    true_std: 0.022
    value_gap_source_arxiv: '2508.10651'
    value_gap_source_title: Graph Learning via Logic-Based Weisfeiler--Leman Variants
      and Tabularization
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.68
    sort_std: 0.022
    is_best: false
  - model: Q-WL-RF (Hyb.)
    model_key: q-wl-rf (hyb.)
    model_plain: Q-WL-RF (Hyb.)
    value: 0.68
    std: 0.022
    paper_value: 0.68
    paper_std: 0.022
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to clintox (score=90)'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 39
    true_value: 0.68
    true_std: 0.022
    value_gap_source_arxiv: '2508.10651'
    value_gap_source_title: Graph Learning via Logic-Based Weisfeiler--Leman Variants
      and Tabularization
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.68
    sort_std: 0.022
    is_best: false
  - model: Q-WL-RF (Ours) Full
    model_key: q-wl-rf (ours) full
    model_plain: Q-WL-RF (Ours) Full
    value: 0.656
    std: 0.013
    paper_value: 0.656
    paper_std: 0.013
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 44
    true_value: 0.656
    true_std: 0.013
    value_gap_source_arxiv: '2508.10651'
    value_gap_source_title: Graph Learning via Logic-Based Weisfeiler--Leman Variants
      and Tabularization
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 44
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.656
    sort_std: 0.013
    is_best: false
  - model: Q-WL-RF (Full)
    model_key: q-wl-rf (full)
    model_plain: Q-WL-RF (Full)
    value: 0.656
    std: 0.013
    paper_value: 0.656
    paper_std: 0.013
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to clintox (score=90)'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 45
    true_value: 0.656
    true_std: 0.013
    value_gap_source_arxiv: '2508.10651'
    value_gap_source_title: Graph Learning via Logic-Based Weisfeiler--Leman Variants
      and Tabularization
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 45
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.656
    sort_std: 0.013
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.64
    std: 0.047
    paper_value: 0.64
    paper_std: 0.047
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to clintox (score=90)'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 49
    true_value: 0.64
    true_std: 0.047
    value_gap_source_arxiv: '2508.10651'
    value_gap_source_title: Graph Learning via Logic-Based Weisfeiler--Leman Variants
      and Tabularization
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 49
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.64
    sort_std: 0.047
    is_best: false
  - model: Kern. WL
    model_key: kern. wl
    model_plain: Kern. WL
    value: 0.537
    std: 0.041
    paper_value: 0.537
    paper_std: 0.041
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to clintox (score=90)'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 54
    true_value: 0.537
    true_std: 0.041
    value_gap_source_arxiv: '2508.10651'
    value_gap_source_title: Graph Learning via Logic-Based Weisfeiler--Leman Variants
      and Tabularization
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 54
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.537
    sort_std: 0.041
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id001
  dataset: Peptides-func
  rows:
  - model: LightGBM (ECFP)
    model_key: lightgbm (ecfp)
    model_plain: LightGBM (ECFP)
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
    date_display: Jan 2025
    date_iso: '2025-01-29'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.746
    sort_std: null
    is_best: true
  - model: Random Forest (ECFP)
    model_key: random forest (ecfp)
    model_plain: Random Forest (ECFP)
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
    date_display: Jan 2025
    date_iso: '2025-01-29'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.7355
    sort_std: 0.001
    is_best: false
  - model: LightGBM (TT)
    model_key: lightgbm (tt)
    model_plain: LightGBM (TT)
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
    date_display: Jan 2025
    date_iso: '2025-01-29'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.7318
    sort_std: null
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.541
    std: 0.007
    paper_value: 0.541
    paper_std: 0.007
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 9
    true_value: 0.7261
    true_std: 0.0067
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.18509999999999993
    value_note: ''
    paper_rank: 291
    rank_delta: 282
    rank_delta_abs: 282
    rank_delta_direction: worse
    sort_value: 0.7261
    sort_std: 0.0067
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.594
    std: 0.012
    paper_value: 0.594
    paper_std: 0.012
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 41
    true_value: 0.7059
    true_std: 0.0089
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1119
    value_note: ''
    paper_rank: 260
    rank_delta: 219
    rank_delta_abs: 219
    rank_delta_direction: worse
    sort_value: 0.7059
    sort_std: 0.0089
    is_best: false
  - model: Full
    model_key: full
    model_plain: Full
    value: 0.705
    std: 0.003
    paper_value: 0.705
    paper_std: 0.003
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 42
    true_value: 0.705
    true_std: 0.003
    value_gap_source_arxiv: '2508.10651'
    value_gap_source_title: Graph Learning via Logic-Based Weisfeiler--Leman Variants
      and Tabularization
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 42
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.705
    sort_std: 0.003
    is_best: false
  - model: Hyb.
    model_key: hyb.
    model_plain: Hyb.
    value: 0.705
    std: 0.003
    paper_value: 0.705
    paper_std: 0.003
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 43
    true_value: 0.705
    true_std: 0.003
    value_gap_source_arxiv: '2508.10651'
    value_gap_source_title: Graph Learning via Logic-Based Weisfeiler--Leman Variants
      and Tabularization
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 43
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.705
    sort_std: 0.003
    is_best: false
  - model: WL-GK
    model_key: wl-gk
    model_plain: WL-GK
    value: 0.671
    std: 0.0
    paper_value: 0.671
    paper_std: 0.0
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 127
    true_value: 0.671
    true_std: 0.0
    value_gap_source_arxiv: '2508.10651'
    value_gap_source_title: Graph Learning via Logic-Based Weisfeiler--Leman Variants
      and Tabularization
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 127
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.671
    sort_std: 0.0
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.654
    std: 0.01
    paper_value: 0.654
    paper_std: 0.01
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 166
    true_value: 0.655
    true_std: 0.004
    value_gap_source_arxiv: '2604.24293'
    value_gap_source_title: 'Latent-Hysteresis Graph ODEs: Modeling Coupled Topology-Feature
      Evolution via Continuous Phase Transitions'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0010000000000000009
    value_note: global 0.6550 within std
    paper_rank: 168
    rank_delta: 2
    rank_delta_abs: 2
    rank_delta_direction: worse
    sort_value: 0.655
    sort_std: 0.004
    is_best: false
  - model: Plain
    model_key: plain
    model_plain: Plain
    value: 0.306
    std: 0.001
    paper_value: 0.306
    paper_std: 0.001
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 319
    true_value: 0.306
    true_std: 0.001
    value_gap_source_arxiv: '2508.10651'
    value_gap_source_title: Graph Learning via Logic-Based Weisfeiler--Leman Variants
      and Tabularization
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 319
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.306
    sort_std: 0.001
    is_best: false
  - model: Maj.
    model_key: maj.
    model_plain: Maj.
    value: 0.306
    std: 0.001
    paper_value: 0.306
    paper_std: 0.001
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 320
    true_value: 0.306
    true_std: 0.001
    value_gap_source_arxiv: '2508.10651'
    value_gap_source_title: Graph Learning via Logic-Based Weisfeiler--Leman Variants
      and Tabularization
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 320
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.306
    sort_std: 0.001
    is_best: false
  - model: Int.
    model_key: int.
    model_plain: Int.
    value: 0.306
    std: 0.001
    paper_value: 0.306
    paper_std: 0.001
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 321
    true_value: 0.306
    true_std: 0.001
    value_gap_source_arxiv: '2508.10651'
    value_gap_source_title: Graph Learning via Logic-Based Weisfeiler--Leman Variants
      and Tabularization
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 321
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.306
    sort_std: 0.001
    is_best: false
  metric: AP
  higher_is_better: true
- &id002
  dataset: ogbg-molhiv
  rows:
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.9685
    std: 0.0001
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.16767'
    title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed Graphs as
      Effectively as We Expected'
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.9685
    sort_std: 0.0001
    is_best: true
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.9682
    std: 0.0003
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.16767'
    title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed Graphs as
      Effectively as We Expected'
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.9682
    sort_std: 0.0003
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.737
    std: 0.017
    paper_value: 0.737
    paper_std: 0.017
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 3
    true_value: 0.9681
    true_std: 0.0003
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.23109999999999997
    value_note: ''
    paper_rank: 197
    rank_delta: 194
    rank_delta_abs: 194
    rank_delta_direction: worse
    sort_value: 0.9681
    sort_std: 0.0003
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.737
    std: 0.017
    paper_value: 0.737
    paper_std: 0.017
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 4
    true_value: 0.968
    true_std: 0.002
    value_gap_source_arxiv: '2502.02379'
    value_gap_source_title: 'No Metric to Rule Them All: Toward Principled Evaluations
      of Graph-Learning Datasets'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.23099999999999998
    value_note: ''
    paper_rank: 197
    rank_delta: 193
    rank_delta_abs: 193
    rank_delta_direction: worse
    sort_value: 0.968
    sort_std: 0.002
    is_best: true
  - model: SigGate-GT
    model_key: siggate-gt
    model_plain: SigGate-GT
    value: 0.8247
    std: 0.0063
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.17324'
    title: 'SigGate-GT: Taming Over-Smoothing in Graph Transformers via Sigmoid-Gated
      Attention'
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    codebase_url: https://github.com/bettyguo/SigGate-GT
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    sort_value: 0.8247
    sort_std: 0.0063
    is_best: false
  - model: Q-WL-RF (Ours) Full
    model_key: q-wl-rf (ours) full
    model_plain: Q-WL-RF (Ours) Full
    value: 0.789
    std: 0.004
    paper_value: 0.789
    paper_std: 0.004
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 71
    true_value: 0.789
    true_std: 0.004
    value_gap_source_arxiv: '2508.10651'
    value_gap_source_title: Graph Learning via Logic-Based Weisfeiler--Leman Variants
      and Tabularization
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 71
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.789
    sort_std: 0.004
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.768
    std: 0.008
    paper_value: 0.768
    paper_std: 0.008
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 76
    true_value: 0.788
    true_std: 0.01
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.020000000000000018
    value_note: ''
    paper_rank: 142
    rank_delta: 66
    rank_delta_abs: 66
    rank_delta_direction: worse
    sort_value: 0.788
    sort_std: 0.01
    is_best: false
  - model: Q-WL-RF (Ours) Hyb.
    model_key: q-wl-rf (ours) hyb.
    model_plain: Q-WL-RF (Ours) Hyb.
    value: 0.783
    std: 0.01
    paper_value: 0.783
    paper_std: 0.01
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 97
    true_value: 0.783
    true_std: 0.01
    value_gap_source_arxiv: '2508.10651'
    value_gap_source_title: Graph Learning via Logic-Based Weisfeiler--Leman Variants
      and Tabularization
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 97
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.783
    sort_std: 0.01
    is_best: false
  - model: Q-WL-RF (Ours) Plain
    model_key: q-wl-rf (ours) plain
    model_plain: Q-WL-RF (Ours) Plain
    value: 0.78
    std: 0.005
    paper_value: 0.78
    paper_std: 0.005
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 114
    true_value: 0.78
    true_std: 0.005
    value_gap_source_arxiv: '2508.10651'
    value_gap_source_title: Graph Learning via Logic-Based Weisfeiler--Leman Variants
      and Tabularization
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 114
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.78
    sort_std: 0.005
    is_best: false
  - model: Q-WL-RF (Ours) Maj.
    model_key: q-wl-rf (ours) maj.
    model_plain: Q-WL-RF (Ours) Maj.
    value: 0.756
    std: 0.013
    paper_value: 0.756
    paper_std: 0.013
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 171
    true_value: 0.756
    true_std: 0.013
    value_gap_source_arxiv: '2508.10651'
    value_gap_source_title: Graph Learning via Logic-Based Weisfeiler--Leman Variants
      and Tabularization
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 171
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.756
    sort_std: 0.013
    is_best: false
  - model: Q-WL-RF (Ours) Int.
    model_key: q-wl-rf (ours) int.
    model_plain: Q-WL-RF (Ours) Int.
    value: 0.753
    std: 0.01
    paper_value: 0.753
    paper_std: 0.01
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 177
    true_value: 0.753
    true_std: 0.01
    value_gap_source_arxiv: '2508.10651'
    value_gap_source_title: Graph Learning via Logic-Based Weisfeiler--Leman Variants
      and Tabularization
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 177
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.753
    sort_std: 0.01
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
results_grouped:
- benchmark: LRGB
  datasets:
  - *id001
- benchmark: OGB
  datasets:
  - *id002
- benchmark: MoleculeNet
  datasets:
  - *id003
main_figure: /figures/2508.10651/main_figure.png
---

