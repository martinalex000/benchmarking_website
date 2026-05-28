---
title: Graph-level Representation Learning with Joint-Embedding Predictive Architectures
arxiv_id: '2309.16014'
source_url: ''
authors: []
published_date: Sep 2023
published_date_iso: 2023-09
abstract: Joint-Embedding Predictive Architectures (JEPAs) have recently emerged as
  a novel and powerful technique for self-supervised representation learning. They
  aim to learn an energy-based model by predicting the latent representation of a
  target signal $y$ from the latent representation of a context signal $x$. JEPAs
  bypass the need for negative and positive samples, traditionally required by contrastive
  learning while avoiding the overfitting issues associated with generative pretraining.
  In this paper, we show that graph-level representations can be effectively modeled
  using this paradigm by proposing a Graph Joint-Embedding Predictive Architecture
  (Graph-JEPA). In particular, we employ masked modeling and focus on predicting the
  latent representations of masked subgraphs starting from the latent representation
  of a context subgraph. To endow the representations with the implicit hierarchy
  that is often present in graph-level concepts, we devise an alternative prediction
  objective that consists of predicting the coordinates of the encoded subgraphs on
  the unit hyperbola in the 2D plane. Through multiple experimental evaluations, we
  show that Graph-JEPA can learn highly semantic and expressive representations, as
  shown by the downstream performance in graph classification, regression, and distinguishing
  non-isomorphic graphs. The code is available at https://github.com/geriskenderi/graph-jepa.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- Graph-JEPA
- Graph-JEPA (Transformer Encoders)
- Graph-JEPA (MLP Encoders)
- Graph-JEPA (METIS)
- Graph-JEPA (Random)
- Graph-JEPA (Node RWSE)
- Graph-JEPA (Patch RWSE)
mrr: 0.1071
adjusted_mrr: 0.1071
mrr_dataset_count: 9
benchmark_categories:
- Classic
- LRGB
- TU Dortmund
task_categories:
- graph_classification
- graph_regression
experiment_scopes:
- graph-level
results:
- &id006
  dataset: IMDB-BINARY
  rows:
  - model: GPM
    model_key: gpm
    model_plain: GPM
    value: 0.8267
    std: 0.0047
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.8267
    sort_std: 0.0047
    is_best: true
  - model: RUM
    model_key: rum
    model_plain: RUM
    value: 0.811
    std: 0.045
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.811
    sort_std: 0.045
    is_best: true
  - model: nsqure~
    model_key: nsqure~
    model_plain: nsqure~
    value: 0.7995
    std: 0.0246
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.7995
    sort_std: 0.0246
    is_best: true
  - model: S2GAE
    model_key: s2gae
    model_plain: S2GAE
    value: 0.7576
    std: 0.0062
    paper_value: 0.7576
    paper_std: 0.0062
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tan 2023
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 19
    true_value: 0.7576
    true_std: 0.0062
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7576
    sort_std: 0.0062
    is_best: false
  - model: GraphMAE
    model_key: graphmae
    model_plain: GraphMAE
    value: 0.7552
    std: 0.0066
    paper_value: 0.7552
    paper_std: 0.0066
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 2.26
    table_ref: Table 1
    source_ref: Hou 2022
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 22
    true_value: 0.7552
    true_std: 0.0066
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7552
    sort_std: 0.0066
    is_best: false
  - model: Graph-JEPA (MLP Encoders)
    model_key: graph-jepa (mlp encoders)
    model_plain: Graph-JEPA (MLP Encoders)
    value: 0.7426
    std: 0.0356
    paper_value: 0.7426
    paper_std: 0.0356
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 29
    true_value: 0.7426
    true_std: 0.0356
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7426
    sort_std: 0.0356
    is_best: false
  - model: MVGRL
    model_key: mvgrl
    model_plain: MVGRL
    value: 0.742
    std: 0.007
    paper_value: 0.742
    paper_std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hassani 2020
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 30
    true_value: 0.742
    true_std: 0.007
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 30
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.742
    sort_std: 0.007
    is_best: false
  - model: LaGraph
    model_key: lagraph
    model_plain: LaGraph
    value: 0.737
    std: 0.009
    paper_value: 0.737
    paper_std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xie 2022
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 34
    true_value: 0.737
    true_std: 0.009
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 34
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.737
    sort_std: 0.009
    is_best: false
  - model: Graph-JEPA
    model_key: graph-jepa
    model_plain: Graph-JEPA
    value: 0.7368
    std: 0.0324
    paper_value: 0.7368
    paper_std: 0.0324
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 19.22
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 36
    true_value: 0.7368
    true_std: 0.0324
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 36
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7368
    sort_std: 0.0324
    is_best: false
  - model: Graph-JEPA (Transformer Encoders)
    model_key: graph-jepa (transformer encoders)
    model_plain: Graph-JEPA (Transformer Encoders)
    value: 0.7368
    std: 0.0324
    paper_value: 0.7368
    paper_std: 0.0324
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 37
    true_value: 0.7368
    true_std: 0.0324
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 37
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7368
    sort_std: 0.0324
    is_best: false
  - model: Graph-JEPA (METIS)
    model_key: graph-jepa (metis)
    model_plain: Graph-JEPA (METIS)
    value: 0.7368
    std: 0.0324
    paper_value: 0.7368
    paper_std: 0.0324
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 6
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 38
    true_value: 0.7368
    true_std: 0.0324
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7368
    sort_std: 0.0324
    is_best: false
  - model: Graph-JEPA (Node RWSE)
    model_key: graph-jepa (node rwse)
    model_plain: Graph-JEPA (Node RWSE)
    value: 0.7368
    std: 0.0324
    paper_value: 0.7368
    paper_std: 0.0324
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 6
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 39
    true_value: 0.7368
    true_std: 0.0324
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7368
    sort_std: 0.0324
    is_best: false
  - model: Graph-JEPA (Patch RWSE)
    model_key: graph-jepa (patch rwse)
    model_plain: Graph-JEPA (Patch RWSE)
    value: 0.7358
    std: 0.0447
    paper_value: 0.7358
    paper_std: 0.0447
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 6
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 40
    true_value: 0.7358
    true_std: 0.0447
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 40
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7358
    sort_std: 0.0447
    is_best: false
  - model: Graph-JEPA (Random)
    model_key: graph-jepa (random)
    model_plain: Graph-JEPA (Random)
    value: 0.7352
    std: 0.0308
    paper_value: 0.7352
    paper_std: 0.0308
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 6
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 41
    true_value: 0.7352
    true_std: 0.0308
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 41
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7352
    sort_std: 0.0308
    is_best: false
  - model: Graph-JEPA (Hyperbolic LD)
    model_key: graph-jepa (hyperbolic ld)
    model_plain: Graph-JEPA (Hyperbolic LD)
    value: 0.734
    std: 0.0407
    paper_value: 0.734
    paper_std: 0.0407
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 44
    true_value: 0.734
    true_std: 0.0407
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 44
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.734
    sort_std: 0.0407
    is_best: false
  - model: Graph-JEPA (Euclidean)
    model_key: graph-jepa (euclidean)
    model_plain: Graph-JEPA (Euclidean)
    value: 0.725
    std: 0.0397
    paper_value: 0.725
    paper_std: 0.0397
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 58
    true_value: 0.725
    true_std: 0.0397
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 58
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.725
    sort_std: 0.0397
    is_best: false
  - model: AD-GCL-OPT
    model_key: ad-gcl-opt
    model_plain: AD-GCL-OPT
    value: 0.7233
    std: 0.0056
    paper_value: 0.7233
    paper_std: 0.0056
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Suresh 2021
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 59
    true_value: 0.7233
    true_std: 0.0056
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 59
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7233
    sort_std: 0.0056
    is_best: false
  - model: GIN + FA
    model_key: gin + fa
    model_plain: GIN + FA
    value: 0.7183
    std: 0.0193
    paper_value: 0.7183
    paper_std: 0.0193
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 68
    true_value: 0.7183
    true_std: 0.0193
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 68
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7183
    sort_std: 0.0193
    is_best: false
  - model: AD-GCL-FIX
    model_key: ad-gcl-fix
    model_plain: AD-GCL-FIX
    value: 0.7157
    std: 0.0101
    paper_value: 0.7157
    paper_std: 0.0101
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Suresh 2021
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 76
    true_value: 0.7157
    true_std: 0.0101
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 76
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7157
    sort_std: 0.0101
    is_best: false
  - model: InfoGraph
    model_key: infograph
    model_plain: InfoGraph
    value: 0.7111
    std: 0.0088
    paper_value: 0.7111
    paper_std: 0.0088
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Sun 2019
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 82
    true_value: 0.7111
    true_std: 0.0088
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 82
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7111
    sort_std: 0.0088
    is_best: false
  - model: GraphCL
    model_key: graphcl
    model_plain: GraphCL
    value: 0.708
    std: 0.0077
    paper_value: 0.708
    paper_std: 0.0077
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: You 2020
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 91
    true_value: 0.708
    true_std: 0.0077
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 91
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.708
    sort_std: 0.0077
    is_best: false
  - model: BGRL
    model_key: bgrl
    model_plain: BGRL
    value: 0.005
    std: 0.0
    paper_value: 0.005
    paper_std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Thakoor 2021
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 169
    true_value: 0.005
    true_std: 0.0
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 169
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.005
    sort_std: 0.0
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id007
  dataset: IMDB-MULTI
  rows:
  - model: KMIS
    model_key: kmis
    model_plain: KMIS
    value: 0.63
    std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.09821'
    title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 1
    sort_value: 0.63
    sort_std: 0.02
    is_best: true
  - model: DMON
    model_key: dmon
    model_plain: DMON
    value: 0.62
    std: 0.03
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.09821'
    title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 2
    sort_value: 0.62
    sort_std: 0.03
    is_best: true
  - model: SEP
    model_key: sep
    model_plain: SEP
    value: 0.61
    std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.09821'
    title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 3
    sort_value: 0.61
    sort_std: 0.02
    is_best: true
  - model: S2GAE
    model_key: s2gae
    model_plain: S2GAE
    value: 0.5179
    std: 0.0036
    paper_value: 0.5179
    paper_std: 0.0036
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tan et al.
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 23
    true_value: 0.5179
    true_std: 0.0036
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5179
    sort_std: 0.0036
    is_best: false
  - model: GraphMAE
    model_key: graphmae
    model_plain: GraphMAE
    value: 0.5163
    std: 0.0052
    paper_value: 0.5163
    paper_std: 0.0052
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 2.26
    table_ref: Table 1
    source_ref: Hou et al.
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 24
    true_value: 0.5163
    true_std: 0.0052
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5163
    sort_std: 0.0052
    is_best: false
  - model: MVGRL
    model_key: mvgrl
    model_plain: MVGRL
    value: 0.512
    std: 0.005
    paper_value: 0.512
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hassani et al.
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 26
    true_value: 0.512
    true_std: 0.005
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.512
    sort_std: 0.005
    is_best: false
  - model: Graph-JEPA
    model_key: graph-jepa
    model_plain: Graph-JEPA
    value: 0.5069
    std: 0.0291
    paper_value: 0.5069
    paper_std: 0.0291
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 19.22
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 33
    true_value: 0.5069
    true_std: 0.0291
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5069
    sort_std: 0.0291
    is_best: false
  - model: AD-GCL-OPT
    model_key: ad-gcl-opt
    model_plain: AD-GCL-OPT
    value: 0.4989
    std: 0.0066
    paper_value: 0.4989
    paper_std: 0.0066
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Suresh et al.
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 43
    true_value: 0.4989
    true_std: 0.0066
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 43
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4989
    sort_std: 0.0066
    is_best: false
  - model: AD-GCL-FIX
    model_key: ad-gcl-fix
    model_plain: AD-GCL-FIX
    value: 0.4904
    std: 0.0053
    paper_value: 0.4904
    paper_std: 0.0053
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Suresh et al.
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 51
    true_value: 0.4904
    true_std: 0.0053
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 51
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4904
    sort_std: 0.0053
    is_best: false
  - model: InfoGraph
    model_key: infograph
    model_plain: InfoGraph
    value: 0.4866
    std: 0.0067
    paper_value: 0.4866
    paper_std: 0.0067
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Sun et al.
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 58
    true_value: 0.4866
    true_std: 0.0067
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 58
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4866
    sort_std: 0.0067
    is_best: false
  - model: GraphCL
    model_key: graphcl
    model_plain: GraphCL
    value: 0.4849
    std: 0.0063
    paper_value: 0.4849
    paper_std: 0.0063
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: You et al.
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 62
    true_value: 0.4849
    true_std: 0.0063
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 62
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4849
    sort_std: 0.0063
    is_best: false
  - model: GIN + FA
    model_key: gin + fa
    model_plain: GIN + FA
    value: 0.4846
    std: 0.0231
    paper_value: 0.4846
    paper_std: 0.0231
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 63
    true_value: 0.4846
    true_std: 0.0231
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 63
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4846
    sort_std: 0.0231
    is_best: false
  - model: BGRL
    model_key: bgrl
    model_plain: BGRL
    value: 0.0033
    std: 0.0
    paper_value: 0.0033
    paper_std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Thakoor et al.
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 80
    true_value: 0.0033
    true_std: 0.0
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 80
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.0033
    sort_std: 0.0
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id005
  dataset: MUTAG
  rows:
  - model: PR-MPNN
    model_key: pr-mpnn
    model_plain: PR-MPNN
    value: 0.984
    std: 0.024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.17311'
    title: Probabilistic Graph Rewiring via Virtual Nodes
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.984
    sort_std: 0.024
    is_best: true
  - model: PR-MPNN (10-fold CV)
    model_key: pr-mpnn (10-fold cv)
    model_plain: PR-MPNN (10-fold CV)
    value: 0.984
    std: 0.024
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.02156'
    title: Probabilistically Rewired Message-Passing Neural Networks
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.984
    sort_std: 0.024
    is_best: true
  - model: IPR-MPNN
    model_key: ipr-mpnn
    model_plain: IPR-MPNN
    value: 0.98
    std: 0.034
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.17311'
    title: Probabilistic Graph Rewiring via Virtual Nodes
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.98
    sort_std: 0.034
    is_best: true
  - model: Graph-JEPA
    model_key: graph-jepa
    model_plain: Graph-JEPA
    value: 0.9125
    std: 0.0575
    paper_value: 0.9125
    paper_std: 0.0575
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 19.22
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 8
    true_value: 0.9125
    true_std: 0.0575
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9125
    sort_std: 0.0575
    is_best: true
  - model: GIN + FA
    model_key: gin + fa
    model_plain: GIN + FA
    value: 0.9041
    std: 0.0461
    paper_value: 0.9041
    paper_std: 0.0461
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 15
    true_value: 0.9041
    true_std: 0.0461
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9041
    sort_std: 0.0461
    is_best: false
  - model: LaGraph
    model_key: lagraph
    model_plain: LaGraph
    value: 0.902
    std: 0.011
    paper_value: 0.902
    paper_std: 0.011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xie 2022
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 21
    true_value: 0.902
    true_std: 0.011
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.902
    sort_std: 0.011
    is_best: false
  - model: AD-GCL-OPT
    model_key: ad-gcl-opt
    model_plain: AD-GCL-OPT
    value: 0.897
    std: 0.0103
    paper_value: 0.897
    paper_std: 0.0103
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Suresh 2021
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 25
    true_value: 0.897
    true_std: 0.0103
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.897
    sort_std: 0.0103
    is_best: false
  - model: AD-GCL-FIX
    model_key: ad-gcl-fix
    model_plain: AD-GCL-FIX
    value: 0.8925
    std: 0.0145
    paper_value: 0.8925
    paper_std: 0.0145
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Suresh 2021
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 33
    true_value: 0.8925
    true_std: 0.0145
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8925
    sort_std: 0.0145
    is_best: false
  - model: GraphCL
    model_key: graphcl
    model_plain: GraphCL
    value: 0.8829
    std: 0.0131
    paper_value: 0.8829
    paper_std: 0.0131
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: You 2020
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 39
    true_value: 0.8829
    true_std: 0.0131
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8829
    sort_std: 0.0131
    is_best: false
  - model: S2GAE
    model_key: s2gae
    model_plain: S2GAE
    value: 0.8826
    std: 0.0076
    paper_value: 0.8826
    paper_std: 0.0076
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tan 2023
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 40
    true_value: 0.8826
    true_std: 0.0076
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 40
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8826
    sort_std: 0.0076
    is_best: false
  - model: GraphMAE
    model_key: graphmae
    model_plain: GraphMAE
    value: 0.8819
    std: 0.0126
    paper_value: 0.8819
    paper_std: 0.0126
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 2.26
    table_ref: Table 1
    source_ref: Hou 2022
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 41
    true_value: 0.8819
    true_std: 0.0126
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 41
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8819
    sort_std: 0.0126
    is_best: false
  - model: InfoGraph
    model_key: infograph
    model_plain: InfoGraph
    value: 0.8771
    std: 0.0177
    paper_value: 0.8771
    paper_std: 0.0177
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Sun 2019
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 45
    true_value: 0.8771
    true_std: 0.0177
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 45
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8771
    sort_std: 0.0177
    is_best: false
  - model: BGRL
    model_key: bgrl
    model_plain: BGRL
    value: 0.7499
    std: 0.0883
    paper_value: 0.7499
    paper_std: 0.0883
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Thakoor 2021
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 136
    true_value: 0.7499
    true_std: 0.0883
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 136
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7499
    sort_std: 0.0883
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: PROTEINS
  rows:
  - model: IPR-MPNN
    model_key: ipr-mpnn
    model_plain: IPR-MPNN
    value: 0.854
    std: 0.044
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.17311'
    title: Probabilistic Graph Rewiring via Virtual Nodes
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.854
    sort_std: 0.044
    is_best: true
  - model: PR-MPNN
    model_key: pr-mpnn
    model_plain: PR-MPNN
    value: 0.807
    std: 0.039
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.17311'
    title: Probabilistic Graph Rewiring via Virtual Nodes
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.807
    sort_std: 0.039
    is_best: true
  - model: PR-MPNN (10-fold CV)
    model_key: pr-mpnn (10-fold cv)
    model_plain: PR-MPNN (10-fold CV)
    value: 0.807
    std: 0.039
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.02156'
    title: Probabilistically Rewired Message-Passing Neural Networks
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.807
    sort_std: 0.039
    is_best: true
  - model: S2GAE
    model_key: s2gae
    model_plain: S2GAE
    value: 0.7637
    std: 0.0043
    paper_value: 0.7637
    paper_std: 0.0043
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tan 2023
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 27
    true_value: 0.7637
    true_std: 0.0043
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 27
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7637
    sort_std: 0.0043
    is_best: false
  - model: Graph-JEPA
    model_key: graph-jepa
    model_plain: Graph-JEPA
    value: 0.7568
    std: 0.0378
    paper_value: 0.7568
    paper_std: 0.0378
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 19.22
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 48
    true_value: 0.7568
    true_std: 0.0378
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 48
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7568
    sort_std: 0.0378
    is_best: false
  - model: GraphMAE
    model_key: graphmae
    model_plain: GraphMAE
    value: 0.753
    std: 0.0039
    paper_value: 0.753
    paper_std: 0.0039
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 2.26
    table_ref: Table 1
    source_ref: Hou 2022
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 54
    true_value: 0.753
    true_std: 0.0039
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 54
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.753
    sort_std: 0.0039
    is_best: false
  - model: LaGraph
    model_key: lagraph
    model_plain: LaGraph
    value: 0.752
    std: 0.004
    paper_value: 0.752
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xie 2022
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 57
    true_value: 0.752
    true_std: 0.004
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 57
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.752
    sort_std: 0.004
    is_best: false
  - model: AD-GCL-OPT
    model_key: ad-gcl-opt
    model_plain: AD-GCL-OPT
    value: 0.7381
    std: 0.0046
    paper_value: 0.7381
    paper_std: 0.0046
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Suresh 2021
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 100
    true_value: 0.7381
    true_std: 0.0046
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 100
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7381
    sort_std: 0.0046
    is_best: false
  - model: AD-GCL-FIX
    model_key: ad-gcl-fix
    model_plain: AD-GCL-FIX
    value: 0.7359
    std: 0.0065
    paper_value: 0.7359
    paper_std: 0.0065
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Suresh 2021
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 104
    true_value: 0.7359
    true_std: 0.0065
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 104
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7359
    sort_std: 0.0065
    is_best: false
  - model: GIN + FA
    model_key: gin + fa
    model_plain: GIN + FA
    value: 0.7239
    std: 0.0276
    paper_value: 0.7239
    paper_std: 0.0276
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 123
    true_value: 0.72902
    true_std: 0.01419
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.005120000000000013
    value_note: global 0.7290 within std
    paper_rank: 136
    rank_delta: 13
    rank_delta_abs: 13
    rank_delta_direction: worse
    sort_value: 0.72902
    sort_std: 0.01419
    is_best: false
  - model: GraphCL
    model_key: graphcl
    model_plain: GraphCL
    value: 0.7286
    std: 0.0101
    paper_value: 0.7286
    paper_std: 0.0101
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: You 2020
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 126
    true_value: 0.7286
    true_std: 0.0101
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 126
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7286
    sort_std: 0.0101
    is_best: false
  - model: InfoGraph
    model_key: infograph
    model_plain: InfoGraph
    value: 0.7257
    std: 0.0065
    paper_value: 0.7257
    paper_std: 0.0065
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Sun 2019
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 134
    true_value: 0.7257
    true_std: 0.0065
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 134
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7257
    sort_std: 0.0065
    is_best: false
  - model: BGRL
    model_key: bgrl
    model_plain: BGRL
    value: 0.7099
    std: 0.0386
    paper_value: 0.7099
    paper_std: 0.0386
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Thakoor 2021
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 166
    true_value: 0.7099
    true_std: 0.0386
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 166
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7099
    sort_std: 0.0386
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id002
  dataset: Peptides-func
  rows:
  - model: LightGBM (ECFP)
    model_key: lightgbm (ecfp)
    model_plain: LightGBM (ECFP)
    value: 0.746
    std: null
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.746
    sort_std: null
    is_best: true
  - model: Random Forest (ECFP)
    model_key: random forest (ecfp)
    model_plain: Random Forest (ECFP)
    value: 0.7355
    std: 0.001
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.7355
    sort_std: 0.001
    is_best: false
  - model: LightGBM (TT)
    model_key: lightgbm (tt)
    model_plain: LightGBM (TT)
    value: 0.7318
    std: null
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.7318
    sort_std: null
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.593
    std: 0.002
    paper_value: 0.593
    paper_std: 0.002
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: dwivedi2022long
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 9
    true_value: 0.7261
    true_std: 0.0067
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1331
    value_note: ''
    paper_rank: 261
    rank_delta: 252
    rank_delta_abs: 252
    rank_delta_direction: worse
    sort_value: 0.7261
    sort_std: 0.0067
    is_best: false
  - model: GatedGCN+RWSE
    model_key: gatedgcn+rwse
    model_plain: GatedGCN+RWSE
    value: 0.607
    std: 0.004
    paper_value: 0.607
    paper_std: 0.004
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: dwivedi2022long
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 133
    true_value: 0.6685
    true_std: 0.0062
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0615
    value_note: ''
    paper_rank: 239
    rank_delta: 106
    rank_delta_abs: 106
    rank_delta_direction: worse
    sort_value: 0.6685
    sort_std: 0.0062
    is_best: false
  - model: SAN+RWSE
    model_key: san+rwse
    model_plain: SAN+RWSE
    value: 0.644
    std: 0.008
    paper_value: 0.644
    paper_std: 0.008
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: dwivedi2022long
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 200
    true_value: 0.644
    true_std: 0.008
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 200
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.644
    sort_std: 0.008
    is_best: false
  - model: Graph-JEPA
    model_key: graph-jepa
    model_plain: Graph-JEPA
    value: 0.263
    std: 0.003
    paper_value: 0.263
    paper_std: 0.003
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 19.22
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 322
    true_value: 0.263
    true_std: 0.003
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 322
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.263
    sort_std: 0.003
    is_best: false
  - model: Graph-JEPA \dagger
    model_key: graph-jepa \dagger
    model_plain: Graph-JEPA \dagger
    value: 0.252
    std: 0.002
    paper_value: 0.252
    paper_std: 0.002
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 323
    true_value: 0.252
    true_std: 0.002
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 323
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.252
    sort_std: 0.002
    is_best: false
  metric: AP
  higher_is_better: true
- &id003
  dataset: Peptides-struct
  rows:
  - model: ESA
    model_key: esa
    model_plain: ESA
    value: 0.2393
    std: 0.0004
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.10793'
    title: An end-to-end attention-based approach for learning on graphs
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.2393
    sort_std: 0.0004
    is_best: true
  - model: GRPE-FFGT
    model_key: grpe-ffgt
    model_plain: GRPE-FFGT
    value: 0.2416
    std: 0.0026
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.04653'
    title: Hybrid Focal and Full-Range Attention Based Graph Transformers
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.2416
    sort_std: 0.0026
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.35
    std: 0.001
    paper_value: 0.35
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: dwivedi2022long
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 3
    true_value: 0.2421
    true_std: 0.0016
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10789999999999997
    value_note: ''
    paper_rank: 306
    rank_delta: 303
    rank_delta_abs: 303
    rank_delta_direction: worse
    sort_value: 0.2421
    sort_std: 0.0016
    is_best: false
  - model: Tango_GPS
    model_key: tango_gps
    model_plain: Tango_GPS
    value: 0.2422
    std: 0.0014
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.05070'
    title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential Flows'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.2422
    sort_std: 0.0014
    is_best: false
  - model: GatedGCN+RWSE
    model_key: gatedgcn+rwse
    model_plain: GatedGCN+RWSE
    value: 0.3357
    std: 0.001
    paper_value: 0.3357
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: dwivedi2022long
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 167
    true_value: 0.2529
    true_std: 0.0009
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08279999999999998
    value_note: ''
    paper_rank: 289
    rank_delta: 122
    rank_delta_abs: 122
    rank_delta_direction: worse
    sort_value: 0.2529
    sort_std: 0.0009
    is_best: false
  - model: SAN+RWSE
    model_key: san+rwse
    model_plain: SAN+RWSE
    value: 0.2545
    std: 0.001
    paper_value: 0.2545
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: dwivedi2022long
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 188
    true_value: 0.2545
    true_std: 0.0012
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: LRGB
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 188
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2545
    sort_std: 0.0012
    is_best: false
  - model: Graph-JEPA
    model_key: graph-jepa
    model_plain: Graph-JEPA
    value: 0.305
    std: 0.002
    paper_value: 0.305
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 19.22
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 274
    true_value: 0.305
    true_std: 0.002
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 274
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.305
    sort_std: 0.002
    is_best: false
  metric: MAE
  higher_is_better: false
- &id008
  dataset: REDDIT-BINARY
  rows:
  - model: R-method
    model_key: r-method
    model_plain: R-method
    value: 0.945
    std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.01122'
    title: Learning Efficient Positional Encodings with Graph Neural Networks
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.945
    sort_std: 0.004
    is_best: true
  - model: Graph-JEPA
    model_key: graph-jepa
    model_plain: Graph-JEPA
    value: 0.9199
    std: 0.0159
    paper_value: 0.9199
    paper_std: 0.0159
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 19.22
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 2
    true_value: 0.9199
    true_std: 0.0159
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9199
    sort_std: 0.0159
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.918
    std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.01122'
    title: Learning Efficient Positional Encodings with Graph Neural Networks
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.918
    sort_std: 0.01
    is_best: false
  - model: GIN + rand id
    model_key: gin + rand id
    model_plain: GIN + rand id
    value: 0.918
    std: 0.016
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.01122'
    title: Learning Efficient Positional Encodings with Graph Neural Networks
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.918
    sort_std: 0.016
    is_best: false
  - model: LaGraph
    model_key: lagraph
    model_plain: LaGraph
    value: 0.904
    std: 0.008
    paper_value: 0.904
    paper_std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xie 2022
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 6
    true_value: 0.904
    true_std: 0.008
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.904
    sort_std: 0.008
    is_best: false
  - model: GraphMAE
    model_key: graphmae
    model_plain: GraphMAE
    value: 0.8801
    std: 0.0019
    paper_value: 0.8801
    paper_std: 0.0019
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 2.26
    table_ref: Table 1
    source_ref: Hou 2022
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 8
    true_value: 0.8801
    true_std: 0.0019
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8801
    sort_std: 0.0019
    is_best: false
  - model: S2GAE
    model_key: s2gae
    model_plain: S2GAE
    value: 0.8783
    std: 0.0027
    paper_value: 0.8783
    paper_std: 0.0027
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tan 2023
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 10
    true_value: 0.8783
    true_std: 0.0027
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8783
    sort_std: 0.0027
    is_best: false
  - model: GIN + FA
    model_key: gin + fa
    model_plain: GIN + FA
    value: 0.8679
    std: 0.0204
    paper_value: 0.8679
    paper_std: 0.0204
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 11
    true_value: 0.8679
    true_std: 0.0204
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8679
    sort_std: 0.0204
    is_best: false
  - model: AD-GCL-FIX
    model_key: ad-gcl-fix
    model_plain: AD-GCL-FIX
    value: 0.8552
    std: 0.0079
    paper_value: 0.8552
    paper_std: 0.0079
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Suresh 2021
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 14
    true_value: 0.8552
    true_std: 0.0079
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8552
    sort_std: 0.0079
    is_best: false
  - model: AD-GCL-OPT
    model_key: ad-gcl-opt
    model_plain: AD-GCL-OPT
    value: 0.8552
    std: 0.0079
    paper_value: 0.8552
    paper_std: 0.0079
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Suresh 2021
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 15
    true_value: 0.8552
    true_std: 0.0079
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8552
    sort_std: 0.0079
    is_best: false
  - model: MVGRL
    model_key: mvgrl
    model_plain: MVGRL
    value: 0.845
    std: 0.006
    paper_value: 0.845
    paper_std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hassani 2020
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 19
    true_value: 0.845
    true_std: 0.006
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.845
    sort_std: 0.006
    is_best: false
  - model: GraphCL
    model_key: graphcl
    model_plain: GraphCL
    value: 0.8263
    std: 0.0099
    paper_value: 0.8263
    paper_std: 0.0099
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: You 2020
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 20
    true_value: 0.8263
    true_std: 0.0099
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8263
    sort_std: 0.0099
    is_best: false
  - model: InfoGraph
    model_key: infograph
    model_plain: InfoGraph
    value: 0.7879
    std: 0.0214
    paper_value: 0.7879
    paper_std: 0.0214
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Sun 2019
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 28
    true_value: 0.7879
    true_std: 0.0214
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 28
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7879
    sort_std: 0.0214
    is_best: false
  - model: BGRL
    model_key: bgrl
    model_plain: BGRL
    value: 0.5
    std: 0.0
    paper_value: 0.5
    paper_std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Thakoor 2021
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 35
    true_value: 0.5
    true_std: 0.0
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5
    sort_std: 0.0
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id009
  dataset: REDDIT-MULTI-5K
  rows:
  - model: R-method
    model_key: r-method
    model_plain: R-method
    value: 0.606
    std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.01122'
    title: Learning Efficient Positional Encodings with Graph Neural Networks
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.606
    sort_std: 0.003
    is_best: true
  - model: GIN + rand id
    model_key: gin + rand id
    model_plain: GIN + rand id
    value: 0.57
    std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.01122'
    title: Learning Efficient Positional Encodings with Graph Neural Networks
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.57
    sort_std: 0.021
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.569
    std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.01122'
    title: Learning Efficient Positional Encodings with Graph Neural Networks
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.569
    sort_std: 0.02
    is_best: false
  - model: Graph-JEPA
    model_key: graph-jepa
    model_plain: Graph-JEPA
    value: 0.5673
    std: 0.0196
    paper_value: 0.5673
    paper_std: 0.0196
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 19.22
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 4
    true_value: 0.5673
    true_std: 0.0196
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5673
    sort_std: 0.0196
    is_best: false
  - model: LaGraph
    model_key: lagraph
    model_plain: LaGraph
    value: 0.564
    std: 0.004
    paper_value: 0.564
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xie et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 5
    true_value: 0.564
    true_std: 0.004
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.564
    sort_std: 0.004
    is_best: false
  - model: AD-GCL-OPT
    model_key: ad-gcl-opt
    model_plain: AD-GCL-OPT
    value: 0.5493
    std: 0.0043
    paper_value: 0.5493
    paper_std: 0.0043
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Suresh et al. 2021
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 8
    true_value: 0.5493
    true_std: 0.0043
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5493
    sort_std: 0.0043
    is_best: false
  - model: GIN + FA
    model_key: gin + fa
    model_plain: GIN + FA
    value: 0.5328
    std: 0.0317
    paper_value: 0.5328
    paper_std: 0.0317
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 9
    true_value: 0.5328
    true_std: 0.0317
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5328
    sort_std: 0.0317
    is_best: false
  - model: GraphCL
    model_key: graphcl
    model_plain: GraphCL
    value: 0.5305
    std: 0.004
    paper_value: 0.5305
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: You et al. 2020
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 10
    true_value: 0.5305
    true_std: 0.004
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5305
    sort_std: 0.004
    is_best: false
  - model: AD-GCL-FIX
    model_key: ad-gcl-fix
    model_plain: AD-GCL-FIX
    value: 0.53
    std: 0.0082
    paper_value: 0.53
    paper_std: 0.0082
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Suresh et al. 2021
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 11
    true_value: 0.53
    true_std: 0.0082
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.53
    sort_std: 0.0082
    is_best: false
  - model: InfoGraph
    model_key: infograph
    model_plain: InfoGraph
    value: 0.5111
    std: 0.0055
    paper_value: 0.5111
    paper_std: 0.0055
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Sun et al. 2019
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 12
    true_value: 0.5111
    true_std: 0.0055
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5111
    sort_std: 0.0055
    is_best: false
  - model: GraphMAE
    model_key: graphmae
    model_plain: GraphMAE
    value: 0.4606
    std: 0.0344
    paper_value: 0.4606
    paper_std: 0.0344
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 2.26
    table_ref: Table 1
    source_ref: Hou et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 17
    true_value: 0.4606
    true_std: 0.0344
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4606
    sort_std: 0.0344
    is_best: false
  - model: BGRL
    model_key: bgrl
    model_plain: BGRL
    value: 0.2
    std: 0.001
    paper_value: 0.2
    paper_std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Thakoor et al. 2021
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 32
    true_value: 0.2
    true_std: 0.001
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2
    sort_std: 0.001
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id001
  dataset: ZINC
  rows:
  - model: FloydNet
    model_key: floydnet
    model_plain: FloydNet
    value: 0.016
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.19094'
    title: 'FloydNet: A Learning Paradigm for Global Relational Reasoning'
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.016
    sort_std: null
    is_best: true
  - model: ESA (PE)
    model_key: esa (pe)
    model_plain: ESA (PE)
    value: 0.017331929457918168
    std: 0.0009253668251948539
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.10793'
    title: An end-to-end attention-based approach for learning on graphs
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.017331929457918168
    sort_std: 0.0009253668251948539
    is_best: false
  - model: PST
    model_key: pst
    model_plain: PST
    value: 0.018
    std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 1.0
    arxiv_id: '2405.02795'
    title: Graph as Point Set
    date: May 5, 2024
    date_display: May 2024
    date_iso: '2024-05-05'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.018
    sort_std: 0.001
    is_best: false
  - model: GIN + FA
    model_key: gin + fa
    model_plain: GIN + FA
    value: 0.254
    std: 0.005
    paper_value: 0.254
    paper_std: 0.005
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 267
    true_value: 0.254
    true_std: 0.005
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 267
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.254
    sort_std: 0.005
    is_best: false
  - model: Graph-JEPA
    model_key: graph-jepa
    model_plain: Graph-JEPA
    value: 0.434
    std: 0.014
    paper_value: 0.434
    paper_std: 0.014
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 19.22
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 293
    true_value: 0.434
    true_std: 0.014
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 293
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.434
    sort_std: 0.014
    is_best: false
  - model: AD-GCL-OPT
    model_key: ad-gcl-opt
    model_plain: AD-GCL-OPT
    value: 0.544
    std: 0.004
    paper_value: 0.544
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: suresh2021adversarial
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 295
    true_value: 0.544
    true_std: 0.004
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 295
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.544
    sort_std: 0.004
    is_best: false
  - model: AD-GCL-FIX
    model_key: ad-gcl-fix
    model_plain: AD-GCL-FIX
    value: 0.578
    std: 0.012
    paper_value: 0.578
    paper_std: 0.012
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: suresh2021adversarial
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 297
    true_value: 0.578
    true_std: 0.012
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 297
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.578
    sort_std: 0.012
    is_best: false
  - model: GraphCL
    model_key: graphcl
    model_plain: GraphCL
    value: 0.627
    std: 0.013
    paper_value: 0.627
    paper_std: 0.013
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: you2020graph
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 301
    true_value: 0.627
    true_std: 0.013
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 301
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.627
    sort_std: 0.013
    is_best: false
  - model: InfoGraph
    model_key: infograph
    model_plain: InfoGraph
    value: 0.89
    std: 0.017
    paper_value: 0.89
    paper_std: 0.017
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: sun2019infograph
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 305
    true_value: 0.89
    true_std: 0.017
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 305
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.89
    sort_std: 0.017
    is_best: false
  - model: GraphMAE
    model_key: graphmae
    model_plain: GraphMAE
    value: 0.935
    std: 0.034
    paper_value: 0.935
    paper_std: 0.034
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 2.26
    table_ref: Table 1
    source_ref: hou2022graphmae
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 306
    true_value: 0.935
    true_std: 0.034
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 306
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.935
    sort_std: 0.034
    is_best: false
  - model: BGRL
    model_key: bgrl
    model_plain: BGRL
    value: 1.2
    std: 0.011
    paper_value: 1.2
    paper_std: 0.011
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: thakoor2021large
    variant_inference_reason: ''
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    global_rank: 308
    true_value: 1.2
    true_std: 0.011
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 308
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.2
    sort_std: 0.011
    is_best: false
  metric: MAE
  higher_is_better: false
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
- benchmark: LRGB
  datasets:
  - *id002
  - *id003
- benchmark: TU Dortmund
  datasets:
  - *id004
  - *id005
  - *id006
  - *id007
  - *id008
  - *id009
main_figure: /figures/2309.16014/main_figure.png
---

