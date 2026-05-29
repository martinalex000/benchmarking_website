---
title: 'DualEquiNet: A Dual-Space Hierarchical Equivariant Network for Large Biomolecules'
arxiv_id: '2506.19862'
source_url: ''
authors: []
published_date: Jun 2025
published_date_iso: 2025-06
abstract: Geometric graph neural networks (GNNs) that respect E(3) symmetries have
  achieved strong performance on small molecule modeling, but they face scalability
  and expressiveness challenges when applied to large biomolecules such as RNA and
  proteins. These systems require models that can simultaneously capture fine-grained
  atomic interactions, long-range dependencies across spatially distant components,
  and biologically relevant hierarchical structure—such as atoms forming residues,
  which in turn form higher-order domains. Existing geometric GNNs, which typically
  operate exclusively in either Euclidean or Spherical Harmonics space, are limited
  in their ability to capture both the fine-scale atomic details and the long-range,
  symmetry-aware dependencies required for modeling the multi-scale structure of large
  biomolecules. We introduce DualEquiNet, a Dual-Space Hierarchical Equivariant Network
  that constructs complementary representations in both Euclidean and Spherical Harmonics
  spaces to capture local geometry and global symmetry-aware features. DualEquiNet
  employs bidirectional cross-space message passing and a novel Cross-Space Interaction
  Pooling mechanism to hierarchically aggregate atomic features into biologically
  meaningful units, such as residues, enabling efficient and expressive multi-scale
  modeling for large biomolecular systems. DualEquiNet achieves state-of-the-art performance
  on multiple existing benchmarks for RNA property prediction and protein modeling,
  and outperforms prior methods on two newly introduced 3D structural benchmarks demonstrating
  its broad effectiveness across a range of large biomolecule modeling tasks.
codebase_url: ''
extraction_model: Qwen/Qwen3.6-35B-A3B-FP8
has_results: true
paper_type: method
proposed_models:
- DualEquiNet
mrr: 0.0
adjusted_mrr: 0.0
mrr_dataset_count: 0
benchmark_categories:
- DualEquiNet RNA Benchmarks
task_categories:
- graph_regression
experiment_scopes:
- graph-level
results:
- &id002
  dataset: COVID
  rows:
  - model: DualEquiNet
    model_key: dualequinet
    model_plain: DualEquiNet
    value: 0.353
    std: 0.006
    paper_value: 0.353
    paper_std: 0.006
    metric: RMSE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 1
    true_value: 0.353
    true_std: 0.006
    value_gap_source_arxiv: '2506.19862'
    value_gap_source_title: 'DualEquiNet: A Dual-Space Hierarchical Equivariant Network
      for Large Biomolecules'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.353
    sort_std: 0.006
    is_best: true
  - model: GotenNet
    model_key: gotennet
    model_plain: GotenNet
    value: 0.475
    std: 0.009
    paper_value: 0.475
    paper_std: 0.009
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 2
    true_value: 0.475
    true_std: 0.009
    value_gap_source_arxiv: '2506.19862'
    value_gap_source_title: 'DualEquiNet: A Dual-Space Hierarchical Equivariant Network
      for Large Biomolecules'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.475
    sort_std: 0.009
    is_best: false
  - model: FastEGNN
    model_key: fastegnn
    model_plain: FastEGNN
    value: 0.478
    std: 0.031
    paper_value: 0.478
    paper_std: 0.031
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 3
    true_value: 0.478
    true_std: 0.031
    value_gap_source_arxiv: '2506.19862'
    value_gap_source_title: 'DualEquiNet: A Dual-Space Hierarchical Equivariant Network
      for Large Biomolecules'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.478
    sort_std: 0.031
    is_best: false
  - model: GVPGNN
    model_key: gvpgnn
    model_plain: GVPGNN
    value: 0.531
    std: 0.011
    paper_value: 0.531
    paper_std: 0.011
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 4
    true_value: 0.531
    true_std: 0.011
    value_gap_source_arxiv: '2506.19862'
    value_gap_source_title: 'DualEquiNet: A Dual-Space Hierarchical Equivariant Network
      for Large Biomolecules'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.531
    sort_std: 0.011
    is_best: false
  - model: EGNN
    model_key: egnn
    model_plain: EGNN
    value: 0.533
    std: 0.011
    paper_value: 0.533
    paper_std: 0.011
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 5
    true_value: 0.533
    true_std: 0.011
    value_gap_source_arxiv: '2506.19862'
    value_gap_source_title: 'DualEquiNet: A Dual-Space Hierarchical Equivariant Network
      for Large Biomolecules'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.533
    sort_std: 0.011
    is_best: false
  - model: SchNet
    model_key: schnet
    model_plain: SchNet
    value: 0.534
    std: 0.011
    paper_value: 0.534
    paper_std: 0.011
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 6
    true_value: 0.534
    true_std: 0.011
    value_gap_source_arxiv: '2506.19862'
    value_gap_source_title: 'DualEquiNet: A Dual-Space Hierarchical Equivariant Network
      for Large Biomolecules'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.534
    sort_std: 0.011
    is_best: false
  - model: TFN
    model_key: tfn
    model_plain: TFN
    value: 0.535
    std: 0.011
    paper_value: 0.535
    paper_std: 0.011
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 7
    true_value: 0.535
    true_std: 0.011
    value_gap_source_arxiv: '2506.19862'
    value_gap_source_title: 'DualEquiNet: A Dual-Space Hierarchical Equivariant Network
      for Large Biomolecules'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.535
    sort_std: 0.011
    is_best: false
  metric: RMSE
  higher_is_better: false
- &id003
  dataset: Ribonanza
  rows:
  - model: EU
    model_key: eu
    model_plain: EU
    value: 0.558
    std: 0.012
    paper_value: 0.558
    paper_std: 0.012
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 1
    true_value: 0.558
    true_std: 0.012
    value_gap_source_arxiv: '2506.19862'
    value_gap_source_title: 'DualEquiNet: A Dual-Space Hierarchical Equivariant Network
      for Large Biomolecules'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.558
    sort_std: 0.012
    is_best: true
  - model: FastEGNN
    model_key: fastegnn
    model_plain: FastEGNN
    value: 0.839
    std: 0.02
    paper_value: 0.839
    paper_std: 0.02
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 2
    true_value: 0.839
    true_std: 0.02
    value_gap_source_arxiv: '2506.19862'
    value_gap_source_title: 'DualEquiNet: A Dual-Space Hierarchical Equivariant Network
      for Large Biomolecules'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.839
    sort_std: 0.02
    is_best: false
  - model: GotenNet
    model_key: gotennet
    model_plain: GotenNet
    value: 0.857
    std: 0.013
    paper_value: 0.857
    paper_std: 0.013
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 3
    true_value: 0.857
    true_std: 0.013
    value_gap_source_arxiv: '2506.19862'
    value_gap_source_title: 'DualEquiNet: A Dual-Space Hierarchical Equivariant Network
      for Large Biomolecules'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.857
    sort_std: 0.013
    is_best: false
  - model: GVPGNN
    model_key: gvpgnn
    model_plain: GVPGNN
    value: 0.932
    std: 0.01
    paper_value: 0.932
    paper_std: 0.01
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 4
    true_value: 0.932
    true_std: 0.01
    value_gap_source_arxiv: '2506.19862'
    value_gap_source_title: 'DualEquiNet: A Dual-Space Hierarchical Equivariant Network
      for Large Biomolecules'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.932
    sort_std: 0.01
    is_best: false
  - model: EGNN
    model_key: egnn
    model_plain: EGNN
    value: 0.934
    std: 0.01
    paper_value: 0.934
    paper_std: 0.01
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 5
    true_value: 0.934
    true_std: 0.01
    value_gap_source_arxiv: '2506.19862'
    value_gap_source_title: 'DualEquiNet: A Dual-Space Hierarchical Equivariant Network
      for Large Biomolecules'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.934
    sort_std: 0.01
    is_best: false
  - model: SchNet
    model_key: schnet
    model_plain: SchNet
    value: 0.937
    std: 0.012
    paper_value: 0.937
    paper_std: 0.012
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 6
    true_value: 0.937
    true_std: 0.012
    value_gap_source_arxiv: '2506.19862'
    value_gap_source_title: 'DualEquiNet: A Dual-Space Hierarchical Equivariant Network
      for Large Biomolecules'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.937
    sort_std: 0.012
    is_best: false
  - model: TFN
    model_key: tfn
    model_plain: TFN
    value: 0.939
    std: 0.012
    paper_value: 0.939
    paper_std: 0.012
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 7
    true_value: 0.939
    true_std: 0.012
    value_gap_source_arxiv: '2506.19862'
    value_gap_source_title: 'DualEquiNet: A Dual-Space Hierarchical Equivariant Network
      for Large Biomolecules'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.939
    sort_std: 0.012
    is_best: false
  metric: RMSE
  higher_is_better: false
- &id004
  dataset: Tc-Ribo
  rows:
  - model: DualEquiNet
    model_key: dualequinet
    model_plain: DualEquiNet
    value: 0.636
    std: 0.049
    paper_value: 0.636
    paper_std: 0.049
    metric: RMSE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 1
    true_value: 0.636
    true_std: 0.049
    value_gap_source_arxiv: '2506.19862'
    value_gap_source_title: 'DualEquiNet: A Dual-Space Hierarchical Equivariant Network
      for Large Biomolecules'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.636
    sort_std: 0.049
    is_best: true
  - model: TFN
    model_key: tfn
    model_plain: TFN
    value: 0.694
    std: 0.008
    paper_value: 0.694
    paper_std: 0.008
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 2
    true_value: 0.694
    true_std: 0.008
    value_gap_source_arxiv: '2506.19862'
    value_gap_source_title: 'DualEquiNet: A Dual-Space Hierarchical Equivariant Network
      for Large Biomolecules'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.694
    sort_std: 0.008
    is_best: false
  - model: GotenNet
    model_key: gotennet
    model_plain: GotenNet
    value: 0.718
    std: 0.002
    paper_value: 0.718
    paper_std: 0.002
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 3
    true_value: 0.718
    true_std: 0.002
    value_gap_source_arxiv: '2506.19862'
    value_gap_source_title: 'DualEquiNet: A Dual-Space Hierarchical Equivariant Network
      for Large Biomolecules'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.718
    sort_std: 0.002
    is_best: false
  - model: EGNN
    model_key: egnn
    model_plain: EGNN
    value: 0.729
    std: 0.007
    paper_value: 0.729
    paper_std: 0.007
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 4
    true_value: 0.729
    true_std: 0.007
    value_gap_source_arxiv: '2506.19862'
    value_gap_source_title: 'DualEquiNet: A Dual-Space Hierarchical Equivariant Network
      for Large Biomolecules'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.729
    sort_std: 0.007
    is_best: false
  - model: FastEGNN
    model_key: fastegnn
    model_plain: FastEGNN
    value: 0.731
    std: 0.006
    paper_value: 0.731
    paper_std: 0.006
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 5
    true_value: 0.731
    true_std: 0.006
    value_gap_source_arxiv: '2506.19862'
    value_gap_source_title: 'DualEquiNet: A Dual-Space Hierarchical Equivariant Network
      for Large Biomolecules'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.731
    sort_std: 0.006
    is_best: false
  - model: GVPGNN
    model_key: gvpgnn
    model_plain: GVPGNN
    value: 0.736
    std: 0.003
    paper_value: 0.736
    paper_std: 0.003
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 6
    true_value: 0.736
    true_std: 0.003
    value_gap_source_arxiv: '2506.19862'
    value_gap_source_title: 'DualEquiNet: A Dual-Space Hierarchical Equivariant Network
      for Large Biomolecules'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.736
    sort_std: 0.003
    is_best: false
  - model: SchNet
    model_key: schnet
    model_plain: SchNet
    value: 0.737
    std: 0.002
    paper_value: 0.737
    paper_std: 0.002
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 7
    true_value: 0.737
    true_std: 0.002
    value_gap_source_arxiv: '2506.19862'
    value_gap_source_title: 'DualEquiNet: A Dual-Space Hierarchical Equivariant Network
      for Large Biomolecules'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.737
    sort_std: 0.002
    is_best: false
  metric: RMSE
  higher_is_better: false
- &id001
  dataset: TorsionAngle
  rows:
  - model: DualEquiNet
    model_key: dualequinet
    model_plain: DualEquiNet
    value: 15.87
    std: 2.03
    paper_value: 15.87
    paper_std: 2.03
    metric: Circular MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 1
    true_value: 15.87
    true_std: 2.03
    value_gap_source_arxiv: '2506.19862'
    value_gap_source_title: 'DualEquiNet: A Dual-Space Hierarchical Equivariant Network
      for Large Biomolecules'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 15.87
    sort_std: 2.03
    is_best: true
  - model: GotenNet
    model_key: gotennet
    model_plain: GotenNet
    value: 16.27
    std: 1.19
    paper_value: 16.27
    paper_std: 1.19
    metric: Circular MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 2
    true_value: 16.27
    true_std: 1.19
    value_gap_source_arxiv: '2506.19862'
    value_gap_source_title: 'DualEquiNet: A Dual-Space Hierarchical Equivariant Network
      for Large Biomolecules'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 16.27
    sort_std: 1.19
    is_best: true
  - model: GVPGNN
    model_key: gvpgnn
    model_plain: GVPGNN
    value: 17.56
    std: 0.21
    paper_value: 17.56
    paper_std: 0.21
    metric: Circular MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 3
    true_value: 17.56
    true_std: 0.21
    value_gap_source_arxiv: '2506.19862'
    value_gap_source_title: 'DualEquiNet: A Dual-Space Hierarchical Equivariant Network
      for Large Biomolecules'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 17.56
    sort_std: 0.21
    is_best: true
  - model: EGNN
    model_key: egnn
    model_plain: EGNN
    value: 18.41
    std: 0.22
    paper_value: 18.41
    paper_std: 0.22
    metric: Circular MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 4
    true_value: 18.41
    true_std: 0.22
    value_gap_source_arxiv: '2506.19862'
    value_gap_source_title: 'DualEquiNet: A Dual-Space Hierarchical Equivariant Network
      for Large Biomolecules'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 18.41
    sort_std: 0.22
    is_best: false
  - model: SchNet
    model_key: schnet
    model_plain: SchNet
    value: 18.54
    std: 0.86
    paper_value: 18.54
    paper_std: 0.86
    metric: Circular MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 5
    true_value: 18.54
    true_std: 0.86
    value_gap_source_arxiv: '2506.19862'
    value_gap_source_title: 'DualEquiNet: A Dual-Space Hierarchical Equivariant Network
      for Large Biomolecules'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 18.54
    sort_std: 0.86
    is_best: true
  - model: FastEGNN
    model_key: fastegnn
    model_plain: FastEGNN
    value: 18.89
    std: 0.22
    paper_value: 18.89
    paper_std: 0.22
    metric: Circular MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 6
    true_value: 18.89
    true_std: 0.22
    value_gap_source_arxiv: '2506.19862'
    value_gap_source_title: 'DualEquiNet: A Dual-Space Hierarchical Equivariant Network
      for Large Biomolecules'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 18.89
    sort_std: 0.22
    is_best: false
  - model: TFN
    model_key: tfn
    model_plain: TFN
    value: 21.97
    std: 0.45
    paper_value: 21.97
    paper_std: 0.45
    metric: Circular MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 7
    true_value: 21.97
    true_std: 0.45
    value_gap_source_arxiv: '2506.19862'
    value_gap_source_title: 'DualEquiNet: A Dual-Space Hierarchical Equivariant Network
      for Large Biomolecules'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 21.97
    sort_std: 0.45
    is_best: false
  metric: Circular MAE
  higher_is_better: false
results_grouped:
- benchmark: DualEquiNet RNA Benchmarks
  datasets:
  - *id001
  - *id002
  - *id003
  - *id004
single_proposed_model: DualEquiNet
main_figure: /figures/2506.19862/main_figure.png
---

