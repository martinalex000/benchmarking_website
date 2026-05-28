---
title: E(3)-Equivariant Mesh Neural Networks
arxiv_id: '2402.04821'
source_url: ''
authors: []
published_date: Feb 7, 2024
published_date_iso: '2024-02-07'
abstract: Triangular meshes are widely used to represent three-dimensional objects.
  As a result, many recent works have address the need for geometric deep learning
  on 3D mesh. However, we observe that the complexities in many of these architectures
  does not translate to practical performance, and simple deep models for geometric
  graphs are competitive in practice. Motivated by this observation, we minimally
  extend the update equations of E(n)-Equivariant Graph Neural Networks (EGNNs) (Satorras
  et al., 2021) to incorporate mesh face information, and further improve it to account
  for long-range interactions through hierarchy. The resulting architecture, Equivariant
  Mesh Neural Network (EMNN), outperforms other, more complicated equivariant methods
  on mesh tasks, with a fast run-time and no expensive pre-processing. Our implementation
  is available at https://github.com/HySonLab/EquiMesh
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: dataset
proposed_models: []
mrr: null
adjusted_mrr: null
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
  - model: MPNN
    model_key: mpnn
    model_plain: MPNN
    value: 0.989
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.15671'
    title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence Models'
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.989
    sort_std: null
    is_best: true
  - model: HAC (BFS)
    model_key: hac (bfs)
    model_plain: HAC (BFS)
    value: 0.981
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.15671'
    title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence Models'
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.981
    sort_std: null
    is_best: false
  - model: k-hop
    model_key: k-hop
    model_plain: k-hop
    value: 0.976
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.15671'
    title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence Models'
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.976
    sort_std: null
    is_best: false
  - model: SubdivNet
    model_key: subdivnet
    model_plain: SubdivNet
    value: 0.917
    std: null
    paper_value: 0.917
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hu 2022
    variant_inference_reason: ''
    date: Feb 7, 2024
    date_display: Feb 2024
    date_iso: '2024-02-07'
    global_rank: 6
    true_value: 0.917
    true_std: null
    value_gap_source_arxiv: '2402.04821'
    value_gap_source_title: E(3)-Equivariant Mesh Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.917
    sort_std: null
    is_best: false
  - model: DiffusionNet
    model_key: diffusionnet
    model_plain: DiffusionNet
    value: 0.903
    std: null
    paper_value: 0.903
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: DiffusionNet
    variant_inference_reason: ''
    date: Feb 7, 2024
    date_display: Feb 2024
    date_iso: '2024-02-07'
    global_rank: 7
    true_value: 0.903
    true_std: null
    value_gap_source_arxiv: '2402.04821'
    value_gap_source_title: E(3)-Equivariant Mesh Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.903
    sort_std: null
    is_best: false
  - model: Mesh-MLP
    model_key: mesh-mlp
    model_plain: Mesh-MLP
    value: 0.888
    std: null
    paper_value: 0.888
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: MeshMLP
    variant_inference_reason: ''
    date: Feb 7, 2024
    date_display: Feb 2024
    date_iso: '2024-02-07'
    global_rank: 8
    true_value: 0.888
    true_std: null
    value_gap_source_arxiv: '2402.04821'
    value_gap_source_title: E(3)-Equivariant Mesh Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.888
    sort_std: null
    is_best: false
  - model: EGNN+MC+Hier
    model_key: egnn+mc+hier
    model_plain: EGNN+MC+Hier
    value: 0.887
    std: null
    paper_value: 0.887
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 7, 2024
    date_display: Feb 2024
    date_iso: '2024-02-07'
    global_rank: 9
    true_value: 0.887
    true_std: null
    value_gap_source_arxiv: '2402.04821'
    value_gap_source_title: E(3)-Equivariant Mesh Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.887
    sort_std: null
    is_best: false
  - model: Laplacian2Mesh
    model_key: laplacian2mesh
    model_plain: Laplacian2Mesh
    value: 0.886
    std: null
    paper_value: 0.886
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Laplacian2Mesh
    variant_inference_reason: ''
    date: Feb 7, 2024
    date_display: Feb 2024
    date_iso: '2024-02-07'
    global_rank: 10
    true_value: 0.886
    true_std: null
    value_gap_source_arxiv: '2402.04821'
    value_gap_source_title: E(3)-Equivariant Mesh Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.886
    sort_std: null
    is_best: false
  - model: PD-MeshNet
    model_key: pd-meshnet
    model_plain: PD-MeshNet
    value: 0.856
    std: null
    paper_value: 0.856
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Milano 2020
    variant_inference_reason: ''
    date: Feb 7, 2024
    date_display: Feb 2024
    date_iso: '2024-02-07'
    global_rank: 12
    true_value: 0.856
    true_std: null
    value_gap_source_arxiv: '2402.04821'
    value_gap_source_title: E(3)-Equivariant Mesh Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.856
    sort_std: null
    is_best: false
  - model: MeshCNN
    model_key: meshcnn
    model_plain: MeshCNN
    value: 0.854
    std: null
    paper_value: 0.854
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: MeshCNN
    variant_inference_reason: ''
    date: Feb 7, 2024
    date_display: Feb 2024
    date_iso: '2024-02-07'
    global_rank: 13
    true_value: 0.854
    true_std: null
    value_gap_source_arxiv: '2402.04821'
    value_gap_source_title: E(3)-Equivariant Mesh Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.854
    sort_std: null
    is_best: false
  - model: HodgeNet
    model_key: hodgenet
    model_plain: HodgeNet
    value: 0.85
    std: null
    paper_value: 0.85
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Smirnov 2021
    variant_inference_reason: ''
    date: Feb 7, 2024
    date_display: Feb 2024
    date_iso: '2024-02-07'
    global_rank: 14
    true_value: 0.85
    true_std: null
    value_gap_source_arxiv: '2402.04821'
    value_gap_source_title: E(3)-Equivariant Mesh Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.85
    sort_std: null
    is_best: false
  - model: EMNN+MC
    model_key: emnn+mc
    model_plain: EMNN+MC
    value: 0.835
    std: null
    paper_value: 0.835
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 7, 2024
    date_display: Feb 2024
    date_iso: '2024-02-07'
    global_rank: 17
    true_value: 0.835
    true_std: null
    value_gap_source_arxiv: '2402.04821'
    value_gap_source_title: E(3)-Equivariant Mesh Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.835
    sort_std: null
    is_best: false
  - model: EGNN+MC
    model_key: egnn+mc
    model_plain: EGNN+MC
    value: 0.827
    std: null
    paper_value: 0.827
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 7, 2024
    date_display: Feb 2024
    date_iso: '2024-02-07'
    global_rank: 21
    true_value: 0.827
    true_std: null
    value_gap_source_arxiv: '2402.04821'
    value_gap_source_title: E(3)-Equivariant Mesh Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.827
    sort_std: null
    is_best: false
  - model: PointNet++
    model_key: pointnet++
    model_plain: PointNet++
    value: 0.823
    std: null
    paper_value: 0.823
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Qi 2016
    variant_inference_reason: ''
    date: Feb 7, 2024
    date_display: Feb 2024
    date_iso: '2024-02-07'
    global_rank: 22
    true_value: 0.823
    true_std: null
    value_gap_source_arxiv: '2402.04821'
    value_gap_source_title: E(3)-Equivariant Mesh Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.823
    sort_std: null
    is_best: false
  - model: EMNN
    model_key: emnn
    model_plain: EMNN
    value: 0.81
    std: null
    paper_value: 0.81
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 7, 2024
    date_display: Feb 2024
    date_iso: '2024-02-07'
    global_rank: 27
    true_value: 0.81
    true_std: null
    value_gap_source_arxiv: '2402.04821'
    value_gap_source_title: E(3)-Equivariant Mesh Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 27
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.81
    sort_std: null
    is_best: false
  - model: EGNN
    model_key: egnn
    model_plain: EGNN
    value: 0.806
    std: null
    paper_value: 0.806
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: EGNN
    variant_inference_reason: ''
    date: Feb 7, 2024
    date_display: Feb 2024
    date_iso: '2024-02-07'
    global_rank: 28
    true_value: 0.806
    true_std: null
    value_gap_source_arxiv: '2402.04821'
    value_gap_source_title: E(3)-Equivariant Mesh Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 28
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.806
    sort_std: null
    is_best: false
  metric: Accuracy
  higher_is_better: true
results_grouped:
- benchmark: TU Dortmund
  datasets:
  - *id001
main_figure: /figures/2402.04821/main_figure.png
---

