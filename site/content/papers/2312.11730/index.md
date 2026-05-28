---
title: Stronger Graph Transformer with Regularized Attention Scores
arxiv_id: '2312.11730'
source_url: ''
authors: []
published_date: Dec 2023
published_date_iso: 2023-12
abstract: 1cmGraph Neural Networks are notorious for its memory consumption. A recent
  Transformer-based GNN called Graph Transformer is shown to obtain superior performances
  when long range dependencies exist. However, combining graph data and Transformer
  architecture led to a combinationally worse memory issue. We propose a novel version
  of "edge regularization technique" that alleviates the need for Positional Encoding
  and ultimately alleviate GT's out of memory issue. We observe that it is not clear
  whether having an edge regularization on top of positional encoding is helpful.
  However, it seems evident that applying our edge regularization technique indeed
  stably improves GT's performance compared to GT without Positional Encoding.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- GraphGPS (w/ Positional Encoding, 0.01 CE)
- GraphGPS (w/ Positional Encoding, w/out backprop cut-off 0.01 CE)
- 0.01 L1
- 0.05 L1
- 0.01 CE
- No-PE 0.1 L1
mrr: 0.0079
adjusted_mrr: 0.0026
mrr_dataset_count: 1
benchmark_categories:
- LRGB
task_categories:
- graph_classification
- graph_regression
experiment_scopes:
- graph-level
results:
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
  - model: 0.01 L1
    model_key: 0.01 l1
    model_plain: 0.01 L1
    value: 0.6477
    std: null
    paper_value: 0.6477
    paper_std: null
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: 'Figure: Regularization on Peptides-Func'
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 188
    true_value: 0.6477
    true_std: null
    value_gap_source_arxiv: '2312.11730'
    value_gap_source_title: Stronger Graph Transformer with Regularized Attention
      Scores
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 188
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6477
    sort_std: null
    is_best: false
  - model: 0.05 L1
    model_key: 0.05 l1
    model_plain: 0.05 L1
    value: 0.6468
    std: 0.002
    paper_value: 0.6468
    paper_std: 0.002
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: 'Figure: Regularization on Peptides-Func'
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 190
    true_value: 0.6468
    true_std: 0.002
    value_gap_source_arxiv: '2312.11730'
    value_gap_source_title: Stronger Graph Transformer with Regularized Attention
      Scores
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 190
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6468
    sort_std: 0.002
    is_best: false
  - model: Baseline
    model_key: baseline
    model_plain: Baseline
    value: 0.6435
    std: null
    paper_value: 0.6435
    paper_std: null
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: 'Figure: Regularization on Peptides-Func'
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 204
    true_value: 0.6435
    true_std: null
    value_gap_source_arxiv: '2312.11730'
    value_gap_source_title: Stronger Graph Transformer with Regularized Attention
      Scores
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 204
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6435
    sort_std: null
    is_best: false
  - model: 0.01 CE
    model_key: 0.01 ce
    model_plain: 0.01 CE
    value: 0.6423
    std: null
    paper_value: 0.6423
    paper_std: null
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: 'Figure: Regularization on Peptides-Func'
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 207
    true_value: 0.6423
    true_std: null
    value_gap_source_arxiv: '2312.11730'
    value_gap_source_title: Stronger Graph Transformer with Regularized Attention
      Scores
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 207
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6423
    sort_std: null
    is_best: false
  - model: No-PE 0.1 L1
    model_key: no-pe 0.1 l1
    model_plain: No-PE 0.1 L1
    value: 0.6096
    std: 0.00185
    paper_value: 0.6096
    paper_std: 0.00185
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: 'Figure: Regularization on Peptides-Func'
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 238
    true_value: 0.6096
    true_std: 0.00185
    value_gap_source_arxiv: '2312.11730'
    value_gap_source_title: Stronger Graph Transformer with Regularized Attention
      Scores
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 238
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6096
    sort_std: 0.00185
    is_best: false
  - model: No-PE Baseline
    model_key: no-pe baseline
    model_plain: No-PE Baseline
    value: 0.5866
    std: 0.0184
    paper_value: 0.5866
    paper_std: 0.0184
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: 'Figure: Regularization on Peptides-Func'
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 273
    true_value: 0.5866
    true_std: 0.0184
    value_gap_source_arxiv: '2312.11730'
    value_gap_source_title: Stronger Graph Transformer with Regularized Attention
      Scores
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 273
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5866
    sort_std: 0.0184
    is_best: false
  metric: AP
  higher_is_better: true
- &id002
  dataset: Peptides-struct
  rows:
  - model: ESA
    model_key: esa
    model_plain: ESA
    value: 0.2393
    std: 0.0004
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.10793'
    title: An end-to-end attention-based approach for learning on graphs
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.2393
    sort_std: 0.0004
    is_best: true
  - model: GRPE-FFGT
    model_key: grpe-ffgt
    model_plain: GRPE-FFGT
    value: 0.2416
    std: 0.0026
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.04653'
    title: Hybrid Focal and Full-Range Attention Based Graph Transformers
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.2416
    sort_std: 0.0026
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.2421
    std: 0.0016
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09263'
    title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks? Simple Architectures
      Meet Excellence
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.2421
    sort_std: 0.0016
    is_best: false
  - model: GraphGPS (w/ Positional Encoding, 0.01 CE)
    model_key: graphgps (w/ positional encoding, 0.01 ce)
    model_plain: GraphGPS (w/ Positional Encoding, 0.01 CE)
    value: 0.2491
    std: 0.0024
    paper_value: 0.2491
    paper_std: 0.0024
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Figure 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 127
    true_value: 0.2491
    true_std: 0.0024
    value_gap_source_arxiv: '2312.11730'
    value_gap_source_title: Stronger Graph Transformer with Regularized Attention
      Scores
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 127
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2491
    sort_std: 0.0024
    is_best: false
  - model: GraphGPS (w/ Positional Encoding, No Reg)
    model_key: graphgps (w/ positional encoding, no reg)
    model_plain: GraphGPS (w/ Positional Encoding, No Reg)
    value: 0.2499
    std: 0.0003
    paper_value: 0.2499
    paper_std: 0.0003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Figure 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 134
    true_value: 0.2499
    true_std: 0.0003
    value_gap_source_arxiv: '2312.11730'
    value_gap_source_title: Stronger Graph Transformer with Regularized Attention
      Scores
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 134
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2499
    sort_std: 0.0003
    is_best: false
  - model: GraphGPS (w/ Positional Encoding, w/out backprop cut-off 0.01 CE)
    model_key: graphgps (w/ positional encoding, w/out backprop cut-off 0.01 ce)
    model_plain: GraphGPS (w/ Positional Encoding, w/out backprop cut-off 0.01 CE)
    value: 0.25
    std: null
    paper_value: 0.25
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Figure 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 141
    true_value: 0.25
    true_std: null
    value_gap_source_arxiv: '2312.11730'
    value_gap_source_title: Stronger Graph Transformer with Regularized Attention
      Scores
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 141
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.25
    sort_std: null
    is_best: false
  - model: Baseline (w/out Positional Encoding)
    model_key: baseline (w/out positional encoding)
    model_plain: Baseline (w/out Positional Encoding)
    value: 0.257
    std: 0.0015
    paper_value: 0.257
    paper_std: 0.0015
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Figure 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 207
    true_value: 0.257
    true_std: 0.0015
    value_gap_source_arxiv: '2312.11730'
    value_gap_source_title: Stronger Graph Transformer with Regularized Attention
      Scores
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 207
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.257
    sort_std: 0.0015
    is_best: false
  metric: MAE
  higher_is_better: false
results_grouped:
- benchmark: LRGB
  datasets:
  - *id001
  - *id002
main_figure: /figures/2312.11730/main_figure.png
---

