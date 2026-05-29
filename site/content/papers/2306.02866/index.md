---
title: Learning Probabilistic Symmetrization for Architecture Agnostic Equivariance
arxiv_id: '2306.02866'
source_url: ''
authors: []
published_date: Jun 2023
published_date_iso: 2023-06
abstract: We present a novel framework to overcome the limitations of equivariant
  architectures in learning functions with group symmetries. In contrary to equivariant
  architectures, we use an arbitrary base model such as an MLP or a transformer and
  symmetrize it to be equivariant to the given group by employing a small equivariant
  network that parameterizes the probabilistic distribution underlying the symmetrization.
  The distribution is end-to-end trained with the base model which can maximize performance
  while reducing sample complexity of symmetrization. We show that this approach ensures
  not only equivariance to given group but also universal approximation capability
  in expectation. We implement our method on various base models, including patch-based
  transformers that can be initialized from pretrained vision transformers, and test
  them for a wide range of symmetry groups including permutation and Euclidean groups
  and their combinations. Empirical tests show competitive results against tailored
  equivariant architectures, suggesting the potential for learning equivariant functions
  for diverse groups using a non-equivariant universal base architecture. We further
  show evidence of enhanced learning in symmetric modalities, like graphs, when pretrained
  from non-symmetric modalities, like vision. Code is available at.
codebase_url: https://github.com/jw9730/lps
extraction_model: Qwen/Qwen3.6-35B-A3B-FP8
has_results: true
paper_type: dataset
proposed_models: []
mrr: null
adjusted_mrr: null
mrr_dataset_count: 0
benchmark_categories:
- TU Dortmund
- LRGB
- GNNBenchmark
task_categories:
- graph_classification
- graph_regression
- link_prediction
- node_classification
experiment_scopes:
- edge-level
- graph-level
- node-level
results:
- &id001
  dataset: D&D
  rows:
  - model: GPS+Transformer
    model_key: gps+transformer
    model_plain: GPS+Transformer
    value: 0.00401
    std: 1.0e-05
    paper_value: 0.00401
    paper_std: 1.0e-05
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: null
    sort_value: 0.00401
    sort_std: 1.0e-05
    is_best: true
  - model: GNN-Canonical
    model_key: gnn-canonical
    model_plain: GNN-Canonical
    value: 0.0043
    std: null
    paper_value: 0.0043
    paper_std: null
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kaba et al. 2022
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: null
    sort_value: 0.0043
    sort_std: null
    is_best: false
  - model: Transformer-Canonical
    model_key: transformer-canonical
    model_plain: Transformer-Canonical
    value: 0.00508
    std: null
    paper_value: 0.00508
    paper_std: null
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: null
    sort_value: 0.00508
    sort_std: null
    is_best: false
  - model: GNN-FA
    model_key: gnn-fa
    model_plain: GNN-FA
    value: 0.0057
    std: null
    paper_value: 0.0057
    paper_std: null
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Puny et al. 2022
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: null
    sort_value: 0.0057
    sort_std: null
    is_best: false
  - model: EGNN
    model_key: egnn
    model_plain: EGNN
    value: 0.0071
    std: null
    paper_value: 0.0071
    paper_std: null
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Satorras et al. 2021
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: null
    sort_value: 0.0071
    sort_std: null
    is_best: false
  - model: Radial Field
    model_key: radial field
    model_plain: Radial Field
    value: 0.0104
    std: null
    paper_value: 0.0104
    paper_std: null
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kohler et al. 2019
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: null
    sort_value: 0.0104
    sort_std: null
    is_best: false
  - model: TFN
    model_key: tfn
    model_plain: TFN
    value: 0.0155
    std: null
    paper_value: 0.0155
    paper_std: null
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Thomas et al. 2018
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: null
    sort_value: 0.0155
    sort_std: null
    is_best: false
  - model: SE(3)-Transformer
    model_key: se(3)-transformer
    model_plain: SE(3)-Transformer
    value: 0.0244
    std: null
    paper_value: 0.0244
    paper_std: null
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Fuchs et al. 2020
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: null
    sort_value: 0.0244
    sort_std: null
    is_best: false
  - model: KNN graph-convolution
    model_key: knn graph-convolution
    model_plain: KNN graph-convolution
    value: 0.58
    std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1703.06114'
    title: Deep Sets
    date: Mar 2017
    date_display: Mar 2017
    date_iso: 2017-03
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.58
    sort_std: 0.02
    is_best: false
  - model: MMGCN + ImageBind/ImageBind
    model_key: mmgcn + imagebind/imagebind
    model_plain: MMGCN + ImageBind/ImageBind
    value: 0.5875
    std: 0.0005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.16321'
    title: 'Mosaic of Modalities: A Comprehensive Benchmark for Multimodal Graph Learning'
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: true
    is_global_top: true
    global_rank: 2
    sort_value: 0.5875
    sort_std: 0.0005
    is_best: false
  - model: DGCNN(L8)
    model_key: dgcnn(l8)
    model_plain: DGCNN(L8)
    value: 0.6163
    std: 0.0533
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.08671'
    title: Search to Capture Long-range Dependency with Stacking GNNs for Graph Classification
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    codebase_url: https://github.com/LARS-research/LRGNN
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.6163
    sort_std: 0.0533
    is_best: false
  metric: Accuracy
  higher_is_better: false
- &id005
  dataset: PATTERN
  rows:
  - model: DGN
    model_key: dgn
    model_plain: DGN
    value: 0.96
    std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.02863'
    title: Directional Graph Networks
    date: Oct 2020
    date_display: Oct 2020
    date_iso: 2020-10
    codebase_url: https://github.com/Saro00/DGN
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.96
    sort_std: 0.002
    is_best: true
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.93
    std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.02863'
    title: Directional Graph Networks
    date: Oct 2020
    date_display: Oct 2020
    date_iso: 2020-10
    codebase_url: https://github.com/Saro00/DGN
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.93
    sort_std: 0.002
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.92
    std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.02863'
    title: Directional Graph Networks
    date: Oct 2020
    date_display: Oct 2020
    date_iso: 2020-10
    codebase_url: https://github.com/Saro00/DGN
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.92
    sort_std: 0.003
    is_best: false
  - model: RingGNN, 2 layers
    model_key: ringgnn, 2 layers
    model_plain: RingGNN, 2 layers
    value: 0.86245
    std: null
    paper_value: 0.86245
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Dwivedi et al. 2020
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 31
    true_value: 0.86245
    true_std: null
    value_gap_source_arxiv: '2306.02866'
    value_gap_source_title: Learning Probabilistic Symmetrization for Architecture
      Agnostic Equivariance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.86245
    sort_std: null
    is_best: false
  - model: ViT-PS (Ours), 10-sample
    model_key: vit-ps (ours), 10-sample
    model_plain: ViT-PS (Ours), 10-sample
    value: 0.85989
    std: 0.00011
    paper_value: 0.85989
    paper_std: 0.00011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 33
    true_value: 0.85989
    true_std: 0.00011
    value_gap_source_arxiv: '2306.02866'
    value_gap_source_title: Learning Probabilistic Symmetrization for Architecture
      Agnostic Equivariance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.85989
    sort_std: 0.00011
    is_best: false
  - model: ViT-Canonical
    model_key: vit-canonical
    model_plain: ViT-Canonical
    value: 0.85825
    std: null
    paper_value: 0.85825
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 34
    true_value: 0.85825
    true_std: null
    value_gap_source_arxiv: '2306.02866'
    value_gap_source_title: Learning Probabilistic Symmetrization for Architecture
      Agnostic Equivariance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 34
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.85825
    sort_std: null
    is_best: false
  - model: PPGN, 3 layers
    model_key: ppgn, 3 layers
    model_plain: PPGN, 3 layers
    value: 0.85661
    std: null
    paper_value: 0.85661
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Dwivedi et al. 2020
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 35
    true_value: 0.85661
    true_std: null
    value_gap_source_arxiv: '2306.02866'
    value_gap_source_title: Learning Probabilistic Symmetrization for Architecture
      Agnostic Equivariance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.85661
    sort_std: null
    is_best: false
  - model: GatedGCN, 16 layers
    model_key: gatedgcn, 16 layers
    model_plain: GatedGCN, 16 layers
    value: 0.85568
    std: null
    paper_value: 0.85568
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Dwivedi et al. 2020
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 37
    true_value: 0.85568
    true_std: null
    value_gap_source_arxiv: '2306.02866'
    value_gap_source_title: Learning Probabilistic Symmetrization for Architecture
      Agnostic Equivariance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 37
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.85568
    sort_std: null
    is_best: false
  - model: GCN, 16 layers
    model_key: gcn, 16 layers
    model_plain: GCN, 16 layers
    value: 0.85387
    std: null
    paper_value: 0.85387
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Dwivedi et al. 2020
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 39
    true_value: 0.85387
    true_std: null
    value_gap_source_arxiv: '2306.02866'
    value_gap_source_title: Learning Probabilistic Symmetrization for Architecture
      Agnostic Equivariance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.85387
    sort_std: null
    is_best: false
  - model: ViT-GA, 10-sample
    model_key: vit-ga, 10-sample
    model_plain: ViT-GA, 10-sample
    value: 0.8322
    std: 0.00057
    paper_value: 0.8322
    paper_std: 0.00057
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 43
    true_value: 0.8322
    true_std: 0.00057
    value_gap_source_arxiv: '2306.02866'
    value_gap_source_title: Learning Probabilistic Symmetrization for Architecture
      Agnostic Equivariance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 43
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8322
    sort_std: 0.00057
    is_best: false
  - model: GAT, 16 layers
    model_key: gat, 16 layers
    model_plain: GAT, 16 layers
    value: 0.78271
    std: null
    paper_value: 0.78271
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Dwivedi et al. 2020
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 44
    true_value: 0.78271
    true_std: null
    value_gap_source_arxiv: '2306.02866'
    value_gap_source_title: Learning Probabilistic Symmetrization for Architecture
      Agnostic Equivariance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 44
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.78271
    sort_std: null
    is_best: false
  - model: ViT-FA
    model_key: vit-fa
    model_plain: ViT-FA
    value: 0.71377
    std: null
    paper_value: 0.71377
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 46
    true_value: 0.71377
    true_std: null
    value_gap_source_arxiv: '2306.02866'
    value_gap_source_title: Learning Probabilistic Symmetrization for Architecture
      Agnostic Equivariance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 46
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.71377
    sort_std: null
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: PCQM-Contact
  rows:
  - model: ViT-PS
    model_key: vit-ps
    model_plain: ViT-PS
    value: 0.5341
    std: null
    paper_value: 0.5341
    paper_std: null
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 1
    true_value: 0.5341
    true_std: null
    value_gap_source_arxiv: '2306.02866'
    value_gap_source_title: Learning Probabilistic Symmetrization for Architecture
      Agnostic Equivariance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5341
    sort_std: null
    is_best: true
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.3637
    std: null
    paper_value: 0.3637
    paper_std: null
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Shirzad 2023
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 2
    true_value: 0.3637
    true_std: 0.002
    value_gap_source_arxiv: '2303.06147'
    value_gap_source_title: 'Exphormer: Sparse Transformers for Graphs'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3637
    sort_std: 0.002
    is_best: false
  - model: SGT
    model_key: sgt
    model_plain: SGT
    value: 0.345
    std: 0.0002
    metric: MRR
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    codebase_url: https://github.com/liun-online/WaveGC
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.345
    sort_std: 0.0002
    is_best: false
  - model: GPS+Transformer
    model_key: gps+transformer
    model_plain: GPS+Transformer
    value: 0.3442
    std: 0.0009
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.286725
    arxiv_id: '2402.00789'
    title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling with Selective
      State Spaces'
    date: Feb 1, 2024
    date_display: Feb 2024
    date_iso: '2024-02-01'
    codebase_url: https://github.com/bowang-lab/Graph-Mamba
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.3442
    sort_std: 0.0009
    is_best: false
  - model: GPS+Performer
    model_key: gps+performer
    model_plain: GPS+Performer
    value: 0.3437
    std: 0.0005
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.00789'
    title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling with Selective
      State Spaces'
    date: Feb 1, 2024
    date_display: Feb 2024
    date_iso: '2024-02-01'
    codebase_url: https://github.com/bowang-lab/Graph-Mamba
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    sort_value: 0.3437
    sort_std: 0.0005
    is_best: false
  - model: SAN+LapPE
    model_key: san+lappe
    model_plain: SAN+LapPE
    value: 0.335
    std: null
    paper_value: 0.335
    paper_std: null
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kreuzer 2021
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 13
    true_value: 0.335
    true_std: 0.0003
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.335
    sort_std: 0.0003
    is_best: false
  - model: SAN+RWSE
    model_key: san+rwse
    model_plain: SAN+RWSE
    value: 0.3341
    std: null
    paper_value: 0.3341
    paper_std: null
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kreuzer 2021
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 14
    true_value: 0.3341
    true_std: 0.0006
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3341
    sort_std: 0.0006
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.3337
    std: null
    paper_value: 0.3337
    paper_std: null
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Rampasek 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 16
    true_value: 0.3337
    true_std: 0.0006
    value_gap_source_arxiv: '2303.06147'
    value_gap_source_title: 'Exphormer: Sparse Transformers for Graphs'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3337
    sort_std: 0.0006
    is_best: false
  - model: GatedGCN+RWSE
    model_key: gatedgcn+rwse
    model_plain: GatedGCN+RWSE
    value: 0.3242
    std: null
    paper_value: 0.3242
    paper_std: null
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Bresson 2017
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 20
    true_value: 0.3242
    true_std: 0.0008
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3242
    sort_std: 0.0008
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.3234
    std: null
    paper_value: 0.3234
    paper_std: null
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kipf 2017
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 21
    true_value: 0.3234
    true_std: 0.0006
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3234
    sort_std: 0.0006
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.3218
    std: null
    paper_value: 0.3218
    paper_std: null
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Bresson 2017
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 22
    true_value: 0.3218
    true_std: 0.0011
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3218
    sort_std: 0.0011
    is_best: false
  - model: GINE
    model_key: gine
    model_plain: GINE
    value: 0.318
    std: null
    paper_value: 0.318
    paper_std: null
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hu 2020
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 23
    true_value: 0.318
    true_std: 0.0027
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.318
    sort_std: 0.0027
    is_best: false
  - model: Transformer+LapPE
    model_key: transformer+lappe
    model_plain: Transformer+LapPE
    value: 0.3174
    std: null
    paper_value: 0.3174
    paper_std: null
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Dwivedi 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 25
    true_value: 0.3174
    true_std: 0.002
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3174
    sort_std: 0.002
    is_best: false
  - model: GCNII
    model_key: gcnii
    model_plain: GCNII
    value: 0.3161
    std: null
    paper_value: 0.3161
    paper_std: null
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Chen 2020
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 26
    true_value: 0.3161
    true_std: 0.0004
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3161
    sort_std: 0.0004
    is_best: false
  metric: MRR
  higher_is_better: true
- &id003
  dataset: Peptides-func
  rows:
  - model: S2GCN +PE
    model_key: s2gcn +pe
    model_plain: S2GCN +PE
    value: 0.7311
    std: 0.0066
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.7311
    sort_std: 0.0066
    is_best: true
  - model: S2GCN
    model_key: s2gcn
    model_plain: S2GCN
    value: 0.7275
    std: 0.0066
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.7275
    sort_std: 0.0066
    is_best: true
  - model: LRDs
    model_key: lrds
    model_plain: LRDs
    value: 0.7182
    std: 0.0024
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.00282'
    title: 'GraphMinNet: Learning Dependencies in Graphs with Light Complexity Minimal
      Architecture'
    date: Feb 1, 2025
    date_display: Feb 2025
    date_iso: '2025-02-01'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.7182
    sort_std: 0.0024
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.593
    std: null
    paper_value: 0.593
    paper_std: null
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kipf 2017
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 28
    true_value: 0.686
    true_std: 0.005
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09300000000000008
    value_note: ''
    paper_rank: 78
    rank_delta: 50
    rank_delta_abs: 50
    rank_delta_direction: worse
    sort_value: 0.686
    sort_std: 0.005
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.5864
    std: null
    paper_value: 0.5864
    paper_std: null
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Bresson 2017
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 35
    true_value: 0.6765
    true_std: 0.0047
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09009999999999996
    value_note: ''
    paper_rank: 78
    rank_delta: 43
    rank_delta_abs: 43
    rank_delta_direction: worse
    sort_value: 0.6765
    sort_std: 0.0047
    is_best: false
  - model: GINE
    model_key: gine
    model_plain: GINE
    value: 0.5498
    std: null
    paper_value: 0.5498
    paper_std: null
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hu 2020
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 45
    true_value: 0.6621
    true_std: 0.0067
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11230000000000007
    value_note: ''
    paper_rank: 83
    rank_delta: 38
    rank_delta_abs: 38
    rank_delta_direction: worse
    sort_value: 0.6621
    sort_std: 0.0067
    is_best: false
  - model: ViT-PS
    model_key: vit-ps
    model_plain: ViT-PS
    value: 0.6575
    std: null
    paper_value: 0.6575
    paper_std: null
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 48
    true_value: 0.6575
    true_std: null
    value_gap_source_arxiv: '2306.02866'
    value_gap_source_title: Learning Probabilistic Symmetrization for Architecture
      Agnostic Equivariance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 48
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6575
    sort_std: null
    is_best: false
  - model: SAN+RWSE
    model_key: san+rwse
    model_plain: SAN+RWSE
    value: 0.6439
    std: null
    paper_value: 0.6439
    paper_std: null
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kreuzer 2021
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 51
    true_value: 0.6562
    true_std: 0.0075
    value_gap_source_arxiv: '2302.08647'
    value_gap_source_title: Multiresolution Graph Transformers and Wavelet Positional
      Encoding for Learning Hierarchical Structures
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.012299999999999978
    value_note: ''
    paper_rank: 63
    rank_delta: 12
    rank_delta_abs: 12
    rank_delta_direction: worse
    sort_value: 0.6562
    sort_std: 0.0075
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.6535
    std: null
    paper_value: 0.6535
    paper_std: null
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Rampasek 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 53
    true_value: 0.6535
    true_std: 0.0041
    value_gap_source_arxiv: '2502.00282'
    value_gap_source_title: 'GraphMinNet: Learning Dependencies in Graphs with Light
      Complexity Minimal Architecture'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 53
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6535
    sort_std: 0.0041
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.6527
    std: null
    paper_value: 0.6527
    paper_std: null
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Shirzad 2023
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 58
    true_value: 0.6527
    true_std: 0.0043
    value_gap_source_arxiv: '2502.00282'
    value_gap_source_title: 'GraphMinNet: Learning Dependencies in Graphs with Light
      Complexity Minimal Architecture'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 58
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6527
    sort_std: 0.0043
    is_best: false
  - model: SAN+LapPE
    model_key: san+lappe
    model_plain: SAN+LapPE
    value: 0.6384
    std: null
    paper_value: 0.6384
    paper_std: null
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kreuzer 2021
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 67
    true_value: 0.6384
    true_std: 0.0121
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 67
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6384
    sort_std: 0.0121
    is_best: false
  - model: Transformer+LapPE
    model_key: transformer+lappe
    model_plain: Transformer+LapPE
    value: 0.6326
    std: null
    paper_value: 0.6326
    paper_std: null
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Dwivedi 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 69
    true_value: 0.6326
    true_std: 0.0126
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 69
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6326
    sort_std: 0.0126
    is_best: false
  - model: GatedGCN+RWSE
    model_key: gatedgcn+rwse
    model_plain: GatedGCN+RWSE
    value: 0.6069
    std: null
    paper_value: 0.6069
    paper_std: null
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Bresson 2017
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 75
    true_value: 0.6069
    true_std: 0.0035
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 75
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6069
    sort_std: 0.0035
    is_best: false
  - model: GCNII
    model_key: gcnii
    model_plain: GCNII
    value: 0.5543
    std: null
    paper_value: 0.5543
    paper_std: null
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Chen 2020
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 83
    true_value: 0.5543
    true_std: 0.0078
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 83
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5543
    sort_std: 0.0078
    is_best: false
  metric: AP
  higher_is_better: true
- &id002
  dataset: Peptides-struct
  rows:
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
    global_rank: 1
    sort_value: 0.2422
    sort_std: 0.0014
    is_best: true
  - model: B-PEARL+SRF
    model_key: b-pearl+srf
    model_plain: B-PEARL+SRF
    value: 0.243
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.03824'
    title: Sketch-Augmented Features Improve Learning Long-Range Dependencies in Graph
      Neural Networks
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    codebase_url: https://github.com/ryienh/sketched-random-features
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.243
    sort_std: null
    is_best: true
  - model: GRAMA
    model_key: grama
    model_plain: GRAMA
    value: 0.2436
    std: 0.0022
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: null
    is_global_top: true
    global_rank: 3
    sort_value: 0.2436
    sort_std: 0.0022
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.3496
    std: null
    paper_value: 0.3496
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kipf 2017
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 14
    true_value: 0.246
    true_std: 0.0007
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10360000000000003
    value_note: ''
    paper_rank: 94
    rank_delta: 80
    rank_delta_abs: 80
    rank_delta_direction: worse
    sort_value: 0.246
    sort_std: 0.0007
    is_best: false
  - model: GINE
    model_key: gine
    model_plain: GINE
    value: 0.3547
    std: null
    paper_value: 0.3547
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hu 2020
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 22
    true_value: 0.2473
    true_std: 0.0017
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10740000000000002
    value_note: ''
    paper_rank: 94
    rank_delta: 72
    rank_delta_abs: 72
    rank_delta_direction: worse
    sort_value: 0.2473
    sort_std: 0.0017
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.342
    std: null
    paper_value: 0.342
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Bresson 2017
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 31
    true_value: 0.2477
    true_std: 0.0009
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09430000000000002
    value_note: ''
    paper_rank: 93
    rank_delta: 62
    rank_delta_abs: 62
    rank_delta_direction: worse
    sort_value: 0.2477
    sort_std: 0.0009
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.2481
    std: null
    paper_value: 0.2481
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Shirzad 2023
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 37
    true_value: 0.2481
    true_std: 0.0007
    value_gap_source_arxiv: '2502.00282'
    value_gap_source_title: 'GraphMinNet: Learning Dependencies in Graphs with Light
      Complexity Minimal Architecture'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 37
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2481
    sort_std: 0.0007
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.25
    std: null
    paper_value: 0.25
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Rampasek 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 45
    true_value: 0.25
    true_std: 0.0005
    value_gap_source_arxiv: '2502.00282'
    value_gap_source_title: 'GraphMinNet: Learning Dependencies in Graphs with Light
      Complexity Minimal Architecture'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 45
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.25
    sort_std: 0.0005
    is_best: false
  - model: Transformer+LapPE
    model_key: transformer+lappe
    model_plain: Transformer+LapPE
    value: 0.2529
    std: null
    paper_value: 0.2529
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Dwivedi 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 55
    true_value: 0.2529
    true_std: 0.0016
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 55
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2529
    sort_std: 0.0016
    is_best: false
  - model: SAN+RWSE
    model_key: san+rwse
    model_plain: SAN+RWSE
    value: 0.2545
    std: null
    paper_value: 0.2545
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kreuzer 2021
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 64
    true_value: 0.2545
    true_std: 0.0012
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 64
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2545
    sort_std: 0.0012
    is_best: false
  - model: ViT-PS
    model_key: vit-ps
    model_plain: ViT-PS
    value: 0.2559
    std: null
    paper_value: 0.2559
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 67
    true_value: 0.2559
    true_std: null
    value_gap_source_arxiv: '2306.02866'
    value_gap_source_title: Learning Probabilistic Symmetrization for Architecture
      Agnostic Equivariance
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 67
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2559
    sort_std: null
    is_best: false
  - model: SAN+LapPE
    model_key: san+lappe
    model_plain: SAN+LapPE
    value: 0.2683
    std: null
    paper_value: 0.2683
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kreuzer 2021
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 78
    true_value: 0.268
    true_std: 0.004
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.00029999999999996696
    value_note: global 0.2680 within std
    paper_rank: 78
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.268
    sort_std: 0.004
    is_best: false
  - model: GatedGCN+RWSE
    model_key: gatedgcn+rwse
    model_plain: GatedGCN+RWSE
    value: 0.3357
    std: null
    paper_value: 0.3357
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Bresson 2017
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 92
    true_value: 0.3357
    true_std: 0.0006
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 92
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3357
    sort_std: 0.0006
    is_best: false
  - model: GCNII
    model_key: gcnii
    model_plain: GCNII
    value: 0.3471
    std: null
    paper_value: 0.3471
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Chen 2020
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 94
    true_value: 0.3471
    true_std: 0.001
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 94
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3471
    sort_std: 0.001
    is_best: false
  metric: MAE
  higher_is_better: false
results_grouped:
- benchmark: TU Dortmund
  datasets:
  - *id001
- benchmark: LRGB
  datasets:
  - *id002
  - *id003
  - *id004
- benchmark: GNNBenchmark
  datasets:
  - *id005
main_figure: /figures/2306.02866/main_figure.png
---

