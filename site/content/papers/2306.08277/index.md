---
title: 'Frigate: Frugal Spatio-temporal Forecasting on Road Networks'
arxiv_id: '2306.08277'
source_url: ''
authors: []
published_date: Jun 2023
published_date_iso: 2023-06
abstract: Modelling spatio-temporal processes on road networks is a task of growing
  importance. While significant progress has been made on developing spatio-temporal
  graph neural networks (Gnns), existing works are built upon three assumptions that
  are not practical on real-world road networks. First, they assume sensing on every
  node of a road network. In reality, due to budget-constraints or sensor failures,
  all locations (nodes) may not be equipped with sensors. Second, they assume that
  sensing history is available at all installed sensors. This is unrealistic as well
  due to sensor failures, loss of packets during communication, etc. Finally, there
  is an assumption of static road networks. Connectivity within networks change due
  to road closures, constructions of new roads, etc. In this work, we develop Frigate
  to address all these shortcomings. Frigate is powered by a spatio-temporal Gnn that
  integrates positional, topological, and temporal information into rich inductive
  node representations. The joint fusion of this diverse information is made feasible
  through a novel combination of gated Lipschitz embeddings with Lstms. We prove that
  the proposed Gnn architecture is provably more expressive than message-passing Gnns
  used in state-of-the-art algorithms. The higher expressivity of Frigate naturally
  translates to superior empirical performance conducted on real-world network-constrained
  traffic data. In addition, Frigate is robust to frugal sensor deployment, changes
  in road network connectivity, and temporal irregularity in sensing.
codebase_url: https://github.com/idea-iitd/Frigate
extraction_model: Qwen/Qwen3.6-35B-A3B-FP8
has_results: true
paper_type: method
proposed_models:
- Frigate
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
  - model: KNN graph-convolution
    model_key: knn graph-convolution
    model_plain: KNN graph-convolution
    value: 0.58
    std: 0.02
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
    global_rank: 1
    sort_value: 0.58
    sort_std: 0.02
    is_best: true
  - model: MMGCN + ImageBind/ImageBind
    model_key: mmgcn + imagebind/imagebind
    model_plain: MMGCN + ImageBind/ImageBind
    value: 0.5875
    std: 0.0005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: true
    is_global_top: true
    global_rank: 2
    sort_value: 0.5875
    sort_std: 0.0005
    is_best: true
  - model: DGCNN(L8)
    model_key: dgcnn(l8)
    model_plain: DGCNN(L8)
    value: 0.6163
    std: 0.0533
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.08671'
    title: Search to Capture Long-range Dependency with Stacking GNNs for Graph Classification
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    codebase_url: https://github.com/LARS-research/LRGNN
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.6163
    sort_std: 0.0533
    is_best: true
  - model: Frigate
    model_key: frigate
    model_plain: Frigate
    value: 3.547
    std: 0.2
    paper_value: 3.547
    paper_std: 0.2
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: null
    sort_value: 3.547
    sort_std: 0.2
    is_best: false
  - model: LocaleGN
    model_key: localegn
    model_plain: LocaleGN
    value: 4.597
    std: 0.22
    paper_value: 4.597
    paper_std: 0.22
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: null
    sort_value: 4.597
    sort_std: 0.22
    is_best: false
  - model: STGODE
    model_key: stgode
    model_plain: STGODE
    value: 4.693
    std: 0.19
    paper_value: 4.693
    paper_std: 0.19
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: null
    sort_value: 4.693
    sort_std: 0.19
    is_best: false
  - model: DCRNN
    model_key: dcrnn
    model_plain: DCRNN
    value: 4.893
    std: 0.26
    paper_value: 4.893
    paper_std: 0.26
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: null
    sort_value: 4.893
    sort_std: 0.26
    is_best: false
  - model: GraphWavenet
    model_key: graphwavenet
    model_plain: GraphWavenet
    value: 5.308
    std: 0.3
    paper_value: 5.308
    paper_std: 0.3
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: null
    sort_value: 5.308
    sort_std: 0.3
    is_best: false
  - model: STNN
    model_key: stnn
    model_plain: STNN
    value: 5.633
    std: 0.18
    paper_value: 5.633
    paper_std: 0.18
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: null
    sort_value: 5.633
    sort_std: 0.18
    is_best: false
  - model: STGCN
    model_key: stgcn
    model_plain: STGCN
    value: 5.712
    std: 0.33
    paper_value: 5.712
    paper_std: 0.33
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: null
    sort_value: 5.712
    sort_std: 0.33
    is_best: false
  metric: Accuracy
  higher_is_better: false
results_grouped:
- benchmark: TU Dortmund
  datasets:
  - *id001
single_proposed_model: Frigate
main_figure: /figures/2306.08277/main_figure.png
---

