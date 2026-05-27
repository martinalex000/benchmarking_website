---
title: CosmoBench
arxiv_id: '2507.03707'
authors: []
published_date: Jul 2025
abstract: 'Cosmological simulations provide a wealth of data in the form of point clouds and directed
  trees. A crucial goal is to extract insights from this data that shed light on the nature and composition
  of the Universe. In this paper we introduce CosmoBench, a benchmark dataset curated from state-of-the-art
  cosmological simulations whose runs required more than 41 million core-hours and generated over two
  petabytes of data. CosmoBench is the largest dataset of its kind: it contains 34 thousand point clouds
  from simulations of dark matter halos and galaxies at three different length scales, as well as 25 thousand
  directed trees that record the formation history of halos on two different time scales. The data in
  CosmoBench can be used for multiple tasks---to predict cosmological parameters from point clouds and
  merger trees, to predict the velocities of individual halos and galaxies from their collective positions,
  and to reconstruct merger trees on finer time scales from those on coarser time scales. We provide multiple
  baselines on these tasks, some based on established approaches from cosmological modeling and others
  rooted in machine learning. For the latter, we study different approaches---from simple linear models
  that are minimally constrained by symmetries to much larger and more computationally-demanding models
  in deep learning, such as graph neural networks. We find that least-squares fits with a handful of invariant
  features sometimes outperform deep architectures with many more parameters and far longer training times.
  Still there remains tremendous potential to improve these baselines by combining machine learning and
  cosmological modeling in a more principled way, one that fully exploits the structure in the data. CosmoBench
  sets the stage for bridging cosmology and geometric deep learning at scale. We invite the community
  to push the frontier of scientific discovery by engaging with this challenging, high-impact dataset.
  The data and code are available at https://cosmobench.streamlit.app/this URL.'
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
proposed_models:
- GNN
- CO-GNN
- GNN (M)
- GNN (v_max)
- GNN (a)
- GNN (M,c,v_max,a)
mrr: 0.0
results:
- &id004
  dataset: CAMELS-SAM
  rows:
  - model: 2PCF
    value: 0.84
    std: 0.02
    metric: R^2
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.011
    table_ref: Table 1
    source_ref: this paper
    global_rank: 1
    is_best: true
  - model: GNN (w/o edgeMP)
    value: 0.8
    std: 0.02
    metric: R^2
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.128
    table_ref: Table 1
    source_ref: this paper
    global_rank: 2
    is_best: true
  - model: LLS
    value: 0.78
    std: 0.03
    metric: R^2
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.049
    table_ref: Table 1
    source_ref: this paper
    global_rank: 3
    is_best: false
  - model: GNN
    value: 0.78
    std: 0.03
    metric: R^2
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 1.26
    table_ref: Table 1
    source_ref: this paper
    global_rank: 4
    is_best: false
  - model: Linear theory oracle
    value: 0.297
    std: null
    metric: R^2
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.001
    table_ref: Table 2
    source_ref: this paper
    global_rank: 5
    is_best: false
  - model: LLS w/ modification
    value: 0.2185
    std: null
    metric: R^2
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    global_rank: 6
    is_best: false
  - model: Linear theory oracle w/ modification
    value: 0.0732
    std: null
    metric: R^2
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    global_rank: 7
    is_best: false
  metric: R^2
  higher_is_better: true
- &id002
  dataset: CS-Trees
  rows:
  - model: GNN (M,c,v_max,a)
    value: 0.996
    std: 0.001
    metric: R2
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 1
    is_best: true
  - model: DeepSet (M,c,v_max,a)
    value: 0.993
    std: 0.001
    metric: R2
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 2
    is_best: false
  - model: CO-GNN
    value: 0.84
    std: 0.004
    metric: R2
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 3
    is_best: false
  - model: GNN (v_max)
    value: 0.69
    std: 0.008
    metric: R2
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 4
    is_best: false
  - model: 1NN
    value: 0.64
    std: 0.063
    metric: R2
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 5
    is_best: false
  - model: DeepSet (v_max)
    value: 0.57
    std: 0.01
    metric: R2
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 6
    is_best: false
  - model: EPS
    value: 0.53
    std: 0.073
    metric: R2
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 7
    is_best: false
  - model: GNN (a)
    value: 0.33
    std: 0.011
    metric: R2
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 8
    is_best: false
  - model: DeepSet (c)
    value: 0.23
    std: 0.012
    metric: R2
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 9
    is_best: false
  - model: GNN (M)
    value: 0.16
    std: 0.01
    metric: R2
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 10
    is_best: false
  - model: DeepSet (M)
    value: 0.12
    std: 0.009
    metric: R2
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 11
    is_best: false
  metric: R2
  higher_is_better: true
- &id003
  dataset: CS-Trees-200
  rows:
  - model: GNN (a)
    value: 0.7
    std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 1
    is_best: true
  - model: GNN (M,c,v_max,a)
    value: 0.69
    std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 2
    is_best: true
  - model: GNN (M)
    value: 0.63
    std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 3
    is_best: false
  - model: DeepSet (M,c,v_max,a)
    value: 0.62
    std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 4
    is_best: false
  - model: CO-GNN
    value: 0.61
    std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 6
    is_best: false
  - model: DeepSet (M)
    value: 0.61
    std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 5
    is_best: false
  - model: GNN (v_max)
    value: 0.61
    std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 7
    is_best: false
  - model: DeepSet (v_max)
    value: 0.59
    std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 8
    is_best: false
  - model: EPS
    value: 0.53
    std: 0.073
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 9
    is_best: false
  - model: DeepSet (c)
    value: 0.53
    std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 10
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id001
  dataset: Chameleon
  rows:
  - model: 2PCF
    value: 0.84
    std: 0.02
    metric: R^2
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.011
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: true
  - model: GraphMAE
    value: 0.8051
    std: 0.0125
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23345'
    title: Graph Positional Autoencoders as Self-supervised Learners
    date: May 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: false
  - model: MRS-Dir-GCN_DA
    value: 0.8017
    std: 0.0188
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.11504'
    title: Preventing Representational Rank Collapse in MPNNs by Splitting the Computational
      Graph
    date: Sep 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: true
  - model: Supervised
    value: 0.8002
    std: 0.0087
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23345'
    title: Graph Positional Autoencoders as Self-supervised Learners
    date: May 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: GNN (w/o edgeMP)
    value: 0.8
    std: 0.02
    metric: R^2
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.128
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: true
  - model: LLS
    value: 0.78
    std: 0.03
    metric: R^2
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.049
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: GNN
    value: 0.78
    std: 0.03
    metric: R^2
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 1.26
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: Linear theory oracle
    value: 0.297
    std: null
    metric: R^2
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.001
    table_ref: Table 2
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: LLS w/ modification
    value: 0.2185
    std: null
    metric: R^2
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: Linear theory oracle w/ modification
    value: 0.0732
    std: null
    metric: R^2
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    global_rank: null
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id005
  dataset: Quijote
  rows:
  - model: 2PCF
    value: 0.85
    std: 0.004
    metric: R^2
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.011
    table_ref: Table 1
    source_ref: this paper
    global_rank: 1
    is_best: true
  - model: LLS
    value: 0.83
    std: 0.004
    metric: R^2
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.049
    table_ref: Table 1
    source_ref: this paper
    global_rank: 2
    is_best: false
  - model: GNN
    value: 0.8
    std: 0.004
    metric: R^2
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 1.26
    table_ref: Table 1
    source_ref: this paper
    global_rank: 3
    is_best: false
  - model: GNN (w/o edgeMP)
    value: 0.8
    std: 0.004
    metric: R^2
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.128
    table_ref: Table 1
    source_ref: this paper
    global_rank: 4
    is_best: false
  - model: LLS (1<=P<=4)
    value: 0.435
    std: null
    metric: R^2
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 7
    source_ref: this paper
    global_rank: 5
    is_best: false
  - model: Linear theory oracle
    value: 0.3769
    std: null
    metric: R^2
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.001
    table_ref: Table 2
    source_ref: this paper
    global_rank: 6
    is_best: false
  metric: R^2
  higher_is_better: true
results_grouped:
- benchmark: Heterophilic Graphs
  datasets:
  - *id001
- benchmark: CosmoBench
  datasets:
  - *id002
  - *id003
  - *id004
  - *id005
main_figure: /figures/2507.03707/main_figure.png
---

