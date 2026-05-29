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
  - model: DC-GSAT
    model_key: dc-gsat
    model_plain: DC-GSAT
    value: 1.0
    std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.02719'
    title: 'Beyond Topological Self-Explainable GNNs: A Formal Explainability Perspective'
    date: Feb 4, 2025
    date_display: Feb 2025
    date_iso: '2025-02-04'
    codebase_url: https://github.com/steveazzolin/beyond-topo-segnns
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 1.0
    sort_std: 0.0
    is_best: true
  - model: DC-SMGNN
    model_key: dc-smgnn
    model_plain: DC-SMGNN
    value: 1.0
    std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.02719'
    title: 'Beyond Topological Self-Explainable GNNs: A Formal Explainability Perspective'
    date: Feb 4, 2025
    date_display: Feb 2025
    date_iso: '2025-02-04'
    codebase_url: https://github.com/steveazzolin/beyond-topo-segnns
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 1.0
    sort_std: 0.0
    is_best: true
  - model: A graph neural network
    model_key: a graph neural network
    model_plain: A graph neural network
    value: 1.0
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.11118'
    title: 'Dorylus: Affordable, Scalable, and Accurate GNN Training with Distributed
      CPU Servers and Serverless Threads'
    date: May 2021
    date_display: May 2021
    date_iso: 2021-05
    codebase_url: https://github.com/uclasystem/dorylus
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 1.0
    sort_std: null
    is_best: true
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
    global_rank: 27
    true_value: 0.9
    true_std: null
    value_gap_source_arxiv: '2511.20406'
    value_gap_source_title: Short-Range Oversquashing
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 27
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9
    sort_std: null
    is_best: false
  metric: Accuracy
  higher_is_better: true
results_grouped:
- benchmark: TU Dortmund
  datasets:
  - *id001
main_figure: /figures/2511.20406/main_figure.png
---

