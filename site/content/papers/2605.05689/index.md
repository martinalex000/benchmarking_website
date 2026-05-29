---
title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive Consistency Model'
arxiv_id: '2605.05689'
source_url: ''
authors: []
published_date: May 2026
published_date_iso: 2026-05
abstract: 'Conditional generative models, particularly diffusion-based methods, have
  recently been applied to graph prediction by modeling the target as a conditional
  distribution given the input graph, yielding competitive results compared to deterministic
  predictor. However, existing diffusion-based prediction methods typically require
  expensive iterative denoising at inference and often suffer from unstable sampling,
  which motivates recent efforts to reduce inference denoising steps and enable stable
  sampling via techniques such as consistency training. Despite this progress, we
  find that existing consistency training methods for graph prediction could potentially
  fall into a shortcut solution: the model may attempt to satisfy the self-consistency
  constraint by ignoring the noisy target (i.e., assigning it negligible weight),
  ultimately collapsing into a purely deterministic predictor. To mitigate such shortcut
  solution, we propose GCCM, a graph contrastive consistency model that goes beyond
  isolated pairwise matching between the same target at different noise levels by
  introducing negative pairs into a contrastive consistency objective. This adds an
  additional separation requirement, making the shortcut solution no longer trivially
  sufficient to satisfy the proposed objective. Moreover, we apply feature perturbation
  to the input node/edge features to break identical conditioning on the input graph,
  so that the shortcut no longer yields the same predictions across noise levels and
  becomes less attractive. Extensive experiments on benchmark datasets demonstrate
  that GCCM mitigates the shortcut solution and yields consistent performance improvements
  in graph prediction compared to deterministic predictors.'
codebase_url: ''
extraction_model: Qwen/Qwen3.6-35B-A3B-FP8
has_results: true
paper_type: method
proposed_models:
- GPS-GCCM
mrr: 0.0556
adjusted_mrr: 0.0185
mrr_dataset_count: 1
benchmark_categories:
- GNNBenchmark
task_categories:
- graph_classification
experiment_scopes:
- graph-level
results:
- &id001
  dataset: MNIST
  rows:
  - model: Classical CNN
    model_key: classical cnn
    model_plain: Classical CNN
    value: 0.9933
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1606.09375'
    title: Convolutional Neural Networks on Graphs with Fast Localized Spectral Filtering
    date: Jun 2016
    date_display: Jun 2016
    date_iso: 2016-06
    codebase_url: https://github.com/mdeff/cnn_graph
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.9933
    sort_std: null
    is_best: true
  - model: LeNet5
    model_key: lenet5
    model_plain: LeNet5
    value: 0.9933
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1705.07664'
    title: 'CayleyNets: Graph Convolutional Neural Networks with Complex Rational
      Spectral Filters'
    date: May 2017
    date_display: May 2017
    date_iso: 2017-05
    codebase_url: https://github.com/fmonti/mgcnn
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.9933
    sort_std: null
    is_best: true
  - model: CayleyNets
    model_key: cayleynets
    model_plain: CayleyNets
    value: 0.9918
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1705.07664'
    title: 'CayleyNets: Graph Convolutional Neural Networks with Complex Rational
      Spectral Filters'
    date: May 2017
    date_display: May 2017
    date_iso: 2017-05
    codebase_url: https://github.com/fmonti/mgcnn
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.9918
    sort_std: null
    is_best: false
  - model: GPS-GCCM
    model_key: gps-gccm
    model_plain: GPS-GCCM
    value: 0.98236
    std: 0.0006
    paper_value: 0.98236
    paper_std: 0.0006
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 18
    true_value: 0.98236
    true_std: 0.0006
    value_gap_source_arxiv: '2605.05689'
    value_gap_source_title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive
      Consistency Model'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.98236
    sort_std: 0.0006
    is_best: false
  - model: EGT
    model_key: egt
    model_plain: EGT
    value: 0.98173
    std: 0.00087
    paper_value: 0.98173
    paper_std: 0.00087
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hussain 2022
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 25
    true_value: 0.98173
    true_std: 0.00087
    value_gap_source_arxiv: '2205.12454'
    value_gap_source_title: Recipe for a General, Powerful, Scalable Graph Transformer
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.98173
    sort_std: 0.00087
    is_best: false
  - model: GPS-PCL
    model_key: gps-pcl
    model_plain: GPS-PCL
    value: 0.98114
    std: 0.00183
    paper_value: 0.98114
    paper_std: 0.00183
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Li 2025
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 30
    true_value: 0.98114
    true_std: 0.00183
    value_gap_source_arxiv: '2605.05689'
    value_gap_source_title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive
      Consistency Model'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 30
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.98114
    sort_std: 0.00183
    is_best: false
  - model: GRIT
    model_key: grit
    model_plain: GRIT
    value: 0.98108
    std: 0.00111
    paper_value: 0.98108
    paper_std: 0.00111
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: GRIT 2023
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 32
    true_value: 0.98108
    true_std: 0.00111
    value_gap_source_arxiv: '2502.00282'
    value_gap_source_title: 'GraphMinNet: Learning Dependencies in Graphs with Light
      Complexity Minimal Architecture'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.98108
    sort_std: 0.00111
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.9794
    std: 0.0012
    paper_value: 0.9794
    paper_std: 0.0012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Corso 2020
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 34
    true_value: 0.981
    true_std: 0.002
    value_gap_source_arxiv: '1806.09231'
    value_gap_source_title: 'Clebsch--Gordan Nets: a Fully Fourier Space Spherical
      Convolutional Neural Network'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0015999999999999348
    value_note: global 0.9810 within std
    paper_rank: 38
    rank_delta: 4
    rank_delta_abs: 4
    rank_delta_direction: worse
    sort_value: 0.981
    sort_std: 0.002
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.98082
    std: 0.00114
    paper_value: 0.98082
    paper_std: 0.00114
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Rampásek 2023
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 35
    true_value: 0.98082
    true_std: 0.00114
    value_gap_source_arxiv: '2605.05689'
    value_gap_source_title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive
      Consistency Model'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.98082
    sort_std: 0.00114
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.96485
    std: 0.00252
    paper_value: 0.96485
    paper_std: 0.00252
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xu 2019
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 40
    true_value: 0.979
    true_std: 0.003
    value_gap_source_arxiv: '1806.09231'
    value_gap_source_title: 'Clebsch--Gordan Nets: a Fully Fourier Space Spherical
      Convolutional Neural Network'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.014149999999999996
    value_note: ''
    paper_rank: 50
    rank_delta: 10
    rank_delta_abs: 10
    rank_delta_direction: worse
    sort_value: 0.979
    sort_std: 0.003
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.90705
    std: 0.00218
    paper_value: 0.90705
    paper_std: 0.00218
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kipf 2017
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 41
    true_value: 0.978
    true_std: 0.003
    value_gap_source_arxiv: '1806.09231'
    value_gap_source_title: 'Clebsch--Gordan Nets: a Fully Fourier Space Spherical
      Convolutional Neural Network'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07094999999999996
    value_note: ''
    paper_rank: 56
    rank_delta: 15
    rank_delta_abs: 15
    rank_delta_direction: worse
    sort_value: 0.978
    sort_std: 0.003
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.9734
    std: 0.00143
    paper_value: 0.9734
    paper_std: 0.00143
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Bresson 2018
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 47
    true_value: 0.9734
    true_std: 0.00143
    value_gap_source_arxiv: '2205.12454'
    value_gap_source_title: Recipe for a General, Powerful, Scalable Graph Transformer
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 47
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9734
    sort_std: 0.00143
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.95535
    std: 0.00205
    paper_value: 0.95535
    paper_std: 0.00205
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Veličković 2018
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 48
    true_value: 0.972
    true_std: 0.005
    value_gap_source_arxiv: '1806.09231'
    value_gap_source_title: 'Clebsch--Gordan Nets: a Fully Fourier Space Spherical
      Convolutional Neural Network'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.016649999999999943
    value_note: ''
    paper_rank: 52
    rank_delta: 4
    rank_delta_abs: 4
    rank_delta_direction: worse
    sort_value: 0.972
    sort_std: 0.005
    is_best: false
  - model: GPS-LGD
    model_key: gps-lgd
    model_plain: GPS-LGD
    value: 0.95461
    std: 0.00613
    paper_value: 0.95461
    paper_std: 0.00613
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou 2024
    variant_inference_reason: 'dataset: exact match'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    global_rank: 53
    true_value: 0.95461
    true_std: 0.00613
    value_gap_source_arxiv: '2605.05689'
    value_gap_source_title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive
      Consistency Model'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 53
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.95461
    sort_std: 0.00613
    is_best: false
  metric: Accuracy
  higher_is_better: true
results_grouped:
- benchmark: GNNBenchmark
  datasets:
  - *id001
single_proposed_model: GPS-GCCM
main_figure: /figures/2605.05689/main_figure.png
---

