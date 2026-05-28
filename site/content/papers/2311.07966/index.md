---
title: Higher-Order Expander Graph Propagation
arxiv_id: '2311.07966'
source_url: ''
authors: []
published_date: Nov 2023
published_date_iso: 2023-11
abstract: Graph neural networks operate on graph-structured data via exchanging messages
  along edges. One limitation of this message passing paradigm is the over-squashing
  problem. Over-squashing occurs when messages from a node's expanded receptive field
  are compressed into fixed-size vectors, potentially causing information loss. To
  address this issue, recent works have explored using expander graphs, which are
  highly-connected sparse graphs with low diameters, to perform message passing. However,
  current methods on expander graph propagation only consider pair-wise interactions,
  ignoring higher-order structures in complex data. To explore the benefits of capturing
  these higher-order correlations while still leveraging expander graphs, we introduce
  higher-order expander graph propagation. We propose two methods for constructing
  bipartite expanders and evaluate their performance on both synthetic and real-world
  datasets.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- GIN + 3-Regular Bipartite Expander + Learned Features
mrr: 0.0455
adjusted_mrr: 0.0152
mrr_dataset_count: 1
benchmark_categories:
- OGB
task_categories:
- graph_classification
experiment_scopes:
- graph-level
results:
- &id002
  dataset: Code
  rows:
  - model: CodeT5-small + GFSA
    model_key: codet5-small + gfsa
    model_plain: CodeT5-small + GFSA
    value: 0.9494
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.04234'
    title: Graph Convolutions Enrich the Self-Attention in Transformers!
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 1
    sort_value: 0.9494
    sort_std: null
    is_best: true
  - model: CodeT5-base + GFSA
    model_key: codet5-base + gfsa
    model_plain: CodeT5-base + GFSA
    value: 0.9492
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.04234'
    title: Graph Convolutions Enrich the Self-Attention in Transformers!
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 2
    sort_value: 0.9492
    sort_std: null
    is_best: false
  - model: CodeT5-small
    model_key: codet5-small
    model_plain: CodeT5-small
    value: 0.9436
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.04234'
    title: Graph Convolutions Enrich the Self-Attention in Transformers!
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 3
    sort_value: 0.9436
    sort_std: null
    is_best: false
  - model: GIN + 3-Regular Bipartite Expander + Learned Features
    model_key: gin + 3-regular bipartite expander + learned features
    model_plain: GIN + 3-Regular Bipartite Expander + Learned Features
    value: 0.1519
    std: 0.002
    paper_value: 0.1519
    paper_std: 0.002
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 22
    true_value: 0.1519
    true_std: 0.002
    value_gap_source_arxiv: '2311.07966'
    value_gap_source_title: Higher-Order Expander Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1519
    sort_std: 0.002
    is_best: false
  - model: EGP
    model_key: egp
    model_plain: EGP
    value: 0.1497
    std: 0.0015
    paper_value: 0.1497
    paper_std: 0.0015
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Deac et al. 2022
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 23
    true_value: 0.1497
    true_std: 0.0015
    value_gap_source_arxiv: '2311.07966'
    value_gap_source_title: Higher-Order Expander Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1497
    sort_std: 0.0015
    is_best: false
  - model: Plain GIN
    model_key: plain gin
    model_plain: Plain GIN
    value: 0.1495
    std: 0.0023
    paper_value: 0.1495
    paper_std: 0.0023
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hu et al. 2020
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 24
    true_value: 0.1495
    true_std: 0.0023
    value_gap_source_arxiv: '2311.07966'
    value_gap_source_title: Higher-Order Expander Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1495
    sort_std: 0.0023
    is_best: false
  - model: GIN + 3-Regular Bipartite Expander + Summation
    model_key: gin + 3-regular bipartite expander + summation
    model_plain: GIN + 3-Regular Bipartite Expander + Summation
    value: 0.1254
    std: 0.0029
    paper_value: 0.1254
    paper_std: 0.0029
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 25
    true_value: 0.1254
    true_std: 0.0029
    value_gap_source_arxiv: '2311.07966'
    value_gap_source_title: Higher-Order Expander Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1254
    sort_std: 0.0029
    is_best: false
  metric: F1
  higher_is_better: true
- &id001
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
    value: 0.9681
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
    global_rank: 3
    sort_value: 0.9681
    sort_std: 0.0003
    is_best: false
  - model: EGP
    model_key: egp
    model_plain: EGP
    value: 0.7934
    std: 0.0035
    paper_value: 0.7934
    paper_std: 0.0035
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Deac et al. 2022
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 56
    true_value: 0.7934
    true_std: 0.0035
    value_gap_source_arxiv: '2311.07966'
    value_gap_source_title: Higher-Order Expander Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 56
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7934
    sort_std: 0.0035
    is_best: false
  - model: k=3 Ramanujan Expander
    model_key: k=3 ramanujan expander
    model_plain: k=3 Ramanujan Expander
    value: 0.7848
    std: 0.0135
    paper_value: 0.7848
    paper_std: 0.0135
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 90
    true_value: 0.7848
    true_std: 0.0135
    value_gap_source_arxiv: '2311.07966'
    value_gap_source_title: Higher-Order Expander Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 90
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7848
    sort_std: 0.0135
    is_best: false
  - model: GIN + PM_at (Summation-MLP)
    model_key: gin + pm_at (summation-mlp)
    model_plain: GIN + PM_at (Summation-MLP)
    value: 0.7614
    std: 0.0056
    paper_value: 0.7614
    paper_std: 0.0056
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 160
    true_value: 0.7614
    true_std: 0.0056
    value_gap_source_arxiv: '2311.07966'
    value_gap_source_title: Higher-Order Expander Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 160
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7614
    sort_std: 0.0056
    is_best: false
  - model: Plain GIN
    model_key: plain gin
    model_plain: Plain GIN
    value: 0.7558
    std: 0.014
    paper_value: 0.7558
    paper_std: 0.014
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Hu et al. 2020
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 173
    true_value: 0.7558
    true_std: 0.014
    value_gap_source_arxiv: '2311.07966'
    value_gap_source_title: Higher-Order Expander Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 173
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7558
    sort_std: 0.014
    is_best: false
  - model: GIN + PM (Summation)
    model_key: gin + pm (summation)
    model_plain: GIN + PM (Summation)
    value: 0.7538
    std: 0.015
    paper_value: 0.7538
    paper_std: 0.015
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 175
    true_value: 0.7538
    true_std: 0.015
    value_gap_source_arxiv: '2311.07966'
    value_gap_source_title: Higher-Order Expander Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 175
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7538
    sort_std: 0.015
    is_best: false
  - model: GIN + PM_sp (Summation-MLP)
    model_key: gin + pm_sp (summation-mlp)
    model_plain: GIN + PM_sp (Summation-MLP)
    value: 0.7524
    std: 0.0206
    paper_value: 0.7524
    paper_std: 0.0206
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 180
    true_value: 0.7524
    true_std: 0.0206
    value_gap_source_arxiv: '2311.07966'
    value_gap_source_title: Higher-Order Expander Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 180
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7524
    sort_std: 0.0206
    is_best: false
  - model: GIN + RM (Learn-Features)
    model_key: gin + rm (learn-features)
    model_plain: GIN + RM (Learn-Features)
    value: 0.7511
    std: 0.0133
    paper_value: 0.7511
    paper_std: 0.0133
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 184
    true_value: 0.7511
    true_std: 0.0133
    value_gap_source_arxiv: '2311.07966'
    value_gap_source_title: Higher-Order Expander Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 184
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7511
    sort_std: 0.0133
    is_best: false
  - model: GIN + PM (Learnt)
    model_key: gin + pm (learnt)
    model_plain: GIN + PM (Learnt)
    value: 0.7503
    std: 0.0201
    paper_value: 0.7503
    paper_std: 0.0201
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 186
    true_value: 0.7503
    true_std: 0.0201
    value_gap_source_arxiv: '2311.07966'
    value_gap_source_title: Higher-Order Expander Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 186
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7503
    sort_std: 0.0201
    is_best: false
  - model: GIN + RM (Masking)
    model_key: gin + rm (masking)
    model_plain: GIN + RM (Masking)
    value: 0.7439
    std: 0.0219
    paper_value: 0.7439
    paper_std: 0.0219
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    global_rank: 190
    true_value: 0.7439
    true_std: 0.0219
    value_gap_source_arxiv: '2311.07966'
    value_gap_source_title: Higher-Order Expander Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 190
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7439
    sort_std: 0.0219
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
results_grouped:
- benchmark: OGB
  datasets:
  - *id001
  - *id002
single_proposed_model: GIN + 3-Regular Bipartite Expander + Learned Features
main_figure: /figures/2311.07966/main_figure.png
---

