---
title: 'Range-aware Positional Encoding via High-order Pretraining: Theory and Practice'
arxiv_id: '2409.19117'
source_url: ''
authors: []
published_date: Sep 2024
published_date_iso: 2024-09
abstract: Unsupervised pre-training on vast amounts of graph data is critical in real-world
  applications wherein labeled data is limited, such as molecule properties prediction
  or materials science. Existing approaches pre-train models for specific graph domains,
  neglecting the inherent connections within networks. This limits their ability to
  transfer knowledge to various supervised tasks. In this work, we propose a novel
  pre-training strategy on graphs that focuses on modeling their multi-resolution
  structural information, allowing us to capture global information of the whole graph
  while preserving local structures around its nodes. We extend the work of Wavelet
  Positional Encoding (WavePE) from 10.1063/5.0152833 by pretraining a High-Order
  Permutation-Equivariant Autoencoder (HOPE-WavePE) to reconstruct node connectivities
  from their multi-resolution wavelet signals. Unlike existing positional encodings,
  our method is designed to become sensitivity to the input graph size in downstream
  tasks, which efficiently capture global structure on graphs. Since our approach
  relies solely on the graph structure, it is also domain-agnostic and adaptable to
  datasets from various domains, therefore paving the wave for developing general
  graph structure encoders and graph foundation models. We theoretically demonstrate
  that there exists a parametrization of such architecture that it can predict the
  output adjacency up to arbitrarily low error. We also evaluate HOPE-WavePE on graph-level
  prediction tasks of different areas and show its superiority compared to other methods.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- MPNN + HOPE-WavePE
- GatedGCN + VN + HOPE-WavePE
- GIN + HOPE-WavePE
- GPS + HOPE-WavePE
- HOPE-WavePE
mrr: 0.2797
adjusted_mrr: 0.2797
mrr_dataset_count: 5
benchmark_categories:
- Classic
- LRGB
- TU Dortmund
- GNNBenchmark
- OGB
- MoleculeNet
task_categories:
- graph_classification
- graph_regression
- link_prediction
experiment_scopes:
- edge-level
- graph-level
results:
- &id012
  dataset: BACE
  rows:
  - model: MPNN + HOPE-WavePE
    model_key: mpnn + hope-wavepe
    model_plain: MPNN + HOPE-WavePE
    value: 0.868
    std: 0.004
    paper_value: 0.868
    paper_std: 0.004
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 1
    true_value: 0.868
    true_std: 0.004
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.868
    sort_std: 0.004
    is_best: true
  - model: BiScale-GTR (Molecule)
    model_key: biscale-gtr (molecule)
    model_plain: BiScale-GTR (Molecule)
    value: 0.85
    std: 0.011
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.06336'
    title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale Molecular
      Representation Learning'
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    codebase_url: ''
    uses_external_data: true
    is_global_top: true
    global_rank: 2
    sort_value: 0.85
    sort_std: 0.011
    is_best: false
  - model: Subgraphormer
    model_key: subgraphormer
    model_plain: Subgraphormer
    value: 0.8435
    std: 0.0065
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.293
    arxiv_id: '2402.08450'
    title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via Graph
      Products'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.8435
    sort_std: 0.0065
    is_best: false
  - model: SimSGT
    model_key: simsgt
    model_plain: SimSGT
    value: 0.843
    std: 0.006
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.06336'
    title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale Molecular
      Representation Learning'
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    codebase_url: ''
    uses_external_data: true
    is_global_top: true
    global_rank: 4
    sort_value: 0.843
    sort_std: 0.006
    is_best: false
  - model: GROVERbase
    model_key: groverbase
    model_plain: GROVERbase
    value: 0.826
    std: 0.007
    paper_value: 0.826
    paper_std: 0.007
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: GROVER
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 10
    true_value: 0.826
    true_std: 0.007
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.826
    sort_std: 0.007
    is_best: false
  - model: GROVER_large
    model_key: grover_large
    model_plain: GROVER_large
    value: 0.81
    std: 0.014
    paper_value: 0.81
    paper_std: 0.014
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: GROVER
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 15
    true_value: 0.81
    true_std: 0.014
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.81
    sort_std: 0.014
    is_best: false
  - model: D-MPNN
    model_key: d-mpnn
    model_plain: D-MPNN
    value: 0.809
    std: 0.006
    paper_value: 0.809
    paper_std: 0.006
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: yang2019analyzing
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 16
    true_value: 0.809
    true_std: 0.006
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.809
    sort_std: 0.006
    is_best: false
  - model: PretrainGNN
    model_key: pretraingnn
    model_plain: PretrainGNN
    value: 0.799
    std: 0.009
    paper_value: 0.799
    paper_std: 0.009
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: strategies_pretrain
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 25
    true_value: 0.799
    true_std: 0.009
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.799
    sort_std: 0.009
    is_best: false
  - model: N-GramXGB
    model_key: n-gramxgb
    model_plain: N-GramXGB
    value: 0.791
    std: 0.013
    paper_value: 0.791
    paper_std: 0.013
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: N_gram
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 35
    true_value: 0.791
    true_std: 0.013
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.791
    sort_std: 0.013
    is_best: false
  - model: AttentiveFP
    model_key: attentivefp
    model_plain: AttentiveFP
    value: 0.784
    std: 0.0
    paper_value: 0.784
    paper_std: 0.0
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: xiong2019pushing
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 41
    true_value: 0.784
    true_std: 0.0
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 41
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.784
    sort_std: 0.0
    is_best: false
  - model: N-GramRF
    model_key: n-gramrf
    model_plain: N-GramRF
    value: 0.779
    std: 0.015
    paper_value: 0.779
    paper_std: 0.015
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: N_gram
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 45
    true_value: 0.779
    true_std: 0.015
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 45
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.779
    sort_std: 0.015
    is_best: false
  - model: GraphLOG pretrained
    model_key: graphlog pretrained
    model_plain: GraphLOG pretrained
    value: 0.754
    std: 0.014
    paper_value: 0.754
    paper_std: 0.014
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: GraphLog
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 54
    true_value: 0.754
    true_std: 0.014
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 54
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.754
    sort_std: 0.014
    is_best: false
  - model: InfoGraph pretrained
    model_key: infograph pretrained
    model_plain: InfoGraph pretrained
    value: 0.648
    std: 0.007
    paper_value: 0.648
    paper_std: 0.007
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: InfoGraph
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 62
    true_value: 0.648
    true_std: 0.007
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 62
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.648
    sort_std: 0.007
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id014
  dataset: BBBP
  rows:
  - model: BiScale-GTR (Fragment)
    model_key: biscale-gtr (fragment)
    model_plain: BiScale-GTR (Fragment)
    value: 0.738
    std: 0.004
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.06336'
    title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale Molecular
      Representation Learning'
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    codebase_url: ''
    uses_external_data: true
    is_global_top: true
    global_rank: 1
    sort_value: 0.738
    sort_std: 0.004
    is_best: true
  - model: GraphGPS+LAC
    model_key: graphgps+lac
    model_plain: GraphGPS+LAC
    value: 0.736
    std: null
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.06336'
    title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale Molecular
      Representation Learning'
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 2
    sort_value: 0.736
    sort_std: null
    is_best: true
  - model: GraphLoG
    model_key: graphlog
    model_plain: GraphLoG
    value: 0.725
    std: 0.008
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    codebase_url: ''
    uses_external_data: true
    is_global_top: true
    global_rank: 3
    sort_value: 0.725
    sort_std: 0.008
    is_best: false
  - model: MPNN + HOPE-WavePE
    model_key: mpnn + hope-wavepe
    model_plain: MPNN + HOPE-WavePE
    value: 0.712
    std: 0.004
    paper_value: 0.712
    paper_std: 0.004
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 14
    true_value: 0.712
    true_std: 0.004
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.712
    sort_std: 0.004
    is_best: false
  - model: D-MPNN
    model_key: d-mpnn
    model_plain: D-MPNN
    value: 0.71
    std: 0.003
    paper_value: 0.71
    paper_std: 0.003
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: yang2019analyzing
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 15
    true_value: 0.71
    true_std: 0.003
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.71
    sort_std: 0.003
    is_best: false
  - model: GROVERbase
    model_key: groverbase
    model_plain: GROVERbase
    value: 0.7
    std: 0.001
    paper_value: 0.7
    paper_std: 0.001
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: GROVER
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 21
    true_value: 0.7
    true_std: 0.001
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7
    sort_std: 0.001
    is_best: false
  - model: N-GramRF
    model_key: n-gramrf
    model_plain: N-GramRF
    value: 0.697
    std: 0.006
    paper_value: 0.697
    paper_std: 0.006
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: N_gram
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 24
    true_value: 0.697
    true_std: 0.006
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.697
    sort_std: 0.006
    is_best: false
  - model: GraphLOG pretrained
    model_key: graphlog pretrained
    model_plain: GraphLOG pretrained
    value: 0.697
    std: 0.007
    paper_value: 0.697
    paper_std: 0.007
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: GraphLog
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 25
    true_value: 0.697
    true_std: 0.007
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.697
    sort_std: 0.007
    is_best: false
  - model: GROVER_large
    model_key: grover_large
    model_plain: GROVER_large
    value: 0.695
    std: 0.001
    paper_value: 0.695
    paper_std: 0.001
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: GROVER
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 26
    true_value: 0.695
    true_std: 0.001
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.695
    sort_std: 0.001
    is_best: false
  - model: N-GramXGB
    model_key: n-gramxgb
    model_plain: N-GramXGB
    value: 0.691
    std: 0.008
    paper_value: 0.691
    paper_std: 0.008
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: N_gram
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 27
    true_value: 0.691
    true_std: 0.008
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 27
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.691
    sort_std: 0.008
    is_best: false
  - model: PretrainGNN
    model_key: pretraingnn
    model_plain: PretrainGNN
    value: 0.687
    std: 0.013
    paper_value: 0.687
    paper_std: 0.013
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: strategies_pretrain
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 31
    true_value: 0.687
    true_std: 0.013
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.687
    sort_std: 0.013
    is_best: false
  - model: InfoGraph pretrained
    model_key: infograph pretrained
    model_plain: InfoGraph pretrained
    value: 0.663
    std: 0.006
    paper_value: 0.663
    paper_std: 0.006
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: InfoGraph
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 45
    true_value: 0.663
    true_std: 0.006
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 45
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.663
    sort_std: 0.006
    is_best: false
  - model: AttentiveFP
    model_key: attentivefp
    model_plain: AttentiveFP
    value: 0.643
    std: 0.018
    paper_value: 0.643
    paper_std: 0.018
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: xiong2019pushing
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 51
    true_value: 0.643
    true_std: 0.018
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 51
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.643
    sort_std: 0.018
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id009
  dataset: CIFAR10
  rows:
  - model: GRASS
    model_key: grass
    model_plain: GRASS
    value: 0.8375
    std: 0.00141
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    arxiv_id: '2407.05649'
    title: 'Greener GRASS: Enhancing GNNs with Encoding, Rewiring, and Attention'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.8375
    sort_std: 0.00141
    is_best: true
  - model: NeuralWalker
    model_key: neuralwalker
    model_plain: NeuralWalker
    value: 0.80027
    std: 0.00185
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.05649'
    title: 'Greener GRASS: Enhancing GNNs with Encoding, Rewiring, and Attention'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.80027
    sort_std: 0.00185
    is_best: false
  - model: RandAlign (4 layers)
    model_key: randalign (4 layers)
    model_plain: RandAlign (4 layers)
    value: 0.7942
    std: 0.00072
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.09774'
    title: 'RandAlign: A Parameter-Free Method for Regularizing Graph Convolutional
      Networks'
    date: Apr 2024
    date_display: Apr 2024
    date_iso: 2024-04
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.7942
    sort_std: 0.00072
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.6731
    std: 0.0031
    paper_value: 0.6731
    paper_std: 0.0031
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 12
    true_value: 0.77218
    true_std: 0.00381
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09907999999999995
    value_note: ''
    paper_rank: 105
    rank_delta: 93
    rank_delta_abs: 93
    rank_delta_direction: worse
    sort_value: 0.77218
    sort_std: 0.00381
    is_best: false
  - model: Graph MLP-Mixer
    model_key: graph mlp-mixer
    model_plain: Graph MLP-Mixer
    value: 0.7246
    std: 0.0036
    paper_value: 0.7246
    paper_std: 0.0036
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 39
    true_value: 0.73961
    true_std: 0.0033
    value_gap_source_arxiv: '2308.11129'
    value_gap_source_title: Enhancing Graph Transformers with Hierarchical Distance
      Structural Encoding
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.015009999999999968
    value_note: ''
    paper_rank: 53
    rank_delta: 14
    rank_delta_abs: 14
    rank_delta_direction: worse
    sort_value: 0.73961
    sort_std: 0.0033
    is_best: false
  - model: GPS + HOPE-WavePE
    model_key: gps + hope-wavepe
    model_plain: GPS + HOPE-WavePE
    value: 0.7301
    std: 0.0081
    paper_value: 0.7301
    paper_std: 0.0081
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 50
    true_value: 0.7301
    true_std: 0.0081
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 50
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7301
    sort_std: 0.0081
    is_best: false
  - model: GPS + (RWSE/LapPE)
    model_key: gps + (rwse/lappe)
    model_plain: GPS + (RWSE/LapPE)
    value: 0.723
    std: 0.0036
    paper_value: 0.723
    paper_std: 0.0036
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 61
    true_value: 0.723
    true_std: 0.0036
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 61
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.723
    sort_std: 0.0036
    is_best: false
  - model: GPS
    model_key: gps (none)
    model_plain: GPS
    value: 0.7176
    std: 0.0001
    paper_value: 0.7176
    paper_std: 0.0001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 75
    true_value: 0.7176
    true_std: 0.0001
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 75
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7176
    sort_std: 0.0001
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.5526
    std: 0.0153
    paper_value: 0.5526
    paper_std: 0.0153
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 97
    true_value: 0.69592
    true_std: 0.00287
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.14332
    value_note: ''
    paper_rank: 115
    rank_delta: 18
    rank_delta_abs: 18
    rank_delta_direction: worse
    sort_value: 0.69592
    sort_std: 0.00287
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.6422
    std: 0.0045
    paper_value: 0.6422
    paper_std: 0.0045
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 110
    true_value: 0.64223
    true_std: 0.00455
    value_gap_source_arxiv: '2605.05689'
    value_gap_source_title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive
      Consistency Model'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 2.999999999997449e-05
    value_note: global 0.6422 within std
    paper_rank: 111
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.64223
    sort_std: 0.00455
    is_best: false
  metric: Accuracy
  higher_is_better: true
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
  - model: GSN
    model_key: gsn
    model_plain: GSN
    value: 0.778
    std: 0.033
    paper_value: 0.778
    paper_std: 0.033
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to imdb-binary (score=90)'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 7
    true_value: 0.778
    true_std: 0.033
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.778
    sort_std: 0.033
    is_best: false
  - model: GIN + HOPE-WavePE
    model_key: gin + hope-wavepe
    model_plain: GIN + HOPE-WavePE
    value: 0.76
    std: 0.037
    paper_value: 0.76
    paper_std: 0.037
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to imdb-binary (score=90)'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 17
    true_value: 0.76
    true_std: 0.037
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.76
    sort_std: 0.037
    is_best: false
  - model: CIN
    model_key: cin
    model_plain: CIN
    value: 0.756
    std: 0.037
    paper_value: 0.756
    paper_std: 0.037
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to imdb-binary (score=90)'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 21
    true_value: 0.756
    true_std: 0.037
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.756
    sort_std: 0.037
    is_best: false
  - model: SIN
    model_key: sin
    model_plain: SIN
    value: 0.756
    std: 0.032
    paper_value: 0.756
    paper_std: 0.032
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to imdb-binary (score=90)'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 20
    true_value: 0.756
    true_std: 0.032
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.756
    sort_std: 0.032
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.751
    std: 0.051
    paper_value: 0.751
    paper_std: 0.051
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to imdb-binary (score=90)'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 25
    true_value: 0.751
    true_std: 0.051
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.751
    sort_std: 0.051
    is_best: false
  - model: Natural GN
    model_key: natural gn
    model_plain: Natural GN
    value: 0.735
    std: 0.02
    paper_value: 0.735
    paper_std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to imdb-binary (score=90)'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 27
    true_value: 0.748
    true_std: 0.02
    value_gap_source_arxiv: '2310.02156'
    value_gap_source_title: Probabilistically Rewired Message-Passing Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.013000000000000012
    value_note: global 0.7480 within std
    paper_rank: 41
    rank_delta: 14
    rank_delta_abs: 14
    rank_delta_direction: worse
    sort_value: 0.748
    sort_std: 0.02
    is_best: false
  - model: Kern. WL
    model_key: kern. wl
    model_plain: Kern. WL
    value: 0.738
    std: 0.039
    paper_value: 0.738
    paper_std: 0.039
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to imdb-binary (score=90)'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 33
    true_value: 0.738
    true_std: 0.039
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.738
    sort_std: 0.039
    is_best: false
  - model: PPGNs
    model_key: ppgns
    model_plain: PPGNs
    value: 0.73
    std: 0.058
    paper_value: 0.73
    paper_std: 0.058
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to imdb-binary (score=90)'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 50
    true_value: 0.73
    true_std: 0.058
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 50
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.73
    sort_std: 0.058
    is_best: false
  - model: IGN
    model_key: ign
    model_plain: IGN
    value: 0.72
    std: 0.055
    paper_value: 0.72
    paper_std: 0.055
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to imdb-binary (score=90)'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 67
    true_value: 0.72
    true_std: 0.055
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 67
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.72
    sort_std: 0.055
    is_best: false
  - model: DGCNN
    model_key: dgcnn
    model_plain: DGCNN
    value: 0.7
    std: 0.009
    paper_value: 0.7
    paper_std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to imdb-binary (score=90)'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 100
    true_value: 0.7
    true_std: 0.009
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 100
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7
    sort_std: 0.009
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id008
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
  - model: GSN
    model_key: gsn
    model_plain: GSN
    value: 0.543
    std: 0.033
    paper_value: 0.543
    paper_std: 0.033
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: GSN
    variant_inference_reason: 'dataset: fuzzy match to imdb-multi (score=90)'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 13
    true_value: 0.543
    true_std: 0.033
    value_gap_source_arxiv: '2310.02156'
    value_gap_source_title: Probabilistically Rewired Message-Passing Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.543
    sort_std: 0.033
    is_best: false
  - model: CIN
    model_key: cin
    model_plain: CIN
    value: 0.527
    std: 0.031
    paper_value: 0.527
    paper_std: 0.031
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: CIN
    variant_inference_reason: 'dataset: fuzzy match to imdb-multi (score=90)'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 18
    true_value: 0.527
    true_std: 0.031
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.527
    sort_std: 0.031
    is_best: false
  - model: GIN + HOPE-WavePE
    model_key: gin + hope-wavepe
    model_plain: GIN + HOPE-WavePE
    value: 0.527
    std: 0.029
    paper_value: 0.527
    paper_std: 0.029
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to imdb-multi (score=90)'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 19
    true_value: 0.527
    true_std: 0.029
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.527
    sort_std: 0.029
    is_best: false
  - model: SIN
    model_key: sin
    model_plain: SIN
    value: 0.524
    std: 0.029
    paper_value: 0.524
    paper_std: 0.029
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: SIN
    variant_inference_reason: 'dataset: fuzzy match to imdb-multi (score=90)'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 20
    true_value: 0.524
    true_std: 0.029
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.524
    sort_std: 0.029
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.523
    std: 0.028
    paper_value: 0.523
    paper_std: 0.028
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: gin
    variant_inference_reason: 'dataset: fuzzy match to imdb-multi (score=90)'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 22
    true_value: 0.523
    true_std: 0.028
    value_gap_source_arxiv: '2310.02156'
    value_gap_source_title: Probabilistically Rewired Message-Passing Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.523
    sort_std: 0.028
    is_best: false
  - model: Natural GN
    model_key: natural gn
    model_plain: Natural GN
    value: 0.513
    std: 0.015
    paper_value: 0.513
    paper_std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: naturalGN
    variant_inference_reason: 'dataset: fuzzy match to imdb-multi (score=90)'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 25
    true_value: 0.513
    true_std: 0.015
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.513
    sort_std: 0.015
    is_best: false
  - model: Kern. WL
    model_key: kern. wl
    model_plain: Kern. WL
    value: 0.509
    std: 0.038
    paper_value: 0.509
    paper_std: 0.038
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: WLkernel
    variant_inference_reason: 'dataset: fuzzy match to imdb-multi (score=90)'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 28
    true_value: 0.509
    true_std: 0.038
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 28
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.509
    sort_std: 0.038
    is_best: false
  - model: PPGNs
    model_key: ppgns
    model_plain: PPGNs
    value: 0.505
    std: 0.036
    paper_value: 0.505
    paper_std: 0.036
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ppgn
    variant_inference_reason: 'dataset: fuzzy match to imdb-multi (score=90)'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 35
    true_value: 0.505
    true_std: 0.036
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.505
    sort_std: 0.036
    is_best: false
  - model: IGN
    model_key: ign
    model_plain: IGN
    value: 0.487
    std: 0.034
    paper_value: 0.487
    paper_std: 0.034
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: maron2018invariant
    variant_inference_reason: 'dataset: fuzzy match to imdb-multi (score=90)'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 56
    true_value: 0.487
    true_std: 0.034
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 56
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.487
    sort_std: 0.034
    is_best: false
  - model: DGCNN
    model_key: dgcnn
    model_plain: DGCNN
    value: 0.478
    std: 0.009
    paper_value: 0.478
    paper_std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: DCNN
    variant_inference_reason: 'dataset: fuzzy match to imdb-multi (score=90)'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 66
    true_value: 0.478
    true_std: 0.009
    value_gap_source_arxiv: '2310.02156'
    value_gap_source_title: Probabilistically Rewired Message-Passing Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 66
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.478
    sort_std: 0.009
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id010
  dataset: MNIST
  rows:
  - model: GRASS
    model_key: grass
    model_plain: GRASS
    value: 0.98932
    std: 0.00076
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    arxiv_id: '2407.05649'
    title: 'Greener GRASS: Enhancing GNNs with Encoding, Rewiring, and Attention'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.98932
    sort_std: 0.00076
    is_best: true
  - model: GSM++ (MoT)
    model_key: gsm++ (mot)
    model_plain: GSM++ (MoT)
    value: 0.9884
    std: 0.0015
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.15671'
    title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence Models'
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 2
    sort_value: 0.9884
    sort_std: 0.0015
    is_best: true
  - model: NeuralWalker
    model_key: neuralwalker
    model_plain: NeuralWalker
    value: 0.9876
    std: 0.00079
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.05649'
    title: 'Greener GRASS: Enhancing GNNs with Encoding, Rewiring, and Attention'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.9876
    sort_std: 0.00079
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.9734
    std: 0.0014
    paper_value: 0.9734
    paper_std: 0.0014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 4
    true_value: 0.98712
    true_std: 0.00137
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.013719999999999954
    value_note: ''
    paper_rank: 80
    rank_delta: 76
    rank_delta_abs: 76
    rank_delta_direction: worse
    sort_value: 0.98712
    sort_std: 0.00137
    is_best: false
  - model: Graph MLP-Mixer
    model_key: graph mlp-mixer
    model_plain: Graph MLP-Mixer
    value: 0.9835
    std: 0.001
    paper_value: 0.9835
    paper_std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 18
    true_value: 0.9846
    true_std: 0.0009
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0010999999999999899
    value_note: ''
    paper_rank: 28
    rank_delta: 10
    rank_delta_abs: 10
    rank_delta_direction: worse
    sort_value: 0.9846
    sort_std: 0.0009
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.9649
    std: 0.0025
    paper_value: 0.9649
    paper_std: 0.0025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 32
    true_value: 0.98285
    true_std: 0.00103
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.01795000000000002
    value_note: ''
    paper_rank: 88
    rank_delta: 56
    rank_delta_abs: 56
    rank_delta_direction: worse
    sort_value: 0.98285
    sort_std: 0.00103
    is_best: false
  - model: GPS + HOPE-WavePE
    model_key: gps + hope-wavepe
    model_plain: GPS + HOPE-WavePE
    value: 0.9815
    std: 0.0011
    paper_value: 0.9815
    paper_std: 0.0011
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 47
    true_value: 0.9815
    true_std: 0.0011
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 47
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9815
    sort_std: 0.0011
    is_best: false
  - model: GPS
    model_key: gps (none)
    model_plain: GPS
    value: 0.9805
    std: 0.0
    paper_value: 0.9805
    paper_std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 66
    true_value: 0.9805
    true_std: 0.0
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 66
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9805
    sort_std: 0.0
    is_best: false
  - model: GPS + (RWSE/LapPE)
    model_key: gps + (rwse/lappe)
    model_plain: GPS + (RWSE/LapPE)
    value: 0.9805
    std: 0.0013
    paper_value: 0.9805
    paper_std: 0.0013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 67
    true_value: 0.9805
    true_std: 0.0013
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 67
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9805
    sort_std: 0.0013
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.9553
    std: 0.002
    paper_value: 0.9553
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 92
    true_value: 0.9554
    true_std: 0.0021
    value_gap_source_arxiv: '2411.15671'
    value_gap_source_title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence
      Models'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 9.999999999998899e-05
    value_note: global 0.9554 within std
    paper_rank: 93
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.9554
    sort_std: 0.0021
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
  - model: CIN
    model_key: cin
    model_plain: CIN
    value: 0.927
    std: 0.061
    paper_value: 0.927
    paper_std: 0.061
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: 'Table: TU datasets'
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 4
    true_value: 0.944
    true_std: 0.037
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.016999999999999904
    value_note: global 0.9440 within std
    paper_rank: 6
    rank_delta: 2
    rank_delta_abs: 2
    rank_delta_direction: worse
    sort_value: 0.944
    sort_std: 0.037
    is_best: true
  - model: GIN + HOPE-WavePE
    model_key: gin + hope-wavepe
    model_plain: GIN + HOPE-WavePE
    value: 0.936
    std: 0.058
    paper_value: 0.936
    paper_std: 0.058
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: 'Table: TU datasets'
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 6
    true_value: 0.936
    true_std: 0.058
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.936
    sort_std: 0.058
    is_best: true
  - model: GSN
    model_key: gsn
    model_plain: GSN
    value: 0.922
    std: 0.075
    paper_value: 0.922
    paper_std: 0.075
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: 'Table: TU datasets'
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 7
    true_value: 0.922
    true_std: 0.075
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.922
    sort_std: 0.075
    is_best: true
  - model: PPGNs
    model_key: ppgns
    model_plain: PPGNs
    value: 0.906
    std: 0.087
    paper_value: 0.906
    paper_std: 0.087
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: 'Table: TU datasets'
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 12
    true_value: 0.906
    true_std: 0.087
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.906
    sort_std: 0.087
    is_best: true
  - model: Kern. WL
    model_key: kern. wl
    model_plain: Kern. WL
    value: 0.904
    std: 0.057
    paper_value: 0.904
    paper_std: 0.057
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: 'Table: TU datasets'
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 17
    true_value: 0.904
    true_std: 0.057
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.904
    sort_std: 0.057
    is_best: true
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.894
    std: 0.056
    paper_value: 0.894
    paper_std: 0.056
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: 'Table: TU datasets'
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 28
    true_value: 0.894
    true_std: 0.056
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 28
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.894
    sort_std: 0.056
    is_best: false
  - model: Natural GN
    model_key: natural gn
    model_plain: Natural GN
    value: 0.894
    std: 0.016
    paper_value: 0.894
    paper_std: 0.016
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: 'Table: TU datasets'
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 29
    true_value: 0.894
    true_std: 0.016
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.894
    sort_std: 0.016
    is_best: false
  - model: DGCNN
    model_key: dgcnn
    model_plain: DGCNN
    value: 0.858
    std: 0.018
    paper_value: 0.858
    paper_std: 0.018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: 'Table: TU datasets'
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 58
    true_value: 0.858
    true_std: 0.018
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 58
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.858
    sort_std: 0.018
    is_best: false
  - model: IGN
    model_key: ign
    model_plain: IGN
    value: 0.839
    std: 0.13
    paper_value: 0.839
    paper_std: 0.13
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: 'Table: TU datasets'
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 71
    true_value: 0.839
    true_std: 0.13
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 71
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.839
    sort_std: 0.13
    is_best: true
  - model: GK (k=3)
    model_key: gk (k=3)
    model_plain: GK (k=3)
    value: 0.814
    std: 0.017
    paper_value: 0.814
    paper_std: 0.017
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: 'Table: TU datasets'
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 92
    true_value: 0.814
    true_std: 0.017
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 92
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.814
    sort_std: 0.017
    is_best: false
  - model: RWK
    model_key: rwk
    model_plain: RWK
    value: 0.792
    std: 0.021
    paper_value: 0.792
    paper_std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: 'Table: TU datasets'
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 111
    true_value: 0.792
    true_std: 0.021
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 111
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.792
    sort_std: 0.021
    is_best: false
  - model: PK
    model_key: pk
    model_plain: PK
    value: 0.76
    std: 0.027
    paper_value: 0.76
    paper_std: 0.027
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: 'Table: TU datasets'
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 133
    true_value: 0.76
    true_std: 0.027
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 133
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.76
    sort_std: 0.027
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id007
  dataset: NCI1
  rows:
  - model: IPR-MPNN
    model_key: ipr-mpnn
    model_plain: IPR-MPNN
    value: 0.865
    std: 0.014
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
    sort_value: 0.865
    sort_std: 0.014
    is_best: true
  - model: Kern. WL
    model_key: kern. wl
    model_plain: Kern. WL
    value: 0.86
    std: 0.018
    paper_value: 0.86
    paper_std: 0.018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 2
    true_value: 0.86
    true_std: 0.018
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.86
    sort_std: 0.018
    is_best: true
  - model: CoCN expanded
    model_key: cocn expanded
    model_plain: CoCN expanded
    value: 0.8583
    std: 0.0086
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.18480'
    title: Scalable Graph Compressed Convolutions
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.8583
    sort_std: 0.0086
    is_best: true
  - model: PR-MPNN (10-fold CV)
    model_key: pr-mpnn (10-fold cv)
    model_plain: PR-MPNN (10-fold CV)
    value: 0.846
    std: 0.012
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
    global_rank: 4
    sort_value: 0.846
    sort_std: 0.012
    is_best: true
  - model: CIN
    model_key: cin
    model_plain: CIN
    value: 0.84
    std: 0.016
    paper_value: 0.84
    paper_std: 0.016
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to nci1 (score=90)'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 6
    true_value: 0.845
    true_std: 0.024
    value_gap_source_arxiv: '2310.02156'
    value_gap_source_title: Probabilistically Rewired Message-Passing Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0050000000000000044
    value_note: global 0.8450 within std
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.845
    sort_std: 0.024
    is_best: true
  - model: GSN
    model_key: gsn
    model_plain: GSN
    value: 0.835
    std: 0.02
    paper_value: 0.835
    paper_std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 9
    true_value: 0.835
    true_std: 0.02
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.835
    sort_std: 0.02
    is_best: true
  - model: GIN + HOPE-WavePE
    model_key: gin + hope-wavepe
    model_plain: GIN + HOPE-WavePE
    value: 0.831
    std: 0.019
    paper_value: 0.831
    paper_std: 0.019
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to nci1 (score=90)'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 11
    true_value: 0.831
    true_std: 0.019
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.831
    sort_std: 0.019
    is_best: false
  - model: Natural GN
    model_key: natural gn
    model_plain: Natural GN
    value: 0.824
    std: 0.013
    paper_value: 0.824
    paper_std: 0.013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 12
    true_value: 0.83
    true_std: 0.019
    value_gap_source_arxiv: '2310.02156'
    value_gap_source_title: Probabilistically Rewired Message-Passing Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.006000000000000005
    value_note: global 0.8300 within std
    paper_rank: 20
    rank_delta: 8
    rank_delta_abs: 8
    rank_delta_direction: worse
    sort_value: 0.83
    sort_std: 0.019
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.827
    std: 0.017
    paper_value: 0.827
    paper_std: 0.017
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 18
    true_value: 0.827
    true_std: 0.017
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.827
    sort_std: 0.017
    is_best: false
  - model: SIN
    model_key: sin
    model_plain: SIN
    value: 0.827
    std: 0.021
    paper_value: 0.827
    paper_std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 19
    true_value: 0.827
    true_std: 0.021
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.827
    sort_std: 0.021
    is_best: false
  - model: PK
    model_key: pk
    model_plain: PK
    value: 0.825
    std: 0.005
    paper_value: 0.825
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 20
    true_value: 0.825
    true_std: 0.005
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.825
    sort_std: 0.005
    is_best: false
  - model: PPGNs
    model_key: ppgns
    model_plain: PPGNs
    value: 0.822
    std: 0.014
    paper_value: 0.822
    paper_std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to nci1 (score=90)'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 26
    true_value: 0.822
    true_std: 0.014
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.822
    sort_std: 0.014
    is_best: false
  - model: DGCNN
    model_key: dgcnn
    model_plain: DGCNN
    value: 0.744
    std: 0.005
    paper_value: 0.744
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 61
    true_value: 0.764
    true_std: 0.017
    value_gap_source_arxiv: '2310.01267'
    value_gap_source_title: Cooperative Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.020000000000000018
    value_note: ''
    paper_rank: 69
    rank_delta: 8
    rank_delta_abs: 8
    rank_delta_direction: worse
    sort_value: 0.764
    sort_std: 0.017
    is_best: false
  - model: IGN
    model_key: ign
    model_plain: IGN
    value: 0.728
    std: 0.015
    paper_value: 0.728
    paper_std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to nci1 (score=90)'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 75
    true_value: 0.728
    true_std: 0.015
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 75
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.728
    sort_std: 0.015
    is_best: false
  - model: GK (k=3)
    model_key: gk (k=3)
    model_plain: GK (k=3)
    value: 0.624
    std: 0.003
    paper_value: 0.624
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to nci1 (score=90)'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 87
    true_value: 0.624
    true_std: 0.003
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 87
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.624
    sort_std: 0.003
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
  - model: CIN
    model_key: cin
    model_plain: CIN
    value: 0.77
    std: 0.043
    paper_value: 0.77
    paper_std: 0.043
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: CIN
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 4
    true_value: 0.805
    true_std: 0.039
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.03500000000000003
    value_note: global 0.8050 within std
    paper_rank: 15
    rank_delta: 11
    rank_delta_abs: 11
    rank_delta_direction: worse
    sort_value: 0.805
    sort_std: 0.039
    is_best: true
  - model: GIN + HOPE-WavePE
    model_key: gin + hope-wavepe
    model_plain: GIN + HOPE-WavePE
    value: 0.795
    std: 0.0481
    paper_value: 0.795
    paper_std: 0.0481
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 5
    true_value: 0.795
    true_std: 0.0481
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.795
    sort_std: 0.0481
    is_best: true
  - model: PPGNs
    model_key: ppgns
    model_plain: PPGNs
    value: 0.772
    std: 0.047
    paper_value: 0.772
    paper_std: 0.047
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ppgn
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 15
    true_value: 0.772
    true_std: 0.047
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.772
    sort_std: 0.047
    is_best: true
  - model: GSN
    model_key: gsn
    model_plain: GSN
    value: 0.766
    std: 0.05
    paper_value: 0.766
    paper_std: 0.05
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: GSN
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 23
    true_value: 0.766
    true_std: 0.05
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.766
    sort_std: 0.05
    is_best: true
  - model: IGN
    model_key: ign
    model_plain: IGN
    value: 0.766
    std: 0.055
    paper_value: 0.766
    paper_std: 0.055
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: maron2018invariant
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 22
    true_value: 0.766
    true_std: 0.055
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.766
    sort_std: 0.055
    is_best: true
  - model: SIN
    model_key: sin
    model_plain: SIN
    value: 0.764
    std: 0.033
    paper_value: 0.764
    paper_std: 0.033
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: SIN
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 26
    true_value: 0.764
    true_std: 0.033
    value_gap_source_arxiv: '2306.03561'
    value_gap_source_title: 'CIN++: Enhancing Topological Message Passing'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.764
    sort_std: 0.033
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.762
    std: 0.028
    paper_value: 0.762
    paper_std: 0.028
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: gin
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 32
    true_value: 0.762
    true_std: 0.028
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.762
    sort_std: 0.028
    is_best: false
  - model: DGCNN
    model_key: dgcnn
    model_plain: DGCNN
    value: 0.755
    std: 0.009
    paper_value: 0.755
    paper_std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: DCNN
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 50
    true_value: 0.755
    true_std: 0.009
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 50
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.755
    sort_std: 0.009
    is_best: false
  - model: Kern. WL
    model_key: kern. wl
    model_plain: Kern. WL
    value: 0.75
    std: 0.031
    paper_value: 0.75
    paper_std: 0.031
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: WLkernel
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 68
    true_value: 0.75
    true_std: 0.031
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 68
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.75
    sort_std: 0.031
    is_best: false
  - model: PK
    model_key: pk
    model_plain: PK
    value: 0.737
    std: 0.007
    paper_value: 0.737
    paper_std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: PK
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 102
    true_value: 0.737
    true_std: 0.007
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 102
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.737
    sort_std: 0.007
    is_best: false
  - model: Natural GN
    model_key: natural gn
    model_plain: Natural GN
    value: 0.717
    std: 0.01
    paper_value: 0.717
    paper_std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: naturalGN
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 153
    true_value: 0.717
    true_std: 0.01
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 153
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.717
    sort_std: 0.01
    is_best: false
  - model: GK (k=3)
    model_key: gk (k=3)
    model_plain: GK (k=3)
    value: 0.714
    std: 0.003
    paper_value: 0.714
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: GK3
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 160
    true_value: 0.714
    true_std: 0.003
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 160
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.714
    sort_std: 0.003
    is_best: false
  - model: RWK
    model_key: rwk
    model_plain: RWK
    value: 0.596
    std: 0.001
    paper_value: 0.596
    paper_std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: RWK
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 200
    true_value: 0.596
    true_std: 0.001
    value_gap_source_arxiv: '2306.03561'
    value_gap_source_title: 'CIN++: Enhancing Topological Message Passing'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 200
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.596
    sort_std: 0.001
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
    std: 0.0023
    paper_value: 0.593
    paper_std: 0.0023
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
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
  - model: GatedGCN + VN + HOPE-WavePE
    model_key: gatedgcn + vn + hope-wavepe
    model_plain: GatedGCN + VN + HOPE-WavePE
    value: 0.7171
    std: 0.0023
    paper_value: 0.7171
    paper_std: 0.0023
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 18
    true_value: 0.7171
    true_std: 0.0023
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7171
    sort_std: 0.0023
    is_best: false
  - model: DRew-GCN+LapPE
    model_key: drew-gcn+lappe
    model_plain: DRew-GCN+LapPE
    value: 0.715
    std: 0.0044
    paper_value: 0.715
    paper_std: 0.0044
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 23
    true_value: 0.715
    true_std: 0.0044
    value_gap_source_arxiv: '2510.02565'
    value_gap_source_title: On The Expressive Power of GNN Derivatives
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.715
    sort_std: 0.0044
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.5864
    std: 0.0077
    paper_value: 0.5864
    paper_std: 0.0077
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 49
    true_value: 0.7006
    true_std: 0.0033
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11419999999999997
    value_note: ''
    paper_rank: 273
    rank_delta: 224
    rank_delta_abs: 224
    rank_delta_direction: worse
    sort_value: 0.7006
    sort_std: 0.0033
    is_best: false
  - model: GRIT
    model_key: grit
    model_plain: GRIT
    value: 0.6988
    std: 0.0082
    paper_value: 0.6988
    paper_std: 0.0082
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 53
    true_value: 0.6988
    true_std: 0.0082
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 53
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6988
    sort_std: 0.0082
    is_best: false
  - model: Graph ViT
    model_key: graph vit
    model_plain: Graph ViT
    value: 0.6942
    std: 0.0075
    paper_value: 0.6942
    paper_std: 0.0075
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 61
    true_value: 0.697
    true_std: 0.008
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0027999999999999137
    value_note: global 0.6970 within std
    paper_rank: 74
    rank_delta: 13
    rank_delta_abs: 13
    rank_delta_direction: worse
    sort_value: 0.697
    sort_std: 0.008
    is_best: false
  - model: GraphMLPMixer
    model_key: graphmlpmixer
    model_plain: GraphMLPMixer
    value: 0.6921
    std: 0.0054
    paper_value: 0.6921
    paper_std: 0.0054
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 64
    true_value: 0.697
    true_std: 0.008
    value_gap_source_arxiv: '2405.02795'
    value_gap_source_title: Graph as Point Set
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.004899999999999904
    value_note: global 0.6970 within std
    paper_rank: 78
    rank_delta: 14
    rank_delta_abs: 14
    rank_delta_direction: worse
    sort_value: 0.697
    sort_std: 0.008
    is_best: false
  - model: GatedGCN+RWSE
    model_key: gatedgcn+rwse
    model_plain: GatedGCN+RWSE
    value: 0.6685
    std: 0.0062
    paper_value: 0.6685
    paper_std: 0.0062
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 133
    true_value: 0.6685
    true_std: 0.0062
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 133
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6685
    sort_std: 0.0062
    is_best: false
  - model: GINE
    model_key: gine
    model_plain: GINE
    value: 0.5498
    std: 0.0079
    paper_value: 0.5498
    paper_std: 0.0079
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 142
    true_value: 0.6621
    true_std: 0.0067
    value_gap_source_arxiv: '2309.00367'
    value_gap_source_title: Where Did the Gap Go? Reassessing the Long-Range Graph
      Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11230000000000007
    value_note: ''
    paper_rank: 288
    rank_delta: 146
    rank_delta_abs: 146
    rank_delta_direction: worse
    sort_value: 0.6621
    sort_std: 0.0067
    is_best: false
  - model: GraphGPS+LapPE
    model_key: graphgps+lappe
    model_plain: GraphGPS+LapPE
    value: 0.6535
    std: 0.0041
    paper_value: 0.6535
    paper_std: 0.0041
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 169
    true_value: 0.6535
    true_std: 0.0040999999999999995
    value_gap_source_arxiv: '2510.02565'
    value_gap_source_title: On The Expressive Power of GNN Derivatives
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 169
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6535
    sort_std: 0.0040999999999999995
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
    value: 0.3496
    std: 0.0013
    paper_value: 0.3496
    paper_std: 0.0013
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: tab:LRGB
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 3
    true_value: 0.2421
    true_std: 0.0016
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10750000000000001
    value_note: ''
    paper_rank: 304
    rank_delta: 301
    rank_delta_abs: 301
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
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.342
    std: 0.0013
    paper_value: 0.342
    paper_std: 0.0013
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: tab:LRGB
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 12
    true_value: 0.2431
    true_std: 0.002
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09890000000000002
    value_note: ''
    paper_rank: 297
    rank_delta: 285
    rank_delta_abs: 285
    rank_delta_direction: worse
    sort_value: 0.2431
    sort_std: 0.002
    is_best: false
  - model: GatedGCN + VN + HOPE-WavePE
    model_key: gatedgcn + vn + hope-wavepe
    model_plain: GatedGCN + VN + HOPE-WavePE
    value: 0.2433
    std: 0.0011
    paper_value: 0.2433
    paper_std: 0.0011
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: tab:LRGB
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 19
    true_value: 0.2433
    true_std: 0.0011
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2433
    sort_std: 0.0011
    is_best: false
  - model: Graph ViT
    model_key: graph vit
    model_plain: Graph ViT
    value: 0.2449
    std: 0.0016
    paper_value: 0.2449
    paper_std: 0.0016
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: tab:LRGB
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 31
    true_value: 0.2449
    true_std: 0.0016
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2449
    sort_std: 0.0016
    is_best: false
  - model: GRIT
    model_key: grit
    model_plain: GRIT
    value: 0.246
    std: 0.0012
    paper_value: 0.246
    paper_std: 0.0012
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: tab:LRGB
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 56
    true_value: 0.246
    true_std: 0.0012
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 56
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.246
    sort_std: 0.0012
    is_best: false
  - model: GINE
    model_key: gine
    model_plain: GINE
    value: 0.6346
    std: 0.0071
    paper_value: 0.6346
    paper_std: 0.0071
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: tab:LRGB
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 79
    true_value: 0.2473
    true_std: 0.0017
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.3873000000000001
    value_note: ''
    paper_rank: 338
    rank_delta: 259
    rank_delta_abs: 259
    rank_delta_direction: worse
    sort_value: 0.2473
    sort_std: 0.0017
    is_best: false
  - model: GraphMLPMixer
    model_key: graphmlpmixer
    model_plain: GraphMLPMixer
    value: 0.2475
    std: 0.0015
    paper_value: 0.2475
    paper_std: 0.0015
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: tab:LRGB
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 88
    true_value: 0.2475
    true_std: 0.0015
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 88
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2475
    sort_std: 0.0015
    is_best: false
  - model: GraphGPS+LapPE
    model_key: graphgps+lappe
    model_plain: GraphGPS+LapPE
    value: 0.25
    std: 0.0005
    paper_value: 0.25
    paper_std: 0.0005
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: tab:LRGB
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 138
    true_value: 0.25
    true_std: 0.0005
    value_gap_source_arxiv: '2510.02565'
    value_gap_source_title: On The Expressive Power of GNN Derivatives
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 138
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.25
    sort_std: 0.0005
    is_best: false
  - model: GatedGCN+RWSE
    model_key: gatedgcn+rwse
    model_plain: GatedGCN+RWSE
    value: 0.2529
    std: 0.0009
    paper_value: 0.2529
    paper_std: 0.0009
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: tab:LRGB
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 167
    true_value: 0.2529
    true_std: 0.0009
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 167
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2529
    sort_std: 0.0009
    is_best: false
  - model: DRew-GCN+LapPE
    model_key: drew-gcn+lappe
    model_plain: DRew-GCN+LapPE
    value: 0.2536
    std: 0.0015
    paper_value: 0.2536
    paper_std: 0.0015
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: tab:LRGB
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 175
    true_value: 0.2536
    true_std: 0.0015
    value_gap_source_arxiv: '2510.02565'
    value_gap_source_title: On The Expressive Power of GNN Derivatives
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 175
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2536
    sort_std: 0.0015
    is_best: false
  metric: MAE
  higher_is_better: false
- &id016
  dataset: SIDER
  rows:
  - model: N-GramRF
    model_key: n-gramrf
    model_plain: N-GramRF
    value: 0.668
    std: 0.007
    paper_value: 0.668
    paper_std: 0.007
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 1
    true_value: 0.668
    true_std: 0.007
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.668
    sort_std: 0.007
    is_best: true
  - model: N-GramXGB
    model_key: n-gramxgb
    model_plain: N-GramXGB
    value: 0.655
    std: 0.007
    paper_value: 0.655
    paper_std: 0.007
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 2
    true_value: 0.655
    true_std: 0.007
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.655
    sort_std: 0.007
    is_best: true
  - model: GROVER_large
    model_key: grover_large
    model_plain: GROVER_large
    value: 0.654
    std: 0.001
    paper_value: 0.654
    paper_std: 0.001
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 3
    true_value: 0.654
    true_std: 0.001
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.654
    sort_std: 0.001
    is_best: false
  - model: GROVERbase
    model_key: groverbase
    model_plain: GROVERbase
    value: 0.648
    std: 0.006
    paper_value: 0.648
    paper_std: 0.006
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 4
    true_value: 0.648
    true_std: 0.006
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.648
    sort_std: 0.006
    is_best: false
  - model: MPNN + HOPE-WavePE
    model_key: mpnn + hope-wavepe
    model_plain: MPNN + HOPE-WavePE
    value: 0.647
    std: 0.003
    paper_value: 0.647
    paper_std: 0.003
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 5
    true_value: 0.647
    true_std: 0.003
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.647
    sort_std: 0.003
    is_best: false
  - model: BiScale-GTR (Molecule)
    model_key: biscale-gtr (molecule)
    model_plain: BiScale-GTR (Molecule)
    value: 0.642
    std: 0.009
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.06336'
    title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale Molecular
      Representation Learning'
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    codebase_url: ''
    uses_external_data: true
    is_global_top: true
    global_rank: 6
    sort_value: 0.642
    sort_std: 0.009
    is_best: false
  - model: GraphFP
    model_key: graphfp
    model_plain: GraphFP
    value: 0.636
    std: 0.012
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.06336'
    title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale Molecular
      Representation Learning'
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    codebase_url: ''
    uses_external_data: true
    is_global_top: true
    global_rank: 7
    sort_value: 0.636
    sort_std: 0.012
    is_best: false
  - model: GraphFP_CP
    model_key: graphfp_cp
    model_plain: GraphFP_CP
    value: 0.636
    std: 0.012
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: true
    is_global_top: true
    global_rank: 8
    sort_value: 0.636
    sort_std: 0.012
    is_best: false
  - model: PretrainGNN
    model_key: pretraingnn
    model_plain: PretrainGNN
    value: 0.627
    std: 0.008
    paper_value: 0.627
    paper_std: 0.008
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 12
    true_value: 0.627
    true_std: 0.008
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.627
    sort_std: 0.008
    is_best: false
  - model: AttentiveFP
    model_key: attentivefp
    model_plain: AttentiveFP
    value: 0.606
    std: 0.032
    paper_value: 0.606
    paper_std: 0.032
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 28
    true_value: 0.606
    true_std: 0.032
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 28
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.606
    sort_std: 0.032
    is_best: false
  - model: GraphLOG pretrained
    model_key: graphlog pretrained
    model_plain: GraphLOG pretrained
    value: 0.605
    std: 0.009
    paper_value: 0.605
    paper_std: 0.009
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 30
    true_value: 0.605
    true_std: 0.009
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 30
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.605
    sort_std: 0.009
    is_best: false
  - model: InfoGraph pretrained
    model_key: infograph pretrained
    model_plain: InfoGraph pretrained
    value: 0.571
    std: 0.008
    paper_value: 0.571
    paper_std: 0.008
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 45
    true_value: 0.571
    true_std: 0.008
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 45
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.571
    sort_std: 0.008
    is_best: false
  - model: D-MPNN
    model_key: d-mpnn
    model_plain: D-MPNN
    value: 0.57
    std: 0.007
    paper_value: 0.57
    paper_std: 0.007
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 46
    true_value: 0.57
    true_std: 0.007
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 46
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.57
    sort_std: 0.007
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id013
  dataset: Tox21
  rows:
  - model: HIMP
    model_key: himp
    model_plain: HIMP
    value: 0.874
    std: 0.005
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01704'
    title: Transformers are efficient hierarchical chemical graph learners
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.874
    sort_std: 0.005
    is_best: true
  - model: Ours(dual readout)
    model_key: ours(dual readout)
    model_plain: Ours(dual readout)
    value: 0.851
    std: 0.008
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01704'
    title: Transformers are efficient hierarchical chemical graph learners
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.851
    sort_std: 0.008
    is_best: false
  - model: GNNs (dual readout, VN)
    model_key: gnns (dual readout, vn)
    model_plain: GNNs (dual readout, VN)
    value: 0.851
    std: 0.008
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01704'
    title: Transformers are efficient hierarchical chemical graph learners
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.851
    sort_std: 0.008
    is_best: false
  - model: MPNN + HOPE-WavePE
    model_key: mpnn + hope-wavepe
    model_plain: MPNN + HOPE-WavePE
    value: 0.78
    std: 0.001
    paper_value: 0.78
    paper_std: 0.001
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 18
    true_value: 0.78
    true_std: 0.001
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.78
    sort_std: 0.001
    is_best: false
  - model: PretrainGNN
    model_key: pretraingnn
    model_plain: PretrainGNN
    value: 0.767
    std: 0.004
    paper_value: 0.767
    paper_std: 0.004
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 30
    true_value: 0.767
    true_std: 0.004
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 30
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.767
    sort_std: 0.004
    is_best: false
  - model: AttentiveFP
    model_key: attentivefp
    model_plain: AttentiveFP
    value: 0.761
    std: 0.005
    paper_value: 0.761
    paper_std: 0.005
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 40
    true_value: 0.761
    true_std: 0.005
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 40
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.761
    sort_std: 0.005
    is_best: false
  - model: D-MPNN
    model_key: d-mpnn
    model_plain: D-MPNN
    value: 0.759
    std: 0.007
    paper_value: 0.759
    paper_std: 0.007
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 44
    true_value: 0.759
    true_std: 0.007
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 44
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.759
    sort_std: 0.007
    is_best: false
  - model: N-GramXGB
    model_key: n-gramxgb
    model_plain: N-GramXGB
    value: 0.758
    std: 0.009
    paper_value: 0.758
    paper_std: 0.009
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 46
    true_value: 0.758
    true_std: 0.009
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 46
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.758
    sort_std: 0.009
    is_best: false
  - model: N-GramRF
    model_key: n-gramrf
    model_plain: N-GramRF
    value: 0.743
    std: 0.004
    paper_value: 0.743
    paper_std: 0.004
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 61
    true_value: 0.743
    true_std: 0.004
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 61
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.743
    sort_std: 0.004
    is_best: false
  - model: GROVERbase
    model_key: groverbase
    model_plain: GROVERbase
    value: 0.743
    std: 0.001
    paper_value: 0.743
    paper_std: 0.001
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 62
    true_value: 0.743
    true_std: 0.001
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 62
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.743
    sort_std: 0.001
    is_best: false
  - model: GraphLOG pretrained
    model_key: graphlog pretrained
    model_plain: GraphLOG pretrained
    value: 0.739
    std: 0.007
    paper_value: 0.739
    paper_std: 0.007
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 68
    true_value: 0.739
    true_std: 0.007
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 68
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.739
    sort_std: 0.007
    is_best: false
  - model: GROVER_large
    model_key: grover_large
    model_plain: GROVER_large
    value: 0.735
    std: 0.001
    paper_value: 0.735
    paper_std: 0.001
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 71
    true_value: 0.735
    true_std: 0.001
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 71
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.735
    sort_std: 0.001
    is_best: false
  - model: InfoGraph pretrained
    model_key: infograph pretrained
    model_plain: InfoGraph pretrained
    value: 0.681
    std: 0.006
    paper_value: 0.681
    paper_std: 0.006
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 77
    true_value: 0.681
    true_std: 0.006
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 77
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.681
    sort_std: 0.006
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id015
  dataset: ToxCast
  rows:
  - model: Ours(dual readout)
    model_key: ours(dual readout)
    model_plain: Ours(dual readout)
    value: 0.752
    std: 0.003
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01704'
    title: Transformers are efficient hierarchical chemical graph learners
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.752
    sort_std: 0.003
    is_best: true
  - model: GNNs (dual readout, VN)
    model_key: gnns (dual readout, vn)
    model_plain: GNNs (dual readout, VN)
    value: 0.752
    std: 0.003
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01704'
    title: Transformers are efficient hierarchical chemical graph learners
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.752
    sort_std: 0.003
    is_best: true
  - model: Graph neural networks(dual readout,VN, 567k)
    model_key: graph neural networks(dual readout,vn, 567k)
    model_plain: Graph neural networks(dual readout,VN, 567k)
    value: 0.752
    std: 0.003
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01704'
    title: Transformers are efficient hierarchical chemical graph learners
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.752
    sort_std: 0.003
    is_best: true
  - model: MPNN + HOPE-WavePE
    model_key: mpnn + hope-wavepe
    model_plain: MPNN + HOPE-WavePE
    value: 0.669
    std: 0.005
    paper_value: 0.669
    paper_std: 0.005
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 14
    true_value: 0.669
    true_std: 0.005
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.669
    sort_std: 0.005
    is_best: false
  - model: PretrainGNN
    model_key: pretraingnn
    model_plain: PretrainGNN
    value: 0.657
    std: 0.006
    paper_value: 0.657
    paper_std: 0.006
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: strategies_pretrain
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 18
    true_value: 0.657
    true_std: 0.006
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.657
    sort_std: 0.006
    is_best: false
  - model: D-MPNN
    model_key: d-mpnn
    model_plain: D-MPNN
    value: 0.655
    std: 0.003
    paper_value: 0.655
    paper_std: 0.003
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Yang et al. 2019
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 20
    true_value: 0.655
    true_std: 0.003
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.655
    sort_std: 0.003
    is_best: false
  - model: GROVERbase
    model_key: groverbase
    model_plain: GROVERbase
    value: 0.654
    std: 0.004
    paper_value: 0.654
    paper_std: 0.004
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: GROVER
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 21
    true_value: 0.654
    true_std: 0.004
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.654
    sort_std: 0.004
    is_best: false
  - model: GROVER_large
    model_key: grover_large
    model_plain: GROVER_large
    value: 0.653
    std: 0.005
    paper_value: 0.653
    paper_std: 0.005
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: GROVER
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 22
    true_value: 0.653
    true_std: 0.005
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.653
    sort_std: 0.005
    is_best: false
  - model: AttentiveFP
    model_key: attentivefp
    model_plain: AttentiveFP
    value: 0.637
    std: 0.002
    paper_value: 0.637
    paper_std: 0.002
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xiong et al. 2019
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 36
    true_value: 0.637
    true_std: 0.002
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 36
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.637
    sort_std: 0.002
    is_best: false
  - model: GraphLOG pretrained
    model_key: graphlog pretrained
    model_plain: GraphLOG pretrained
    value: 0.624
    std: 0.006
    paper_value: 0.624
    paper_std: 0.006
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: GraphLog
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 49
    true_value: 0.624
    true_std: 0.006
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 49
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.624
    sort_std: 0.006
    is_best: false
  - model: InfoGraph pretrained
    model_key: infograph pretrained
    model_plain: InfoGraph pretrained
    value: 0.584
    std: 0.006
    paper_value: 0.584
    paper_std: 0.006
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: InfoGraph
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 53
    true_value: 0.584
    true_std: 0.006
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 53
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.584
    sort_std: 0.006
    is_best: false
  metric: ROC-AUC
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
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.526
    std: 0.051
    paper_value: 0.526
    paper_std: 0.051
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 75
    true_value: 0.065
    true_std: 0.004
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.461
    value_note: ''
    paper_rank: 293
    rank_delta: 218
    rank_delta_abs: 218
    rank_delta_direction: worse
    sort_value: 0.065
    sort_std: 0.004
    is_best: false
  - model: GPS + HOPE-WavePE
    model_key: gps + hope-wavepe
    model_plain: GPS + HOPE-WavePE
    value: 0.067
    std: 0.002
    paper_value: 0.067
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: default subset fallback'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 84
    true_value: 0.067
    true_std: 0.002
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 84
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.067
    sort_std: 0.002
    is_best: false
  - model: GPS + HOPE-WavePE
    model_key: gps + hope-wavepe
    model_plain: GPS + HOPE-WavePE
    value: 0.067
    std: 0.002
    paper_value: 0.067
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 84
    true_value: 0.067
    true_std: 0.002
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 84
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.067
    sort_std: 0.002
    is_best: false
  - model: GPS + (RWSE/LapPE)
    model_key: gps + (rwse/lappe)
    model_plain: GPS + (RWSE/LapPE)
    value: 0.07
    std: 0.004
    paper_value: 0.07
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 109
    true_value: 0.07
    true_std: 0.004
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 109
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.07
    sort_std: 0.004
    is_best: false
  - model: Graph MLP-Mixer
    model_key: graph mlp-mixer
    model_plain: Graph MLP-Mixer
    value: 0.077
    std: 0.003
    paper_value: 0.077
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 118
    true_value: 0.073
    true_std: 0.001
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0040000000000000036
    value_note: ''
    paper_rank: 131
    rank_delta: 13
    rank_delta_abs: 13
    rank_delta_direction: worse
    sort_value: 0.073
    sort_std: 0.001
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.282
    std: 0.015
    paper_value: 0.282
    paper_std: 0.015
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 132
    true_value: 0.077
    true_std: 0.005
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.20499999999999996
    value_note: ''
    paper_rank: 270
    rank_delta: 138
    rank_delta_abs: 138
    rank_delta_direction: worse
    sort_value: 0.077
    sort_std: 0.005
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.384
    std: 0.007
    paper_value: 0.384
    paper_std: 0.007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 142
    true_value: 0.0776354896230479
    true_std: 0.005512609666895327
    value_gap_source_arxiv: '2402.10793'
    value_gap_source_title: An end-to-end attention-based approach for learning on
      graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.3063645103769521
    value_note: ''
    paper_rank: 285
    rank_delta: 143
    rank_delta_abs: 143
    rank_delta_direction: worse
    sort_value: 0.0776354896230479
    sort_std: 0.005512609666895327
    is_best: false
  metric: MAE
  higher_is_better: false
- &id011
  dataset: ogbl-citation2
  rows:
  - model: HOPE-WavePE
    model_key: hope-wavepe
    model_plain: HOPE-WavePE
    value: 0.9912
    std: null
    paper_value: 0.9912
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: ''
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: null
    sort_value: 0.9912
    sort_std: null
    is_best: true
  - model: QGAT
    model_key: qgat
    model_plain: QGAT
    value: 0.822
    std: 0.0127
    metric: MRR
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.17630'
    title: 'Quantum Graph Attention Network: A Novel Quantum Multi-Head Attention
      Mechanism for Graph Learning'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.822
    sort_std: 0.0127
    is_best: false
  - model: GATv2
    model_key: gatv2
    model_plain: GATv2
    value: 0.8014
    std: 0.0071
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.17630'
    title: 'Quantum Graph Attention Network: A Novel Quantum Multi-Head Attention
      Mechanism for Graph Learning'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.8014
    sort_std: 0.0071
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.7595
    std: 0.0131
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.17630'
    title: 'Quantum Graph Attention Network: A Novel Quantum Multi-Head Attention
      Mechanism for Graph Learning'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.7595
    sort_std: 0.0131
    is_best: false
  metric: MRR
  higher_is_better: true
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
- benchmark: GNNBenchmark
  datasets:
  - *id009
  - *id010
- benchmark: OGB
  datasets:
  - *id011
- benchmark: MoleculeNet
  datasets:
  - *id012
  - *id013
  - *id014
  - *id015
  - *id016
main_figure: /figures/2409.19117/main_figure.png
---

