---
title: Fragment-based Pretraining and Finetuning on Molecular Graphs
arxiv_id: '2310.03274'
source_url: ''
authors: []
published_date: Oct 2023
published_date_iso: 2023-10
abstract: 'Property prediction on molecular graphs is an important application of
  Graph Neural Networks (GNNs). Recently, unlabeled molecular data has become abundant,
  which facilitates the rapid development of self-supervised learning for GNNs in
  the chemical domain. In this work, we propose pretraining GNNs at the fragment level,
  a promising middle ground to overcome the limitations of node-level and graph-level
  pretraining. Borrowing techniques from recent work on principal subgraph mining,
  we obtain a compact vocabulary of prevalent fragments from a large pretraining dataset.
  From the extracted vocabulary, we introduce several fragment-based contrastive and
  predictive pretraining tasks. The contrastive learning task jointly pretrains two
  different GNNs: one on molecular graphs and the other on fragment graphs, which
  represents higher-order connectivity within molecules. By enforcing consistency
  between the fragment embedding and the aggregated embedding of the corresponding
  atoms from the molecular graphs, we ensure that the embeddings capture structural
  information at multiple resolutions. The structural information of fragment graphs
  is further exploited to extract auxiliary labels for graph-level predictive pretraining.
  We employ both the pretrained molecular-based and fragment-based GNNs for downstream
  prediction, thus utilizing the fragment information during finetuning. Our graph
  fragment-based pretraining (GraphFP) advances the performances on $5$ out of $8$
  common molecular benchmarks and improves the performances on long-range biological
  benchmarks by at least $11.5\'
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- GraphMVP
- GraphSAGE
- GraphCL
- GraphFP
- GraphLoG
- GraphFP-JT_C
- GraphFP_CP
- CP, alpha=0.1
- GIN_C (Vocab 200)
mrr: 0.0
adjusted_mrr: 0.0
mrr_dataset_count: 0
benchmark_categories:
- LRGB
- OGB
- MoleculeNet
task_categories:
- graph_classification
- graph_regression
experiment_scopes:
- graph-level
results:
- &id004
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
    value: 0.802
    std: 0.035
    paper_value: 0.802
    paper_std: 0.035
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xu et al. 2021
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 6
    true_value: 0.835
    true_std: 0.012
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.03299999999999992
    value_note: global 0.8350 within std
    paper_rank: 23
    rank_delta: 17
    rank_delta_abs: 17
    rank_delta_direction: worse
    sort_value: 0.835
    sort_std: 0.012
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.825
    std: 0.019
    paper_value: 0.825
    paper_std: 0.019
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 11
    true_value: 0.825
    true_std: 0.019
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.825
    sort_std: 0.019
    is_best: false
  - model: MGSSL
    model_key: mgssl
    model_plain: MGSSL
    value: 0.821
    std: 0.027
    paper_value: 0.821
    paper_std: 0.027
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhang et al.
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 14
    true_value: 0.821
    true_std: 0.027
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.821
    sort_std: 0.027
    is_best: false
  - model: GraphFP
    model_key: graphfp
    model_plain: GraphFP
    value: 0.807
    std: 0.048
    paper_value: 0.807
    paper_std: 0.048
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 19
    true_value: 0.807
    true_std: 0.048
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.807
    sort_std: 0.048
    is_best: false
  - model: GraphFP_CP
    model_key: graphfp_cp
    model_plain: GraphFP_CP
    value: 0.805
    std: 0.018
    paper_value: 0.805
    paper_std: 0.018
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 21
    true_value: 0.805
    true_std: 0.018
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.805
    sort_std: 0.018
    is_best: false
  - model: CP, alpha=0.1
    model_key: cp, alpha=0.1
    model_plain: CP, alpha=0.1
    value: 0.801
    std: 0.012
    paper_value: 0.801
    paper_std: 0.012
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 24
    true_value: 0.801
    true_std: 0.012
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.801
    sort_std: 0.012
    is_best: false
  - model: ContextPred
    model_key: contextpred
    model_plain: ContextPred
    value: 0.796
    std: 0.012
    paper_value: 0.796
    paper_std: 0.012
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hu et al. 2020
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 28
    true_value: 0.796
    true_std: 0.012
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 28
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.796
    sort_std: 0.012
    is_best: false
  - model: GIN_C (Vocab 200)
    model_key: gin_c (vocab 200)
    model_plain: GIN_C (Vocab 200)
    value: 0.794
    std: 0.045
    paper_value: 0.794
    paper_std: 0.045
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 30
    true_value: 0.794
    true_std: 0.045
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 30
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.794
    sort_std: 0.045
    is_best: false
  - model: GraphMVP
    model_key: graphmvp
    model_plain: GraphMVP
    value: 0.768
    std: 0.011
    paper_value: 0.768
    paper_std: 0.011
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Liu et al. 2022
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 31
    true_value: 0.793
    true_std: 0.015
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.025000000000000022
    value_note: ''
    paper_rank: 49
    rank_delta: 18
    rank_delta_abs: 18
    rank_delta_direction: worse
    sort_value: 0.793
    sort_std: 0.015
    is_best: false
  - model: AttrMasking
    model_key: attrmasking
    model_plain: AttrMasking
    value: 0.793
    std: 0.016
    paper_value: 0.793
    paper_std: 0.016
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hu et al. 2020
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 32
    true_value: 0.793
    true_std: 0.016
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.793
    sort_std: 0.016
    is_best: false
  - model: G-Contextual
    model_key: g-contextual
    model_plain: G-Contextual
    value: 0.793
    std: 0.011
    paper_value: 0.793
    paper_std: 0.011
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Rong et al. 2020
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 33
    true_value: 0.793
    true_std: 0.011
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.793
    sort_std: 0.011
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.762
    std: 0.021
    paper_value: 0.762
    paper_std: 0.021
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 34
    true_value: 0.7915
    true_std: 0.0144
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.02949999999999997
    value_note: ''
    paper_rank: 51
    rank_delta: 17
    rank_delta_abs: 17
    rank_delta_direction: worse
    sort_value: 0.7915
    sort_std: 0.0144
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.78
    std: 0.036
    paper_value: 0.78
    paper_std: 0.036
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 44
    true_value: 0.78
    true_std: 0.036
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 44
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.78
    sort_std: 0.036
    is_best: false
  - model: GPT-GNN
    model_key: gpt-gnn
    model_plain: GPT-GNN
    value: 0.779
    std: 0.032
    paper_value: 0.779
    paper_std: 0.032
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hu et al. 2020
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 46
    true_value: 0.779
    true_std: 0.032
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 46
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.779
    sort_std: 0.032
    is_best: false
  - model: JOAO
    model_key: joao
    model_plain: JOAO
    value: 0.773
    std: 0.005
    paper_value: 0.773
    paper_std: 0.005
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: You et al. 2021
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 48
    true_value: 0.773
    true_std: 0.005
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 48
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.773
    sort_std: 0.005
    is_best: false
  - model: JOAOv2
    model_key: joaov2
    model_plain: JOAOv2
    value: 0.755
    std: 0.013
    paper_value: 0.755
    paper_std: 0.013
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: You et al. 2021
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 52
    true_value: 0.755
    true_std: 0.013
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 52
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.755
    sort_std: 0.013
    is_best: false
  - model: GraphCL
    model_key: graphcl
    model_plain: GraphCL
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
    source_ref: You et al. 2020
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 53
    true_value: 0.754
    true_std: 0.014
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 53
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.754
    sort_std: 0.014
    is_best: false
  - model: GraphFP-JT_C
    model_key: graphfp-jt_c
    model_plain: GraphFP-JT_C
    value: 0.742
    std: 0.028
    paper_value: 0.742
    paper_std: 0.028
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 56
    true_value: 0.742
    true_std: 0.028
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 56
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.742
    sort_std: 0.028
    is_best: false
  - model: G-Motif
    model_key: g-motif
    model_plain: G-Motif
    value: 0.73
    std: 0.033
    paper_value: 0.73
    paper_std: 0.033
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Rong et al. 2020
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 58
    true_value: 0.73
    true_std: 0.033
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 58
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.73
    sort_std: 0.033
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id006
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
    value: 0.678
    std: 0.019
    paper_value: 0.678
    paper_std: 0.019
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xu et al. 2021
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 3
    true_value: 0.725
    true_std: 0.008
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04699999999999993
    value_note: ''
    paper_rank: 35
    rank_delta: 32
    rank_delta_abs: 32
    rank_delta_direction: worse
    sort_value: 0.725
    sort_std: 0.008
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.723
    std: 0.015
    paper_value: 0.723
    paper_std: 0.015
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 4
    true_value: 0.723
    true_std: 0.015
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.723
    sort_std: 0.015
    is_best: true
  - model: SimSGT
    model_key: simsgt
    model_plain: SimSGT
    value: 0.722
    std: 0.009
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
    global_rank: 5
    sort_value: 0.722
    sort_std: 0.009
    is_best: false
  - model: GraphFP
    model_key: graphfp
    model_plain: GraphFP
    value: 0.682
    std: 0.012
    paper_value: 0.682
    paper_std: 0.012
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 7
    true_value: 0.72
    true_std: 0.017
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.03799999999999992
    value_note: ''
    paper_rank: 32
    rank_delta: 25
    rank_delta_abs: 25
    rank_delta_direction: worse
    sort_value: 0.72
    sort_std: 0.017
    is_best: true
  - model: GraphFP_CP
    model_key: graphfp_cp
    model_plain: GraphFP_CP
    value: 0.72
    std: 0.017
    paper_value: 0.72
    paper_std: 0.017
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 8
    true_value: 0.72
    true_std: 0.017
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.72
    sort_std: 0.017
    is_best: true
  - model: JOAOv2
    model_key: joaov2
    model_plain: JOAOv2
    value: 0.714
    std: 0.009
    paper_value: 0.714
    paper_std: 0.009
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: You et al. 2021
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 11
    true_value: 0.714
    true_std: 0.009
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.714
    sort_std: 0.009
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.713
    std: 0.008
    paper_value: 0.713
    paper_std: 0.008
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 12
    true_value: 0.713
    true_std: 0.008
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.713
    sort_std: 0.008
    is_best: false
  - model: GIN_C (Vocab 200)
    model_key: gin_c (vocab 200)
    model_plain: GIN_C (Vocab 200)
    value: 0.713
    std: 0.008
    paper_value: 0.713
    paper_std: 0.008
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 13
    true_value: 0.713
    true_std: 0.008
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.713
    sort_std: 0.008
    is_best: false
  - model: GraphMVP
    model_key: graphmvp
    model_plain: GraphMVP
    value: 0.685
    std: 0.002
    paper_value: 0.685
    paper_std: 0.002
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Liu et al. 2022
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 16
    true_value: 0.708
    true_std: 0.005
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.02299999999999991
    value_note: ''
    paper_rank: 31
    rank_delta: 15
    rank_delta_abs: 15
    rank_delta_direction: worse
    sort_value: 0.708
    sort_std: 0.005
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.705
    std: 0.012
    paper_value: 0.705
    paper_std: 0.012
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 17
    true_value: 0.705
    true_std: 0.012
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.705
    sort_std: 0.012
    is_best: false
  - model: CP, alpha=0.1
    model_key: cp, alpha=0.1
    model_plain: CP, alpha=0.1
    value: 0.703
    std: 0.009
    paper_value: 0.703
    paper_std: 0.009
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 18
    true_value: 0.703
    true_std: 0.009
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.703
    sort_std: 0.009
    is_best: false
  - model: JOAO
    model_key: joao
    model_plain: JOAO
    value: 0.702
    std: 0.01
    paper_value: 0.702
    paper_std: 0.01
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: You et al. 2021
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 19
    true_value: 0.702
    true_std: 0.01
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.702
    sort_std: 0.01
    is_best: false
  - model: GraphFP-JT_C
    model_key: graphfp-jt_c
    model_plain: GraphFP-JT_C
    value: 0.702
    std: 0.017
    paper_value: 0.702
    paper_std: 0.017
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 20
    true_value: 0.702
    true_std: 0.017
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.702
    sort_std: 0.017
    is_best: false
  - model: G-Contextual
    model_key: g-contextual
    model_plain: G-Contextual
    value: 0.699
    std: 0.021
    paper_value: 0.699
    paper_std: 0.021
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Rong et al. 2020
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 22
    true_value: 0.699
    true_std: 0.021
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.699
    sort_std: 0.021
    is_best: false
  - model: GraphCL
    model_key: graphcl
    model_plain: GraphCL
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
    source_ref: You et al. 2020
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 23
    true_value: 0.697
    true_std: 0.007
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.697
    sort_std: 0.007
    is_best: false
  - model: MGSSL
    model_key: mgssl
    model_plain: MGSSL
    value: 0.689
    std: 0.025
    paper_value: 0.689
    paper_std: 0.025
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhang et al.
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 28
    true_value: 0.689
    true_std: 0.025
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 28
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.689
    sort_std: 0.025
    is_best: false
  - model: ContextPred
    model_key: contextpred
    model_plain: ContextPred
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
    source_ref: Hu et al. 2020
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 34
    true_value: 0.68
    true_std: 0.02
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 34
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.68
    sort_std: 0.02
    is_best: false
  - model: G-Motif
    model_key: g-motif
    model_plain: G-Motif
    value: 0.669
    std: 0.031
    paper_value: 0.669
    paper_std: 0.031
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Rong et al. 2020
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 42
    true_value: 0.669
    true_std: 0.031
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 42
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.669
    sort_std: 0.031
    is_best: false
  - model: GPT-GNN
    model_key: gpt-gnn
    model_plain: GPT-GNN
    value: 0.645
    std: 0.014
    paper_value: 0.645
    paper_std: 0.014
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hu et al. 2020
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 50
    true_value: 0.645
    true_std: 0.014
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 50
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.645
    sort_std: 0.014
    is_best: false
  - model: AttrMasking
    model_key: attrmasking
    model_plain: AttrMasking
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
    source_ref: Hu et al. 2020
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 52
    true_value: 0.643
    true_std: 0.028
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 52
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.643
    sort_std: 0.028
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id008
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
  - model: GraphFP_CP
    model_key: graphfp_cp
    model_plain: GraphFP_CP
    value: 0.847
    std: 0.058
    paper_value: 0.847
    paper_std: 0.058
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 4
    true_value: 0.847
    true_std: 0.058
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.847
    sort_std: 0.058
    is_best: true
  - model: CP, \(α = 0.1\)
    model_key: cp, \(α = 0.1\)
    model_plain: CP, \(α = 0.1\)
    value: 0.847
    std: 0.088
    paper_value: 0.847
    paper_std: 0.088
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 5
    true_value: 0.847
    true_std: 0.088
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.847
    sort_std: 0.088
    is_best: true
  - model: JOAO
    model_key: joao
    model_plain: JOAO
    value: 0.813
    std: 0.025
    paper_value: 0.813
    paper_std: 0.025
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: You et al. 2021
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 8
    true_value: 0.813
    true_std: 0.025
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.813
    sort_std: 0.025
    is_best: false
  - model: JOAOv2
    model_key: joaov2
    model_plain: JOAOv2
    value: 0.81
    std: 0.016
    paper_value: 0.81
    paper_std: 0.016
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: You et al. 2021
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 9
    true_value: 0.81
    true_std: 0.016
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.81
    sort_std: 0.016
    is_best: false
  - model: CP, alpha=0.1
    model_key: cp, alpha=0.1
    model_plain: CP, alpha=0.1
    value: 0.793
    std: 0.031
    paper_value: 0.793
    paper_std: 0.031
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 12
    true_value: 0.793
    true_std: 0.031
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.793
    sort_std: 0.031
    is_best: false
  - model: CPF, \(α = 0.2\)
    model_key: cpf, \(α = 0.2\)
    model_plain: CPF, \(α = 0.2\)
    value: 0.793
    std: 0.031
    paper_value: 0.793
    paper_std: 0.031
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 13
    true_value: 0.793
    true_std: 0.031
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.793
    sort_std: 0.031
    is_best: false
  - model: GraphMVP
    model_key: graphmvp
    model_plain: GraphMVP
    value: 0.79
    std: 0.025
    paper_value: 0.79
    paper_std: 0.025
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Liu et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 14
    true_value: 0.79
    true_std: 0.025
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.79
    sort_std: 0.025
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.781
    std: 0.058
    paper_value: 0.781
    paper_std: 0.058
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 16
    true_value: 0.781
    true_std: 0.058
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.781
    sort_std: 0.058
    is_best: false
  - model: G-Motif
    model_key: g-motif
    model_plain: G-Motif
    value: 0.777
    std: 0.027
    paper_value: 0.777
    paper_std: 0.027
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Rong et al. 2020
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 17
    true_value: 0.777
    true_std: 0.027
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.777
    sort_std: 0.027
    is_best: false
  - model: GraphLoG
    model_key: graphlog
    model_plain: GraphLoG
    value: 0.653
    std: 0.032
    paper_value: 0.653
    paper_std: 0.032
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xu et al. 2021
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 18
    true_value: 0.767
    true_std: 0.033
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11399999999999999
    value_note: ''
    paper_rank: 45
    rank_delta: 27
    rank_delta_abs: 27
    rank_delta_direction: worse
    sort_value: 0.767
    sort_std: 0.033
    is_best: false
  - model: GraphCL
    model_key: graphcl
    model_plain: GraphCL
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
    source_ref: You et al. 2020
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 20
    true_value: 0.76
    true_std: 0.027
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.76
    sort_std: 0.027
    is_best: false
  - model: GraphFP-JT_C
    model_key: graphfp-jt_c
    model_plain: GraphFP-JT_C
    value: 0.759
    std: 0.056
    paper_value: 0.759
    paper_std: 0.056
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 22
    true_value: 0.759
    true_std: 0.056
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.759
    sort_std: 0.056
    is_best: false
  - model: GIN_C (Vocab 200)
    model_key: gin_c (vocab 200)
    model_plain: GIN_C (Vocab 200)
    value: 0.755
    std: 0.059
    paper_value: 0.755
    paper_std: 0.059
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 23
    true_value: 0.755
    true_std: 0.059
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.755
    sort_std: 0.059
    is_best: false
  - model: AttrMasking
    model_key: attrmasking
    model_plain: AttrMasking
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
    table_ref: Table 1
    source_ref: Hu et al. 2020
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 29
    true_value: 0.718
    true_std: 0.041
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.718
    sort_std: 0.041
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.696
    std: 0.031
    paper_value: 0.696
    paper_std: 0.031
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 35
    true_value: 0.696
    true_std: 0.031
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.696
    sort_std: 0.031
    is_best: false
  - model: MGSSL
    model_key: mgssl
    model_plain: MGSSL
    value: 0.675
    std: 0.055
    paper_value: 0.675
    paper_std: 0.055
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhang et al.
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 40
    true_value: 0.675
    true_std: 0.055
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 40
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.675
    sort_std: 0.055
    is_best: false
  - model: ContextPred
    model_key: contextpred
    model_plain: ContextPred
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
    table_ref: Table 1
    source_ref: Hu et al. 2020
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 42
    true_value: 0.659
    true_std: 0.038
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 42
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.659
    sort_std: 0.038
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.632
    std: 0.01
    paper_value: 0.632
    paper_std: 0.01
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 49
    true_value: 0.64
    true_std: 0.047
    value_gap_source_arxiv: '2508.10651'
    value_gap_source_title: Graph Learning via Logic-Based Weisfeiler--Leman Variants
      and Tabularization
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.008000000000000007
    value_note: global 0.6400 within std
    paper_rank: 49
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.64
    sort_std: 0.047
    is_best: false
  - model: G-Contextual
    model_key: g-contextual
    model_plain: G-Contextual
    value: 0.606
    std: 0.052
    paper_value: 0.606
    paper_std: 0.052
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Rong et al. 2020
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 50
    true_value: 0.606
    true_std: 0.052
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 50
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.606
    sort_std: 0.052
    is_best: false
  - model: GPT-GNN
    model_key: gpt-gnn
    model_plain: GPT-GNN
    value: 0.583
    std: 0.052
    paper_value: 0.583
    paper_std: 0.052
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hu et al. 2020
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 51
    true_value: 0.583
    true_std: 0.052
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 51
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.583
    sort_std: 0.052
    is_best: false
  - model: GraphFP
    model_key: graphfp
    model_plain: GraphFP
    value: 0.538
    std: 0.038
    paper_value: 0.538
    paper_std: 0.038
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 53
    true_value: 0.538
    true_std: 0.038
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 53
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.538
    sort_std: 0.038
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id010
  dataset: MUV
  rows:
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.778
    std: 0.018
    paper_value: 0.778
    paper_std: 0.018
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 1
    true_value: 0.778
    true_std: 0.018
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.778
    sort_std: 0.018
    is_best: true
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.773
    std: 0.013
    paper_value: 0.773
    paper_std: 0.013
    metric: AUROC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 2
    true_value: 0.773
    true_std: 0.013
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.773
    sort_std: 0.013
    is_best: true
  - model: GIN_C (Vocab 200)
    model_key: gin_c (vocab 200)
    model_plain: GIN_C (Vocab 200)
    value: 0.771
    std: 0.019
    paper_value: 0.771
    paper_std: 0.019
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 3
    true_value: 0.771
    true_std: 0.019
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.771
    sort_std: 0.019
    is_best: true
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.762
    std: 0.02
    paper_value: 0.762
    paper_std: 0.02
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 4
    true_value: 0.762
    true_std: 0.02
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.762
    sort_std: 0.02
    is_best: true
  - model: GPT-GNN
    model_key: gpt-gnn
    model_plain: GPT-GNN
    value: 0.759
    std: 0.023
    paper_value: 0.759
    paper_std: 0.023
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hu et al. 2020
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 5
    true_value: 0.759
    true_std: 0.023
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.759
    sort_std: 0.023
    is_best: true
  - model: ContextPred
    model_key: contextpred
    model_plain: ContextPred
    value: 0.758
    std: 0.017
    paper_value: 0.758
    paper_std: 0.017
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hu et al. 2020
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 6
    true_value: 0.758
    true_std: 0.017
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.758
    sort_std: 0.017
    is_best: true
  - model: GraphFP_CP
    model_key: graphfp_cp
    model_plain: GraphFP_CP
    value: 0.754
    std: 0.019
    paper_value: 0.754
    paper_std: 0.019
    metric: AUROC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 7
    true_value: 0.754
    true_std: 0.019
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.754
    sort_std: 0.019
    is_best: true
  - model: GraphMVP
    model_key: graphmvp
    model_plain: GraphMVP
    value: 0.75
    std: 0.014
    paper_value: 0.75
    paper_std: 0.014
    metric: AUROC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Liu et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 8
    true_value: 0.75
    true_std: 0.014
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.75
    sort_std: 0.014
    is_best: true
  - model: AttrMasking
    model_key: attrmasking
    model_plain: AttrMasking
    value: 0.747
    std: 0.014
    paper_value: 0.747
    paper_std: 0.014
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hu et al. 2020
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 9
    true_value: 0.747
    true_std: 0.014
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.747
    sort_std: 0.014
    is_best: true
  - model: GraphFP
    model_key: graphfp
    model_plain: GraphFP
    value: 0.745
    std: 0.021
    paper_value: 0.745
    paper_std: 0.021
    metric: AUROC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 10
    true_value: 0.745
    true_std: 0.021
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.745
    sort_std: 0.021
    is_best: true
  - model: GraphFP-JT_C
    model_key: graphfp-jt_c
    model_plain: GraphFP-JT_C
    value: 0.739
    std: 0.013
    paper_value: 0.739
    paper_std: 0.013
    metric: AUROC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 11
    true_value: 0.739
    true_std: 0.013
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.739
    sort_std: 0.013
    is_best: false
  - model: JOAOv2
    model_key: joaov2
    model_plain: JOAOv2
    value: 0.737
    std: 0.01
    paper_value: 0.737
    paper_std: 0.01
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: You et al. 2021
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 12
    true_value: 0.737
    true_std: 0.01
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.737
    sort_std: 0.01
    is_best: false
  - model: GraphLoG
    model_key: graphlog
    model_plain: GraphLoG
    value: 0.736
    std: 0.012
    paper_value: 0.736
    paper_std: 0.012
    metric: AUROC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xu et al. 2021
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 13
    true_value: 0.736
    true_std: 0.012
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.736
    sort_std: 0.012
    is_best: false
  - model: CP, alpha=0.1
    model_key: cp, alpha=0.1
    model_plain: CP, alpha=0.1
    value: 0.734
    std: 0.028
    paper_value: 0.734
    paper_std: 0.028
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 14
    true_value: 0.734
    true_std: 0.028
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.734
    sort_std: 0.028
    is_best: true
  - model: MGSSL
    model_key: mgssl
    model_plain: MGSSL
    value: 0.732
    std: 0.019
    paper_value: 0.732
    paper_std: 0.019
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhang et al.
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 15
    true_value: 0.732
    true_std: 0.019
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.732
    sort_std: 0.019
    is_best: false
  - model: G-Motif
    model_key: g-motif
    model_plain: G-Motif
    value: 0.73
    std: 0.018
    paper_value: 0.73
    paper_std: 0.018
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Rong et al. 2020
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 16
    true_value: 0.73
    true_std: 0.018
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.73
    sort_std: 0.018
    is_best: false
  - model: G-Contextual
    model_key: g-contextual
    model_plain: G-Contextual
    value: 0.721
    std: 0.007
    paper_value: 0.721
    paper_std: 0.007
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Rong et al. 2020
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 17
    true_value: 0.721
    true_std: 0.007
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.721
    sort_std: 0.007
    is_best: false
  - model: JOAO
    model_key: joao
    model_plain: JOAO
    value: 0.717
    std: 0.014
    paper_value: 0.717
    paper_std: 0.014
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: You et al. 2021
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 18
    true_value: 0.717
    true_std: 0.014
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.717
    sort_std: 0.014
    is_best: false
  - model: GraphCL
    model_key: graphcl
    model_plain: GraphCL
    value: 0.698
    std: 0.027
    paper_value: 0.698
    paper_std: 0.027
    metric: AUROC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: You et al. 2020
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 19
    true_value: 0.698
    true_std: 0.027
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.698
    sort_std: 0.027
    is_best: false
  metric: AUROC
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
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
  - model: GIN
    model_key: gin
    model_plain: GIN
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
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 41
    true_value: 0.7059
    true_std: 0.0089
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.15610000000000002
    value_note: ''
    paper_rank: 288
    rank_delta: 247
    rank_delta_abs: 247
    rank_delta_direction: worse
    sort_value: 0.7059
    sort_std: 0.0089
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
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
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
  - model: GatedGCN+RWSE
    model_key: gatedgcn+rwse
    model_plain: GatedGCN+RWSE
    value: 0.6069
    std: 0.0035
    paper_value: 0.6069
    paper_std: 0.0035
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 133
    true_value: 0.6685
    true_std: 0.0062
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.06159999999999999
    value_note: ''
    paper_rank: 239
    rank_delta: 106
    rank_delta_abs: 106
    rank_delta_direction: worse
    sort_value: 0.6685
    sort_std: 0.0062
    is_best: false
  - model: GraphFP_CP
    model_key: graphfp_cp
    model_plain: GraphFP_CP
    value: 0.6267
    std: 0.0073
    paper_value: 0.6267
    paper_std: 0.0073
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 228
    true_value: 0.6267
    true_std: 0.0073
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 228
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6267
    sort_std: 0.0073
    is_best: false
  - model: GCNII
    model_key: gcnii
    model_plain: GCNII
    value: 0.5543
    std: 0.0078
    paper_value: 0.5543
    paper_std: 0.0078
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 285
    true_value: 0.5543
    true_std: 0.0078
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: LRGB
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 285
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
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
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.3547
    std: 0.0045
    paper_value: 0.3547
    paper_std: 0.0045
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 9
    true_value: 0.2429
    true_std: 0.0019
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11180000000000001
    value_note: ''
    paper_rank: 311
    rank_delta: 302
    rank_delta_abs: 302
    rank_delta_direction: worse
    sort_value: 0.2429
    sort_std: 0.0019
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
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
  - model: GatedGCN+RWSE
    model_key: gatedgcn+rwse
    model_plain: GatedGCN+RWSE
    value: 0.3357
    std: 0.0006
    paper_value: 0.3357
    paper_std: 0.0006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
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
  - model: GraphFP
    model_key: graphfp
    model_plain: GraphFP
    value: 0.3137
    std: 0.0019
    paper_value: 0.3137
    paper_std: 0.0019
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 279
    true_value: 0.3137
    true_std: 0.0019
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 279
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3137
    sort_std: 0.0019
    is_best: false
  - model: GraphFP_CP
    model_key: graphfp_cp
    model_plain: GraphFP_CP
    value: 0.3137
    std: 0.0019
    paper_value: 0.3137
    paper_std: 0.0019
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 280
    true_value: 0.3137
    true_std: 0.0019
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 280
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3137
    sort_std: 0.0019
    is_best: false
  - model: GCNII
    model_key: gcnii
    model_plain: GCNII
    value: 0.3471
    std: 0.001
    paper_value: 0.3471
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 300
    true_value: 0.3471
    true_std: 0.001
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: LRGB
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 300
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3471
    sort_std: 0.001
    is_best: false
  metric: MAE
  higher_is_better: false
- &id009
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
  - model: GraphFP
    model_key: graphfp
    model_plain: GraphFP
    value: 0.593
    std: 0.01
    paper_value: 0.593
    paper_std: 0.01
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 7
    true_value: 0.636
    true_std: 0.012
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04300000000000004
    value_note: ''
    paper_rank: 36
    rank_delta: 29
    rank_delta_abs: 29
    rank_delta_direction: worse
    sort_value: 0.636
    sort_std: 0.012
    is_best: false
  - model: GraphFP_CP
    model_key: graphfp_cp
    model_plain: GraphFP_CP
    value: 0.636
    std: 0.012
    paper_value: 0.636
    paper_std: 0.012
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 8
    true_value: 0.636
    true_std: 0.012
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.636
    sort_std: 0.012
    is_best: false
  - model: CP, \(α = 0.1\)
    model_key: cp, \(α = 0.1\)
    model_plain: CP, \(α = 0.1\)
    value: 0.636
    std: 0.012
    paper_value: 0.636
    paper_std: 0.012
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 9
    true_value: 0.636
    true_std: 0.012
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.636
    sort_std: 0.012
    is_best: false
  - model: CP, alpha=0.1
    model_key: cp, alpha=0.1
    model_plain: CP, alpha=0.1
    value: 0.627
    std: 0.009
    paper_value: 0.627
    paper_std: 0.009
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 13
    true_value: 0.627
    true_std: 0.009
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.627
    sort_std: 0.009
    is_best: false
  - model: CPF, \(α = 0.2\)
    model_key: cpf, \(α = 0.2\)
    model_plain: CPF, \(α = 0.2\)
    value: 0.627
    std: 0.009
    paper_value: 0.627
    paper_std: 0.009
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 14
    true_value: 0.627
    true_std: 0.009
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.627
    sort_std: 0.009
    is_best: false
  - model: GraphMVP
    model_key: graphmvp
    model_plain: GraphMVP
    value: 0.623
    std: 0.016
    paper_value: 0.623
    paper_std: 0.016
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Liu et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 15
    true_value: 0.623
    true_std: 0.016
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.623
    sort_std: 0.016
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.615
    std: 0.008
    paper_value: 0.615
    paper_std: 0.008
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 17
    true_value: 0.615
    true_std: 0.008
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.615
    sort_std: 0.008
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.613
    std: 0.004
    paper_value: 0.613
    paper_std: 0.004
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 18
    true_value: 0.613
    true_std: 0.004
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.613
    sort_std: 0.004
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.612
    std: 0.008
    paper_value: 0.612
    paper_std: 0.008
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 20
    true_value: 0.612
    true_std: 0.008
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.612
    sort_std: 0.008
    is_best: false
  - model: GraphLoG
    model_key: graphlog
    model_plain: GraphLoG
    value: 0.595
    std: 0.015
    paper_value: 0.595
    paper_std: 0.015
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xu et al. 2021
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 19
    true_value: 0.612
    true_std: 0.011
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.017000000000000015
    value_note: ''
    paper_rank: 36
    rank_delta: 17
    rank_delta_abs: 17
    rank_delta_direction: worse
    sort_value: 0.612
    sort_std: 0.011
    is_best: false
  - model: AttrMasking
    model_key: attrmasking
    model_plain: AttrMasking
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
    source_ref: Hu et al. 2020
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 22
    true_value: 0.61
    true_std: 0.007
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.61
    sort_std: 0.007
    is_best: false
  - model: G-Motif
    model_key: g-motif
    model_plain: G-Motif
    value: 0.61
    std: 0.015
    paper_value: 0.61
    paper_std: 0.015
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Rong et al. 2020
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 23
    true_value: 0.61
    true_std: 0.015
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.61
    sort_std: 0.015
    is_best: false
  - model: ContextPred
    model_key: contextpred
    model_plain: ContextPred
    value: 0.609
    std: 0.006
    paper_value: 0.609
    paper_std: 0.006
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hu et al. 2020
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 26
    true_value: 0.609
    true_std: 0.006
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.609
    sort_std: 0.006
    is_best: false
  - model: GIN_C (Vocab 200)
    model_key: gin_c (vocab 200)
    model_plain: GIN_C (Vocab 200)
    value: 0.606
    std: 0.005
    paper_value: 0.606
    paper_std: 0.005
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 29
    true_value: 0.606
    true_std: 0.005
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.606
    sort_std: 0.005
    is_best: false
  - model: GraphCL
    model_key: graphcl
    model_plain: GraphCL
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
    source_ref: You et al. 2020
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 32
    true_value: 0.605
    true_std: 0.009
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.605
    sort_std: 0.009
    is_best: false
  - model: JOAOv2
    model_key: joaov2
    model_plain: JOAOv2
    value: 0.605
    std: 0.007
    paper_value: 0.605
    paper_std: 0.007
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: You et al. 2021
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 33
    true_value: 0.605
    true_std: 0.007
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.605
    sort_std: 0.007
    is_best: false
  - model: JOAO
    model_key: joao
    model_plain: JOAO
    value: 0.6
    std: 0.008
    paper_value: 0.6
    paper_std: 0.008
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: You et al. 2021
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 36
    true_value: 0.6
    true_std: 0.008
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 36
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6
    sort_std: 0.008
    is_best: false
  - model: GraphFP-JT_C
    model_key: graphfp-jt_c
    model_plain: GraphFP-JT_C
    value: 0.593
    std: 0.013
    paper_value: 0.593
    paper_std: 0.013
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 37
    true_value: 0.593
    true_std: 0.013
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 37
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.593
    sort_std: 0.013
    is_best: false
  - model: G-Contextual
    model_key: g-contextual
    model_plain: G-Contextual
    value: 0.587
    std: 0.01
    paper_value: 0.587
    paper_std: 0.01
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Rong et al. 2020
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 40
    true_value: 0.587
    true_std: 0.01
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 40
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.587
    sort_std: 0.01
    is_best: false
  - model: GPT-GNN
    model_key: gpt-gnn
    model_plain: GPT-GNN
    value: 0.581
    std: 0.003
    paper_value: 0.581
    paper_std: 0.003
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hu et al. 2020
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 42
    true_value: 0.581
    true_std: 0.003
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 42
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.581
    sort_std: 0.003
    is_best: false
  - model: MGSSL
    model_key: mgssl
    model_plain: MGSSL
    value: 0.577
    std: 0.007
    paper_value: 0.577
    paper_std: 0.007
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhang et al.
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 43
    true_value: 0.577
    true_std: 0.007
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 43
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.577
    sort_std: 0.007
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id005
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
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.758
    std: 0.003
    paper_value: 0.758
    paper_std: 0.003
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 5
    true_value: 0.85
    true_std: 0.009
    value_gap_source_arxiv: '2310.01704'
    value_gap_source_title: Transformers are efficient hierarchical chemical graph
      learners
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09199999999999997
    value_note: ''
    paper_rank: 45
    rank_delta: 40
    rank_delta_abs: 40
    rank_delta_direction: worse
    sort_value: 0.85
    sort_std: 0.009
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.743
    std: 0.003
    paper_value: 0.743
    paper_std: 0.003
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 12
    true_value: 0.84
    true_std: 0.004
    value_gap_source_arxiv: '2310.01704'
    value_gap_source_title: Transformers are efficient hierarchical chemical graph
      learners
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09699999999999998
    value_note: ''
    paper_rank: 60
    rank_delta: 48
    rank_delta_abs: 48
    rank_delta_direction: worse
    sort_value: 0.84
    sort_std: 0.004
    is_best: false
  - model: AttrMasking
    model_key: attrmasking
    model_plain: AttrMasking
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
    source_ref: Hu et al. 2020
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 31
    true_value: 0.767
    true_std: 0.004
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.767
    sort_std: 0.004
    is_best: false
  - model: GraphFP
    model_key: graphfp
    model_plain: GraphFP
    value: 0.76
    std: 0.005
    paper_value: 0.76
    paper_std: 0.005
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 43
    true_value: 0.76
    true_std: 0.005
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 43
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.76
    sort_std: 0.005
    is_best: false
  - model: ContextPred
    model_key: contextpred
    model_plain: ContextPred
    value: 0.757
    std: 0.007
    paper_value: 0.757
    paper_std: 0.007
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hu et al. 2020
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 48
    true_value: 0.757
    true_std: 0.007
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 48
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.757
    sort_std: 0.007
    is_best: false
  - model: GraphLoG
    model_key: graphlog
    model_plain: GraphLoG
    value: 0.751
    std: 0.01
    paper_value: 0.751
    paper_std: 0.01
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xu et al. 2021
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 49
    true_value: 0.757
    true_std: 0.005
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.006000000000000005
    value_note: global 0.7570 within std
    paper_rank: 53
    rank_delta: 4
    rank_delta_abs: 4
    rank_delta_direction: worse
    sort_value: 0.757
    sort_std: 0.005
    is_best: false
  - model: GIN_C (Vocab 200)
    model_key: gin_c (vocab 200)
    model_plain: GIN_C (Vocab 200)
    value: 0.754
    std: 0.004
    paper_value: 0.754
    paper_std: 0.004
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 52
    true_value: 0.754
    true_std: 0.004
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 52
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.754
    sort_std: 0.004
    is_best: false
  - model: JOAO
    model_key: joao
    model_plain: JOAO
    value: 0.75
    std: 0.003
    paper_value: 0.75
    paper_std: 0.003
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: You et al. 2021
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 55
    true_value: 0.75
    true_std: 0.003
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 55
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.75
    sort_std: 0.003
    is_best: false
  - model: G-Contextual
    model_key: g-contextual
    model_plain: G-Contextual
    value: 0.75
    std: 0.006
    paper_value: 0.75
    paper_std: 0.006
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Rong et al. 2020
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 54
    true_value: 0.75
    true_std: 0.006
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 54
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.75
    sort_std: 0.006
    is_best: false
  - model: GraphMVP
    model_key: graphmvp
    model_plain: GraphMVP
    value: 0.745
    std: 0.004
    paper_value: 0.745
    paper_std: 0.004
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Liu et al. 2022
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 56
    true_value: 0.749
    true_std: 0.008
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0040000000000000036
    value_note: global 0.7490 within std
    paper_rank: 58
    rank_delta: 2
    rank_delta_abs: 2
    rank_delta_direction: worse
    sort_value: 0.749
    sort_std: 0.008
    is_best: false
  - model: GPT-GNN
    model_key: gpt-gnn
    model_plain: GPT-GNN
    value: 0.749
    std: 0.003
    paper_value: 0.749
    paper_std: 0.003
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hu et al. 2020
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 57
    true_value: 0.749
    true_std: 0.003
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 57
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.749
    sort_std: 0.003
    is_best: false
  - model: MGSSL
    model_key: mgssl
    model_plain: MGSSL
    value: 0.749
    std: 0.006
    paper_value: 0.749
    paper_std: 0.006
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhang et al.
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 58
    true_value: 0.749
    true_std: 0.006
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 58
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.749
    sort_std: 0.006
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.745
    std: 0.006
    paper_value: 0.745
    paper_std: 0.006
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 59
    true_value: 0.745
    true_std: 0.006
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 59
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.745
    sort_std: 0.006
    is_best: false
  - model: JOAOv2
    model_key: joaov2
    model_plain: JOAOv2
    value: 0.743
    std: 0.006
    paper_value: 0.743
    paper_std: 0.006
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: You et al. 2021
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 63
    true_value: 0.743
    true_std: 0.006
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 63
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.743
    sort_std: 0.006
    is_best: false
  - model: CP, alpha=0.1
    model_key: cp, alpha=0.1
    model_plain: CP, alpha=0.1
    value: 0.742
    std: 0.007
    paper_value: 0.742
    paper_std: 0.007
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 64
    true_value: 0.742
    true_std: 0.007
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 64
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.742
    sort_std: 0.007
    is_best: false
  - model: GraphFP_CP
    model_key: graphfp_cp
    model_plain: GraphFP_CP
    value: 0.74
    std: 0.007
    paper_value: 0.74
    paper_std: 0.007
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 66
    true_value: 0.74
    true_std: 0.007
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 66
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.74
    sort_std: 0.007
    is_best: false
  - model: GraphCL
    model_key: graphcl
    model_plain: GraphCL
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
    source_ref: You et al. 2020
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 69
    true_value: 0.739
    true_std: 0.007
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 69
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.739
    sort_std: 0.007
    is_best: false
  - model: G-Motif
    model_key: g-motif
    model_plain: G-Motif
    value: 0.736
    std: 0.007
    paper_value: 0.736
    paper_std: 0.007
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Rong et al. 2020
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 70
    true_value: 0.736
    true_std: 0.007
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 70
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.736
    sort_std: 0.007
    is_best: false
  - model: GraphFP-JT_C
    model_key: graphfp-jt_c
    model_plain: GraphFP-JT_C
    value: 0.727
    std: 0.008
    paper_value: 0.727
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
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 75
    true_value: 0.727
    true_std: 0.008
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 75
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.727
    sort_std: 0.008
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id007
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
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.639
    std: 0.004
    paper_value: 0.639
    paper_std: 0.004
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 5
    true_value: 0.741
    true_std: 0.004
    value_gap_source_arxiv: '2310.01704'
    value_gap_source_title: Transformers are efficient hierarchical chemical graph
      learners
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10199999999999998
    value_note: ''
    paper_rank: 29
    rank_delta: 24
    rank_delta_abs: 24
    rank_delta_direction: worse
    sort_value: 0.741
    sort_std: 0.004
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.633
    std: 0.005
    paper_value: 0.633
    paper_std: 0.005
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 7
    true_value: 0.735
    true_std: 0.002
    value_gap_source_arxiv: '2310.01704'
    value_gap_source_title: Transformers are efficient hierarchical chemical graph
      learners
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10199999999999998
    value_note: ''
    paper_rank: 39
    rank_delta: 32
    rank_delta_abs: 32
    rank_delta_direction: worse
    sort_value: 0.735
    sort_std: 0.002
    is_best: false
  - model: CP, alpha=0.1
    model_key: cp, alpha=0.1
    model_plain: CP, alpha=0.1
    value: 0.648
    std: 0.005
    paper_value: 0.648
    paper_std: 0.005
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 23
    true_value: 0.648
    true_std: 0.005
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.648
    sort_std: 0.005
    is_best: false
  - model: AttrMasking
    model_key: attrmasking
    model_plain: AttrMasking
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
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 26
    true_value: 0.642
    true_std: 0.005
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.642
    sort_std: 0.005
    is_best: false
  - model: GraphFP
    model_key: graphfp
    model_plain: GraphFP
    value: 0.632
    std: 0.007
    paper_value: 0.632
    paper_std: 0.007
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 30
    true_value: 0.639
    true_std: 0.009
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.007000000000000006
    value_note: global 0.6390 within std
    paper_rank: 40
    rank_delta: 10
    rank_delta_abs: 10
    rank_delta_direction: worse
    sort_value: 0.639
    sort_std: 0.009
    is_best: false
  - model: ContextPred
    model_key: contextpred
    model_plain: ContextPred
    value: 0.639
    std: 0.006
    paper_value: 0.639
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
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 32
    true_value: 0.639
    true_std: 0.006
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.639
    sort_std: 0.006
    is_best: false
  - model: GraphFP_CP
    model_key: graphfp_cp
    model_plain: GraphFP_CP
    value: 0.639
    std: 0.009
    paper_value: 0.639
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
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 33
    true_value: 0.639
    true_std: 0.009
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.639
    sort_std: 0.009
    is_best: false
  - model: GIN_C (Vocab 200)
    model_key: gin_c (vocab 200)
    model_plain: GIN_C (Vocab 200)
    value: 0.637
    std: 0.006
    paper_value: 0.637
    paper_std: 0.006
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 35
    true_value: 0.637
    true_std: 0.006
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.637
    sort_std: 0.006
    is_best: false
  - model: GraphLoG
    model_key: graphlog
    model_plain: GraphLoG
    value: 0.624
    std: 0.002
    paper_value: 0.624
    paper_std: 0.002
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xu 2021
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 38
    true_value: 0.635
    true_std: 0.007
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.01100000000000001
    value_note: ''
    paper_rank: 47
    rank_delta: 9
    rank_delta_abs: 9
    rank_delta_direction: worse
    sort_value: 0.635
    sort_std: 0.007
    is_best: false
  - model: MGSSL
    model_key: mgssl
    model_plain: MGSSL
    value: 0.633
    std: 0.005
    paper_value: 0.633
    paper_std: 0.005
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhang et al.
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 40
    true_value: 0.633
    true_std: 0.005
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 40
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.633
    sort_std: 0.005
    is_best: false
  - model: JOAOv2
    model_key: joaov2
    model_plain: JOAOv2
    value: 0.632
    std: 0.005
    paper_value: 0.632
    paper_std: 0.005
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: You 2021
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 41
    true_value: 0.632
    true_std: 0.005
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 41
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.632
    sort_std: 0.005
    is_best: false
  - model: GraphMVP
    model_key: graphmvp
    model_plain: GraphMVP
    value: 0.627
    std: 0.001
    paper_value: 0.627
    paper_std: 0.001
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Liu 2022
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 42
    true_value: 0.631
    true_std: 0.002
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0040000000000000036
    value_note: ''
    paper_rank: 45
    rank_delta: 3
    rank_delta_abs: 3
    rank_delta_direction: worse
    sort_value: 0.631
    sort_std: 0.002
    is_best: false
  - model: JOAO
    model_key: joao
    model_plain: JOAO
    value: 0.629
    std: 0.005
    paper_value: 0.629
    paper_std: 0.005
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: You 2021
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 43
    true_value: 0.629
    true_std: 0.005
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 43
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.629
    sort_std: 0.005
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.628
    std: 0.003
    paper_value: 0.628
    paper_std: 0.003
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 45
    true_value: 0.628
    true_std: 0.003
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 45
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.628
    sort_std: 0.003
    is_best: false
  - model: G-Contextual
    model_key: g-contextual
    model_plain: G-Contextual
    value: 0.628
    std: 0.007
    paper_value: 0.628
    paper_std: 0.007
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Rong 2020
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 44
    true_value: 0.628
    true_std: 0.007
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 44
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.628
    sort_std: 0.007
    is_best: false
  - model: GPT-GNN
    model_key: gpt-gnn
    model_plain: GPT-GNN
    value: 0.625
    std: 0.004
    paper_value: 0.625
    paper_std: 0.004
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hu 2020
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 46
    true_value: 0.625
    true_std: 0.004
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 46
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.625
    sort_std: 0.004
    is_best: false
  - model: GraphFP-JT_C
    model_key: graphfp-jt_c
    model_plain: GraphFP-JT_C
    value: 0.625
    std: 0.009
    paper_value: 0.625
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
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 47
    true_value: 0.625
    true_std: 0.009
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 47
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.625
    sort_std: 0.009
    is_best: false
  - model: GraphCL
    model_key: graphcl
    model_plain: GraphCL
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
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 48
    true_value: 0.624
    true_std: 0.006
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 48
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.624
    sort_std: 0.006
    is_best: false
  - model: G-Motif
    model_key: g-motif
    model_plain: G-Motif
    value: 0.623
    std: 0.006
    paper_value: 0.623
    paper_std: 0.006
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Rong 2020
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 50
    true_value: 0.623
    true_std: 0.006
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 50
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.623
    sort_std: 0.006
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id003
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
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.746
    std: 0.009
    paper_value: 0.746
    paper_std: 0.009
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to ogbg-molhiv (score=90)'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 3
    true_value: 0.9681
    true_std: 0.0003
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.22209999999999996
    value_note: ''
    paper_rank: 189
    rank_delta: 186
    rank_delta_abs: 186
    rank_delta_direction: worse
    sort_value: 0.9681
    sort_std: 0.0003
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.761
    std: 0.014
    paper_value: 0.761
    paper_std: 0.014
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to ogbg-molhiv (score=90)'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 4
    true_value: 0.968
    true_std: 0.002
    value_gap_source_arxiv: '2502.02379'
    value_gap_source_title: 'No Metric to Rule Them All: Toward Principled Evaluations
      of Graph-Learning Datasets'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.20699999999999996
    value_note: ''
    paper_rank: 160
    rank_delta: 156
    rank_delta_abs: 156
    rank_delta_direction: worse
    sort_value: 0.968
    sort_std: 0.002
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
  - model: GraphCL
    model_key: graphcl
    model_plain: GraphCL
    value: 0.785
    std: 0.012
    paper_value: 0.785
    paper_std: 0.012
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: You2020GraphCL
    variant_inference_reason: 'dataset: fuzzy match to ogbg-molhiv (score=90)'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 88
    true_value: 0.785
    true_std: 0.012
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 88
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.785
    sort_std: 0.012
    is_best: false
  - model: GraphFP
    model_key: graphfp
    model_plain: GraphFP
    value: 0.767
    std: 0.01
    paper_value: 0.767
    paper_std: 0.01
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to ogbg-molhiv (score=90)'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 107
    true_value: 0.78
    true_std: 0.015
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.013000000000000012
    value_note: global 0.7800 within std
    paper_rank: 147
    rank_delta: 40
    rank_delta_abs: 40
    rank_delta_direction: worse
    sort_value: 0.78
    sort_std: 0.015
    is_best: false
  - model: GraphFP_CP
    model_key: graphfp_cp
    model_plain: GraphFP_CP
    value: 0.78
    std: 0.015
    paper_value: 0.78
    paper_std: 0.015
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to ogbg-molhiv (score=90)'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 112
    true_value: 0.78
    true_std: 0.015
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 112
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.78
    sort_std: 0.015
    is_best: false
  - model: JOAOv2
    model_key: joaov2
    model_plain: JOAOv2
    value: 0.775
    std: 0.012
    paper_value: 0.775
    paper_std: 0.012
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: pmlr-v139-you21a
    variant_inference_reason: 'dataset: fuzzy match to ogbg-molhiv (score=90)'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 124
    true_value: 0.775
    true_std: 0.012
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 124
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.775
    sort_std: 0.012
    is_best: false
  - model: ContextPred
    model_key: contextpred
    model_plain: ContextPred
    value: 0.773
    std: 0.01
    paper_value: 0.773
    paper_std: 0.01
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: hu2020pretraining
    variant_inference_reason: 'dataset: fuzzy match to ogbg-molhiv (score=90)'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 130
    true_value: 0.773
    true_std: 0.01
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 130
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.773
    sort_std: 0.01
    is_best: false
  - model: AttrMasking
    model_key: attrmasking
    model_plain: AttrMasking
    value: 0.772
    std: 0.011
    paper_value: 0.772
    paper_std: 0.011
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: hu2020pretraining
    variant_inference_reason: 'dataset: fuzzy match to ogbg-molhiv (score=90)'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 131
    true_value: 0.772
    true_std: 0.011
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 131
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.772
    sort_std: 0.011
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.771
    std: 0.011
    paper_value: 0.771
    paper_std: 0.011
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to ogbg-molhiv (score=90)'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 136
    true_value: 0.771
    true_std: 0.011
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 136
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.771
    sort_std: 0.011
    is_best: false
  - model: JOAO
    model_key: joao
    model_plain: JOAO
    value: 0.767
    std: 0.012
    paper_value: 0.767
    paper_std: 0.012
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: pmlr-v139-you21a
    variant_inference_reason: 'dataset: fuzzy match to ogbg-molhiv (score=90)'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 148
    true_value: 0.767
    true_std: 0.012
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 148
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.767
    sort_std: 0.012
    is_best: false
  - model: CP, alpha=0.1
    model_key: cp, alpha=0.1
    model_plain: CP, alpha=0.1
    value: 0.767
    std: 0.013
    paper_value: 0.767
    paper_std: 0.013
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to ogbg-molhiv (score=90)'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 149
    true_value: 0.767
    true_std: 0.013
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 149
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.767
    sort_std: 0.013
    is_best: false
  - model: G-Contextual
    model_key: g-contextual
    model_plain: G-Contextual
    value: 0.763
    std: 0.015
    paper_value: 0.763
    paper_std: 0.015
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: rong2020grover
    variant_inference_reason: 'dataset: fuzzy match to ogbg-molhiv (score=90)'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 157
    true_value: 0.763
    true_std: 0.015
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 157
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.763
    sort_std: 0.015
    is_best: false
  - model: GraphMVP
    model_key: graphmvp
    model_plain: GraphMVP
    value: 0.748
    std: 0.014
    paper_value: 0.748
    paper_std: 0.014
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: liu2022pretraining
    variant_inference_reason: 'dataset: fuzzy match to ogbg-molhiv (score=90)'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 164
    true_value: 0.76
    true_std: 0.001
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.01200000000000001
    value_note: global 0.7600 within std
    paper_rank: 189
    rank_delta: 25
    rank_delta_abs: 25
    rank_delta_direction: worse
    sort_value: 0.76
    sort_std: 0.001
    is_best: false
  - model: MGSSL
    model_key: mgssl
    model_plain: MGSSL
    value: 0.757
    std: 0.013
    paper_value: 0.757
    paper_std: 0.013
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: zhang_mgssl
    variant_inference_reason: 'dataset: fuzzy match to ogbg-molhiv (score=90)'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 169
    true_value: 0.757
    true_std: 0.013
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 169
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.757
    sort_std: 0.013
    is_best: false
  - model: GIN_C (Vocab 200)
    model_key: gin_c (vocab 200)
    model_plain: GIN_C (Vocab 200)
    value: 0.751
    std: 0.013
    paper_value: 0.751
    paper_std: 0.013
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to ogbg-molhiv (score=90)'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 185
    true_value: 0.751
    true_std: 0.013
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 185
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.751
    sort_std: 0.013
    is_best: false
  - model: G-Motif
    model_key: g-motif
    model_plain: G-Motif
    value: 0.738
    std: 0.012
    paper_value: 0.738
    paper_std: 0.012
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: rong2020grover
    variant_inference_reason: 'dataset: fuzzy match to ogbg-molhiv (score=90)'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 198
    true_value: 0.738
    true_std: 0.012
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 198
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.738
    sort_std: 0.012
    is_best: false
  - model: GraphLoG
    model_key: graphlog
    model_plain: GraphLoG
    value: 0.737
    std: 0.009
    paper_value: 0.737
    paper_std: 0.009
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: xu21graphlog
    variant_inference_reason: 'dataset: fuzzy match to ogbg-molhiv (score=90)'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 199
    true_value: 0.737
    true_std: 0.009
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 199
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.737
    sort_std: 0.009
    is_best: false
  - model: GraphFP-JT_C
    model_key: graphfp-jt_c
    model_plain: GraphFP-JT_C
    value: 0.73
    std: 0.019
    paper_value: 0.73
    paper_std: 0.019
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to ogbg-molhiv (score=90)'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 206
    true_value: 0.73
    true_std: 0.019
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 206
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.73
    sort_std: 0.019
    is_best: false
  - model: GPT-GNN
    model_key: gpt-gnn
    model_plain: GPT-GNN
    value: 0.652
    std: 0.021
    paper_value: 0.652
    paper_std: 0.021
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: hu2020gpt
    variant_inference_reason: 'dataset: fuzzy match to ogbg-molhiv (score=90)'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 217
    true_value: 0.652
    true_std: 0.021
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 217
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.652
    sort_std: 0.021
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
results_grouped:
- benchmark: LRGB
  datasets:
  - *id001
  - *id002
- benchmark: OGB
  datasets:
  - *id003
- benchmark: MoleculeNet
  datasets:
  - *id004
  - *id005
  - *id006
  - *id007
  - *id008
  - *id009
  - *id010
main_figure: /figures/2310.03274/main_figure.png
---

