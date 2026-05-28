---
title: CosmoBench
arxiv_id: '2507.03707'
source_url: ''
authors: []
published_date: Jul 2025
published_date_iso: 2025-07
abstract: 'Cosmological simulations provide a wealth of data in the form of point
  clouds and directed trees. A crucial goal is to extract insights from this data
  that shed light on the nature and composition of the Universe. In this paper we
  introduce CosmoBench, a benchmark dataset curated from state-of-the-art cosmological
  simulations whose runs required more than 41 million core-hours and generated over
  two petabytes of data. CosmoBench is the largest dataset of its kind: it contains
  34 thousand point clouds from simulations of dark matter halos and galaxies at three
  different length scales, as well as 25 thousand directed trees that record the formation
  history of halos on two different time scales. The data in CosmoBench can be used
  for multiple tasks---to predict cosmological parameters from point clouds and merger
  trees, to predict the velocities of individual halos and galaxies from their collective
  positions, and to reconstruct merger trees on finer time scales from those on coarser
  time scales. We provide multiple baselines on these tasks, some based on established
  approaches from cosmological modeling and others rooted in machine learning. For
  the latter, we study different approaches---from simple linear models that are minimally
  constrained by symmetries to much larger and more computationally-demanding models
  in deep learning, such as graph neural networks. We find that least-squares fits
  with a handful of invariant features sometimes outperform deep architectures with
  many more parameters and far longer training times. Still there remains tremendous
  potential to improve these baselines by combining machine learning and cosmological
  modeling in a more principled way, one that fully exploits the structure in the
  data. CosmoBench sets the stage for bridging cosmology and geometric deep learning
  at scale. We invite the community to push the frontier of scientific discovery by
  engaging with this challenging, high-impact dataset. The data and code are available
  at https://cosmobench.streamlit.app/this URL.'
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- GNN
- CO-GNN
- GNN (M)
- GNN (v_max)
- GNN (a)
- GNN (M,c,v_max,a)
mrr: 0.0
adjusted_mrr: 0.0
mrr_dataset_count: 0
benchmark_categories:
- Heterophilic Graphs
- CosmoBench
task_categories:
- graph_classification
- graph_regression
- node_classification
experiment_scopes:
- graph-level
- node-level
results:
- &id004
  dataset: CAMELS-SAM
  rows:
  - model: 2PCF
    model_key: 2pcf
    model_plain: 2PCF
    value: 0.84
    std: 0.02
    paper_value: 0.84
    paper_std: 0.02
    metric: R^2
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.011
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 1
    true_value: 0.84
    true_std: 0.02
    value_gap_source_arxiv: '2507.03707'
    value_gap_source_title: CosmoBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.84
    sort_std: 0.02
    is_best: true
  - model: GNN (w/o edgeMP)
    model_key: gnn (w/o edgemp)
    model_plain: GNN (w/o edgeMP)
    value: 0.8
    std: 0.02
    paper_value: 0.8
    paper_std: 0.02
    metric: R^2
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.128
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 2
    true_value: 0.8
    true_std: 0.02
    value_gap_source_arxiv: '2507.03707'
    value_gap_source_title: CosmoBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8
    sort_std: 0.02
    is_best: true
  - model: LLS
    model_key: lls
    model_plain: LLS
    value: 0.78
    std: 0.03
    paper_value: 0.78
    paper_std: 0.03
    metric: R^2
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.049
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 3
    true_value: 0.78
    true_std: 0.03
    value_gap_source_arxiv: '2507.03707'
    value_gap_source_title: CosmoBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.78
    sort_std: 0.03
    is_best: false
  - model: GNN
    model_key: gnn
    model_plain: GNN
    value: 0.78
    std: 0.03
    paper_value: 0.78
    paper_std: 0.03
    metric: R^2
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 1.26
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 4
    true_value: 0.78
    true_std: 0.03
    value_gap_source_arxiv: '2507.03707'
    value_gap_source_title: CosmoBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.78
    sort_std: 0.03
    is_best: false
  - model: Linear theory oracle
    model_key: linear theory oracle
    model_plain: Linear theory oracle
    value: 0.297
    std: null
    paper_value: 0.297
    paper_std: null
    metric: R^2
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.001
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 5
    true_value: 0.297
    true_std: null
    value_gap_source_arxiv: '2507.03707'
    value_gap_source_title: CosmoBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.297
    sort_std: null
    is_best: false
  - model: LLS w/ modification
    model_key: lls w/ modification
    model_plain: LLS w/ modification
    value: 0.2185
    std: null
    paper_value: 0.2185
    paper_std: null
    metric: R^2
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 6
    true_value: 0.2185
    true_std: null
    value_gap_source_arxiv: '2507.03707'
    value_gap_source_title: CosmoBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2185
    sort_std: null
    is_best: false
  - model: Linear theory oracle w/ modification
    model_key: linear theory oracle w/ modification
    model_plain: Linear theory oracle w/ modification
    value: 0.0732
    std: null
    paper_value: 0.0732
    paper_std: null
    metric: R^2
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 7
    true_value: 0.0732
    true_std: null
    value_gap_source_arxiv: '2507.03707'
    value_gap_source_title: CosmoBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.0732
    sort_std: null
    is_best: false
  metric: R^2
  higher_is_better: true
- &id002
  dataset: CS-Trees
  rows:
  - model: GNN (M,c,v_max,a)
    model_key: gnn (m,c,v_max,a)
    model_plain: GNN (M,c,v_max,a)
    value: 0.996
    std: 0.001
    paper_value: 0.996
    paper_std: 0.001
    metric: R2
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 1
    true_value: 0.996
    true_std: 0.001
    value_gap_source_arxiv: '2507.03707'
    value_gap_source_title: CosmoBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.996
    sort_std: 0.001
    is_best: true
  - model: DeepSet (M,c,v_max,a)
    model_key: deepset (m,c,v_max,a)
    model_plain: DeepSet (M,c,v_max,a)
    value: 0.993
    std: 0.001
    paper_value: 0.993
    paper_std: 0.001
    metric: R2
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 2
    true_value: 0.993
    true_std: 0.001
    value_gap_source_arxiv: '2507.03707'
    value_gap_source_title: CosmoBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.993
    sort_std: 0.001
    is_best: false
  - model: CO-GNN
    model_key: co-gnn
    model_plain: CO-GNN
    value: 0.84
    std: 0.004
    paper_value: 0.84
    paper_std: 0.004
    metric: R2
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 3
    true_value: 0.84
    true_std: 0.004
    value_gap_source_arxiv: '2507.03707'
    value_gap_source_title: CosmoBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.84
    sort_std: 0.004
    is_best: false
  - model: GNN (v_max)
    model_key: gnn (v_max)
    model_plain: GNN (v_max)
    value: 0.69
    std: 0.008
    paper_value: 0.69
    paper_std: 0.008
    metric: R2
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 4
    true_value: 0.69
    true_std: 0.008
    value_gap_source_arxiv: '2507.03707'
    value_gap_source_title: CosmoBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.69
    sort_std: 0.008
    is_best: false
  - model: 1NN
    model_key: 1nn
    model_plain: 1NN
    value: 0.64
    std: 0.063
    paper_value: 0.64
    paper_std: 0.063
    metric: R2
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 5
    true_value: 0.64
    true_std: 0.063
    value_gap_source_arxiv: '2507.03707'
    value_gap_source_title: CosmoBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.64
    sort_std: 0.063
    is_best: false
  - model: DeepSet (v_max)
    model_key: deepset (v_max)
    model_plain: DeepSet (v_max)
    value: 0.57
    std: 0.01
    paper_value: 0.57
    paper_std: 0.01
    metric: R2
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 6
    true_value: 0.57
    true_std: 0.01
    value_gap_source_arxiv: '2507.03707'
    value_gap_source_title: CosmoBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.57
    sort_std: 0.01
    is_best: false
  - model: EPS
    model_key: eps
    model_plain: EPS
    value: 0.53
    std: 0.073
    paper_value: 0.53
    paper_std: 0.073
    metric: R2
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 7
    true_value: 0.53
    true_std: 0.073
    value_gap_source_arxiv: '2507.03707'
    value_gap_source_title: CosmoBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.53
    sort_std: 0.073
    is_best: false
  - model: GNN (a)
    model_key: gnn (a)
    model_plain: GNN (a)
    value: 0.33
    std: 0.011
    paper_value: 0.33
    paper_std: 0.011
    metric: R2
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 8
    true_value: 0.33
    true_std: 0.011
    value_gap_source_arxiv: '2507.03707'
    value_gap_source_title: CosmoBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.33
    sort_std: 0.011
    is_best: false
  - model: DeepSet (c)
    model_key: deepset (c)
    model_plain: DeepSet (c)
    value: 0.23
    std: 0.012
    paper_value: 0.23
    paper_std: 0.012
    metric: R2
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 9
    true_value: 0.23
    true_std: 0.012
    value_gap_source_arxiv: '2507.03707'
    value_gap_source_title: CosmoBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.23
    sort_std: 0.012
    is_best: false
  - model: GNN (M)
    model_key: gnn (m)
    model_plain: GNN (M)
    value: 0.16
    std: 0.01
    paper_value: 0.16
    paper_std: 0.01
    metric: R2
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 10
    true_value: 0.16
    true_std: 0.01
    value_gap_source_arxiv: '2507.03707'
    value_gap_source_title: CosmoBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.16
    sort_std: 0.01
    is_best: false
  - model: DeepSet (M)
    model_key: deepset (m)
    model_plain: DeepSet (M)
    value: 0.12
    std: 0.009
    paper_value: 0.12
    paper_std: 0.009
    metric: R2
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 11
    true_value: 0.12
    true_std: 0.009
    value_gap_source_arxiv: '2507.03707'
    value_gap_source_title: CosmoBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.12
    sort_std: 0.009
    is_best: false
  metric: R2
  higher_is_better: true
- &id003
  dataset: CS-Trees-200
  rows:
  - model: GNN (a)
    model_key: gnn (a)
    model_plain: GNN (a)
    value: 0.7
    std: 0.005
    paper_value: 0.7
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 1
    true_value: 0.7
    true_std: 0.005
    value_gap_source_arxiv: '2507.03707'
    value_gap_source_title: CosmoBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7
    sort_std: 0.005
    is_best: true
  - model: GNN (M,c,v_max,a)
    model_key: gnn (m,c,v_max,a)
    model_plain: GNN (M,c,v_max,a)
    value: 0.69
    std: 0.005
    paper_value: 0.69
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 2
    true_value: 0.69
    true_std: 0.005
    value_gap_source_arxiv: '2507.03707'
    value_gap_source_title: CosmoBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.69
    sort_std: 0.005
    is_best: true
  - model: GNN (M)
    model_key: gnn (m)
    model_plain: GNN (M)
    value: 0.63
    std: 0.004
    paper_value: 0.63
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 3
    true_value: 0.63
    true_std: 0.004
    value_gap_source_arxiv: '2507.03707'
    value_gap_source_title: CosmoBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.63
    sort_std: 0.004
    is_best: false
  - model: DeepSet (M,c,v_max,a)
    model_key: deepset (m,c,v_max,a)
    model_plain: DeepSet (M,c,v_max,a)
    value: 0.62
    std: 0.006
    paper_value: 0.62
    paper_std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 4
    true_value: 0.62
    true_std: 0.006
    value_gap_source_arxiv: '2507.03707'
    value_gap_source_title: CosmoBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.62
    sort_std: 0.006
    is_best: false
  - model: CO-GNN
    model_key: co-gnn
    model_plain: CO-GNN
    value: 0.61
    std: 0.005
    paper_value: 0.61
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 6
    true_value: 0.61
    true_std: 0.005
    value_gap_source_arxiv: '2507.03707'
    value_gap_source_title: CosmoBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.61
    sort_std: 0.005
    is_best: false
  - model: DeepSet (M)
    model_key: deepset (m)
    model_plain: DeepSet (M)
    value: 0.61
    std: 0.005
    paper_value: 0.61
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 5
    true_value: 0.61
    true_std: 0.005
    value_gap_source_arxiv: '2507.03707'
    value_gap_source_title: CosmoBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.61
    sort_std: 0.005
    is_best: false
  - model: GNN (v_max)
    model_key: gnn (v_max)
    model_plain: GNN (v_max)
    value: 0.61
    std: 0.005
    paper_value: 0.61
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 7
    true_value: 0.61
    true_std: 0.005
    value_gap_source_arxiv: '2507.03707'
    value_gap_source_title: CosmoBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.61
    sort_std: 0.005
    is_best: false
  - model: DeepSet (v_max)
    model_key: deepset (v_max)
    model_plain: DeepSet (v_max)
    value: 0.59
    std: 0.005
    paper_value: 0.59
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 8
    true_value: 0.59
    true_std: 0.005
    value_gap_source_arxiv: '2507.03707'
    value_gap_source_title: CosmoBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.59
    sort_std: 0.005
    is_best: false
  - model: EPS
    model_key: eps
    model_plain: EPS
    value: 0.53
    std: 0.073
    paper_value: 0.53
    paper_std: 0.073
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 9
    true_value: 0.53
    true_std: 0.073
    value_gap_source_arxiv: '2507.03707'
    value_gap_source_title: CosmoBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.53
    sort_std: 0.073
    is_best: false
  - model: DeepSet (c)
    model_key: deepset (c)
    model_plain: DeepSet (c)
    value: 0.53
    std: 0.005
    paper_value: 0.53
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 10
    true_value: 0.53
    true_std: 0.005
    value_gap_source_arxiv: '2507.03707'
    value_gap_source_title: CosmoBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.53
    sort_std: 0.005
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id001
  dataset: Chameleon
  rows:
  - model: 2PCF
    model_key: 2pcf
    model_plain: 2PCF
    value: 0.84
    std: 0.02
    paper_value: 0.84
    paper_std: 0.02
    metric: R^2
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.011
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: null
    sort_value: 0.84
    sort_std: 0.02
    is_best: true
  - model: GraphMAE
    model_key: graphmae
    model_plain: GraphMAE
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
    date_display: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.8051
    sort_std: 0.0125
    is_best: false
  - model: MRS-Dir-GCN_DA
    model_key: mrs-dir-gcn_da
    model_plain: MRS-Dir-GCN_DA
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
    date_display: Sep 2024
    date_iso: 2024-09
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.8017
    sort_std: 0.0188
    is_best: true
  - model: Supervised
    model_key: supervised
    model_plain: Supervised
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
    date_display: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.8002
    sort_std: 0.0087
    is_best: false
  - model: GNN (w/o edgeMP)
    model_key: gnn (w/o edgemp)
    model_plain: GNN (w/o edgeMP)
    value: 0.8
    std: 0.02
    paper_value: 0.8
    paper_std: 0.02
    metric: R^2
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.128
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: null
    sort_value: 0.8
    sort_std: 0.02
    is_best: true
  - model: LLS
    model_key: lls
    model_plain: LLS
    value: 0.78
    std: 0.03
    paper_value: 0.78
    paper_std: 0.03
    metric: R^2
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.049
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: null
    sort_value: 0.78
    sort_std: 0.03
    is_best: false
  - model: GNN
    model_key: gnn
    model_plain: GNN
    value: 0.78
    std: 0.03
    paper_value: 0.78
    paper_std: 0.03
    metric: R^2
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 1.26
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: null
    sort_value: 0.78
    sort_std: 0.03
    is_best: false
  - model: Linear theory oracle
    model_key: linear theory oracle
    model_plain: Linear theory oracle
    value: 0.297
    std: null
    paper_value: 0.297
    paper_std: null
    metric: R^2
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.001
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: null
    sort_value: 0.297
    sort_std: null
    is_best: false
  - model: LLS w/ modification
    model_key: lls w/ modification
    model_plain: LLS w/ modification
    value: 0.2185
    std: null
    paper_value: 0.2185
    paper_std: null
    metric: R^2
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: null
    sort_value: 0.2185
    sort_std: null
    is_best: false
  - model: Linear theory oracle w/ modification
    model_key: linear theory oracle w/ modification
    model_plain: Linear theory oracle w/ modification
    value: 0.0732
    std: null
    paper_value: 0.0732
    paper_std: null
    metric: R^2
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: null
    sort_value: 0.0732
    sort_std: null
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id005
  dataset: Quijote
  rows:
  - model: 2PCF
    model_key: 2pcf
    model_plain: 2PCF
    value: 0.85
    std: 0.004
    paper_value: 0.85
    paper_std: 0.004
    metric: R^2
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.011
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 1
    true_value: 0.85
    true_std: 0.004
    value_gap_source_arxiv: '2507.03707'
    value_gap_source_title: CosmoBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.85
    sort_std: 0.004
    is_best: true
  - model: LLS
    model_key: lls
    model_plain: LLS
    value: 0.83
    std: 0.004
    paper_value: 0.83
    paper_std: 0.004
    metric: R^2
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.049
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 2
    true_value: 0.83
    true_std: 0.004
    value_gap_source_arxiv: '2507.03707'
    value_gap_source_title: CosmoBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.83
    sort_std: 0.004
    is_best: false
  - model: GNN
    model_key: gnn
    model_plain: GNN
    value: 0.8
    std: 0.004
    paper_value: 0.8
    paper_std: 0.004
    metric: R^2
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 1.26
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 3
    true_value: 0.8
    true_std: 0.004
    value_gap_source_arxiv: '2507.03707'
    value_gap_source_title: CosmoBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8
    sort_std: 0.004
    is_best: false
  - model: GNN (w/o edgeMP)
    model_key: gnn (w/o edgemp)
    model_plain: GNN (w/o edgeMP)
    value: 0.8
    std: 0.004
    paper_value: 0.8
    paper_std: 0.004
    metric: R^2
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.128
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 4
    true_value: 0.8
    true_std: 0.004
    value_gap_source_arxiv: '2507.03707'
    value_gap_source_title: CosmoBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8
    sort_std: 0.004
    is_best: false
  - model: LLS (1<=P<=4)
    model_key: lls (1<=p<=4)
    model_plain: LLS (1<=P<=4)
    value: 0.435
    std: null
    paper_value: 0.435
    paper_std: null
    metric: R^2
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 7
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 5
    true_value: 0.435
    true_std: null
    value_gap_source_arxiv: '2507.03707'
    value_gap_source_title: CosmoBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.435
    sort_std: null
    is_best: false
  - model: Linear theory oracle
    model_key: linear theory oracle
    model_plain: Linear theory oracle
    value: 0.3769
    std: null
    paper_value: 0.3769
    paper_std: null
    metric: R^2
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.001
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 6
    true_value: 0.3769
    true_std: null
    value_gap_source_arxiv: '2507.03707'
    value_gap_source_title: CosmoBench
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3769
    sort_std: null
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

