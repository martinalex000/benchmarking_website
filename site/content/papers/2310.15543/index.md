---
title: Symmetry-preserving graph attention network to solve routing problems at multiple
  resolutions
arxiv_id: '2310.15543'
source_url: ''
authors: []
published_date: Oct 2023
published_date_iso: 2023-10
abstract: Travelling Salesperson Problems (TSPs) and Vehicle Routing Problems (VRPs)
  have achieved reasonable improvement in accuracy and computation time with the adaptation
  of Machine Learning (ML) methods. However, none of the previous works completely
  respects the symmetries arising from TSPs and VRPs including rotation, translation,
  permutation, and scaling. In this work, we introduce the first-ever completely equivariant
  model and training to solve combinatorial problems. Furthermore, it is essential
  to capture the multiscale structure (i.e. from local to global information) of the
  input graph, especially for the cases of large and long-range graphs, while previous
  methods are limited to extracting only local information that can lead to a local
  or sub-optimal solution. To tackle the above limitation, we propose a multiresolution
  scheme in combination with Equivariant Graph Attention network (mEGAT) architecture,
  which can learn the optimal route based on low-level and high-level graph resolutions
  in an efficient way. In particular, our approach constructs a hierarchy of coarse-graining
  graphs from the input graph, in which we try to solve the routing problems on simple
  low-level graphs first, then utilize that knowledge for the more complex high-level
  graphs. Experimentally, we have shown that our model outperforms existing baselines
  and proved that symmetry preservation and multiresolution are important recipes
  for solving combinatorial problems in a data-driven manner. Our source code is publicly
  available at https://github.com/HySonLab/Multires-NP-hard.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- Ours
- mGAT (s.)
- mGAT
mrr: 0.0
adjusted_mrr: 0.0
mrr_dataset_count: 0
benchmark_categories:
- GNNBenchmark
task_categories:
- link_prediction
experiment_scopes:
- edge-level
results:
- &id001
  dataset: TSP
  rows:
  - model: mGAT (s.)
    model_key: mgat (s.)
    model_plain: mGAT (s.)
    value: 0.0025
    std: null
    paper_value: 0.0025
    paper_std: null
    metric: Gap
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: null
    sort_value: 0.0025
    sort_std: null
    is_best: true
  - model: mGAT
    model_key: mgat
    model_plain: mGAT
    value: 0.0025
    std: null
    paper_value: 0.0025
    paper_std: null
    metric: Gap
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: null
    sort_value: 0.0025
    sort_std: null
    is_best: true
  - model: POMO
    model_key: pomo
    model_plain: POMO
    value: 0.007
    std: null
    paper_value: 0.007
    paper_std: null
    metric: Gap
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: null
    sort_value: 0.007
    sort_std: null
    is_best: false
  - model: Ours
    model_key: ours
    model_plain: Ours
    value: 0.0123
    std: null
    paper_value: 0.0123
    paper_std: null
    metric: Gap
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: null
    sort_value: 0.0123
    sort_std: null
    is_best: false
  - model: Sym-NCO
    model_key: sym-nco
    model_plain: Sym-NCO
    value: 0.019
    std: null
    paper_value: 0.019
    paper_std: null
    metric: Gap
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: null
    sort_value: 0.019
    sort_std: null
    is_best: false
  metric: F1
  higher_is_better: false
results_grouped:
- benchmark: GNNBenchmark
  datasets:
  - *id001
main_figure: /figures/2310.15543/main_figure.png
---

