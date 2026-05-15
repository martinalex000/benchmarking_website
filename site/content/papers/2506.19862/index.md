---
title: DualEquiNet RNA Benchmarks
arxiv_id: '2506.19862'
authors: []
published_date: Jun 2025
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
extraction_model: qwen3.6-35b-a3b
has_results: true
proposed_models:
- DualEquiNet
mrr: 0.0
results:
- &id001
  dataset: COVID
  rows:
  - model: DualEquiNet
    value: 0.353
    std: 0.006
    metric: RMSE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 1
    is_best: true
  - model: w/o CSIP
    value: 0.356
    std: 0.002
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 2
    is_best: true
  - model: w/o CSIP/Cross
    value: 0.356
    std: 0.013
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 3
    is_best: true
  - model: w/o CSIP/Cross/Dual
    value: 0.362
    std: 0.01
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 4
    is_best: true
  - model: GotenNet
    value: 0.475
    std: 0.009
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 5
    is_best: false
  - model: FastEGNN
    value: 0.478
    std: 0.031
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 6
    is_best: false
  - model: GVPGNN
    value: 0.531
    std: 0.011
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 7
    is_best: false
  - model: HGNN
    value: 0.533
    std: 0.011
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 8
    is_best: false
  - model: SchNet
    value: 0.534
    std: 0.011
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 9
    is_best: false
  - model: EGNN
    value: 0.535
    std: 0.011
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 10
    is_best: false
  - model: TFN
    value: 0.535
    std: 0.011
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 11
    is_best: false
  metric: RMSE
  higher_is_better: false
- &id002
  dataset: Ribonanza
  rows:
  - model: DualEquiNet
    value: 0.558
    std: 0.012
    metric: RMSE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 1
    is_best: true
  - model: w/o CSIP
    value: 0.586
    std: 0.016
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 2
    is_best: true
  - model: w/o CSIP/Cross
    value: 0.591
    std: 0.081
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 3
    is_best: true
  - model: w/o CSIP/Cross/Dual
    value: 0.592
    std: 0.028
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 4
    is_best: true
  - model: FastEGNN
    value: 0.839
    std: 0.02
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 5
    is_best: false
  - model: GotenNet
    value: 0.857
    std: 0.013
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 6
    is_best: false
  - model: GVPGNN
    value: 0.932
    std: 0.01
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 7
    is_best: false
  - model: HGNN
    value: 0.934
    std: 0.01
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 8
    is_best: false
  - model: SchNet
    value: 0.937
    std: 0.012
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 9
    is_best: false
  - model: TFN
    value: 0.939
    std: 0.012
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 10
    is_best: false
  - model: EGNN
    value: 0.94
    std: 0.012
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 11
    is_best: false
  metric: RMSE
  higher_is_better: false
- &id003
  dataset: Tc-Ribo
  rows:
  - model: DualEquiNet
    value: 0.636
    std: 0.049
    metric: RMSE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 1
    is_best: true
  - model: w/o CSIP
    value: 0.682
    std: 0.026
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 2
    is_best: true
  - model: TFN
    value: 0.694
    std: 0.008
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 3
    is_best: false
  - model: w/o CSIP/Cross
    value: 0.698
    std: 0.01
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 4
    is_best: false
  - model: w/o CSIP/Cross/Dual
    value: 0.699
    std: 0.01
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 5
    is_best: false
  - model: GotenNet
    value: 0.718
    std: 0.002
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 6
    is_best: false
  - model: EGNN
    value: 0.72
    std: 0.022
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 7
    is_best: false
  - model: HGNN
    value: 0.729
    std: 0.007
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 8
    is_best: false
  - model: FastEGNN
    value: 0.731
    std: 0.006
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 9
    is_best: false
  - model: GVPGNN
    value: 0.736
    std: 0.003
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 10
    is_best: false
  - model: SchNet
    value: 0.737
    std: 0.002
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 11
    is_best: false
  metric: RMSE
  higher_is_better: false
- &id004
  dataset: TorsionAngle
  rows:
  - model: DualEquiNet
    value: 15.87
    std: 2.03
    metric: Circular MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 1
    is_best: true
  - model: GotenNet
    value: 16.27
    std: 1.19
    metric: Circular MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 2
    is_best: true
  - model: GVPGNN
    value: 17.56
    std: 0.21
    metric: Circular MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 3
    is_best: true
  - model: EGNN
    value: 17.79
    std: 0.61
    metric: Circular MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 4
    is_best: true
  - model: HGNN
    value: 18.41
    std: 0.22
    metric: Circular MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 5
    is_best: false
  - model: SchNet
    value: 18.54
    std: 0.86
    metric: Circular MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 6
    is_best: true
  - model: FastEGNN
    value: 18.89
    std: 0.22
    metric: Circular MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 7
    is_best: false
  - model: TFN
    value: 21.97
    std: 0.45
    metric: Circular MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 8
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

