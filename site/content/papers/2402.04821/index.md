---
title: E(3)-Equivariant Mesh Neural Networks
arxiv_id: '2402.04821'
authors: []
published_date: '2024-02-07'
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
proposed_models: []
mrr: null
results:
- &id001
  dataset: D&D
  rows:
  - model: MPNN
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: HAC (BFS)
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: false
  - model: k-hop
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: SubdivNet
    value: 0.917
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hu 2022
    global_rank: 6
    is_best: false
  - model: DiffusionNet
    value: 0.903
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: DiffusionNet
    global_rank: 7
    is_best: false
  - model: Mesh-MLP
    value: 0.888
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: MeshMLP
    global_rank: 8
    is_best: false
  - model: EGNN+MC+Hier
    value: 0.887
    std: null
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
  - model: Laplacian2Mesh
    value: 0.886
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Laplacian2Mesh
    global_rank: 10
    is_best: false
  - model: PD-MeshNet
    value: 0.856
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Milano 2020
    global_rank: 12
    is_best: false
  - model: MeshCNN
    value: 0.854
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: MeshCNN
    global_rank: 13
    is_best: false
  - model: HodgeNet
    value: 0.85
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Smirnov 2021
    global_rank: 14
    is_best: false
  - model: EMNN+MC
    value: 0.835
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 17
    is_best: false
  - model: EGNN+MC
    value: 0.827
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 21
    is_best: false
  - model: PointNet++
    value: 0.823
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Qi 2016
    global_rank: 22
    is_best: false
  - model: EMNN
    value: 0.81
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 27
    is_best: false
  - model: EGNN
    value: 0.806
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: EGNN
    global_rank: 28
    is_best: false
  metric: Accuracy
  higher_is_better: true
results_grouped:
- benchmark: TU Dortmund
  datasets:
  - *id001
main_figure: /figures/2402.04821/main_figure.png
---

