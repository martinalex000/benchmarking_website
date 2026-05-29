---
title: 'Weisfeiler and Leman Go Loopy: A New Hierarchy for Graph Representational
  Learning'
arxiv_id: '2403.13749'
source_url: ''
authors: []
published_date: Mar 2024
published_date_iso: 2024-03
abstract: We introduce $r$-loopy Weisfeiler-Leman ($r$-$ $WL), a novel hierarchy of
  graph isomorphism tests and a corresponding GNN framework, $r$-$ $MPNN, that can
  count cycles up to length $r+2$. Most notably, we show that $r$-$ $WL can count
  homomorphisms of cactus graphs. This extends 1-WL, which can only count homomorphisms
  of trees and, in fact, we prove that $r$-$ $WL is incomparable to $k$-WL for any
  fixed $k$. We empirically validate the expressive and counting power of $r$-$ $MPNN
  on several synthetic datasets and demonstrate the scalability and strong performance
  on various real-world datasets, particularly on sparse graphs. Our code is available.
codebase_url: https://github.com/RPaolino/loopy
extraction_model: Qwen/Qwen3.6-35B-A3B-FP8
has_results: true
paper_type: dataset
proposed_models: []
mrr: null
adjusted_mrr: null
mrr_dataset_count: 0
benchmark_categories:
- Quantum Chemistry
task_categories:
- graph_regression
experiment_scopes:
- graph-level
results:
- &id001
  dataset: QM9
  rows:
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.025
    std: 0.001
    metric: MAE
    higher_is_better: false
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
    global_rank: 1
    sort_value: 0.025
    sort_std: 0.001
    is_best: true
  - model: SphereNet
    model_key: spherenet
    model_plain: SphereNet
    value: 0.026
    std: 0.001
    metric: MAE
    higher_is_better: false
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
    global_rank: 2
    sort_value: 0.026
    sort_std: 0.001
    is_best: true
  - model: PaiNN
    model_key: painn
    model_plain: PaiNN
    value: 0.028
    std: 0.001
    metric: MAE
    higher_is_better: false
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
    sort_value: 0.028
    sort_std: 0.001
    is_best: false
  - model: Maron et al. (2019)
    model_key: maron et al. (2019)
    model_plain: Maron et al. (2019)
    value: 0.231
    std: null
    paper_value: 0.231
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 2024
    date_display: Mar 2024
    date_iso: 2024-03
    global_rank: 15
    true_value: 0.231
    true_std: null
    value_gap_source_arxiv: '2403.13749'
    value_gap_source_title: 'Weisfeiler and Leman Go Loopy: A New Hierarchy for Graph
      Representational Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.231
    sort_std: null
    is_best: false
  - model: Wu et al. (2018)
    model_key: wu et al. (2018)
    model_plain: Wu et al. (2018)
    value: 0.244
    std: null
    paper_value: 0.244
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 2024
    date_display: Mar 2024
    date_iso: 2024-03
    global_rank: 16
    true_value: 0.244
    true_std: null
    value_gap_source_arxiv: '2403.13749'
    value_gap_source_title: 'Weisfeiler and Leman Go Loopy: A New Hierarchy for Graph
      Representational Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.244
    sort_std: null
    is_best: false
  - model: Zhou et al. (2023)
    model_key: zhou et al. (2023)
    model_plain: Zhou et al. (2023)
    value: 0.346
    std: null
    paper_value: 0.346
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 2024
    date_display: Mar 2024
    date_iso: 2024-03
    global_rank: 17
    true_value: 0.346
    true_std: null
    value_gap_source_arxiv: '2403.13749'
    value_gap_source_title: 'Weisfeiler and Leman Go Loopy: A New Hierarchy for Graph
      Representational Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.346
    sort_std: null
    is_best: false
  - model: 5-ℓGIN
    model_key: 5-ℓgin
    model_plain: 5-ℓGIN
    value: 0.35
    std: 0.011
    paper_value: 0.35
    paper_std: 0.011
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 2024
    date_display: Mar 2024
    date_iso: 2024-03
    global_rank: 18
    true_value: 0.35
    true_std: 0.011
    value_gap_source_arxiv: '2403.13749'
    value_gap_source_title: 'Weisfeiler and Leman Go Loopy: A New Hierarchy for Graph
      Representational Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.35
    sort_std: 0.011
    is_best: false
  - model: Chen et al. (2020)
    model_key: chen et al. (2020)
    model_plain: Chen et al. (2020)
    value: 0.364
    std: null
    paper_value: 0.364
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 2024
    date_display: Mar 2024
    date_iso: 2024-03
    global_rank: 20
    true_value: 0.364
    true_std: null
    value_gap_source_arxiv: '2403.13749'
    value_gap_source_title: 'Weisfeiler and Leman Go Loopy: A New Hierarchy for Graph
      Representational Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.364
    sort_std: null
    is_best: false
  - model: Zhang et al. (2021)
    model_key: zhang et al. (2021)
    model_plain: Zhang et al. (2021)
    value: 0.428
    std: null
    paper_value: 0.428
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 2024
    date_display: Mar 2024
    date_iso: 2024-03
    global_rank: 21
    true_value: 0.428
    true_std: null
    value_gap_source_arxiv: '2403.13749'
    value_gap_source_title: 'Weisfeiler and Leman Go Loopy: A New Hierarchy for Graph
      Representational Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.428
    sort_std: null
    is_best: false
  - model: Morris et al. (2019)
    model_key: morris et al. (2019)
    model_plain: Morris et al. (2019)
    value: 0.476
    std: null
    paper_value: 0.476
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 2024
    date_display: Mar 2024
    date_iso: 2024-03
    global_rank: 25
    true_value: 0.476
    true_std: null
    value_gap_source_arxiv: '2403.13749'
    value_gap_source_title: 'Weisfeiler and Leman Go Loopy: A New Hierarchy for Graph
      Representational Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.476
    sort_std: null
    is_best: false
  - model: 1-GNN
    model_key: 1-gnn
    model_plain: 1-GNN
    value: 0.493
    std: null
    paper_value: 0.493
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 2024
    date_display: Mar 2024
    date_iso: 2024-03
    global_rank: 26
    true_value: 0.493
    true_std: null
    value_gap_source_arxiv: '2110.13197'
    value_gap_source_title: Nested Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.493
    sort_std: null
    is_best: false
  metric: MAE
  higher_is_better: false
results_grouped:
- benchmark: Quantum Chemistry
  datasets:
  - *id001
main_figure: /figures/2403.13749/main_figure.png
---

