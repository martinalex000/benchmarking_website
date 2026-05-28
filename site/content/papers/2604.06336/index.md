---
title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale Molecular Representation
  Learning'
arxiv_id: '2604.06336'
source_url: ''
authors: []
published_date: Apr 2026
published_date_iso: 2026-04
abstract: Graph Transformers have recently attracted attention for molecular property
  prediction by combining the inductive biases of graph neural networks (GNNs) with
  the global receptive field of Transformers. However, many existing hybrid architectures
  remain GNN-dominated, causing the resulting representations to remain heavily shaped
  by local message passing. Moreover, most existing methods operate at only a single
  structural granularity, limiting their ability to capture molecular patterns that
  span multiple molecular scales. We introduce BiScale-GTR, a unified framework for
  self-supervised molecular representation learning that combines chemically grounded
  fragment tokenization with adaptive multi-scale reasoning. Our method improves graph
  Byte Pair Encoding (BPE) tokenization to produce consistent, chemically valid, and
  high-coverage fragment tokens, which are used as fragment-level inputs to a parallel
  GNN-Transformer architecture. Architecturally, atom-level representations learned
  by a GNN are pooled into fragment-level embeddings and fused with fragment token
  embeddings before Transformer reasoning, enabling the model to jointly capture local
  chemical environments, substructure-level motifs, and long-range molecular dependencies.
  Experiments on MoleculeNet, PharmaBench, and the Long Range Graph Benchmark (LRGB)
  demonstrate state-of-the-art performance across both classification and regression
  tasks. Attribution analysis further shows that BiScale-GTR highlights chemically
  meaningful functional motifs, providing interpretable links between molecular structure
  and predicted properties. Code will be released upon acceptance.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- BiScale-GTR (Fragment)
- BiScale-GTR (Molecule)
- BiScale-GTR
mrr: 0.008
adjusted_mrr: 0.0027
mrr_dataset_count: 1
benchmark_categories:
- LRGB
- TU Dortmund
- OGB
- MoleculeNet
- GraphBench
task_categories:
- graph_classification
- graph_regression
- node_classification
experiment_scopes:
- graph-level
- node-level
results:
- &id005
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
    paper_value: 0.85
    paper_std: 0.011
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 2
    true_value: 0.85
    true_std: 0.011
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
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
    paper_value: 0.843
    paper_std: 0.006
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Liu et al. 2023
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 4
    true_value: 0.843
    true_std: 0.006
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.843
    sort_std: 0.006
    is_best: false
  - model: BiScale-GTR (Fragment)
    model_key: biscale-gtr (fragment)
    model_plain: BiScale-GTR (Fragment)
    value: 0.838
    std: 0.012
    paper_value: 0.838
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
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 5
    true_value: 0.838
    true_std: 0.012
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.838
    sort_std: 0.012
    is_best: false
  - model: GraphLoG
    model_key: graphlog
    model_plain: GraphLoG
    value: 0.835
    std: 0.012
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
    global_rank: 6
    sort_value: 0.835
    sort_std: 0.012
    is_best: false
  - model: GraphMAE
    model_key: graphmae
    model_plain: GraphMAE
    value: 0.782
    std: 0.015
    paper_value: 0.782
    paper_std: 0.015
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hou et al. 2022
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 7
    true_value: 0.831
    true_std: 0.009
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04899999999999993
    value_note: ''
    paper_rank: 42
    rank_delta: 35
    rank_delta_abs: 35
    rank_delta_direction: worse
    sort_value: 0.831
    sort_std: 0.009
    is_best: false
  - model: MORE
    model_key: more
    model_plain: MORE
    value: 0.828
    std: 0.013
    paper_value: 0.828
    paper_std: 0.013
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Son et al. 2025
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 8
    true_value: 0.828
    true_std: 0.013
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.828
    sort_std: 0.013
    is_best: false
  - model: GraphGPS+LAC
    model_key: graphgps+lac
    model_plain: GraphGPS+LAC
    value: 0.825
    std: null
    paper_value: 0.825
    paper_std: null
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Yang et al. 2025
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 12
    true_value: 0.825
    true_std: null
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.825
    sort_std: null
    is_best: false
  - model: Mole-BERT
    model_key: mole-bert
    model_plain: Mole-BERT
    value: 0.808
    std: 0.014
    paper_value: 0.808
    paper_std: 0.014
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xia et al. 2023
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 17
    true_value: 0.808
    true_std: 0.014
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.808
    sort_std: 0.014
    is_best: false
  - model: GraphFP
    model_key: graphfp
    model_plain: GraphFP
    value: 0.805
    std: 0.018
    paper_value: 0.805
    paper_std: 0.018
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Luong et al. 2023
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 19
    true_value: 0.807
    true_std: 0.048
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0020000000000000018
    value_note: global 0.8070 within std
    paper_rank: 20
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.807
    sort_std: 0.048
    is_best: false
  - model: GraphMVP
    model_key: graphmvp
    model_plain: GraphMVP
    value: 0.793
    std: 0.015
    paper_value: 0.793
    paper_std: 0.015
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Liu et al. 2021
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 31
    true_value: 0.793
    true_std: 0.015
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.793
    sort_std: 0.015
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id007
  dataset: BBBP
  rows:
  - model: BiScale-GTR (Fragment)
    model_key: biscale-gtr (fragment)
    model_plain: BiScale-GTR (Fragment)
    value: 0.738
    std: 0.004
    paper_value: 0.738
    paper_std: 0.004
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 1
    true_value: 0.738
    true_std: 0.004
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.738
    sort_std: 0.004
    is_best: true
  - model: GraphGPS+LAC
    model_key: graphgps+lac
    model_plain: GraphGPS+LAC
    value: 0.736
    std: null
    paper_value: 0.736
    paper_std: null
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Yang et al. 2025
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 2
    true_value: 0.736
    true_std: null
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
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
  - model: SimSGT
    model_key: simsgt
    model_plain: SimSGT
    value: 0.722
    std: 0.009
    paper_value: 0.722
    paper_std: 0.009
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Liu et al. 2023
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 5
    true_value: 0.722
    true_std: 0.009
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.722
    sort_std: 0.009
    is_best: false
  - model: GraphMAE
    model_key: graphmae
    model_plain: GraphMAE
    value: 0.712
    std: 0.01
    paper_value: 0.712
    paper_std: 0.01
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hou et al. 2022
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 6
    true_value: 0.72
    true_std: 0.006
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.008000000000000007
    value_note: global 0.7200 within std
    paper_rank: 13
    rank_delta: 7
    rank_delta_abs: 7
    rank_delta_direction: worse
    sort_value: 0.72
    sort_std: 0.006
    is_best: false
  - model: GraphFP
    model_key: graphfp
    model_plain: GraphFP
    value: 0.72
    std: 0.017
    paper_value: 0.72
    paper_std: 0.017
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Luong et al. 2023
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 7
    true_value: 0.72
    true_std: 0.017
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.72
    sort_std: 0.017
    is_best: true
  - model: GraphFP_CP
    model_key: graphfp_cp
    model_plain: GraphFP_CP
    value: 0.72
    std: 0.017
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
    uses_external_data: false
    is_global_top: true
    global_rank: 8
    sort_value: 0.72
    sort_std: 0.017
    is_best: true
  - model: Mole-BERT
    model_key: mole-bert
    model_plain: Mole-BERT
    value: 0.719
    std: 0.008
    paper_value: 0.719
    paper_std: 0.008
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xia et al. 2023
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 9
    true_value: 0.719
    true_std: 0.008
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.719
    sort_std: 0.008
    is_best: false
  - model: MORE
    model_key: more
    model_plain: MORE
    value: 0.719
    std: 0.009
    paper_value: 0.719
    paper_std: 0.009
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Son et al. 2025
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 10
    true_value: 0.719
    true_std: 0.009
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.719
    sort_std: 0.009
    is_best: false
  - model: GraphMVP
    model_key: graphmvp
    model_plain: GraphMVP
    value: 0.708
    std: 0.005
    paper_value: 0.708
    paper_std: 0.005
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Liu et al. 2021
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 16
    true_value: 0.708
    true_std: 0.005
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.708
    sort_std: 0.005
    is_best: false
  - model: BiScale-GTR (Molecule)
    model_key: biscale-gtr (molecule)
    model_plain: BiScale-GTR (Molecule)
    value: 0.684
    std: 0.008
    paper_value: 0.684
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
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 32
    true_value: 0.684
    true_std: 0.008
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.684
    sort_std: 0.008
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id003
  dataset: D&D
  rows:
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.05
    std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.08618'
    title: HSG-12M
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.05
    sort_std: 0.021
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.093
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
    sort_value: 0.093
    sort_std: null
    is_best: false
  - model: MF
    model_key: mf
    model_plain: MF
    value: 0.271
    std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.08618'
    title: HSG-12M
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.271
    sort_std: 0.004
    is_best: false
  - model: FragFormer
    model_key: fragformer
    model_plain: FragFormer
    value: 14.425
    std: null
    paper_value: 14.425
    paper_std: null
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: null
    sort_value: 14.425
    sort_std: null
    is_best: false
  - model: PharmHGT
    model_key: pharmhgt
    model_plain: PharmHGT
    value: 15.02
    std: null
    paper_value: 15.02
    paper_std: null
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: null
    sort_value: 15.02
    sort_std: null
    is_best: false
  - model: KP-GPT
    model_key: kp-gpt
    model_plain: KP-GPT
    value: 16.86
    std: null
    paper_value: 16.86
    paper_std: null
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: null
    sort_value: 16.86
    sort_std: null
    is_best: false
  - model: BiScale-GTR (Molecule)
    model_key: biscale-gtr (molecule)
    model_plain: BiScale-GTR (Molecule)
    value: 16.901
    std: null
    paper_value: 16.901
    paper_std: null
    metric: RMSE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: null
    sort_value: 16.901
    sort_std: null
    is_best: false
  - model: MPG
    model_key: mpg
    model_plain: MPG
    value: 17.527
    std: null
    paper_value: 17.527
    paper_std: null
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: null
    sort_value: 17.527
    sort_std: null
    is_best: false
  - model: FPGNN
    model_key: fpgnn
    model_plain: FPGNN
    value: 17.611
    std: null
    paper_value: 17.611
    paper_std: null
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: null
    sort_value: 17.611
    sort_std: null
    is_best: false
  - model: KANO
    model_key: kano
    model_plain: KANO
    value: 17.622
    std: null
    paper_value: 17.622
    paper_std: null
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: null
    sort_value: 17.622
    sort_std: null
    is_best: false
  - model: Trans-M
    model_key: trans-m
    model_plain: Trans-M
    value: 17.677
    std: null
    paper_value: 17.677
    paper_std: null
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: null
    sort_value: 17.677
    sort_std: null
    is_best: false
  - model: XGBoost
    model_key: xgboost
    model_plain: XGBoost
    value: 17.819
    std: null
    paper_value: 17.819
    paper_std: null
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: null
    sort_value: 17.819
    sort_std: null
    is_best: false
  - model: DTNN*
    model_key: dtnn*
    model_plain: DTNN*
    value: 17.89
    std: null
    paper_value: 17.89
    paper_std: null
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: null
    sort_value: 17.89
    sort_std: null
    is_best: false
  - model: rf
    model_key: rf
    model_plain: rf
    value: 18.041
    std: null
    paper_value: 18.041
    paper_std: null
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 37
    sort_value: 18.041
    sort_std: null
    is_best: false
  - model: UniMol
    model_key: unimol
    model_plain: UniMol
    value: 18.071
    std: null
    paper_value: 18.071
    paper_std: null
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: null
    sort_value: 18.071
    sort_std: null
    is_best: false
  - model: MPNN
    model_key: mpnn
    model_plain: MPNN
    value: 19.156
    std: null
    paper_value: 19.156
    paper_std: null
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 77
    sort_value: 19.156
    sort_std: null
    is_best: false
  - model: GraphFP
    model_key: graphfp
    model_plain: GraphFP
    value: 21.183
    std: null
    paper_value: 21.183
    paper_std: null
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: null
    sort_value: 21.183
    sort_std: null
    is_best: false
  - model: FraGAT
    model_key: fragat
    model_plain: FraGAT
    value: 22.503
    std: null
    paper_value: 22.503
    paper_std: null
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: null
    sort_value: 22.503
    sort_std: null
    is_best: false
  metric: Accuracy
  higher_is_better: false
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
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
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
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
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
  - model: BiScale-GTR
    model_key: biscale-gtr
    model_plain: BiScale-GTR
    value: 0.6717
    std: 0.0107
    paper_value: 0.6717
    paper_std: 0.0107
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 125
    true_value: 0.6717
    true_std: 0.0107
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 125
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6717
    sort_std: 0.0107
    is_best: false
  - model: FragFormer
    model_key: fragformer
    model_plain: FragFormer
    value: 0.6693
    std: 0.0154
    paper_value: 0.6693
    paper_std: 0.0154
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 129
    true_value: 0.6693
    true_std: 0.0154
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 129
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6693
    sort_std: 0.0154
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
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
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
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
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
  - model: SAN+RWSE
    model_key: san+rwse
    model_plain: SAN+RWSE
    value: 0.6439
    std: 0.0075
    paper_value: 0.6439
    paper_std: 0.0075
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 200
    true_value: 0.644
    true_std: 0.008
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 9.999999999998899e-05
    value_note: global 0.6440 within std
    paper_rank: 201
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.644
    sort_std: 0.008
    is_best: false
  - model: SAN+LapPE
    model_key: san+lappe
    model_plain: SAN+LapPE
    value: 0.6384
    std: 0.0121
    paper_value: 0.6384
    paper_std: 0.0121
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 212
    true_value: 0.6384000000000001
    true_std: 0.0121
    value_gap_source_arxiv: '2510.02565'
    value_gap_source_title: On The Expressive Power of GNN Derivatives
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 212
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6384000000000001
    sort_std: 0.0121
    is_best: false
  - model: Transformer+LapPE
    model_key: transformer+lappe
    model_plain: Transformer+LapPE
    value: 0.6326
    std: 0.0126
    paper_value: 0.6326
    paper_std: 0.0126
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 217
    true_value: 0.6326
    true_std: 0.0126
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: LRGB
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 217
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6326
    sort_std: 0.0126
    is_best: false
  - model: GraphFP
    model_key: graphfp
    model_plain: GraphFP
    value: 0.6267
    std: 0.0073
    paper_value: 0.6267
    paper_std: 0.0073
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 227
    true_value: 0.6267
    true_std: 0.0073
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 227
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
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
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
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
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
  - model: GINE
    model_key: gine
    model_plain: GINE
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
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 79
    true_value: 0.2473
    true_std: 0.0017
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10740000000000002
    value_note: ''
    paper_rank: 311
    rank_delta: 232
    rank_delta_abs: 232
    rank_delta_direction: worse
    sort_value: 0.2473
    sort_std: 0.0017
    is_best: false
  - model: Transformer+LapPE
    model_key: transformer+lappe
    model_plain: Transformer+LapPE
    value: 0.2529
    std: 0.0016
    paper_value: 0.2529
    paper_std: 0.0016
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 168
    true_value: 0.2529
    true_std: 0.0016
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: LRGB
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 168
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2529
    sort_std: 0.0016
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
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
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
    std: 0.0012
    paper_value: 0.2545
    paper_std: 0.0012
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
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
  - model: BiScale-GTR (Molecule)
    model_key: biscale-gtr (molecule)
    model_plain: BiScale-GTR (Molecule)
    value: 0.2621
    std: 0.0022
    paper_value: 0.2621
    paper_std: 0.0022
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 223
    true_value: 0.2621
    true_std: 0.0022
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 223
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2621
    sort_std: 0.0022
    is_best: false
  - model: Graph BPE (with validity/OOV handling)
    model_key: graph bpe (with validity/oov handling)
    model_plain: Graph BPE (with validity/OOV handling)
    value: 0.2621
    std: null
    paper_value: 0.2621
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 224
    true_value: 0.2621
    true_std: null
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 224
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2621
    sort_std: null
    is_best: false
  - model: SAN+LapPE
    model_key: san+lappe
    model_plain: SAN+LapPE
    value: 0.2683
    std: 0.0043
    paper_value: 0.2683
    paper_std: 0.0043
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 242
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
    paper_rank: 242
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.268
    sort_std: 0.004
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 279
    true_value: 0.3137
    true_std: 0.0019
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: true
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
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
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
- &id010
  dataset: SAT Solving
  rows:
  - model: UniMol
    model_key: unimol
    model_plain: UniMol
    value: 0.707
    std: null
    paper_value: 0.707
    paper_std: null
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou 2023
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: null
    sort_value: 0.707
    sort_std: null
    is_best: true
  - model: FPGNN
    model_key: fpgnn
    model_plain: FPGNN
    value: 0.747
    std: null
    paper_value: 0.747
    paper_std: null
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Cai 2022
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: null
    sort_value: 0.747
    sort_std: null
    is_best: false
  - model: MPG
    model_key: mpg
    model_plain: MPG
    value: 0.758
    std: null
    paper_value: 0.758
    paper_std: null
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Li 2020
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: null
    sort_value: 0.758
    sort_std: null
    is_best: false
  - model: KANO
    model_key: kano
    model_plain: KANO
    value: 0.772
    std: null
    paper_value: 0.772
    paper_std: null
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Li 2023
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: null
    sort_value: 0.772
    sort_std: null
    is_best: false
  - model: DTNN*
    model_key: dtnn*
    model_plain: DTNN*
    value: 0.828
    std: null
    paper_value: 0.828
    paper_std: null
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Song 2023
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: null
    sort_value: 0.828
    sort_std: null
    is_best: false
  - model: XGBoost
    model_key: xgboost
    model_plain: XGBoost
    value: 0.832
    std: null
    paper_value: 0.832
    paper_std: null
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Chen 2016
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: null
    sort_value: 0.832
    sort_std: null
    is_best: false
  - model: Trans-M
    model_key: trans-m
    model_plain: Trans-M
    value: 0.834
    std: null
    paper_value: 0.834
    paper_std: null
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Luo 2022
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: null
    sort_value: 0.834
    sort_std: null
    is_best: false
  - model: MPNN
    model_key: mpnn
    model_plain: MPNN
    value: 0.858
    std: null
    paper_value: 0.858
    paper_std: null
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Swanson 2019
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: null
    sort_value: 0.858
    sort_std: null
    is_best: false
  - model: FragFormer
    model_key: fragformer
    model_plain: FragFormer
    value: 0.895
    std: null
    paper_value: 0.895
    paper_std: null
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Wang 2025
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: null
    sort_value: 0.895
    sort_std: null
    is_best: false
  - model: rf
    model_key: rf
    model_plain: rf
    value: 0.918
    std: null
    paper_value: 0.918
    paper_std: null
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Rigatti 2017
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: null
    sort_value: 0.918
    sort_std: null
    is_best: false
  - model: PharmHGT
    model_key: pharmhgt
    model_plain: PharmHGT
    value: 0.954
    std: null
    paper_value: 0.954
    paper_std: null
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Jiang 2023
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: null
    sort_value: 0.954
    sort_std: null
    is_best: false
  - model: BiScale-GTR (Molecule)
    model_key: biscale-gtr (molecule)
    model_plain: BiScale-GTR (Molecule)
    value: 0.977
    std: null
    paper_value: 0.977
    paper_std: null
    metric: RMSE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: null
    sort_value: 0.977
    sort_std: null
    is_best: false
  - model: KP-GPT
    model_key: kp-gpt
    model_plain: KP-GPT
    value: 1.221
    std: null
    paper_value: 1.221
    paper_std: null
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Wu 2018
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: null
    sort_value: 1.221
    sort_std: null
    is_best: false
  - model: FraGAT
    model_key: fragat
    model_plain: FraGAT
    value: 1.352
    std: null
    paper_value: 1.352
    paper_std: null
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhang 2021
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: null
    sort_value: 1.352
    sort_std: null
    is_best: false
  - model: GraphFP
    model_key: graphfp
    model_plain: GraphFP
    value: 1.935
    std: null
    paper_value: 1.935
    paper_std: null
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Luong 2023
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: null
    sort_value: 1.935
    sort_std: null
    is_best: false
  metric: Accuracy
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
  - model: BiScale-GTR (Molecule)
    model_key: biscale-gtr (molecule)
    model_plain: BiScale-GTR (Molecule)
    value: 0.642
    std: 0.009
    paper_value: 0.642
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
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 6
    true_value: 0.642
    true_std: 0.009
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.642
    sort_std: 0.009
    is_best: false
  - model: GraphFP
    model_key: graphfp
    model_plain: GraphFP
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
    table_ref: Table 1
    source_ref: Luong et al. 2023
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 7
    true_value: 0.636
    true_std: 0.012
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.636
    sort_std: 0.012
    is_best: false
  - model: Mole-BERT
    model_key: mole-bert
    model_plain: Mole-BERT
    value: 0.628
    std: 0.011
    paper_value: 0.628
    paper_std: 0.011
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xia et al. 2023
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 11
    true_value: 0.628
    true_std: 0.011
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.628
    sort_std: 0.011
    is_best: false
  - model: GraphMVP
    model_key: graphmvp
    model_plain: GraphMVP
    value: 0.602
    std: 0.011
    paper_value: 0.602
    paper_std: 0.011
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Liu et al. 2021
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 15
    true_value: 0.623
    true_std: 0.016
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.02100000000000002
    value_note: ''
    paper_rank: 34
    rank_delta: 19
    rank_delta_abs: 19
    rank_delta_direction: worse
    sort_value: 0.623
    sort_std: 0.016
    is_best: false
  - model: SimSGT
    model_key: simsgt
    model_plain: SimSGT
    value: 0.617
    std: 0.008
    paper_value: 0.617
    paper_std: 0.008
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Liu et al. 2023
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 16
    true_value: 0.617
    true_std: 0.008
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.617
    sort_std: 0.008
    is_best: false
  - model: MORE
    model_key: more
    model_plain: MORE
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
    source_ref: Son et al. 2025
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 25
    true_value: 0.609
    true_std: 0.006
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.609
    sort_std: 0.006
    is_best: false
  - model: GraphMAE
    model_key: graphmae
    model_plain: GraphMAE
    value: 0.605
    std: 0.012
    paper_value: 0.605
    paper_std: 0.012
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hou et al. 2022
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 31
    true_value: 0.605
    true_std: 0.012
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.605
    sort_std: 0.012
    is_best: false
  - model: GraphGPS+LAC
    model_key: graphgps+lac
    model_plain: GraphGPS+LAC
    value: 0.604
    std: null
    paper_value: 0.604
    paper_std: null
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Yang et al. 2025
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 34
    true_value: 0.604
    true_std: null
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 34
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.604
    sort_std: null
    is_best: false
  - model: BiScale-GTR (Fragment)
    model_key: biscale-gtr (fragment)
    model_plain: BiScale-GTR (Fragment)
    value: 0.601
    std: 0.011
    paper_value: 0.601
    paper_std: 0.011
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 35
    true_value: 0.601
    true_std: 0.011
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.601
    sort_std: 0.011
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id006
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
  - model: Mole-BERT
    model_key: mole-bert
    model_plain: Mole-BERT
    value: 0.768
    std: 0.005
    paper_value: 0.768
    paper_std: 0.005
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xia et al. 2023
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 28
    true_value: 0.768
    true_std: 0.005
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 28
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.768
    sort_std: 0.005
    is_best: false
  - model: SimSGT
    model_key: simsgt
    model_plain: SimSGT
    value: 0.768
    std: 0.009
    paper_value: 0.768
    paper_std: 0.009
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Liu et al. 2023
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 29
    true_value: 0.768
    true_std: 0.009
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.768
    sort_std: 0.009
    is_best: false
  - model: BiScale-GTR (Molecule)
    model_key: biscale-gtr (molecule)
    model_plain: BiScale-GTR (Molecule)
    value: 0.761
    std: 0.004
    paper_value: 0.761
    paper_std: 0.004
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 41
    true_value: 0.761
    true_std: 0.004
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 41
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.761
    sort_std: 0.004
    is_best: false
  - model: GraphFP
    model_key: graphfp
    model_plain: GraphFP
    value: 0.74
    std: 0.007
    paper_value: 0.74
    paper_std: 0.007
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Luong et al. 2023
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 43
    true_value: 0.76
    true_std: 0.005
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.020000000000000018
    value_note: ''
    paper_rank: 64
    rank_delta: 21
    rank_delta_abs: 21
    rank_delta_direction: worse
    sort_value: 0.76
    sort_std: 0.005
    is_best: false
  - model: MORE
    model_key: more
    model_plain: MORE
    value: 0.756
    std: 0.005
    paper_value: 0.756
    paper_std: 0.005
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Son et al. 2025
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 50
    true_value: 0.756
    true_std: 0.005
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 50
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.756
    sort_std: 0.005
    is_best: false
  - model: GraphMAE
    model_key: graphmae
    model_plain: GraphMAE
    value: 0.752
    std: 0.009
    paper_value: 0.752
    paper_std: 0.009
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hou et al. 2022
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 51
    true_value: 0.755
    true_std: 0.006
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0030000000000000027
    value_note: global 0.7550 within std
    paper_rank: 52
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.755
    sort_std: 0.006
    is_best: false
  - model: GraphMVP
    model_key: graphmvp
    model_plain: GraphMVP
    value: 0.749
    std: 0.008
    paper_value: 0.749
    paper_std: 0.008
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Liu et al. 2021
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 56
    true_value: 0.749
    true_std: 0.008
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 56
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.749
    sort_std: 0.008
    is_best: false
  - model: GraphGPS+LAC
    model_key: graphgps+lac
    model_plain: GraphGPS+LAC
    value: 0.74
    std: null
    paper_value: 0.74
    paper_std: null
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Yang et al. 2025
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 65
    true_value: 0.74
    true_std: null
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 65
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.74
    sort_std: null
    is_best: false
  - model: BiScale-GTR (Fragment)
    model_key: biscale-gtr (fragment)
    model_plain: BiScale-GTR (Fragment)
    value: 0.731
    std: 0.009
    paper_value: 0.731
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
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 74
    true_value: 0.731
    true_std: 0.009
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 74
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.731
    sort_std: 0.009
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id008
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
  - model: GraphGPS+LAC
    model_key: graphgps+lac
    model_plain: GraphGPS+LAC
    value: 0.737
    std: null
    paper_value: 0.737
    paper_std: null
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Yang et al. 2025
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 6
    true_value: 0.737
    true_std: null
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.737
    sort_std: null
    is_best: false
  - model: SimSGT
    model_key: simsgt
    model_plain: SimSGT
    value: 0.659
    std: 0.008
    paper_value: 0.659
    paper_std: 0.008
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Liu et al. 2023
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 16
    true_value: 0.659
    true_std: 0.008
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.659
    sort_std: 0.008
    is_best: false
  - model: MORE
    model_key: more
    model_plain: MORE
    value: 0.646
    std: 0.006
    paper_value: 0.646
    paper_std: 0.006
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Son et al. 2025
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 24
    true_value: 0.646
    true_std: 0.006
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.646
    sort_std: 0.006
    is_best: false
  - model: Mole-BERT
    model_key: mole-bert
    model_plain: Mole-BERT
    value: 0.643
    std: 0.002
    paper_value: 0.643
    paper_std: 0.002
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xia et al. 2023
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 25
    true_value: 0.643
    true_std: 0.002
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.643
    sort_std: 0.002
    is_best: false
  - model: GraphMAE
    model_key: graphmae
    model_plain: GraphMAE
    value: 0.636
    std: 0.003
    paper_value: 0.636
    paper_std: 0.003
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hou et al. 2022
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 28
    true_value: 0.641
    true_std: 0.003
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0050000000000000044
    value_note: ''
    paper_rank: 36
    rank_delta: 8
    rank_delta_abs: 8
    rank_delta_direction: worse
    sort_value: 0.641
    sort_std: 0.003
    is_best: false
  - model: GraphFP
    model_key: graphfp
    model_plain: GraphFP
    value: 0.639
    std: 0.009
    paper_value: 0.639
    paper_std: 0.009
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Luong et al. 2023
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 30
    true_value: 0.639
    true_std: 0.009
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 30
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.639
    sort_std: 0.009
    is_best: false
  - model: BiScale-GTR (Fragment)
    model_key: biscale-gtr (fragment)
    model_plain: BiScale-GTR (Fragment)
    value: 0.639
    std: 0.002
    paper_value: 0.639
    paper_std: 0.002
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 31
    true_value: 0.639
    true_std: 0.002
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.639
    sort_std: 0.002
    is_best: false
  - model: GraphMVP
    model_key: graphmvp
    model_plain: GraphMVP
    value: 0.631
    std: 0.002
    paper_value: 0.631
    paper_std: 0.002
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Liu et al. 2021
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 42
    true_value: 0.631
    true_std: 0.002
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 42
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.631
    sort_std: 0.002
    is_best: false
  - model: BiScale-GTR (Molecule)
    model_key: biscale-gtr (molecule)
    model_plain: BiScale-GTR (Molecule)
    value: 0.622
    std: 0.002
    paper_value: 0.622
    paper_std: 0.002
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 51
    true_value: 0.622
    true_std: 0.002
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 51
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.622
    sort_std: 0.002
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id004
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
    value: 0.9681
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
    global_rank: 3
    sort_value: 0.9681
    sort_std: 0.0003
    is_best: false
  - model: BiScale-GTR (Molecule)
    model_key: biscale-gtr (molecule)
    model_plain: BiScale-GTR (Molecule)
    value: 0.792
    std: 0.006
    paper_value: 0.792
    paper_std: 0.006
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 57
    true_value: 0.792
    true_std: 0.006
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 57
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.792
    sort_std: 0.006
    is_best: false
  - model: Mole-BERT
    model_key: mole-bert
    model_plain: Mole-BERT
    value: 0.782
    std: 0.008
    paper_value: 0.782
    paper_std: 0.008
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xia 2023
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 101
    true_value: 0.782
    true_std: 0.008
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 101
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.782
    sort_std: 0.008
    is_best: false
  - model: SimSGT
    model_key: simsgt
    model_plain: SimSGT
    value: 0.78
    std: 0.019
    paper_value: 0.78
    paper_std: 0.019
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Liu 2023
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 106
    true_value: 0.78
    true_std: 0.019
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 106
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.78
    sort_std: 0.019
    is_best: false
  - model: GraphFP
    model_key: graphfp
    model_plain: GraphFP
    value: 0.78
    std: 0.015
    paper_value: 0.78
    paper_std: 0.015
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Luong 2023
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 107
    true_value: 0.78
    true_std: 0.015
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 107
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.78
    sort_std: 0.015
    is_best: false
  - model: BiScale-GTR (Fragment)
    model_key: biscale-gtr (fragment)
    model_plain: BiScale-GTR (Fragment)
    value: 0.779
    std: 0.011
    paper_value: 0.779
    paper_std: 0.011
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 121
    true_value: 0.779
    true_std: 0.011
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 121
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.779
    sort_std: 0.011
    is_best: false
  - model: GraphGPS+LAC
    model_key: graphgps+lac
    model_plain: GraphGPS+LAC
    value: 0.776
    std: null
    paper_value: 0.776
    paper_std: null
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Yang 2025
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 123
    true_value: 0.776
    true_std: null
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 123
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.776
    sort_std: null
    is_best: false
  - model: MORE
    model_key: more
    model_plain: MORE
    value: 0.77
    std: 0.007
    paper_value: 0.77
    paper_std: 0.007
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Son 2025
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 142
    true_value: 0.77
    true_std: 0.007
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 142
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.77
    sort_std: 0.007
    is_best: false
  - model: GraphMAE
    model_key: graphmae
    model_plain: GraphMAE
    value: 0.768
    std: 0.006
    paper_value: 0.768
    paper_std: 0.006
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hou 2022
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 144
    true_value: 0.768
    true_std: 0.006
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 144
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.768
    sort_std: 0.006
    is_best: false
  - model: GraphMVP
    model_key: graphmvp
    model_plain: GraphMVP
    value: 0.76
    std: 0.001
    paper_value: 0.76
    paper_std: 0.001
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Liu 2021
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 164
    true_value: 0.76
    true_std: 0.001
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 164
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.76
    sort_std: 0.001
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
results_grouped:
- benchmark: LRGB
  datasets:
  - *id001
  - *id002
- benchmark: TU Dortmund
  datasets:
  - *id003
- benchmark: OGB
  datasets:
  - *id004
- benchmark: MoleculeNet
  datasets:
  - *id005
  - *id006
  - *id007
  - *id008
  - *id009
- benchmark: GraphBench
  datasets:
  - *id010
main_figure: /figures/2604.06336/main_figure.png
---

