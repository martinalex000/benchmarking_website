---
title: Short-Range Oversquashing
arxiv_id: '2511.20406'
source_url: ''
authors: []
published_date: Nov 2025
published_date_iso: 2025-11
abstract: 'Message Passing Neural Networks (MPNNs) are widely used for learning on
  graphs, but their ability to process long-range information is limited by the phenomenon
  of oversquashing. This limitation has led some researchers to advocate Graph Transformers
  as a better alternative, whereas others suggest that it can be mitigated within
  the MPNN framework, using virtual nodes or other rewiring techniques. In this work,
  we demonstrate that oversquashing is not limited to long-range tasks, but can also
  arise in short-range problems. This observation allows us to disentangle two distinct
  mechanisms underlying oversquashing: (1) the bottleneck phenomenon, which can arise
  even in low-range settings, and (2) the vanishing gradient phenomenon, which is
  closely associated with long-range tasks. We further show that the short-range bottleneck
  effect is not captured by existing explanations for oversquashing, and that adding
  virtual nodes does not resolve it. In contrast, transformers do succeed in such
  tasks, positioning them as the more compelling solution to oversquashing, compared
  to specialized MPNNs..'
codebase_url: https://github.com/YakovM93/Short-Range-Oversquashing
extraction_model: Qwen/Qwen3.6-35B-A3B-FP8
has_results: true
paper_type: dataset
proposed_models: []
mrr: null
adjusted_mrr: null
mrr_dataset_count: 0
benchmark_categories:
- TU Dortmund
task_categories:
- graph_classification
experiment_scopes:
- graph-level
results:
- &id001
  dataset: D&D
  rows:
  - model: Transformer
    model_key: transformer
    model_plain: Transformer
    value: 1.0
    std: null
    paper_value: 1.0
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Figure 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: 1
    true_value: 1.0
    true_std: null
    value_gap_source_arxiv: '2511.20406'
    value_gap_source_title: Short-Range Oversquashing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.0
    sort_std: null
    is_best: true
  - model: VRN Ensemble
    model_key: vrn ensemble
    model_plain: VRN Ensemble
    value: 0.9554
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1703.06114'
    title: Deep Sets
    date: Mar 2017
    date_display: Mar 2017
    date_iso: 2017-03
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.9554
    sort_std: null
    is_best: false
  - model: MVCNN
    model_key: mvcnn
    model_plain: MVCNN
    value: 0.901
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1703.06114'
    title: Deep Sets
    date: Mar 2017
    date_display: Mar 2017
    date_iso: 2017-03
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.901
    sort_std: null
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.9
    std: null
    paper_value: 0.9
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Figure 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    global_rank: 4
    true_value: 0.9
    true_std: null
    value_gap_source_arxiv: '2511.20406'
    value_gap_source_title: Short-Range Oversquashing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9
    sort_std: null
    is_best: false
  - model: DeepSets + transformation
    model_key: deepsets + transformation
    model_plain: DeepSets + transformation
    value: 0.9
    std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1703.06114'
    title: Deep Sets
    date: Mar 2017
    date_display: Mar 2017
    date_iso: 2017-03
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    sort_value: 0.9
    sort_std: 0.003
    is_best: false
  metric: Accuracy
  higher_is_better: true
results_grouped:
- benchmark: TU Dortmund
  datasets:
  - *id001
main_figure: /figures/2511.20406/main_figure.png
---

