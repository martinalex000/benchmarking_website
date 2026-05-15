---
title: Symmetry-preserving graph attention network to solve routing problems at multiple
  resolutions
arxiv_id: '2310.15543'
authors: []
published_date: Oct 2023
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
proposed_models:
- Ours
- mGAT (s.)
- mGAT
mrr: 0.0
results:
- &id001
  dataset: TSP
  rows:
  - model: mGAT (s.)
    value: 0.0025
    std: null
    metric: Gap
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: true
  - model: mGAT
    value: 0.0025
    std: null
    metric: Gap
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: null
    is_best: true
  - model: POMO
    value: 0.007
    std: null
    metric: Gap
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: Ours
    value: 0.0123
    std: null
    metric: Gap
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: Sym-NCO
    value: 0.019
    std: null
    metric: Gap
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  metric: F1
  higher_is_better: false
results_grouped:
- benchmark: GNNBenchmark
  datasets:
  - *id001
main_figure: /figures/2310.15543/main_figure.png
---

