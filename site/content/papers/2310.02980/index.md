---
title: 'Never Train from Scratch: Fair Comparison of long-sequence models requires
  data-driven priors'
arxiv_id: '2310.02980'
source_url: ''
authors: []
published_date: Oct 2023
published_date_iso: 2023-10
abstract: Modeling long-range dependencies across sequences is a longstanding goal
  in machine learning and has led to architectures, such as state space models, that
  dramatically outperform Transformers on long sequences. However, these impressive
  empirical gains have been by and large demonstrated on benchmarks (e.g. Long Range
  Arena), where models are randomly initialized and trained to predict a target label
  from an input sequence. In this work, we show that random initialization leads to
  gross overestimation of the differences between architectures and that pretraining
  with standard denoising objectives, using only the downstream task data, leads to
  dramatic gains across multiple architectures and to very small gaps between Transformers
  and state space models (SSMs). In stark contrast to prior works, we find vanilla
  Transformers to match the performance of S4 on Long Range Arena when properly pretrained,
  and we improve the best reported results of SSMs on the PathX-256 task by 20 absolute
  points. Subsequently, we analyze the utility of previously-proposed structured parameterizations
  for SSMs and show they become mostly redundant in the presence of data-driven initialization
  obtained through pretraining. Our work shows that, when evaluating different architectures
  on supervised tasks, incorporation of data-driven priors via pretraining is essential
  for reliable performance estimation, and can be done efficiently.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- S4 + SPT
- Transformers + SPT
mrr: 0.0909
adjusted_mrr: 0.0303
mrr_dataset_count: 1
benchmark_categories:
- TU Dortmund
task_categories:
- graph_classification
experiment_scopes:
- graph-level
results:
- &id001
  dataset: D&D
  is_multi_metric: true
  rows:
  - model: MPNN
    model_key: mpnn
    model_plain: MPNN
    metric_values:
    - 0.989
    - null
    metric_stds:
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.15671'
    title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence Models'
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
    sort_value: 0.989
    sort_std: null
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: HAC (BFS)
    model_key: hac (bfs)
    model_plain: HAC (BFS)
    metric_values:
    - 0.981
    - null
    metric_stds:
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.15671'
    title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence Models'
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: false
    sort_value: 0.981
    sort_std: null
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: k-hop
    model_key: k-hop
    model_plain: k-hop
    metric_values:
    - 0.976
    - null
    metric_stds:
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.15671'
    title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence Models'
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
    sort_value: 0.976
    sort_std: null
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: S4 + SPT
    model_key: s4 + spt
    model_plain: S4 + SPT
    metric_values:
    - 0.9509
    - 0.999
    metric_stds:
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.9509
    sort_std: null
    true_value: 0.9509
    true_std: null
    paper_value: 0.9509
    paper_std: null
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2310.02980'
    value_gap_source_title: 'Never Train from Scratch: Fair Comparison of long-sequence
      models requires data-driven priors'
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 4
  - model: S4
    model_key: s4
    model_plain: S4
    metric_values:
    - 0.936
    - 0.999
    metric_stds:
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.936
    sort_std: null
    true_value: 0.936
    true_std: null
    paper_value: 0.936
    paper_std: null
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2310.02980'
    value_gap_source_title: 'Never Train from Scratch: Fair Comparison of long-sequence
      models requires data-driven priors'
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 5
  - model: Transformers + SPT
    model_key: transformers + spt
    model_plain: Transformers + SPT
    metric_values:
    - 0.8613
    - 0.992
    metric_stds:
    - null
    - null
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.8613
    sort_std: null
    true_value: 0.8613
    true_std: null
    paper_value: 0.8613
    paper_std: null
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2310.02980'
    value_gap_source_title: 'Never Train from Scratch: Fair Comparison of long-sequence
      models requires data-driven priors'
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 11
  - model: Transformer
    model_key: transformer
    model_plain: Transformer
    metric_values:
    - 0.8455
    - 0.998
    metric_stds:
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.8455
    sort_std: null
    true_value: 0.8455
    true_std: null
    paper_value: 0.8455
    paper_std: null
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2310.02980'
    value_gap_source_title: 'Never Train from Scratch: Fair Comparison of long-sequence
      models requires data-driven priors'
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 15
  metrics:
  - Accuracy
  - R2
  primary_metric: Accuracy
  higher_is_better: true
results_grouped:
- benchmark: TU Dortmund
  datasets:
  - *id001
main_figure: /figures/2310.02980/main_figure.png
---

