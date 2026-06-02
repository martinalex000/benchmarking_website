---
title: 'ReorderBench: A Benchmark for Matrix Reordering'
arxiv_id: '2408.12169'
source_url: ''
authors: []
published_date: Aug 22, 2024
published_date_iso: '2024-08-22'
published_venue: ''
abstract: 'Matrix reordering permutes the rows and columns of a matrix to reveal meaningful
  visual patterns, such as blocks that represent clusters. A comprehensive collection
  of matrices, along with a scoring method for measuring the quality of visual patterns
  in these matrices, contributes to building a benchmark. This benchmark is essential
  for selecting or designing suitable reordering algorithms for. In this paper, we
  build a benchmark, ReorderBench, with the goal of evaluating and improving techniques.
  This is achieved by generating a large set of representative and diverse matrices
  and scoring these matrices with a convolution- and entropy-based method. Our benchmark
  contains 2,835,000 binary matrices and 5,670,000 continuous matrices, each one of
  four visual patterns: block, off-diagonal block, star, or band,. We demonstrate
  the usefulness of ReorderBench through three main applications in matrix reordering:
  1) evaluating different reordering algorithms, 2) creating a unified scoring model
  to measure the visual patterns in any matrix, and 3) developing a deep learning
  model for matrix reordering.'
codebase_url: ''
extraction_model: Qwen/Qwen3.6-35B-A3B-FP8
has_results: true
paper_type: method
proposed_models:
- Deep model
mrr: 0.0
adjusted_mrr: 0.0
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
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.20406'
    title: Short-Range Oversquashing
    date: Nov 25, 2025
    date_display: Nov 2025
    date_iso: '2025-11-25'
    codebase_url: https://github.com/YakovM93/Short-Range-Oversquashing
    uses_external_data: false
    is_global_top: true
    global_rank: 1
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
  - model: Deep model
    model_key: deep model
    model_plain: Deep model
    value: 0.925
    std: null
    paper_value: 0.925
    paper_std: null
    metric: MAE
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Aug 22, 2024
    date_display: Aug 2024
    date_iso: '2024-08-22'
    published_venue: null
    global_rank: null
    sort_value: 0.925
    sort_std: null
    is_best: false
  - model: SPIN
    model_key: spin
    model_plain: SPIN
    value: 0.895
    std: null
    paper_value: 0.895
    paper_std: null
    metric: MAE
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: Tsafrir 2005
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Aug 22, 2024
    date_display: Aug 2024
    date_iso: '2024-08-22'
    published_venue: null
    global_rank: null
    sort_value: 0.895
    sort_std: null
    is_best: false
  - model: OLO_ward
    model_key: olo_ward
    model_plain: OLO_ward
    value: 0.892
    std: null
    paper_value: 0.892
    paper_std: null
    metric: MAE
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: Bar 2001
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Aug 22, 2024
    date_display: Aug 2024
    date_iso: '2024-08-22'
    published_venue: null
    global_rank: null
    sort_value: 0.892
    sort_std: null
    is_best: false
  - model: GW_ward
    model_key: gw_ward
    model_plain: GW_ward
    value: 0.886
    std: null
    paper_value: 0.886
    paper_std: null
    metric: MAE
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: Gruvaeus 1972
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Aug 22, 2024
    date_display: Aug 2024
    date_iso: '2024-08-22'
    published_venue: null
    global_rank: null
    sort_value: 0.886
    sort_std: null
    is_best: false
  - model: BEA_TSP
    model_key: bea_tsp
    model_plain: BEA_TSP
    value: 0.852
    std: null
    paper_value: 0.852
    paper_std: null
    metric: MAE
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: Lenstra 1975
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Aug 22, 2024
    date_display: Aug 2024
    date_iso: '2024-08-22'
    published_venue: null
    global_rank: null
    sort_value: 0.852
    sort_std: null
    is_best: false
  - model: R2E
    model_key: r2e
    model_plain: R2E
    value: 0.83
    std: null
    paper_value: 0.83
    paper_std: null
    metric: MAE
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: Chen 2002
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Aug 22, 2024
    date_display: Aug 2024
    date_iso: '2024-08-22'
    published_venue: null
    global_rank: null
    sort_value: 0.83
    sort_std: null
    is_best: false
  - model: MDS
    model_key: mds
    model_plain: MDS
    value: 0.763
    std: null
    paper_value: 0.763
    paper_std: null
    metric: MAE
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: Kruskal 1964
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Aug 22, 2024
    date_display: Aug 2024
    date_iso: '2024-08-22'
    published_venue: null
    global_rank: null
    sort_value: 0.763
    sort_std: null
    is_best: false
  - model: PCA
    model_key: pca
    model_plain: PCA
    value: 0.763
    std: null
    paper_value: 0.763
    paper_std: null
    metric: MAE
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: Abdi 2010
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Aug 22, 2024
    date_display: Aug 2024
    date_iso: '2024-08-22'
    published_venue: null
    global_rank: null
    sort_value: 0.763
    sort_std: null
    is_best: false
  - model: Spectral_norm
    model_key: spectral_norm
    model_plain: Spectral_norm
    value: 0.726
    std: null
    paper_value: 0.726
    paper_std: null
    metric: MAE
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: Ding 2004
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Aug 22, 2024
    date_display: Aug 2024
    date_iso: '2024-08-22'
    published_venue: null
    global_rank: null
    sort_value: 0.726
    sort_std: null
    is_best: false
  - model: Moment
    model_key: moment
    model_plain: Moment
    value: 0.557
    std: null
    paper_value: 0.557
    paper_std: null
    metric: MAE
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: Deutsch 1971
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Aug 22, 2024
    date_display: Aug 2024
    date_iso: '2024-08-22'
    published_venue: null
    global_rank: null
    sort_value: 0.557
    sort_std: null
    is_best: false
  - model: Barycenter
    model_key: barycenter
    model_plain: Barycenter
    value: 0.46
    std: null
    paper_value: 0.46
    paper_std: null
    metric: MAE
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: Eades 1994
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Aug 22, 2024
    date_display: Aug 2024
    date_iso: '2024-08-22'
    published_venue: null
    global_rank: null
    sort_value: 0.46
    sort_std: null
    is_best: false
  metric: Accuracy
  higher_is_better: true
results_grouped:
- benchmark: TU Dortmund
  datasets:
  - *id001
single_proposed_model: Deep model
---

