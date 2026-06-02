---
title: Improving Compositional Generalization using Iterated Learning and Simplicial
  Embeddings
arxiv_id: '2310.18777'
source_url: ''
authors: []
published_date: Oct 28, 2023
published_date_iso: '2023-10-28'
published_venue: ''
abstract: Compositional generalization, the ability of an agent to generalize to unseen
  combinations of latent factors, is easy for humans but hard for deep neural networks.
  A line of research in cognitive science has hypothesized a process, ``iterated learning,''
  to help explain how human language developed this ability; the theory rests on simultaneous
  pressures towards compressibility (when an ignorant agent learns from an informed
  one) and expressivity (when it uses the representation for downstream tasks). Inspired
  by this process, we propose to improve the compositional generalization of deep
  networks by using iterated learning on models with simplicial embeddings, which
  can approximately discretize representations. This approach is further motivated
  by an analysis of compositionality based on Kolmogorov complexity. We show that
  this combination of changes improves compositional generalization over other approaches,
  demonstrating these improvements both on vision tasks with well-understood latent
  factors and on real molecular graph prediction tasks where the latent structure
  is unknown.
codebase_url: ''
extraction_model: Qwen/Qwen3.6-35B-A3B-FP8
has_results: true
paper_type: method
proposed_models:
- GCN SEM-IL
mrr: 0.0269
adjusted_mrr: 0.0269
mrr_dataset_count: 3
benchmark_categories:
- OGB
task_categories:
- graph_classification
- graph_regression
experiment_scopes:
- graph-level
results:
- &id003
  dataset: PCQM4Mv2
  rows:
  - model: DeMol
    model_key: demol
    model_plain: DeMol
    value: 0.0603
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00568'
    title: Enhancing Molecular Property Predictions by Learning from Bond Modelling
      and Interactions
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.0603
    sort_std: null
    is_best: true
  - model: TGT-At
    model_key: tgt-at
    model_plain: TGT-At
    value: 0.0671
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00568'
    title: Enhancing Molecular Property Predictions by Learning from Bond Modelling
      and Interactions
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.0671
    sort_std: null
    is_best: false
  - model: Unimol+
    model_key: unimol+
    model_plain: Unimol+
    value: 0.0693
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00568'
    title: Enhancing Molecular Property Predictions by Learning from Bond Modelling
      and Interactions
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.0693
    sort_std: null
    is_best: false
  - model: GCN SEM-IL
    model_key: gcn sem-il
    model_plain: GCN SEM-IL
    value: 0.098
    std: 0.005
    paper_value: 0.098
    paper_std: 0.005
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 28, 2023
    date_display: Oct 2023
    date_iso: '2023-10-28'
    published_venue: null
    global_rank: 35
    true_value: 0.098
    true_std: 0.005
    value_gap_source_arxiv: '2310.18777'
    value_gap_source_title: Improving Compositional Generalization using Iterated
      Learning and Simplicial Embeddings
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.098
    sort_std: 0.005
    is_best: false
  - model: GCN SEM-only
    model_key: gcn sem-only
    model_plain: GCN SEM-only
    value: 0.106
    std: 0.004
    paper_value: 0.106
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 28, 2023
    date_display: Oct 2023
    date_iso: '2023-10-28'
    published_venue: null
    global_rank: 38
    true_value: 0.106
    true_std: 0.004
    value_gap_source_arxiv: '2310.18777'
    value_gap_source_title: Improving Compositional Generalization using Iterated
      Learning and Simplicial Embeddings
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.106
    sort_std: 0.004
    is_best: false
  - model: GCN Baseline
    model_key: gcn baseline
    model_plain: GCN Baseline
    value: 0.108
    std: 0.003
    paper_value: 0.108
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 28, 2023
    date_display: Oct 2023
    date_iso: '2023-10-28'
    published_venue: null
    global_rank: 39
    true_value: 0.108
    true_std: 0.003
    value_gap_source_arxiv: '2310.18777'
    value_gap_source_title: Improving Compositional Generalization using Iterated
      Learning and Simplicial Embeddings
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.108
    sort_std: 0.003
    is_best: false
  metric: MAE
  higher_is_better: false
- &id001
  dataset: ogbg-molhiv
  rows:
  - model: ML
    model_key: ml
    model_plain: ML
    value: 0.997
    std: 0.002
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.08443'
    title: 'CLEAR: Generative Counterfactual Explanations on Graphs'
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.997
    sort_std: 0.002
    is_best: true
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.862
    std: 0.002
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.862
    sort_std: 0.002
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.858
    std: 0.002
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.858
    sort_std: 0.002
    is_best: false
  - model: GCN SEM-IL
    model_key: gcn sem-il
    model_plain: GCN SEM-IL
    value: 0.7861
    std: 0.0073
    paper_value: 0.7861
    paper_std: 0.0073
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 28, 2023
    date_display: Oct 2023
    date_iso: '2023-10-28'
    published_venue: null
    global_rank: 57
    true_value: 0.7861
    true_std: 0.0073
    value_gap_source_arxiv: '2310.18777'
    value_gap_source_title: Improving Compositional Generalization using Iterated
      Learning and Simplicial Embeddings
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 57
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7861
    sort_std: 0.0073
    is_best: false
  - model: GCN SEM-only
    model_key: gcn sem-only
    model_plain: GCN SEM-only
    value: 0.7821
    std: 0.0078
    paper_value: 0.7821
    paper_std: 0.0078
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 28, 2023
    date_display: Oct 2023
    date_iso: '2023-10-28'
    published_venue: null
    global_rank: 67
    true_value: 0.7821
    true_std: 0.0078
    value_gap_source_arxiv: '2310.18777'
    value_gap_source_title: Improving Compositional Generalization using Iterated
      Learning and Simplicial Embeddings
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 67
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7821
    sort_std: 0.0078
    is_best: false
  - model: GCN Baseline
    model_key: gcn baseline
    model_plain: GCN Baseline
    value: 0.7701
    std: 0.0094
    paper_value: 0.7701
    paper_std: 0.0094
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 28, 2023
    date_display: Oct 2023
    date_iso: '2023-10-28'
    published_venue: null
    global_rank: 105
    true_value: 0.7701
    true_std: 0.0094
    value_gap_source_arxiv: '2310.18777'
    value_gap_source_title: Improving Compositional Generalization using Iterated
      Learning and Simplicial Embeddings
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 105
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7701
    sort_std: 0.0094
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id002
  dataset: ogbg-molpcba
  rows:
  - model: novel dynamic message-passing mechanism
    model_key: novel dynamic message-passing mechanism
    model_plain: novel dynamic message-passing mechanism
    value: 0.339
    std: 0.0073
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 31, 2024
    date_display: Oct 2024
    date_iso: '2024-10-31'
    codebase_url: https://github.com/sunjss/N2
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.339
    sort_std: 0.0073
    is_best: true
  - model: unified method + FLAG
    model_key: unified method + flag
    model_plain: unified method + FLAG
    value: 0.3174
    std: null
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.08806'
    title: Unified 2D and 3D Pre-Training of Molecular Representations
    date: Jul 2022
    date_display: Jul 2022
    date_iso: 2022-07
    codebase_url: https://github.com/teslacool/UnifiedMolPretrain
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.3174
    sort_std: null
    is_best: false
  - model: TGT-Ag+TGT-At-DP
    model_key: tgt-ag+tgt-at-dp
    model_plain: TGT-Ag+TGT-At-DP
    value: 0.3167
    std: 0.0031
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.04538'
    title: 'Triplet Interaction Improves Graph Transformers: Accurate Molecular Graph
      Learning with Triplet Graph Transformers'
    date: Feb 7, 2024
    date_display: Feb 2024
    date_iso: '2024-02-07'
    codebase_url: https://github.com/shamim-hussain/tgt
    uses_external_data: true
    is_global_top: true
    global_rank: 3
    sort_value: 0.3167
    sort_std: 0.0031
    is_best: false
  - model: GCN SEM-IL
    model_key: gcn sem-il
    model_plain: GCN SEM-IL
    value: 0.2802
    std: 0.0061
    paper_value: 0.2802
    paper_std: 0.0061
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 28, 2023
    date_display: Oct 2023
    date_iso: '2023-10-28'
    published_venue: null
    global_rank: 29
    true_value: 0.2802
    true_std: 0.0061
    value_gap_source_arxiv: '2310.18777'
    value_gap_source_title: Improving Compositional Generalization using Iterated
      Learning and Simplicial Embeddings
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2802
    sort_std: 0.0061
    is_best: false
  - model: GCN SEM-only
    model_key: gcn sem-only
    model_plain: GCN SEM-only
    value: 0.2566
    std: 0.0047
    paper_value: 0.2566
    paper_std: 0.0047
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 28, 2023
    date_display: Oct 2023
    date_iso: '2023-10-28'
    published_venue: null
    global_rank: 44
    true_value: 0.2566
    true_std: 0.0047
    value_gap_source_arxiv: '2310.18777'
    value_gap_source_title: Improving Compositional Generalization using Iterated
      Learning and Simplicial Embeddings
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 44
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2566
    sort_std: 0.0047
    is_best: false
  - model: GCN Baseline
    model_key: gcn baseline
    model_plain: GCN Baseline
    value: 0.2291
    std: 0.004
    paper_value: 0.2291
    paper_std: 0.004
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 28, 2023
    date_display: Oct 2023
    date_iso: '2023-10-28'
    published_venue: null
    global_rank: 55
    true_value: 0.2291
    true_std: 0.004
    value_gap_source_arxiv: '2310.18777'
    value_gap_source_title: Improving Compositional Generalization using Iterated
      Learning and Simplicial Embeddings
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 55
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2291
    sort_std: 0.004
    is_best: false
  metric: AP
  higher_is_better: true
results_grouped:
- benchmark: OGB
  datasets:
  - *id001
  - *id002
  - *id003
single_proposed_model: GCN SEM-IL
---

