---
title: Graph Positional and Structural Encoder
arxiv_id: '2307.07107'
source_url: ''
authors: []
published_date: Jul 14, 2023
published_date_iso: '2023-07-14'
abstract: 'Positional and structural encodings (PSE) enable better identifiability
  of nodes within a graph, rendering them essential tools for empowering modern GNNs,
  and in particular graph Transformers. However, designing PSEs that work optimally
  for all graph prediction tasks is a challenging and unsolved problem. Here, we present
  the Graph Positional and Structural Encoder (GPSE), the first-ever graph encoder
  designed to capture rich PSE representations for augmenting any GNN. GPSE learns
  an efficient common latent representation for multiple PSEs, and is highly transferable:
  The encoder trained on a particular graph dataset can be used effectively on datasets
  drawn from markedly different distributions and modalities. We show that across
  a wide range of benchmarks, GPSE-enhanced models can significantly outperform those
  that employ explicitly computed PSEs, and at least match their performance in others.
  Our results pave the way for the development of foundational pre-trained graph encoders
  for extracting positional and structural information, and highlight their potential
  as a more powerful and efficient alternative to explicitly computed PSEs and existing
  self-supervised pre-training approaches. Our framework and pre-trained models are
  publicly available at https://github.com/G-Taxonomy-Workgroup/GPSE. For convenience,
  GPSE has also been integrated into the PyG library to facilitate downstream applications.'
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- GPSE + GCN
- GPSE + GPS
- GPS w/ Transformer
- GINE+GPSE
- GPSE augmented
- GPS+GPSE (LapPE & EigVals excluded)
- GPS+GPSE (ElstaticPE excluded)
- GPS+GPSE (RWSE excluded)
- GPS+GPSE (HKdiagSE excluded)
- GPS+GPSE (CycleSE excluded)
- GPSE-abs (default)
- GPSE-noabs
- GPSE-signinvar
- GPSE-SignNet
- SAGE+GPSE
- GAT(E)v2+GPSE
mrr: 0.0294
adjusted_mrr: 0.0294
mrr_dataset_count: 5
benchmark_categories:
- LRGB
- TU Dortmund
- GNNBenchmark
- OGB
- MoleculeNet
task_categories:
- graph_classification
- graph_regression
- node_classification
experiment_scopes:
- graph-level
- node-level
results:
- &id010
  dataset: BACE
  rows:
  - model: MPNN + HOPE-WavePE
    model_key: mpnn + hope-wavepe
    model_plain: MPNN + HOPE-WavePE
    value: 0.868
    std: 0.004
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.19117'
    title: 'Range-aware Positional Encoding via High-order Pretraining: Theory and
      Practice'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
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
  - model: GraphLoG
    model_key: graphlog
    model_plain: GraphLoG
    value: 0.835
    std: 0.012
    paper_value: 0.835
    paper_std: 0.012
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: xu 2021 self
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 6
    true_value: 0.835
    true_std: 0.012
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.835
    sort_std: 0.012
    is_best: false
  - model: GraphMAE
    model_key: graphmae
    model_plain: GraphMAE
    value: 0.831
    std: 0.009
    paper_value: 0.831
    paper_std: 0.009
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: hou 2022 graphmae
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 7
    true_value: 0.831
    true_std: 0.009
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.831
    sort_std: 0.009
    is_best: false
  - model: GraphLoG augmented
    model_key: graphlog augmented
    model_plain: GraphLoG augmented
    value: 0.825
    std: 0.012
    paper_value: 0.825
    paper_std: 0.012
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 13
    true_value: 0.825
    true_std: 0.012
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.825
    sort_std: 0.012
    is_best: false
  - model: GPSE augmented
    model_key: gpse augmented
    model_plain: GPSE augmented
    value: 0.808
    std: 0.031
    paper_value: 0.808
    paper_std: 0.031
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 18
    true_value: 0.808
    true_std: 0.031
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.808
    sort_std: 0.031
    is_best: false
  - model: LapPE augmented
    model_key: lappe augmented
    model_plain: LapPE augmented
    value: 0.804
    std: 0.015
    paper_value: 0.804
    paper_std: 0.015
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 23
    true_value: 0.804
    true_std: 0.015
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.804
    sort_std: 0.015
    is_best: false
  - model: Self-supervised pre-trained
    model_key: self-supervised pre-trained
    model_plain: Self-supervised pre-trained
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
    source_ref: Hu* 2020 Strategies
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 26
    true_value: 0.799
    true_std: 0.009
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.799
    sort_std: 0.009
    is_best: false
  - model: RWSE augmented
    model_key: rwse augmented
    model_plain: RWSE augmented
    value: 0.796
    std: 0.028
    paper_value: 0.796
    paper_std: 0.028
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 29
    true_value: 0.796
    true_std: 0.028
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.796
    sort_std: 0.028
    is_best: false
  - model: AllPSE augmented
    model_key: allpse augmented
    model_plain: AllPSE augmented
    value: 0.77
    std: 0.044
    paper_value: 0.77
    paper_std: 0.044
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 49
    true_value: 0.77
    true_std: 0.044
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 49
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.77
    sort_std: 0.044
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
    source_ref: you 2020 graph
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 54
    true_value: 0.754
    true_std: 0.014
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: false
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
  - model: No pre-training
    model_key: no pre-training
    model_plain: No pre-training
    value: 0.701
    std: 0.054
    paper_value: 0.701
    paper_std: 0.054
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hu* 2020 Strategies
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 60
    true_value: 0.701
    true_std: 0.054
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 60
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.701
    sort_std: 0.054
    is_best: false
  - model: JOAOv2 pre-trained
    model_key: joaov2 pre-trained
    model_plain: JOAOv2 pre-trained
    value: 0.674
    std: 0.007
    paper_value: 0.674
    paper_std: 0.007
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wang 2022 evaluating
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 61
    true_value: 0.674
    true_std: 0.007
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 61
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.674
    sort_std: 0.007
    is_best: false
  - model: InfoGraph pretrained
    model_key: infograph pretrained
    model_plain: InfoGraph pretrained
    value: 0.648
    std: 0.008
    paper_value: 0.648
    paper_std: 0.008
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wang 2022 evaluating
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 62
    true_value: 0.648
    true_std: 0.007
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: false
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
- &id012
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
    paper_value: 0.725
    paper_std: 0.008
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: xu 2021 self
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 3
    true_value: 0.725
    true_std: 0.008
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.725
    sort_std: 0.008
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.723
    std: 0.015
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.723
    sort_std: 0.015
    is_best: true
  - model: GraphMAE
    model_key: graphmae
    model_plain: GraphMAE
    value: 0.72
    std: 0.006
    paper_value: 0.72
    paper_std: 0.006
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: hou 2022 graphmae
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 6
    true_value: 0.72
    true_std: 0.006
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.72
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
    source_ref: you 2020 graph
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 25
    true_value: 0.697
    true_std: 0.007
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: false
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
  - model: SSL InfoMax pre-trained
    model_key: ssl infomax pre-trained
    model_plain: SSL InfoMax pre-trained
    value: 0.688
    std: 0.008
    paper_value: 0.688
    paper_std: 0.008
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hu* 2020 Strategies
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 29
    true_value: 0.688
    true_std: 0.008
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.688
    sort_std: 0.008
    is_best: false
  - model: SSL ContextPred pre-trained
    model_key: ssl contextpred pre-trained
    model_plain: SSL ContextPred pre-trained
    value: 0.68
    std: 0.02
    paper_value: 0.68
    paper_std: 0.02
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hu* 2020 Strategies
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 35
    true_value: 0.68
    true_std: 0.02
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.68
    sort_std: 0.02
    is_best: false
  - model: AllPSE augmented
    model_key: allpse augmented
    model_plain: AllPSE augmented
    value: 0.676
    std: 0.012
    paper_value: 0.676
    paper_std: 0.012
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 36
    true_value: 0.676
    true_std: 0.012
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 36
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.676
    sort_std: 0.012
    is_best: false
  - model: SSL EdgePred pre-trained
    model_key: ssl edgepred pre-trained
    model_plain: SSL EdgePred pre-trained
    value: 0.673
    std: 0.024
    paper_value: 0.673
    paper_std: 0.024
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hu* 2020 Strategies
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 37
    true_value: 0.673
    true_std: 0.024
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 37
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.673
    sort_std: 0.024
    is_best: false
  - model: LapPE augmented
    model_key: lappe augmented
    model_plain: LapPE augmented
    value: 0.671
    std: 0.016
    paper_value: 0.671
    paper_std: 0.016
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 39
    true_value: 0.671
    true_std: 0.016
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.671
    sort_std: 0.016
    is_best: false
  - model: RWSE augmented
    model_key: rwse augmented
    model_plain: RWSE augmented
    value: 0.67
    std: 0.014
    paper_value: 0.67
    paper_std: 0.014
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 41
    true_value: 0.67
    true_std: 0.014
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 41
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.67
    sort_std: 0.014
    is_best: false
  - model: JOAOv2 pre-trained
    model_key: joaov2 pre-trained
    model_plain: JOAOv2 pre-trained
    value: 0.664
    std: 0.009
    paper_value: 0.664
    paper_std: 0.009
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wang 2022 evaluating
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 43
    true_value: 0.664
    true_std: 0.009
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 43
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.664
    sort_std: 0.009
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
    source_ref: wang 2022 evaluating
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 45
    true_value: 0.663
    true_std: 0.006
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: false
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
  - model: GPSE augmented
    model_key: gpse augmented
    model_plain: GPSE augmented
    value: 0.662
    std: 0.009
    paper_value: 0.662
    paper_std: 0.009
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 46
    true_value: 0.662
    true_std: 0.009
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 46
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.662
    sort_std: 0.009
    is_best: false
  - model: No pre-training
    model_key: no pre-training
    model_plain: No pre-training
    value: 0.658
    std: 0.045
    paper_value: 0.658
    paper_std: 0.045
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hu* 2020 Strategies
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 47
    true_value: 0.658
    true_std: 0.045
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 47
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.658
    sort_std: 0.045
    is_best: false
  - model: GraphLoG augmented
    model_key: graphlog augmented
    model_plain: GraphLoG augmented
    value: 0.656
    std: 0.01
    paper_value: 0.656
    paper_std: 0.01
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 49
    true_value: 0.656
    true_std: 0.01
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 49
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.656
    sort_std: 0.01
    is_best: false
  - model: SSL AttrMasking pre-trained
    model_key: ssl attrmasking pre-trained
    model_plain: SSL AttrMasking pre-trained
    value: 0.643
    std: 0.028
    paper_value: 0.643
    paper_std: 0.028
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hu* 2020 Strategies
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 53
    true_value: 0.643
    true_std: 0.028
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 53
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.643
    sort_std: 0.028
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id003
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
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
  - model: GPSE + GPS
    model_key: gpse + gps
    model_plain: GPSE + GPS
    value: 0.7231
    std: 0.0025
    paper_value: 0.7231
    paper_std: 0.0025
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 58
    true_value: 0.7231
    true_std: 0.0025
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 58
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7231
    sort_std: 0.0025
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 61
    true_value: 0.723
    true_std: 0.0036
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: false
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
  - model: GPS+AllPSE
    model_key: gps+allpse
    model_plain: GPS+AllPSE
    value: 0.7205
    std: 0.0035
    paper_value: 0.7205
    paper_std: 0.0035
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 68
    true_value: 0.7205
    true_std: 0.0035
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 68
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7205
    sort_std: 0.0035
    is_best: false
  - model: GPS
    model_key: gps (none)
    model_plain: GPS
    value: 0.7167
    std: 0.0001
    paper_value: 0.7167
    paper_std: 0.0001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 75
    true_value: 0.7176
    true_std: 0.0001
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0009000000000000119
    value_note: ''
    paper_rank: 76
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
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
  metric: Accuracy
  higher_is_better: true
- &id005
  dataset: CSL
  rows:
  - model: GIN + RWSE
    model_key: gin + rwse
    model_plain: GIN + RWSE
    value: 1.0
    std: 0.0
    paper_value: 1.0
    paper_std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 14
    true_value: 1.0
    true_std: 0.0
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.0
    sort_std: 0.0
    is_best: true
  - model: B-method
    model_key: b-method
    model_plain: B-method
    value: 1.0
    std: null
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
    sort_value: 1.0
    sort_std: null
    is_best: true
  - model: R-method
    model_key: r-method
    model_plain: R-method
    value: 1.0
    std: null
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
    sort_value: 1.0
    sort_std: null
    is_best: true
  - model: Transformer+LapPE
    model_key: transformer+lappe
    model_plain: Transformer+LapPE
    value: 1.0
    std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.03380'
    title: On the Theoretical Expressive Power and the Design Space of Higher-Order
      Graph Transformers
    date: Apr 4, 2024
    date_display: Apr 2024
    date_iso: '2024-04-04'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 1.0
    sort_std: 0.0
    is_best: true
  - model: GINE + LapPE
    model_key: gine + lappe
    model_plain: GINE + LapPE
    value: 0.925
    std: 0.042
    paper_value: 0.925
    paper_std: 0.042
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 30
    true_value: 0.925
    true_std: 0.042
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 30
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.925
    sort_std: 0.042
    is_best: false
  - model: GINE+GPSE
    model_key: gine+gpse
    model_plain: GINE+GPSE
    value: 0.429
    std: 0.079
    paper_value: 0.429
    paper_std: 0.079
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 32
    true_value: 0.429
    true_std: 0.079
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.429
    sort_std: 0.079
    is_best: false
  - model: GIN+rand
    model_key: gin+rand
    model_plain: GIN+rand
    value: 0.127
    std: 0.064
    paper_value: 0.127
    paper_std: 0.064
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 36
    true_value: 0.127
    true_std: 0.064
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 36
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.127
    sort_std: 0.064
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.1
    std: 0.0
    paper_value: 0.1
    paper_std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 38
    true_value: 0.1
    true_std: 0.0
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1
    sort_std: 0.0
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id014
  dataset: ClinTox
  rows:
  - model: Supervised
    model_key: supervised
    model_plain: Supervised
    value: 0.8814
    std: 0.0251
    metric: ROC-AUC
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
    sort_value: 0.8814
    sort_std: 0.0251
    is_best: true
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.859
    std: 0.04
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.10651'
    title: Graph Learning via Logic-Based Weisfeiler--Leman Variants and Tabularization
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.859
    sort_std: 0.04
    is_best: true
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.859
    std: 0.04
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.10651'
    title: Graph Learning via Logic-Based Weisfeiler--Leman Variants and Tabularization
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.859
    sort_std: 0.04
    is_best: true
  - model: GraphMAE
    model_key: graphmae
    model_plain: GraphMAE
    value: 0.823
    std: 0.012
    paper_value: 0.823
    paper_std: 0.012
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hou 2022
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 6
    true_value: 0.8269
    true_std: 0.0339
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0039000000000000146
    value_note: global 0.8269 within std
    paper_rank: 7
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.8269
    sort_std: 0.0339
    is_best: true
  - model: GPSE augmented
    model_key: gpse augmented
    model_plain: GPSE augmented
    value: 0.788
    std: 0.038
    paper_value: 0.788
    paper_std: 0.038
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 15
    true_value: 0.788
    true_std: 0.038
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.788
    sort_std: 0.038
    is_best: false
  - model: GraphLoG
    model_key: graphlog
    model_plain: GraphLoG
    value: 0.767
    std: 0.033
    paper_value: 0.767
    paper_std: 0.033
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xu 2021
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 18
    true_value: 0.767
    true_std: 0.033
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.767
    sort_std: 0.033
    is_best: false
  - model: LapPE augmented
    model_key: lappe augmented
    model_plain: LapPE augmented
    value: 0.764
    std: 0.023
    paper_value: 0.764
    paper_std: 0.023
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 19
    true_value: 0.764
    true_std: 0.023
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.764
    sort_std: 0.023
    is_best: false
  - model: GraphLOG pretrained
    model_key: graphlog pretrained
    model_plain: GraphLOG pretrained
    value: 0.76
    std: 0.027
    paper_value: 0.76
    paper_std: 0.027
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: You 2020
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 21
    true_value: 0.76
    true_std: 0.027
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.76
    sort_std: 0.027
    is_best: false
  - model: RWSE augmented
    model_key: rwse augmented
    model_plain: RWSE augmented
    value: 0.745
    std: 0.044
    paper_value: 0.745
    paper_std: 0.044
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 24
    true_value: 0.745
    true_std: 0.044
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.745
    sort_std: 0.044
    is_best: false
  - model: AllPSE augmented
    model_key: allpse augmented
    model_plain: AllPSE augmented
    value: 0.726
    std: 0.043
    paper_value: 0.726
    paper_std: 0.043
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 26
    true_value: 0.726
    true_std: 0.043
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.726
    sort_std: 0.043
    is_best: false
  - model: GraphLoG augmented
    model_key: graphlog augmented
    model_plain: GraphLoG augmented
    value: 0.725
    std: 0.035
    paper_value: 0.725
    paper_std: 0.035
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 27
    true_value: 0.725
    true_std: 0.035
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 27
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.725
    sort_std: 0.035
    is_best: false
  - model: SSL AttrMasking pre-trained
    model_key: ssl attrmasking pre-trained
    model_plain: SSL AttrMasking pre-trained
    value: 0.718
    std: 0.041
    paper_value: 0.718
    paper_std: 0.041
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Hu 2020
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 30
    true_value: 0.718
    true_std: 0.041
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 30
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.718
    sort_std: 0.041
    is_best: false
  - model: SSL InfoMax pre-trained
    model_key: ssl infomax pre-trained
    model_plain: SSL InfoMax pre-trained
    value: 0.699
    std: 0.003
    paper_value: 0.699
    paper_std: 0.003
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Hu 2020
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 34
    true_value: 0.699
    true_std: 0.003
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 34
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.699
    sort_std: 0.003
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
    source_ref: Wang 2022
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 41
    true_value: 0.663
    true_std: 0.006
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 41
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.663
    sort_std: 0.006
    is_best: false
  - model: SSL ContextPred pre-trained
    model_key: ssl contextpred pre-trained
    model_plain: SSL ContextPred pre-trained
    value: 0.659
    std: 0.038
    paper_value: 0.659
    paper_std: 0.038
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Hu 2020
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 43
    true_value: 0.659
    true_std: 0.038
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 43
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.659
    sort_std: 0.038
    is_best: false
  - model: JOAOv2 pre-trained
    model_key: joaov2 pre-trained
    model_plain: JOAOv2 pre-trained
    value: 0.645
    std: 0.009
    paper_value: 0.645
    paper_std: 0.009
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Wang 2022
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 47
    true_value: 0.645
    true_std: 0.009
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 47
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.645
    sort_std: 0.009
    is_best: false
  - model: SSL EdgePred pre-trained
    model_key: ssl edgepred pre-trained
    model_plain: SSL EdgePred pre-trained
    value: 0.641
    std: 0.037
    paper_value: 0.641
    paper_std: 0.037
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Hu 2020
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 48
    true_value: 0.641
    true_std: 0.037
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 48
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.641
    sort_std: 0.037
    is_best: false
  - model: No pre-training
    model_key: no pre-training
    model_plain: No pre-training
    value: 0.58
    std: 0.044
    paper_value: 0.58
    paper_std: 0.044
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hu 2020
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 52
    true_value: 0.58
    true_std: 0.044
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 52
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.58
    sort_std: 0.044
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id004
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
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
  - model: GPSE + GPS
    model_key: gpse + gps
    model_plain: GPSE + GPS
    value: 0.9808
    std: 0.0013
    paper_value: 0.9808
    paper_std: 0.0013
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 59
    true_value: 0.98105
    true_std: 0.00158
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.00024999999999997247
    value_note: global 0.9810 within std
    paper_rank: 60
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.98105
    sort_std: 0.00158
    is_best: false
  - model: GPS+AllPSE
    model_key: gps+allpse
    model_plain: GPS+AllPSE
    value: 0.9808
    std: 0.0012
    paper_value: 0.9808
    paper_std: 0.0012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 61
    true_value: 0.9808
    true_std: 0.0012
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 61
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9808
    sort_std: 0.0012
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 66
    true_value: 0.9805
    true_std: 0.0
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: false
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 67
    true_value: 0.9805
    true_std: 0.0013
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: false
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
  metric: Accuracy
  higher_is_better: true
- &id009
  dataset: PCQM4Mv2
  rows:
  - model: GRIT-SPSE
    model_key: grit-spse
    model_plain: GRIT-SPSE
    value: 0.0831
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09365'
    title: Simple Path Structural Encoding for Graph Transformers
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.0831
    sort_std: null
    is_best: true
  - model: GRIT-RWSE
    model_key: grit-rwse
    model_plain: GRIT-RWSE
    value: 0.0838
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09365'
    title: Simple Path Structural Encoding for Graph Transformers
    date: Feb 13, 2025
    date_display: Feb 2025
    date_iso: '2025-02-13'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.0838
    sort_std: null
    is_best: false
  - model: GRIT 2-QiQRW
    model_key: grit 2-qiqrw
    model_plain: GRIT 2-QiQRW
    value: 0.0838
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.20519'
    title: Enhancing Graph Neural Networks with Quantum Computed Encodings
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.0838
    sort_std: null
    is_best: false
  - model: GPSE + GPS
    model_key: gpse + gps
    model_plain: GPSE + GPS
    value: 0.1196
    std: 0.0004
    paper_value: 0.1196
    paper_std: 0.0004
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 19
    true_value: 0.0934
    true_std: null
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0262
    value_note: ''
    paper_rank: 35
    rank_delta: 16
    rank_delta_abs: 16
    rank_delta_direction: worse
    sort_value: 0.0934
    sort_std: null
    is_best: false
  - model: GPSE (Not finetuned)
    model_key: gpse (not finetuned)
    model_plain: GPSE (Not finetuned)
    value: 0.1195
    std: 0.0007
    paper_value: 0.1195
    paper_std: 0.0007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 35
    true_value: 0.1195
    true_std: 0.0007
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1195
    sort_std: 0.0007
    is_best: false
  - model: GPSE (default)
    model_key: gpse (default)
    model_plain: GPSE (default)
    value: 0.1216
    std: 0.0002
    paper_value: 0.1216
    paper_std: 0.0002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 38
    true_value: 0.1216
    true_std: 0.0002
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1216
    sort_std: 0.0002
    is_best: false
  - model: GPS+RWSE
    model_key: gps+rwse
    model_plain: GPS+RWSE
    value: 0.123
    std: 0.0008
    paper_value: 0.123
    paper_std: 0.0008
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 40
    true_value: 0.123
    true_std: 0.0008
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 40
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.123
    sort_std: 0.0008
    is_best: false
  - model: GPS+AllPSE
    model_key: gps+allpse
    model_plain: GPS+AllPSE
    value: 0.1254
    std: 0.0011
    paper_value: 0.1254
    paper_std: 0.0011
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 41
    true_value: 0.1254
    true_std: 0.0011
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 41
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1254
    sort_std: 0.0011
    is_best: false
  - model: GPS+LapPE
    model_key: gps+lappe
    model_plain: GPS+LapPE
    value: 0.1267
    std: 0.0004
    paper_value: 0.1267
    paper_std: 0.0004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 42
    true_value: 0.1267
    true_std: 0.0004
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 42
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1267
    sort_std: 0.0004
    is_best: false
  - model: GPS + (RWSE/LapPE)
    model_key: gps + (rwse/lappe)
    model_plain: GPS + (RWSE/LapPE)
    value: 0.1273
    std: 0.0006
    paper_value: 0.1273
    paper_std: 0.0006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 43
    true_value: 0.1273
    true_std: 0.0006
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 43
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1273
    sort_std: 0.0006
    is_best: false
  - model: GINE+GPSE
    model_key: gine+gpse
    model_plain: GINE+GPSE
    value: 0.1294
    std: 0.0006
    paper_value: 0.1294
    paper_std: 0.0006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 44
    true_value: 0.1294
    true_std: 0.0006
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 44
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1294
    sort_std: 0.0006
    is_best: false
  - model: GPS
    model_key: gps (none)
    model_plain: GPS
    value: 0.1329
    std: 0.003
    paper_value: 0.1329
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 45
    true_value: 0.1329
    true_std: 0.003
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 45
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1329
    sort_std: 0.003
    is_best: false
  - model: GatedGCN+GPSE
    model_key: gatedgcn+gpse
    model_plain: GatedGCN+GPSE
    value: 0.1495
    std: 0.0015
    paper_value: 0.1495
    paper_std: 0.0015
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 47
    true_value: 0.1495
    true_std: 0.0015
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 47
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1495
    sort_std: 0.0015
    is_best: false
  - model: GPSE + GCN
    model_key: gpse + gcn
    model_plain: GPSE + GCN
    value: 0.1615
    std: 0.0015
    paper_value: 0.1615
    paper_std: 0.0015
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 48
    true_value: 0.1615
    true_std: 0.0015
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 48
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1615
    sort_std: 0.0015
    is_best: false
  - model: GPS w/ Transformer
    model_key: gps w/ transformer
    model_plain: GPS w/ Transformer
    value: 0.1805
    std: 0.0021
    paper_value: 0.1805
    paper_std: 0.0021
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 49
    true_value: 0.1805
    true_std: 0.0021
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 49
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1805
    sort_std: 0.0021
    is_best: false
  - model: GPS+rand
    model_key: gps+rand
    model_plain: GPS+rand
    value: 0.4768
    std: 0.0171
    paper_value: 0.4768
    paper_std: 0.0171
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 50
    true_value: 0.4768
    true_std: 0.0171
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 50
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4768
    sort_std: 0.0171
    is_best: false
  metric: MAE
  higher_is_better: false
- &id002
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
  - model: GAT(E)v2+GPSE
    model_key: gat(e)v2+gpse
    model_plain: GAT(E)v2+GPSE
    value: 0.8351
    std: 0.0011
    paper_value: 0.8351
    paper_std: 0.0011
    metric: AUROC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: null
    sort_value: 0.8351
    sort_std: 0.0011
    is_best: true
  - model: GAT(E)v2+none
    model_key: gat(e)v2+none
    model_plain: GAT(E)v2+none
    value: 0.8347
    std: 0.0013
    paper_value: 0.8347
    paper_std: 0.0013
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: null
    sort_value: 0.8347
    sort_std: 0.0013
    is_best: true
  - model: GAT(E)v2+LapPE
    model_key: gat(e)v2+lappe
    model_plain: GAT(E)v2+LapPE
    value: 0.8325
    std: 0.0005
    paper_value: 0.8325
    paper_std: 0.0005
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: null
    sort_value: 0.8325
    sort_std: 0.0005
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
  - model: GCN
    model_key: gcn (none)
    model_plain: GCN
    value: 0.8044
    std: 0.0056
    paper_value: 0.8044
    paper_std: 0.0056
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 167
    sort_value: 0.8044
    sort_std: 0.0056
    is_best: true
  - model: GCN+LapPE
    model_key: gcn+lappe
    model_plain: GCN+LapPE
    value: 0.8038
    std: 0.0016
    paper_value: 0.8038
    paper_std: 0.0016
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: null
    sort_value: 0.8038
    sort_std: 0.0016
    is_best: false
  - model: SAGE+none
    model_key: sage+none
    model_plain: SAGE+none
    value: 0.8035
    std: 0.0007
    paper_value: 0.8035
    paper_std: 0.0007
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: null
    sort_value: 0.8035
    sort_std: 0.0007
    is_best: false
  - model: SAGE+LapPE
    model_key: sage+lappe
    model_plain: SAGE+LapPE
    value: 0.8027
    std: 0.0045
    paper_value: 0.8027
    paper_std: 0.0045
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: null
    sort_value: 0.8027
    sort_std: 0.0045
    is_best: false
  - model: GPSE + GCN
    model_key: gpse + gcn
    model_plain: GPSE + GCN
    value: 0.8025
    std: 0.0019
    paper_value: 0.8025
    paper_std: 0.0019
    metric: AUROC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 45
    sort_value: 0.8025
    sort_std: 0.0019
    is_best: false
  - model: SAGE+GPSE
    model_key: sage+gpse
    model_plain: SAGE+GPSE
    value: 0.8014
    std: 0.0022
    paper_value: 0.8014
    paper_std: 0.0022
    metric: AUROC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: null
    sort_value: 0.8014
    sort_std: 0.0022
    is_best: false
  - model: GPS w/ Transformer
    model_key: gps w/ transformer
    model_plain: GPS w/ Transformer
    value: 0.7467
    std: 0.0074
    paper_value: 0.7467
    paper_std: 0.0074
    metric: AUROC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: null
    sort_value: 0.7467
    sort_std: 0.0074
    is_best: false
  - model: Transformer+LapPE
    model_key: transformer+lappe
    model_plain: Transformer+LapPE
    value: 0.7405
    std: 0.0011
    paper_value: 0.7405
    paper_std: 0.0011
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: null
    sort_value: 0.7405
    sort_std: 0.0011
    is_best: false
  - model: Transformer+none
    model_key: transformer+none
    model_plain: Transformer+none
    value: 0.7393
    std: 0.0144
    paper_value: 0.7393
    paper_std: 0.0144
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: null
    sort_value: 0.7393
    sort_std: 0.0144
    is_best: false
  - model: GPSE + GPS
    model_key: gpse + gps
    model_plain: GPSE + GPS
    value: 0.7205
    std: 0.0375
    paper_value: 0.7205
    paper_std: 0.0375
    metric: AUROC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: null
    sort_value: 0.7205
    sort_std: 0.0375
    is_best: false
  - model: GPS+LapPE
    model_key: gps+lappe
    model_plain: GPS+LapPE
    value: 0.708
    std: 0.0414
    paper_value: 0.708
    paper_std: 0.0414
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: null
    sort_value: 0.708
    sort_std: 0.0414
    is_best: false
  - model: GPS
    model_key: gps (none)
    model_plain: GPS
    value: 0.6955
    std: 0.0567
    paper_value: 0.6955
    paper_std: 0.0567
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: null
    sort_value: 0.6955
    sort_std: 0.0567
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id001
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
    table_ref: Table 1
    source_ref: Bresson et al. 2017
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
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
  - model: Drew-GIN
    model_key: drew-gin
    model_plain: Drew-GIN
    value: 0.6996
    std: 0.0076
    paper_value: 0.6996
    paper_std: 0.0076
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Gutteridge et al. 2023
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 50
    true_value: 0.6996
    true_std: 0.0076
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 50
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6996
    sort_std: 0.0076
    is_best: false
  - model: Graph MLP-Mixer
    model_key: graph mlp-mixer
    model_plain: Graph MLP-Mixer
    value: 0.692
    std: 0.0054
    paper_value: 0.692
    paper_std: 0.0054
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: He et al. 2022
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 63
    true_value: 0.697
    true_std: 0.008
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0050000000000000044
    value_note: global 0.6970 within std
    paper_rank: 79
    rank_delta: 16
    rank_delta_abs: 16
    rank_delta_direction: worse
    sort_value: 0.697
    sort_std: 0.008
    is_best: false
  - model: R-GCN (RWSE)
    model_key: r-gcn (rwse)
    model_plain: R-GCN (RWSE)
    value: 0.6067
    std: 0.0069
    paper_value: 0.6067
    paper_std: 0.0069
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 89
    true_value: 0.686
    true_std: 0.005
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07930000000000004
    value_note: ''
    paper_rank: 241
    rank_delta: 152
    rank_delta_abs: 152
    rank_delta_direction: worse
    sort_value: 0.686
    sort_std: 0.005
    is_best: false
  - model: PR-MPNN
    model_key: pr-mpnn
    model_plain: PR-MPNN
    value: 0.6825
    std: 0.0086
    paper_value: 0.6825
    paper_std: 0.0086
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Qian et al. 2023
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 98
    true_value: 0.6825
    true_std: 0.0086
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 98
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6825
    sort_std: 0.0086
    is_best: false
  - model: GPSE + GPS
    model_key: gpse + gps
    model_plain: GPSE + GPS
    value: 0.6688
    std: 0.0151
    paper_value: 0.6688
    paper_std: 0.0151
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 130
    true_value: 0.6688
    true_std: 0.0151
    value_gap_source_arxiv: '2510.02565'
    value_gap_source_title: On The Expressive Power of GNN Derivatives
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 130
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6688
    sort_std: 0.0151
    is_best: false
  - model: GPSE-noabs
    model_key: gpse-noabs
    model_plain: GPSE-noabs
    value: 0.6687
    std: 0.0119
    paper_value: 0.6687
    paper_std: 0.0119
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 131
    true_value: 0.6687
    true_std: 0.0119
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 131
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6687
    sort_std: 0.0119
    is_best: false
  - model: GPSE-SignNet
    model_key: gpse-signnet
    model_plain: GPSE-SignNet
    value: 0.6647
    std: 0.0093
    paper_value: 0.6647
    paper_std: 0.0093
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 137
    true_value: 0.6647
    true_std: 0.0093
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 137
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6647
    sort_std: 0.0093
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
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
  - model: GPSE-signinvar
    model_key: gpse-signinvar
    model_plain: GPSE-signinvar
    value: 0.6619
    std: 0.0097
    paper_value: 0.6619
    paper_std: 0.0097
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 147
    true_value: 0.6619
    true_std: 0.0097
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 147
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6619
    sort_std: 0.0097
    is_best: false
  - model: GPSE-abs (default)
    model_key: gpse-abs (default)
    model_plain: GPSE-abs (default)
    value: 0.6584
    std: 0.0042
    paper_value: 0.6584
    paper_std: 0.0042
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 161
    true_value: 0.6584
    true_std: 0.0042
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 161
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6584
    sort_std: 0.0042
    is_best: false
  - model: GPS + (RWSE/LapPE)
    model_key: gps + (rwse/lappe)
    model_plain: GPS + (RWSE/LapPE)
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
    table_ref: Table 1
    source_ref: Rampásek et al. 2022
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 172
    true_value: 0.6535
    true_std: 0.0041
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 172
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6535
    sort_std: 0.0041
    is_best: false
  - model: GPS+AllPSE
    model_key: gps+allpse
    model_plain: GPS+AllPSE
    value: 0.6397
    std: 0.0092
    paper_value: 0.6397
    paper_std: 0.0092
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 210
    true_value: 0.6397
    true_std: 0.0092
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 210
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6397
    sort_std: 0.0092
    is_best: false
  - model: GPSE + GCN
    model_key: gpse + gcn
    model_plain: GPSE + GCN
    value: 0.6316
    std: 0.0085
    paper_value: 0.6316
    paper_std: 0.0085
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 222
    true_value: 0.6316
    true_std: 0.0085
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 222
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6316
    sort_std: 0.0085
    is_best: false
  - model: GPS
    model_key: gps (none)
    model_plain: GPS
    value: 0.6231
    std: 0.0252
    paper_value: 0.6231
    paper_std: 0.0252
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 231
    true_value: 0.6231
    true_std: 0.0252
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 231
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6231
    sort_std: 0.0252
    is_best: false
  - model: GCN+LapPE
    model_key: gcn+lappe
    model_plain: GCN+LapPE
    value: 0.6218
    std: 0.0055
    paper_value: 0.6218
    paper_std: 0.0055
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tönshoff et al. 2023
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 233
    true_value: 0.6218
    true_std: 0.0055
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 233
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6218
    sort_std: 0.0055
    is_best: false
  metric: AP
  higher_is_better: true
- &id015
  dataset: SIDER
  rows:
  - model: N-GramRF
    model_key: n-gramrf
    model_plain: N-GramRF
    value: 0.668
    std: 0.007
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.19117'
    title: 'Range-aware Positional Encoding via High-order Pretraining: Theory and
      Practice'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.668
    sort_std: 0.007
    is_best: true
  - model: N-GramXGB
    model_key: n-gramxgb
    model_plain: N-GramXGB
    value: 0.655
    std: 0.007
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.19117'
    title: 'Range-aware Positional Encoding via High-order Pretraining: Theory and
      Practice'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.655
    sort_std: 0.007
    is_best: true
  - model: GROVER_large
    model_key: grover_large
    model_plain: GROVER_large
    value: 0.654
    std: 0.001
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.19117'
    title: 'Range-aware Positional Encoding via High-order Pretraining: Theory and
      Practice'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    codebase_url: ''
    uses_external_data: true
    is_global_top: true
    global_rank: 3
    sort_value: 0.654
    sort_std: 0.001
    is_best: false
  - model: AllPSE augmented
    model_key: allpse augmented
    model_plain: AllPSE augmented
    value: 0.63
    std: 0.006
    paper_value: 0.63
    paper_std: 0.006
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 10
    true_value: 0.63
    true_std: 0.006
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.63
    sort_std: 0.006
    is_best: false
  - model: GraphLoG
    model_key: graphlog
    model_plain: GraphLoG
    value: 0.612
    std: 0.011
    paper_value: 0.612
    paper_std: 0.011
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: xu 2021 self
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 19
    true_value: 0.612
    true_std: 0.011
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.612
    sort_std: 0.011
    is_best: false
  - model: GPSE augmented
    model_key: gpse augmented
    model_plain: GPSE augmented
    value: 0.611
    std: 0.016
    paper_value: 0.611
    paper_std: 0.016
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 21
    true_value: 0.611
    true_std: 0.016
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.611
    sort_std: 0.016
    is_best: false
  - model: Self-supervised pre-trained
    model_key: self-supervised pre-trained
    model_plain: Self-supervised pre-trained
    value: 0.61
    std: 0.007
    paper_value: 0.61
    paper_std: 0.007
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hu* 2020 Strategies
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 24
    true_value: 0.61
    true_std: 0.007
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.61
    sort_std: 0.007
    is_best: false
  - model: GraphLoG augmented
    model_key: graphlog augmented
    model_plain: GraphLoG augmented
    value: 0.609
    std: 0.007
    paper_value: 0.609
    paper_std: 0.007
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 27
    true_value: 0.609
    true_std: 0.007
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 27
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.609
    sort_std: 0.007
    is_best: false
  - model: GraphMAE
    model_key: graphmae
    model_plain: GraphMAE
    value: 0.603
    std: 0.011
    paper_value: 0.603
    paper_std: 0.011
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: hou 2022 graphmae
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 31
    true_value: 0.605
    true_std: 0.012
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0020000000000000018
    value_note: global 0.6050 within std
    paper_rank: 34
    rank_delta: 3
    rank_delta_abs: 3
    rank_delta_direction: worse
    sort_value: 0.605
    sort_std: 0.012
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
    source_ref: you 2020 graph
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 30
    true_value: 0.605
    true_std: 0.009
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: false
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
  - model: LapPE augmented
    model_key: lappe augmented
    model_plain: LapPE augmented
    value: 0.593
    std: 0.017
    paper_value: 0.593
    paper_std: 0.017
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 38
    true_value: 0.593
    true_std: 0.017
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.593
    sort_std: 0.017
    is_best: false
  - model: JOAOv2 pre-trained
    model_key: joaov2 pre-trained
    model_plain: JOAOv2 pre-trained
    value: 0.591
    std: 0.007
    paper_value: 0.591
    paper_std: 0.007
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wang 2022 evaluating
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 39
    true_value: 0.591
    true_std: 0.007
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.591
    sort_std: 0.007
    is_best: false
  - model: RWSE augmented
    model_key: rwse augmented
    model_plain: RWSE augmented
    value: 0.585
    std: 0.014
    paper_value: 0.585
    paper_std: 0.014
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 41
    true_value: 0.585
    true_std: 0.014
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 41
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.585
    sort_std: 0.014
    is_best: false
  - model: No pre-training
    model_key: no pre-training
    model_plain: No pre-training
    value: 0.573
    std: 0.016
    paper_value: 0.573
    paper_std: 0.016
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hu* 2020 Strategies
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 44
    true_value: 0.573
    true_std: 0.016
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 44
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.573
    sort_std: 0.016
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
    source_ref: wang 2022 evaluating
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 45
    true_value: 0.571
    true_std: 0.008
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: false
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
  metric: ROC-AUC
  higher_is_better: true
- &id011
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
  - model: GPSE augmented
    model_key: gpse augmented
    model_plain: GPSE augmented
    value: 0.774
    std: 0.008
    paper_value: 0.774
    paper_std: 0.008
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 23
    true_value: 0.774
    true_std: 0.008
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.774
    sort_std: 0.008
    is_best: false
  - model: Self-supervised pre-trained
    model_key: self-supervised pre-trained
    model_plain: Self-supervised pre-trained
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
    source_ref: Hu* 2020 Strategies
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 32
    true_value: 0.767
    true_std: 0.004
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.767
    sort_std: 0.004
    is_best: false
  - model: LapPE augmented
    model_key: lappe augmented
    model_plain: LapPE augmented
    value: 0.766
    std: 0.003
    paper_value: 0.766
    paper_std: 0.003
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 35
    true_value: 0.766
    true_std: 0.003
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.766
    sort_std: 0.003
    is_best: false
  - model: RWSE augmented
    model_key: rwse augmented
    model_plain: RWSE augmented
    value: 0.763
    std: 0.005
    paper_value: 0.763
    paper_std: 0.005
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 38
    true_value: 0.763
    true_std: 0.005
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.763
    sort_std: 0.005
    is_best: false
  - model: AllPSE augmented
    model_key: allpse augmented
    model_plain: AllPSE augmented
    value: 0.759
    std: 0.01
    paper_value: 0.759
    paper_std: 0.01
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 45
    true_value: 0.759
    true_std: 0.01
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 45
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.759
    sort_std: 0.01
    is_best: false
  - model: GraphLoG
    model_key: graphlog
    model_plain: GraphLoG
    value: 0.757
    std: 0.005
    paper_value: 0.757
    paper_std: 0.005
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: xu 2021 self
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 49
    true_value: 0.757
    true_std: 0.005
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 49
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.757
    sort_std: 0.005
    is_best: false
  - model: GraphMAE
    model_key: graphmae
    model_plain: GraphMAE
    value: 0.755
    std: 0.006
    paper_value: 0.755
    paper_std: 0.006
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: hou 2022 graphmae
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 51
    true_value: 0.755
    true_std: 0.006
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 51
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.755
    sort_std: 0.006
    is_best: false
  - model: No pre-training
    model_key: no pre-training
    model_plain: No pre-training
    value: 0.74
    std: 0.008
    paper_value: 0.74
    paper_std: 0.008
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hu* 2020 Strategies
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 67
    true_value: 0.74
    true_std: 0.008
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 67
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.74
    sort_std: 0.008
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
    source_ref: you 2020 graph
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 68
    true_value: 0.739
    true_std: 0.007
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: false
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
  - model: GraphLoG augmented
    model_key: graphlog augmented
    model_plain: GraphLoG augmented
    value: 0.732
    std: 0.005
    paper_value: 0.732
    paper_std: 0.005
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 73
    true_value: 0.732
    true_std: 0.005
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 73
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.732
    sort_std: 0.005
    is_best: false
  - model: JOAOv2 pre-trained
    model_key: joaov2 pre-trained
    model_plain: JOAOv2 pre-trained
    value: 0.682
    std: 0.008
    paper_value: 0.682
    paper_std: 0.008
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wang 2022 evaluating
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 76
    true_value: 0.682
    true_std: 0.008
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 76
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.682
    sort_std: 0.008
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
    source_ref: wang 2022 evaluating
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 77
    true_value: 0.681
    true_std: 0.006
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: false
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
- &id013
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
  - model: GPSE augmented
    model_key: gpse augmented
    model_plain: GPSE augmented
    value: 0.663
    std: 0.008
    paper_value: 0.663
    paper_std: 0.008
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 15
    true_value: 0.663
    true_std: 0.008
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.663
    sort_std: 0.008
    is_best: false
  - model: LapPE augmented
    model_key: lappe augmented
    model_plain: LapPE augmented
    value: 0.659
    std: 0.007
    paper_value: 0.659
    paper_std: 0.007
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 17
    true_value: 0.659
    true_std: 0.007
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.659
    sort_std: 0.007
    is_best: false
  - model: RWSE augmented
    model_key: rwse augmented
    model_plain: RWSE augmented
    value: 0.656
    std: 0.003
    paper_value: 0.656
    paper_std: 0.003
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 19
    true_value: 0.656
    true_std: 0.003
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.656
    sort_std: 0.003
    is_best: false
  - model: Self-supervised pre-trained
    model_key: self-supervised pre-trained
    model_plain: Self-supervised pre-trained
    value: 0.642
    std: 0.005
    paper_value: 0.642
    paper_std: 0.005
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hu 2020
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 27
    true_value: 0.642
    true_std: 0.005
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 27
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.642
    sort_std: 0.005
    is_best: false
  - model: GraphMAE
    model_key: graphmae
    model_plain: GraphMAE
    value: 0.641
    std: 0.003
    paper_value: 0.641
    paper_std: 0.003
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hou 2022
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 28
    true_value: 0.641
    true_std: 0.003
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 28
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.641
    sort_std: 0.003
    is_best: false
  - model: AllPSE augmented
    model_key: allpse augmented
    model_plain: AllPSE augmented
    value: 0.639
    std: 0.003
    paper_value: 0.639
    paper_std: 0.003
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 34
    true_value: 0.639
    true_std: 0.003
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 34
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.639
    sort_std: 0.003
    is_best: false
  - model: GraphLoG augmented
    model_key: graphlog augmented
    model_plain: GraphLoG augmented
    value: 0.636
    std: 0.004
    paper_value: 0.636
    paper_std: 0.004
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 37
    true_value: 0.636
    true_std: 0.004
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 37
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.636
    sort_std: 0.004
    is_best: false
  - model: GraphLoG
    model_key: graphlog
    model_plain: GraphLoG
    value: 0.635
    std: 0.007
    paper_value: 0.635
    paper_std: 0.007
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xu 2021
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 38
    true_value: 0.635
    true_std: 0.007
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.635
    sort_std: 0.007
    is_best: false
  - model: No pre-training
    model_key: no pre-training
    model_plain: No pre-training
    value: 0.634
    std: 0.006
    paper_value: 0.634
    paper_std: 0.006
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hu 2020
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 39
    true_value: 0.634
    true_std: 0.006
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.634
    sort_std: 0.006
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
    source_ref: You 2020
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 49
    true_value: 0.624
    true_std: 0.006
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
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
    source_ref: Wang 2022
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 53
    true_value: 0.584
    true_std: 0.006
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
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
  - model: JOAOv2 pre-trained
    model_key: joaov2 pre-trained
    model_plain: JOAOv2 pre-trained
    value: 0.57
    std: 0.005
    paper_value: 0.57
    paper_std: 0.005
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Wang 2022
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 54
    true_value: 0.57
    true_std: 0.005
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 54
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.57
    sort_std: 0.005
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id006
  dataset: ogbg-molhiv
  rows:
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.9685
    std: 0.0001
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.16767'
    title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed Graphs as
      Effectively as We Expected'
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.9685
    sort_std: 0.0001
    is_best: true
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.9682
    std: 0.0003
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.16767'
    title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed Graphs as
      Effectively as We Expected'
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.9682
    sort_std: 0.0003
    is_best: true
  - model: SigGate-GT
    model_key: siggate-gt
    model_plain: SigGate-GT
    value: 0.8247
    std: 0.0063
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.17324'
    title: 'SigGate-GT: Taming Over-Smoothing in Graph Transformers via Sigmoid-Gated
      Attention'
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    codebase_url: https://github.com/bettyguo/SigGate-GT
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    sort_value: 0.8247
    sort_std: 0.0063
    is_best: false
  - model: CIN
    model_key: cin
    model_plain: CIN
    value: 0.8094
    std: 0.0057
    paper_value: 0.8094
    paper_std: 0.0057
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Bodnar 2021
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 9
    sort_value: 0.8094
    sort_std: 0.0057
    is_best: false
  - model: PR-MPNN_Sim
    model_key: pr-mpnn_sim
    model_plain: PR-MPNN_Sim
    value: 0.795
    std: 0.009
    paper_value: 0.795
    paper_std: 0.009
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Qian 2023
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 51
    sort_value: 0.795
    sort_std: 0.009
    is_best: false
  - model: GPS+RWSE
    model_key: gps+rwse
    model_plain: GPS+RWSE
    value: 0.788
    std: 0.0101
    paper_value: 0.788
    paper_std: 0.0101
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 134
    sort_value: 0.788
    sort_std: 0.0101
    is_best: false
  - model: GraphLOG pretrained
    model_key: graphlog pretrained
    model_plain: GraphLOG pretrained
    value: 0.785
    std: 0.012
    paper_value: 0.785
    paper_std: 0.012
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: You 2020
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: null
    sort_value: 0.785
    sort_std: 0.012
    is_best: false
  - model: GPS+GPSE (LapPE & EigVals excluded)
    model_key: gps+gpse (lappe & eigvals excluded)
    model_plain: GPS+GPSE (LapPE & EigVals excluded)
    value: 0.7849
    std: 0.0067
    paper_value: 0.7849
    paper_std: 0.0067
    metric: AUROC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: null
    sort_value: 0.7849
    sort_std: 0.0067
    is_best: false
  - model: GPSE + GPS
    model_key: gpse + gps
    model_plain: GPSE + GPS
    value: 0.7815
    std: 0.0133
    paper_value: 0.7815
    paper_std: 0.0133
    metric: AUROC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: null
    sort_value: 0.7815
    sort_std: 0.0133
    is_best: false
  - model: RWSE augmented
    model_key: rwse augmented
    model_plain: RWSE augmented
    value: 0.781
    std: 0.015
    paper_value: 0.781
    paper_std: 0.015
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: null
    sort_value: 0.781
    sort_std: 0.015
    is_best: false
  - model: GPS
    model_key: gps (none)
    model_plain: GPS
    value: 0.7798
    std: 0.0077
    paper_value: 0.7798
    paper_std: 0.0077
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: null
    sort_value: 0.7798
    sort_std: 0.0077
    is_best: false
  - model: GPS+GPSE (HKdiagSE excluded)
    model_key: gps+gpse (hkdiagse excluded)
    model_plain: GPS+GPSE (HKdiagSE excluded)
    value: 0.7787
    std: 0.0198
    paper_value: 0.7787
    paper_std: 0.0198
    metric: AUROC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: null
    sort_value: 0.7787
    sort_std: 0.0198
    is_best: false
  - model: GraphLoG
    model_key: graphlog
    model_plain: GraphLoG
    value: 0.778
    std: 0.008
    paper_value: 0.778
    paper_std: 0.008
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Xu 2021
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 199
    sort_value: 0.778
    sort_std: 0.008
    is_best: false
  - model: GPS+GPSE (RWSE excluded)
    model_key: gps+gpse (rwse excluded)
    model_plain: GPS+GPSE (RWSE excluded)
    value: 0.7771
    std: 0.0105
    paper_value: 0.7771
    paper_std: 0.0105
    metric: AUROC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: null
    sort_value: 0.7771
    sort_std: 0.0105
    is_best: false
  - model: GPS+GPSE (CycleSE excluded)
    model_key: gps+gpse (cyclese excluded)
    model_plain: GPS+GPSE (CycleSE excluded)
    value: 0.7739
    std: 0.024
    paper_value: 0.7739
    paper_std: 0.024
    metric: AUROC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: null
    sort_value: 0.7739
    sort_std: 0.024
    is_best: false
  - model: GPS+LapPE
    model_key: gps+lappe
    model_plain: GPS+LapPE
    value: 0.7736
    std: 0.0097
    paper_value: 0.7736
    paper_std: 0.0097
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: null
    sort_value: 0.7736
    sort_std: 0.0097
    is_best: false
  - model: Self-supervised pre-trained
    model_key: self-supervised pre-trained
    model_plain: Self-supervised pre-trained
    value: 0.773
    std: 0.01
    paper_value: 0.773
    paper_std: 0.01
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Hu 2020
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: null
    sort_value: 0.773
    sort_std: 0.01
    is_best: false
  - model: SSL ContextPred pre-trained
    model_key: ssl contextpred pre-trained
    model_plain: SSL ContextPred pre-trained
    value: 0.773
    std: 0.01
    paper_value: 0.773
    paper_std: 0.01
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hu 2020
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: null
    sort_value: 0.773
    sort_std: 0.01
    is_best: false
  - model: GraphMAE
    model_key: graphmae
    model_plain: GraphMAE
    value: 0.772
    std: 0.01
    paper_value: 0.772
    paper_std: 0.01
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Hou 2022
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 144
    sort_value: 0.772
    sort_std: 0.01
    is_best: false
  - model: GPSE augmented
    model_key: gpse augmented
    model_plain: GPSE augmented
    value: 0.772
    std: 0.015
    paper_value: 0.772
    paper_std: 0.015
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: null
    sort_value: 0.772
    sort_std: 0.015
    is_best: false
  - model: SSL AttrMasking pre-trained
    model_key: ssl attrmasking pre-trained
    model_plain: SSL AttrMasking pre-trained
    value: 0.772
    std: 0.011
    paper_value: 0.772
    paper_std: 0.011
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hu 2020
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: null
    sort_value: 0.772
    sort_std: 0.011
    is_best: false
  - model: GPS + (RWSE/LapPE)
    model_key: gps + (rwse/lappe)
    model_plain: GPS + (RWSE/LapPE)
    value: 0.7719
    std: 0.0129
    paper_value: 0.7719
    paper_std: 0.0129
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: null
    sort_value: 0.7719
    sort_std: 0.0129
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.7707
    std: 0.0149
    paper_value: 0.7707
    paper_std: 0.0149
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xu 2018
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 4
    sort_value: 0.7707
    sort_std: 0.0149
    is_best: false
  - model: GPS+GPSE (ElstaticPE excluded)
    model_key: gps+gpse (elstaticpe excluded)
    model_plain: GPS+GPSE (ElstaticPE excluded)
    value: 0.7681
    std: 0.0146
    paper_value: 0.7681
    paper_std: 0.0146
    metric: AUROC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: null
    sort_value: 0.7681
    sort_std: 0.0146
    is_best: false
  - model: GPS+AllPSE
    model_key: gps+allpse
    model_plain: GPS+AllPSE
    value: 0.7645
    std: 0.0236
    paper_value: 0.7645
    paper_std: 0.0236
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: null
    sort_value: 0.7645
    sort_std: 0.0236
    is_best: false
  - model: SSL EdgePred pre-trained
    model_key: ssl edgepred pre-trained
    model_plain: SSL EdgePred pre-trained
    value: 0.763
    std: 0.01
    paper_value: 0.763
    paper_std: 0.01
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hu 2020
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: null
    sort_value: 0.763
    sort_std: 0.01
    is_best: false
  - model: SSL InfoMax pre-trained
    model_key: ssl infomax pre-trained
    model_plain: SSL InfoMax pre-trained
    value: 0.76
    std: 0.007
    paper_value: 0.76
    paper_std: 0.007
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hu 2020
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: null
    sort_value: 0.76
    sort_std: 0.007
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7599
    std: 0.0119
    paper_value: 0.7599
    paper_std: 0.0119
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kipf 2017
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 3
    sort_value: 0.7599
    sort_std: 0.0119
    is_best: false
  - model: LapPE augmented
    model_key: lappe augmented
    model_plain: LapPE augmented
    value: 0.756
    std: 0.011
    paper_value: 0.756
    paper_std: 0.011
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: null
    sort_value: 0.756
    sort_std: 0.011
    is_best: false
  - model: AllPSE augmented
    model_key: allpse augmented
    model_plain: AllPSE augmented
    value: 0.754
    std: 0.015
    paper_value: 0.754
    paper_std: 0.015
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: null
    sort_value: 0.754
    sort_std: 0.015
    is_best: false
  - model: No augmentation
    model_key: no augmentation
    model_plain: No augmentation
    value: 0.753
    std: 0.019
    paper_value: 0.753
    paper_std: 0.019
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Hu 2020
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: null
    sort_value: 0.753
    sort_std: 0.019
    is_best: false
  - model: No pre-training
    model_key: no pre-training
    model_plain: No pre-training
    value: 0.753
    std: 0.019
    paper_value: 0.753
    paper_std: 0.019
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hu 2020
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: null
    sort_value: 0.753
    sort_std: 0.019
    is_best: false
  - model: GraphLoG augmented
    model_key: graphlog augmented
    model_plain: GraphLoG augmented
    value: 0.744
    std: 0.015
    paper_value: 0.744
    paper_std: 0.015
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Xu 2021
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: null
    sort_value: 0.744
    sort_std: 0.015
    is_best: false
  - model: InfoGraph pretrained
    model_key: infograph pretrained
    model_plain: InfoGraph pretrained
    value: 0.702
    std: 0.006
    paper_value: 0.702
    paper_std: 0.006
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Wang 2022
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: null
    sort_value: 0.702
    sort_std: 0.006
    is_best: false
  - model: JOAOv2 pre-trained
    model_key: joaov2 pre-trained
    model_plain: JOAOv2 pre-trained
    value: 0.684
    std: 0.005
    paper_value: 0.684
    paper_std: 0.005
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Wang 2022
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: null
    sort_value: 0.684
    sort_std: 0.005
    is_best: false
  - model: GPS+rand
    model_key: gps+rand
    model_plain: GPS+rand
    value: 0.621
    std: 0.0444
    paper_value: 0.621
    paper_std: 0.0444
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: null
    sort_value: 0.621
    sort_std: 0.0444
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id008
  dataset: ogbg-molpcba
  rows:
  - model: GatedGCN + VN
    model_key: gatedgcn + vn
    model_plain: GatedGCN + VN
    value: 0.3141
    std: 0.0019
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.11951'
    title: 'Distinguished In Uniform: Self-Attention Vs. Virtual Nodes'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.3141
    sort_std: 0.0019
    is_best: true
  - model: NeuralWalker
    model_key: neuralwalker
    model_plain: NeuralWalker
    value: 0.3086
    std: 0.0031
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.03386'
    title: Learning Long Range Dependencies on Graphs via Random Walks
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.3086
    sort_std: 0.0031
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.3066
    std: 0.0013
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.11951'
    title: 'Distinguished In Uniform: Self-Attention Vs. Virtual Nodes'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.3066
    sort_std: 0.0013
    is_best: false
  - model: CRaWI
    model_key: crawi
    model_plain: CRaWI
    value: 0.2986
    std: 0.0025
    paper_value: 0.2986
    paper_std: 0.0025
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Toenshoff et al. 2021
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 6
    true_value: 0.2986
    true_std: 0.0025
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2986
    sort_std: 0.0025
    is_best: false
  - model: GPS+LapPE
    model_key: gps+lappe
    model_plain: GPS+LapPE
    value: 0.2939
    std: 0.0016
    paper_value: 0.2939
    paper_std: 0.0016
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 11
    true_value: 0.2939
    true_std: 0.0016
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2939
    sort_std: 0.0016
    is_best: false
  - model: GPSE + GPS
    model_key: gpse + gps
    model_plain: GPSE + GPS
    value: 0.2911
    std: 0.0036
    paper_value: 0.2911
    paper_std: 0.0036
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 19
    true_value: 0.2911
    true_std: 0.0036
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2911
    sort_std: 0.0036
    is_best: false
  - model: GPS+RWSE
    model_key: gps+rwse
    model_plain: GPS+RWSE
    value: 0.2907
    std: 0.0028
    paper_value: 0.2907
    paper_std: 0.0028
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 22
    true_value: 0.2907
    true_std: 0.0028
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2907
    sort_std: 0.0028
    is_best: false
  - model: GPS
    model_key: gps (none)
    model_plain: GPS
    value: 0.2869
    std: 0.0012
    paper_value: 0.2869
    paper_std: 0.0012
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 25
    true_value: 0.2869
    true_std: 0.0012
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2869
    sort_std: 0.0012
    is_best: false
  - model: GPS + (RWSE/LapPE)
    model_key: gps + (rwse/lappe)
    model_plain: GPS + (RWSE/LapPE)
    value: 0.2854
    std: 0.0029
    paper_value: 0.2854
    paper_std: 0.0029
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 28
    true_value: 0.2854
    true_std: 0.0029
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 28
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2854
    sort_std: 0.0029
    is_best: false
  - model: GPS+AllPSE
    model_key: gps+allpse
    model_plain: GPS+AllPSE
    value: 0.2826
    std: 0.0001
    paper_value: 0.2826
    paper_std: 0.0001
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 31
    true_value: 0.2826
    true_std: 0.0001
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2826
    sort_std: 0.0001
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.2424
    std: 0.0034
    paper_value: 0.2424
    paper_std: 0.0034
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kipf & Welling 2017
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 40
    true_value: 0.2721
    true_std: 0.0046
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.029700000000000004
    value_note: ''
    paper_rank: 50
    rank_delta: 10
    rank_delta_abs: 10
    rank_delta_direction: worse
    sort_value: 0.2721
    sort_std: 0.0046
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.2703
    std: 0.0023
    paper_value: 0.2703
    paper_std: 0.0023
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xu et al. 2018
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 41
    true_value: 0.2703
    true_std: 0.0024
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 41
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2703
    sort_std: 0.0024
    is_best: false
  - model: GPS+rand
    model_key: gps+rand
    model_plain: GPS+rand
    value: 0.0753
    std: 0.0045
    paper_value: 0.0753
    paper_std: 0.0045
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: 62
    true_value: 0.0753
    true_std: 0.0045
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 62
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.0753
    sort_std: 0.0045
    is_best: false
  metric: AP
  higher_is_better: true
- &id007
  dataset: ogbn-arxiv
  rows:
  - model: GLEM-GNN
    model_key: glem-gnn
    model_plain: GLEM-GNN
    value: 0.7593
    std: 0.0019
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.03393'
    title: Exploring the Potential of Large Language Models (LLMs) in Learning on
      Graphs
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.7593
    sort_std: 0.0019
    is_best: true
  - model: Stable-ChebNet
    model_key: stable-chebnet
    model_plain: Stable-ChebNet
    value: 0.7573
    std: 0.0051
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.7573
    sort_std: 0.0051
    is_best: true
  - model: GLEM-LM
    model_key: glem-lm
    model_plain: GLEM-LM
    value: 0.7571
    std: 0.0024
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.03393'
    title: Exploring the Potential of Large Language Models (LLMs) in Learning on
      Graphs
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    codebase_url: ''
    uses_external_data: true
    is_global_top: true
    global_rank: 3
    sort_value: 0.7571
    sort_std: 0.0024
    is_best: true
  - model: SAGE+none
    model_key: sage+none
    model_plain: SAGE+none
    value: 0.7236
    std: 0.0043
    paper_value: 0.7236
    paper_std: 0.0043
    metric: ACC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: null
    sort_value: 0.7236
    sort_std: 0.0043
    is_best: false
  - model: SAGE+GPSE
    model_key: sage+gpse
    model_plain: SAGE+GPSE
    value: 0.7234
    std: 0.0019
    paper_value: 0.7234
    paper_std: 0.0019
    metric: ACC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: null
    sort_value: 0.7234
    sort_std: 0.0019
    is_best: false
  - model: GAT(E)v2+GPSE
    model_key: gat(e)v2+gpse
    model_plain: GAT(E)v2+GPSE
    value: 0.7217
    std: 0.0042
    paper_value: 0.7217
    paper_std: 0.0042
    metric: ACC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: null
    sort_value: 0.7217
    sort_std: 0.0042
    is_best: false
  - model: GPSE + GCN
    model_key: gpse + gcn
    model_plain: GPSE + GCN
    value: 0.717
    std: 0.0026
    paper_value: 0.717
    paper_std: 0.0026
    metric: ACC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: null
    sort_value: 0.717
    sort_std: 0.0026
    is_best: false
  - model: GAT(E)v2+none
    model_key: gat(e)v2+none
    model_plain: GAT(E)v2+none
    value: 0.7169
    std: 0.0021
    paper_value: 0.7169
    paper_std: 0.0021
    metric: ACC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: null
    sort_value: 0.7169
    sort_std: 0.0021
    is_best: false
  - model: SAGE+LapPE
    model_key: sage+lappe
    model_plain: SAGE+LapPE
    value: 0.7163
    std: 0.0016
    paper_value: 0.7163
    paper_std: 0.0016
    metric: ACC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: null
    sort_value: 0.7163
    sort_std: 0.0016
    is_best: false
  - model: GCN
    model_key: gcn (none)
    model_plain: GCN
    value: 0.7162
    std: 0.0023
    paper_value: 0.7162
    paper_std: 0.0023
    metric: ACC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: null
    sort_value: 0.7162
    sort_std: 0.0023
    is_best: false
  - model: GAT(E)v2+LapPE
    model_key: gat(e)v2+lappe
    model_plain: GAT(E)v2+LapPE
    value: 0.713
    std: 0.0027
    paper_value: 0.713
    paper_std: 0.0027
    metric: ACC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: null
    sort_value: 0.713
    sort_std: 0.0027
    is_best: false
  - model: GCN+LapPE
    model_key: gcn+lappe
    model_plain: GCN+LapPE
    value: 0.7089
    std: 0.002
    paper_value: 0.7089
    paper_std: 0.002
    metric: ACC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: null
    sort_value: 0.7089
    sort_std: 0.002
    is_best: false
  - model: GPSE + GPS
    model_key: gpse + gps
    model_plain: GPSE + GPS
    value: 0.7089
    std: 0.0036
    paper_value: 0.7089
    paper_std: 0.0036
    metric: ACC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: null
    sort_value: 0.7089
    sort_std: 0.0036
    is_best: false
  - model: GPS+LapPE
    model_key: gps+lappe
    model_plain: GPS+LapPE
    value: 0.7062
    std: 0.0041
    paper_value: 0.7062
    paper_std: 0.0041
    metric: ACC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: null
    sort_value: 0.7062
    sort_std: 0.0041
    is_best: false
  - model: GPS
    model_key: gps (none)
    model_plain: GPS
    value: 0.706
    std: 0.0028
    paper_value: 0.706
    paper_std: 0.0028
    metric: ACC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: null
    sort_value: 0.706
    sort_std: 0.0028
    is_best: false
  - model: GPS w/ Transformer
    model_key: gps w/ transformer
    model_plain: GPS w/ Transformer
    value: 0.5917
    std: 0.0021
    paper_value: 0.5917
    paper_std: 0.0021
    metric: ACC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: null
    sort_value: 0.5917
    sort_std: 0.0021
    is_best: false
  - model: Transformer+LapPE
    model_key: transformer+lappe
    model_plain: Transformer+LapPE
    value: 0.5721
    std: 0.0025
    paper_value: 0.5721
    paper_std: 0.0025
    metric: ACC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: null
    sort_value: 0.5721
    sort_std: 0.0025
    is_best: false
  - model: Transformer+none
    model_key: transformer+none
    model_plain: Transformer+none
    value: 0.57
    std: 0.0079
    paper_value: 0.57
    paper_std: 0.0079
    metric: ACC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    global_rank: null
    sort_value: 0.57
    sort_std: 0.0079
    is_best: false
  metric: Accuracy
  higher_is_better: true
results_grouped:
- benchmark: LRGB
  datasets:
  - *id001
- benchmark: TU Dortmund
  datasets:
  - *id002
- benchmark: GNNBenchmark
  datasets:
  - *id003
  - *id004
  - *id005
- benchmark: OGB
  datasets:
  - *id006
  - *id007
  - *id008
  - *id009
- benchmark: MoleculeNet
  datasets:
  - *id010
  - *id011
  - *id012
  - *id013
  - *id014
  - *id015
main_figure: /figures/2307.07107/main_figure.png
---

