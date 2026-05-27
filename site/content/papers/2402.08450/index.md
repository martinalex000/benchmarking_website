---
title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via Graph Products'
arxiv_id: '2402.08450'
source_url: ''
authors: []
published_date: Feb 2024
published_date_iso: 2024-02
abstract: 'In the realm of Graph Neural Networks (GNNs), two exciting research directions
  have recently emerged: Subgraph GNNs and Graph Transformers. In this paper, we propose
  an architecture that integrates both approaches, dubbed Subgraphormer, which combines
  the enhanced expressive power, message-passing mechanisms, and aggregation schemes
  from Subgraph GNNs with attention and positional encodings, arguably the most important
  components in Graph Transformers. Our method is based on an intriguing new connection
  we reveal between Subgraph GNNs and product graphs, suggesting that Subgraph GNNs
  can be formulated as Message Passing Neural Networks (MPNNs) operating on a product
  of the graph with itself. We use this formulation to design our architecture: first,
  we devise an attention mechanism based on the connectivity of the product graph.
  Following this, we propose a novel and efficient positional encoding scheme for
  Subgraph GNNs, which we derive as a positional encoding for the product graph. Our
  experimental results demonstrate significant performance improvements over both
  Subgraph GNNs and Graph Transformers on a wide range of datasets.'
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- Subgraphormer
- Subgraphormer + product graph PE
- Subgraphormer + concatenation PE
mrr: 0.0477
adjusted_mrr: 0.0477
mrr_dataset_count: 3
benchmark_categories:
- Classic
- LRGB
- OGB
- MoleculeNet
task_categories:
- graph_classification
- graph_regression
experiment_scopes:
- graph-level
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
    paper_value: 0.8435
    paper_std: 0.0065
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.293
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to bace (score=90)'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 3
    true_value: 0.8435
    true_std: 0.0065
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
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
  - model: GNN-SSWL+
    model_key: gnn-sswl+
    model_plain: GNN-SSWL+
    value: 0.827
    std: 0.018
    paper_value: 0.827
    paper_std: 0.018
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.387
    table_ref: Table 1
    source_ref: Zhang 2023
    variant_inference_reason: 'dataset: fuzzy match to bace (score=90)'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 9
    true_value: 0.827
    true_std: 0.018
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.827
    sort_std: 0.018
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.7297
    std: 0.04
    paper_value: 0.7297
    paper_std: 0.04
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    table_ref: Table 1
    source_ref: Xu 2018
    variant_inference_reason: 'dataset: fuzzy match to bace (score=90)'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 11
    true_value: 0.825
    true_std: 0.019
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09529999999999994
    value_note: ''
    paper_rank: 58
    rank_delta: 47
    rank_delta_abs: 47
    rank_delta_direction: worse
    sort_value: 0.825
    sort_std: 0.019
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7915
    std: 0.0144
    paper_value: 0.7915
    paper_std: 0.0144
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kipf 2016
    variant_inference_reason: 'dataset: fuzzy match to bace (score=90)'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 34
    true_value: 0.7915
    true_std: 0.0144
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 34
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7915
    sort_std: 0.0144
    is_best: false
  - model: DSS-GNN
    model_key: dss-gnn
    model_plain: DSS-GNN
    value: 0.7841
    std: 0.0194
    paper_value: 0.7841
    paper_std: 0.0194
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.1
    table_ref: Table 1
    source_ref: Bevilacqua 2023
    variant_inference_reason: 'dataset: fuzzy match to bace (score=90)'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 40
    true_value: 0.7841
    true_std: 0.0194
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 40
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7841
    sort_std: 0.0194
    is_best: false
  - model: Recon. GNN
    model_key: recon. gnn
    model_plain: Recon. GNN
    value: 0.7632
    std: 0.014
    paper_value: 0.7632
    paper_std: 0.014
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Cotta 2021
    variant_inference_reason: ''
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 50
    true_value: 0.7632
    true_std: 0.014
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 50
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7632
    sort_std: 0.014
    is_best: false
  - model: OSAN
    model_key: osan
    model_plain: OSAN
    value: 0.723
    std: 0.066
    paper_value: 0.723
    paper_std: 0.066
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    table_ref: Table 1
    source_ref: Qian 2022
    variant_inference_reason: 'dataset: fuzzy match to bace (score=90)'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 59
    true_value: 0.723
    true_std: 0.066
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 59
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.723
    sort_std: 0.066
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id006
  dataset: ESOL
  rows:
  - model: Subgraphormer
    model_key: subgraphormer
    model_plain: Subgraphormer
    value: 0.826
    std: 0.01
    paper_value: 0.826
    paper_std: 0.01
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.293
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to esol (score=90)'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 1
    true_value: 0.826
    true_std: 0.01
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.826
    sort_std: 0.01
    is_best: true
  - model: GNN-SSWL+
    model_key: gnn-sswl+
    model_plain: GNN-SSWL+
    value: 0.837
    std: 0.019
    paper_value: 0.837
    paper_std: 0.019
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.387
    table_ref: Table 1
    source_ref: Zhang 2023
    variant_inference_reason: 'dataset: fuzzy match to esol (score=90)'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 2
    true_value: 0.837
    true_std: 0.019
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.837
    sort_std: 0.019
    is_best: true
  - model: DSS-GNN
    model_key: dss-gnn
    model_plain: DSS-GNN
    value: 0.847
    std: 0.015
    paper_value: 0.847
    paper_std: 0.015
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.1
    table_ref: Table 1
    source_ref: Bevilacqua 2023
    variant_inference_reason: 'dataset: fuzzy match to esol (score=90)'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 3
    true_value: 0.847
    true_std: 0.015
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.847
    sort_std: 0.015
    is_best: true
  - model: OSAN
    model_key: osan
    model_plain: OSAN
    value: 0.98
    std: 0.086
    paper_value: 0.98
    paper_std: 0.086
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    table_ref: Table 1
    source_ref: Qian 2022
    variant_inference_reason: 'dataset: fuzzy match to esol (score=90)'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 4
    true_value: 0.98
    true_std: 0.086
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.98
    sort_std: 0.086
    is_best: false
  - model: Recon. GNN
    model_key: recon. gnn
    model_plain: Recon. GNN
    value: 1.026
    std: 0.033
    paper_value: 1.026
    paper_std: 0.033
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Cotta 2021
    variant_inference_reason: 'dataset: fuzzy match to esol (score=90)'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 5
    true_value: 1.026
    true_std: 0.033
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.026
    sort_std: 0.033
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 1.114
    std: 0.036
    paper_value: 1.114
    paper_std: 0.036
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kipf 2016
    variant_inference_reason: 'dataset: fuzzy match to esol (score=90)'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 6
    true_value: 1.114
    true_std: 0.036
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.114
    sort_std: 0.036
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 1.173
    std: 0.057
    paper_value: 1.173
    paper_std: 0.057
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    table_ref: Table 1
    source_ref: Xu 2018
    variant_inference_reason: 'dataset: fuzzy match to esol (score=90)'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 7
    true_value: 1.173
    true_std: 0.057
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.173
    sort_std: 0.057
    is_best: false
  - model: GraphMAE
    model_key: graphmae
    model_plain: GraphMAE
    value: 2.058
    std: 0.188
    metric: RMSE
    higher_is_better: false
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
    uses_external_data: null
    is_global_top: true
    global_rank: 8
    sort_value: 2.058
    sort_std: 0.188
    is_best: false
  - model: AUG-MAE
    model_key: aug-mae
    model_plain: AUG-MAE
    value: 2.395
    std: 0.158
    metric: RMSE
    higher_is_better: false
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
    uses_external_data: null
    is_global_top: true
    global_rank: 9
    sort_value: 2.395
    sort_std: 0.158
    is_best: false
  - model: StructMAE
    model_key: structmae
    model_plain: StructMAE
    value: 2.568
    std: 0.262
    metric: RMSE
    higher_is_better: false
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
    uses_external_data: null
    is_global_top: true
    global_rank: 10
    sort_value: 2.568
    sort_std: 0.262
    is_best: false
  metric: RMSE
  higher_is_better: false
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
    date: '2025-01-29'
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
    date: '2025-01-29'
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
    date: '2025-01-29'
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
    source_ref: Kipf 2016
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
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
    paper_rank: 259
    rank_delta: 250
    rank_delta_abs: 250
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
    params_millions: 0.5
    table_ref: Table 1
    source_ref: Xu 2018
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 40
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
    paper_rank: 286
    rank_delta: 246
    rank_delta_abs: 246
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
    source_ref: Bresson 2017
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 48
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
    paper_rank: 271
    rank_delta: 223
    rank_delta_abs: 223
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
    source_ref: Dwivedi 2022
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 132
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
    paper_rank: 237
    rank_delta: 105
    rank_delta_abs: 105
    rank_delta_direction: worse
    sort_value: 0.6685
    sort_std: 0.0062
    is_best: false
  - model: Subgraphormer
    model_key: subgraphormer
    model_plain: Subgraphormer
    value: 0.6373
    std: 0.011
    paper_value: 0.6373
    paper_std: 0.011
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.293
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 148
    true_value: 0.661
    true_std: 0.005
    value_gap_source_arxiv: '2604.24293'
    value_gap_source_title: 'Latent-Hysteresis Graph ODEs: Modeling Coupled Topology-Feature
      Evolution via Continuous Phase Transitions'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.023700000000000054
    value_note: ''
    paper_rank: 211
    rank_delta: 63
    rank_delta_abs: 63
    rank_delta_direction: worse
    sort_value: 0.661
    sort_std: 0.005
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.6535
    std: 0.0041
    paper_value: 0.6535
    paper_std: 0.0041
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.424
    table_ref: Table 1
    source_ref: Rampásek 2022
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 152
    true_value: 0.6601
    true_std: 0.0061
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.00660000000000005
    value_note: ''
    paper_rank: 166
    rank_delta: 14
    rank_delta_abs: 14
    rank_delta_direction: worse
    sort_value: 0.6601
    sort_std: 0.0061
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
    source_ref: Kreuzer 2021
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 198
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
    paper_rank: 199
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
    source_ref: Kreuzer 2021
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 210
    true_value: 0.6384000000000001
    true_std: 0.0121
    value_gap_source_arxiv: '2510.02565'
    value_gap_source_title: On The Expressive Power of GNN Derivatives
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 210
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6384000000000001
    sort_std: 0.0121
    is_best: false
  - model: Transf.+LapPE
    model_key: transf.+lappe
    model_plain: Transf.+LapPE
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
    source_ref: Dwivedi 2022
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 218
    true_value: 0.6326
    true_std: 0.0126
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 218
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6326
    sort_std: 0.0126
    is_best: false
  - model: GNN-SSWL+
    model_key: gnn-sswl+
    model_plain: GNN-SSWL+
    value: 0.5847
    std: 0.005
    paper_value: 0.5847
    paper_std: 0.005
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.387
    table_ref: Table 1
    source_ref: Zhang 2023
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 273
    true_value: 0.5847
    true_std: 0.005
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 273
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5847
    sort_std: 0.005
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
    table_ref: Table 1
    source_ref: Kipf 2016
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
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
    paper_rank: 299
    rank_delta: 296
    rank_delta_abs: 296
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
    params_millions: 0.5
    table_ref: Table 1
    source_ref: Xu 2018
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
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
    paper_rank: 306
    rank_delta: 297
    rank_delta_abs: 297
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
    source_ref: Bresson 2017
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
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
    paper_rank: 292
    rank_delta: 280
    rank_delta_abs: 280
    rank_delta_direction: worse
    sort_value: 0.2431
    sort_std: 0.002
    is_best: false
  - model: Subgraphormer
    model_key: subgraphormer
    model_plain: Subgraphormer
    value: 0.2475
    std: 0.0007
    paper_value: 0.2475
    paper_std: 0.0007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.293
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 85
    true_value: 0.2475
    true_std: 0.0007
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 85
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2475
    sort_std: 0.0007
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.25
    std: 0.0005
    paper_value: 0.25
    paper_std: 0.0005
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.424
    table_ref: Table 1
    source_ref: Rampavsek 2022
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 132
    true_value: 0.25
    true_std: 0.0005
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 132
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.25
    sort_std: 0.0005
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
    source_ref: Dwivedi 2022
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 164
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
    paper_rank: 284
    rank_delta: 120
    rank_delta_abs: 120
    rank_delta_direction: worse
    sort_value: 0.2529
    sort_std: 0.0009
    is_best: false
  - model: Transf.+LapPE
    model_key: transf.+lappe
    model_plain: Transf.+LapPE
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
    source_ref: Dwivedi 2022
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 169
    true_value: 0.2529
    true_std: 0.0016
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 169
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
    source_ref: Kreuzer 2021
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 184
    true_value: 0.2545
    true_std: 0.0012
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: LRGB
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 184
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2545
    sort_std: 0.0012
    is_best: false
  - model: GNN-SSWL+
    model_key: gnn-sswl+
    model_plain: GNN-SSWL+
    value: 0.257
    std: 0.0006
    paper_value: 0.257
    paper_std: 0.0006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.387
    table_ref: Table 1
    source_ref: Zhang 2023
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 201
    true_value: 0.257
    true_std: 0.0006
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 201
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.257
    sort_std: 0.0006
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
    source_ref: Kreuzer 2021
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 237
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
    paper_rank: 237
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.268
    sort_std: 0.004
    is_best: false
  metric: MAE
  higher_is_better: false
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
    date: '2024-05-05'
    date_display: May 2024
    date_iso: '2024-05-05'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.018
    sort_std: 0.001
    is_best: false
  - model: PPGN++(6)
    model_key: ppgn++(6)
    model_plain: PPGN++(6)
    value: 0.071
    std: 0.001
    paper_value: 0.071
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    table_ref: Table 1
    source_ref: Puny et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 4
    true_value: 0.02
    true_std: 0.001
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05099999999999999
    value_note: ''
    paper_rank: 107
    rank_delta: 103
    rank_delta_abs: 103
    rank_delta_direction: worse
    sort_value: 0.02
    sort_std: 0.001
    is_best: false
  - model: PPGN++(6)
    model_key: ppgn++(6)
    model_plain: PPGN++(6)
    value: 0.02
    std: 0.001
    paper_value: 0.02
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    table_ref: Table 1
    source_ref: Puny 2023
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 4
    true_value: 0.02
    true_std: 0.001
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.02
    sort_std: 0.001
    is_best: false
  - model: GNN-SSWL+
    model_key: gnn-sswl+
    model_plain: GNN-SSWL+
    value: 0.07
    std: 0.005
    paper_value: 0.07
    paper_std: 0.005
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.387
    table_ref: Table 1
    source_ref: Zhang et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 8
    true_value: 0.022
    true_std: 0.001
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04800000000000001
    value_note: ''
    paper_rank: 104
    rank_delta: 96
    rank_delta_abs: 96
    rank_delta_direction: worse
    sort_value: 0.022
    sort_std: 0.001
    is_best: false
  - model: GNN-SSWL+
    model_key: gnn-sswl+
    model_plain: GNN-SSWL+
    value: 0.022
    std: 0.001
    paper_value: 0.022
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.387
    table_ref: Table 1
    source_ref: Zhang 2023
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 8
    true_value: 0.022
    true_std: 0.001
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.022
    sort_std: 0.001
    is_best: false
  - model: Subgraphormer
    model_key: subgraphormer
    model_plain: Subgraphormer
    value: 0.063
    std: 0.001
    paper_value: 0.063
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.293
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 11
    true_value: 0.023
    true_std: 0.001
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04
    value_note: ''
    paper_rank: 64
    rank_delta: 53
    rank_delta_abs: 53
    rank_delta_direction: worse
    sort_value: 0.023
    sort_std: 0.001
    is_best: false
  - model: Subgraphormer
    model_key: subgraphormer
    model_plain: Subgraphormer
    value: 0.023
    std: 0.001
    paper_value: 0.023
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.293
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 11
    true_value: 0.023
    true_std: 0.001
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.023
    sort_std: 0.001
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.07
    std: 0.004
    paper_value: 0.07
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.424
    table_ref: Table 1
    source_ref: Rampásek et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 13
    true_value: 0.023842
    true_std: 0.0069779309254248125
    value_gap_source_arxiv: '2402.10793'
    value_gap_source_title: An end-to-end attention-based approach for learning on
      graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.046158000000000005
    value_note: ''
    paper_rank: 104
    rank_delta: 91
    rank_delta_abs: 91
    rank_delta_direction: worse
    sort_value: 0.023842
    sort_std: 0.0069779309254248125
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.07
    std: 0.004
    paper_value: 0.07
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.424
    table_ref: Table 1
    source_ref: Rampásek 2022
    variant_inference_reason: ''
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 13
    true_value: 0.023842
    true_std: 0.0069779309254248125
    value_gap_source_arxiv: '2402.10793'
    value_gap_source_title: An end-to-end attention-based approach for learning on
      graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.046158000000000005
    value_note: ''
    paper_rank: 104
    rank_delta: 91
    rank_delta_abs: 91
    rank_delta_direction: worse
    sort_value: 0.023842
    sort_std: 0.0069779309254248125
    is_best: false
  - model: SUN
    model_key: sun
    model_plain: SUN
    value: 0.083
    std: 0.003
    paper_value: 0.083
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.526
    table_ref: Table 1
    source_ref: Frasca et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 14
    true_value: 0.024
    true_std: 0.003
    value_gap_source_arxiv: '2405.02795'
    value_gap_source_title: Graph as Point Set
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.059000000000000004
    value_note: ''
    paper_rank: 142
    rank_delta: 128
    rank_delta_abs: 128
    rank_delta_direction: worse
    sort_value: 0.024
    sort_std: 0.003
    is_best: false
  - model: SUN
    model_key: sun
    model_plain: SUN
    value: 0.024
    std: 0.003
    paper_value: 0.024
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.526
    table_ref: Table 1
    source_ref: Frasca 2022
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 14
    true_value: 0.024
    true_std: 0.003
    value_gap_source_arxiv: '2405.02795'
    value_gap_source_title: Graph as Point Set
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.024
    sort_std: 0.003
    is_best: false
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.122
    std: 0.006
    paper_value: 0.122
    paper_std: 0.006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.489
    table_ref: Table 1
    source_ref: Ying et al. 2021
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 18
    true_value: 0.025
    true_std: 0.004
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.097
    value_note: ''
    paper_rank: 198
    rank_delta: 180
    rank_delta_abs: 180
    rank_delta_direction: worse
    sort_value: 0.025
    sort_std: 0.004
    is_best: false
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.052
    std: 0.005
    paper_value: 0.052
    paper_std: 0.005
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.489
    table_ref: Table 1
    source_ref: Ying 2021
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 18
    true_value: 0.025
    true_std: 0.004
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.026999999999999996
    value_note: ''
    paper_rank: 42
    rank_delta: 24
    rank_delta_abs: 24
    rank_delta_direction: worse
    sort_value: 0.025
    sort_std: 0.004
    is_best: false
  - model: Graphormer-GD
    model_key: graphormer-gd
    model_plain: Graphormer-GD
    value: 0.081
    std: 0.009
    paper_value: 0.081
    paper_std: 0.009
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.503
    table_ref: Table 1
    source_ref: Zhang et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 19
    true_value: 0.025
    true_std: 0.004
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 0.056
    value_note: ''
    paper_rank: 142
    rank_delta: 123
    rank_delta_abs: 123
    rank_delta_direction: worse
    sort_value: 0.025
    sort_std: 0.004
    is_best: false
  - model: Graphormer-GD
    model_key: graphormer-gd
    model_plain: Graphormer-GD
    value: 0.025
    std: 0.004
    paper_value: 0.025
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.503
    table_ref: Table 1
    source_ref: Zhang 2023
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 19
    true_value: 0.025
    true_std: 0.004
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.025
    sort_std: 0.004
    is_best: false
  - model: URPE
    model_key: urpe
    model_plain: URPE
    value: 0.086
    std: 0.007
    paper_value: 0.086
    paper_std: 0.007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.492
    table_ref: Table 1
    source_ref: Luo et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 26
    true_value: 0.028
    true_std: 0.002
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 0.057999999999999996
    value_note: ''
    paper_rank: 155
    rank_delta: 129
    rank_delta_abs: 129
    rank_delta_direction: worse
    sort_value: 0.028
    sort_std: 0.002
    is_best: false
  - model: URPE
    model_key: urpe
    model_plain: URPE
    value: 0.028
    std: 0.002
    paper_value: 0.028
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.492
    table_ref: Table 1
    source_ref: Luo 2022
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 26
    true_value: 0.028
    true_std: 0.002
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.028
    sort_std: 0.002
    is_best: false
  - model: DSS-GNN
    model_key: dss-gnn
    model_plain: DSS-GNN
    value: 0.102
    std: 0.003
    paper_value: 0.102
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.1
    table_ref: Table 1
    source_ref: Bevilacqua et al. 2021
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 29
    true_value: 0.029
    true_std: 0.003
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 0.073
    value_note: ''
    paper_rank: 176
    rank_delta: 147
    rank_delta_abs: 147
    rank_delta_direction: worse
    sort_value: 0.029
    sort_std: 0.003
    is_best: false
  - model: DSS-GNN
    model_key: dss-gnn
    model_plain: DSS-GNN
    value: 0.029
    std: 0.003
    paper_value: 0.029
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.1
    table_ref: Table 1
    source_ref: Bevilacqua 2021
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 29
    true_value: 0.029
    true_std: 0.003
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.029
    sort_std: 0.003
    is_best: false
  - model: NGNN
    model_key: ngnn
    model_plain: NGNN
    value: 0.111
    std: 0.003
    paper_value: 0.111
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    table_ref: Table 1
    source_ref: Zhang et al. 2021
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 28
    true_value: 0.029
    true_std: 0.001
    value_gap_source_arxiv: '2405.02795'
    value_gap_source_title: Graph as Point Set
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.082
    value_note: ''
    paper_rank: 186
    rank_delta: 158
    rank_delta_abs: 158
    rank_delta_direction: worse
    sort_value: 0.029
    sort_std: 0.001
    is_best: false
  - model: NGNN
    model_key: ngnn
    model_plain: NGNN
    value: 0.029
    std: 0.001
    paper_value: 0.029
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    table_ref: Table 1
    source_ref: Zhang 2021
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 28
    true_value: 0.029
    true_std: 0.001
    value_gap_source_arxiv: '2405.02795'
    value_gap_source_title: Graph as Point Set
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 28
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.029
    sort_std: 0.001
    is_best: false
  - model: GNN (a)
    model_key: gnn (a)
    model_plain: GNN (a)
    value: 0.091
    std: 0.002
    paper_value: 0.091
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhao et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 33
    true_value: 0.034
    true_std: 0.007
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.056999999999999995
    value_note: ''
    paper_rank: 168
    rank_delta: 135
    rank_delta_abs: 135
    rank_delta_direction: worse
    sort_value: 0.034
    sort_std: 0.007
    is_best: false
  - model: GNN (a)
    model_key: gnn (a)
    model_plain: GNN (a)
    value: 0.105
    std: 0.01
    paper_value: 0.105
    paper_std: 0.01
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhao 2022
    variant_inference_reason: ''
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 33
    true_value: 0.034
    true_std: 0.007
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.071
    value_note: ''
    paper_rank: 180
    rank_delta: 147
    rank_delta_abs: 147
    rank_delta_direction: worse
    sort_value: 0.034
    sort_std: 0.007
    is_best: false
  - model: CIN (small)
    model_key: cin (small)
    model_plain: CIN (small)
    value: 0.094
    std: 0.004
    paper_value: 0.094
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.1
    table_ref: Table 1
    source_ref: Bodnar et al. 2021
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 39
    true_value: 0.044
    true_std: 0.003
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05
    value_note: ''
    paper_rank: 171
    rank_delta: 132
    rank_delta_abs: 132
    rank_delta_direction: worse
    sort_value: 0.044
    sort_std: 0.003
    is_best: false
  - model: CIN (small)
    model_key: cin (small)
    model_plain: CIN (small)
    value: 0.044
    std: 0.003
    paper_value: 0.044
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.1
    table_ref: Table 1
    source_ref: Bodnar 2021
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 39
    true_value: 0.044
    true_std: 0.003
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.044
    sort_std: 0.003
    is_best: false
  - model: Subgraphormer + product graph PE
    model_key: subgraphormer + product graph pe
    model_plain: Subgraphormer + product graph PE
    value: 0.063
    std: 0.0003
    paper_value: 0.063
    paper_std: 0.0003
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 67
    true_value: 0.063
    true_std: 0.0003
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 67
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.063
    sort_std: 0.0003
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.163
    std: 0.004
    paper_value: 0.163
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    table_ref: Table 1
    source_ref: Xu et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 73
    true_value: 0.065
    true_std: 0.004
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.098
    value_note: ''
    paper_rank: 233
    rank_delta: 160
    rank_delta_abs: 160
    rank_delta_direction: worse
    sort_value: 0.065
    sort_std: 0.004
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.163
    std: 0.004
    paper_value: 0.163
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    table_ref: Table 1
    source_ref: Xu 2018
    variant_inference_reason: ''
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 73
    true_value: 0.065
    true_std: 0.004
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.098
    value_note: ''
    paper_rank: 233
    rank_delta: 160
    rank_delta_abs: 160
    rank_delta_direction: worse
    sort_value: 0.065
    sort_std: 0.004
    is_best: false
  - model: Subgraphormer + concatenation PE
    model_key: subgraphormer + concatenation pe
    model_plain: Subgraphormer + concatenation PE
    value: 0.071
    std: 0.003
    paper_value: 0.071
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 110
    true_value: 0.071
    true_std: 0.003
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 110
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.071
    sort_std: 0.003
    is_best: false
  - model: DS-GNN (efficient)
    model_key: ds-gnn (efficient)
    model_plain: DS-GNN (efficient)
    value: 0.087
    std: 0.003
    paper_value: 0.087
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Bevilacqua 2023
    variant_inference_reason: ''
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 160
    true_value: 0.087
    true_std: 0.003
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 160
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.087
    sort_std: 0.003
    is_best: false
  - model: K-Subgraph SAT
    model_key: k-subgraph sat
    model_plain: K-Subgraph SAT
    value: 0.094
    std: 0.008
    paper_value: 0.094
    paper_std: 0.008
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.523
    table_ref: Table 1
    source_ref: Chen et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 172
    true_value: 0.094
    true_std: 0.008
    value_gap_source_arxiv: '2504.12588'
    value_gap_source_title: Plain Transformers Can be Powerful Graph Learners
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 172
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.094
    sort_std: 0.008
    is_best: false
  - model: K-Subgraph SAT
    model_key: k-subgraph sat
    model_plain: K-Subgraph SAT
    value: 0.094
    std: 0.008
    paper_value: 0.094
    paper_std: 0.008
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.523
    table_ref: Table 1
    source_ref: Chen 2022
    variant_inference_reason: ''
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 172
    true_value: 0.094
    true_std: 0.008
    value_gap_source_arxiv: '2504.12588'
    value_gap_source_title: Plain Transformers Can be Powerful Graph Learners
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 172
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.094
    sort_std: 0.008
    is_best: false
  - model: GSN
    model_key: gsn
    model_plain: GSN
    value: 0.101
    std: 0.01
    paper_value: 0.101
    paper_std: 0.01
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    table_ref: Table 1
    source_ref: Bouritsas et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 176
    true_value: 0.101
    true_std: 0.01
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 176
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.101
    sort_std: 0.01
    is_best: false
  - model: GSN
    model_key: gsn
    model_plain: GSN
    value: 0.101
    std: 0.01
    paper_value: 0.101
    paper_std: 0.01
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    table_ref: Table 1
    source_ref: Bouritsas 2022
    variant_inference_reason: ''
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 176
    true_value: 0.101
    true_std: 0.01
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 176
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.101
    sort_std: 0.01
    is_best: false
  - model: DSS-GNN (EGO+)
    model_key: dss-gnn (ego+)
    model_plain: DSS-GNN (EGO+)
    value: 0.102
    std: 0.003
    paper_value: 0.102
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Bevilacqua 2021
    variant_inference_reason: ''
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 177
    true_value: 0.102
    true_std: 0.003
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 177
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.102
    sort_std: 0.003
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.139
    std: 0.006
    paper_value: 0.139
    paper_std: 0.006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.509
    table_ref: Table 1
    source_ref: Kreuzer et al. 2021
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 211
    true_value: 0.1341
    true_std: 0.0063
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0049000000000000155
    value_note: global 0.1341 within std
    paper_rank: 212
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.1341
    sort_std: 0.0063
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.139
    std: 0.006
    paper_value: 0.139
    paper_std: 0.006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.509
    table_ref: Table 1
    source_ref: Kreuzer 2021
    variant_inference_reason: ''
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 211
    true_value: 0.1341
    true_std: 0.0063
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0049000000000000155
    value_note: global 0.1341 within std
    paper_rank: 212
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.1341
    sort_std: 0.0063
    is_best: false
  - model: OSAN
    model_key: osan
    model_plain: OSAN
    value: 0.154
    std: 0.008
    paper_value: 0.154
    paper_std: 0.008
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    table_ref: Table 1
    source_ref: Qian et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 223
    true_value: 0.154
    true_std: 0.008
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 223
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.154
    sort_std: 0.008
    is_best: false
  - model: OSAN
    model_key: osan
    model_plain: OSAN
    value: 0.154
    std: 0.008
    paper_value: 0.154
    paper_std: 0.008
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    table_ref: Table 1
    source_ref: Qian 2022
    variant_inference_reason: ''
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 223
    true_value: 0.154
    true_std: 0.008
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 223
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.154
    sort_std: 0.008
    is_best: false
  metric: MAE
  higher_is_better: false
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
    value: 0.7606
    std: 0.0097
    paper_value: 0.7606
    paper_std: 0.0097
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kipf 2016
    variant_inference_reason: ''
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 3
    true_value: 0.9681
    true_std: 0.0003
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.2074999999999999
    value_note: ''
    paper_rank: 150
    rank_delta: 147
    rank_delta_abs: 147
    rank_delta_direction: worse
    sort_value: 0.9681
    sort_std: 0.0003
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.7558
    std: 0.014
    paper_value: 0.7558
    paper_std: 0.014
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    table_ref: Table 1
    source_ref: Xu 2018
    variant_inference_reason: ''
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 4
    true_value: 0.968
    true_std: 0.002
    value_gap_source_arxiv: '2502.02379'
    value_gap_source_title: 'No Metric to Rule Them All: Toward Principled Evaluations
      of Graph-Learning Datasets'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.21219999999999994
    value_note: ''
    paper_rank: 158
    rank_delta: 154
    rank_delta_abs: 154
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
  - model: CIN
    model_key: cin
    model_plain: CIN
    value: 0.8094
    std: 0.0057
    paper_value: 0.8094
    paper_std: 0.0057
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Bodnar 2021
    variant_inference_reason: ''
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 9
    true_value: 0.8094
    true_std: 0.0057
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8094
    sort_std: 0.0057
    is_best: false
  - model: GSN
    model_key: gsn
    model_plain: GSN
    value: 0.8039
    std: 0.009
    paper_value: 0.8039
    paper_std: 0.009
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    table_ref: Table 1
    source_ref: Bouritsas 2022
    variant_inference_reason: ''
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 19
    true_value: 0.8039
    true_std: 0.009
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8039
    sort_std: 0.009
    is_best: false
  - model: Subgraphormer
    model_key: subgraphormer
    model_plain: Subgraphormer
    value: 0.7948
    std: 0.0128
    paper_value: 0.7948
    paper_std: 0.0128
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.293
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 22
    true_value: 0.8038
    true_std: 0.0192
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.009000000000000008
    value_note: global 0.8038 within std
    paper_rank: 50
    rank_delta: 28
    rank_delta_abs: 28
    rank_delta_direction: worse
    sort_value: 0.8038
    sort_std: 0.0192
    is_best: false
  - model: SUN
    model_key: sun
    model_plain: SUN
    value: 0.8003
    std: 0.0055
    paper_value: 0.8003
    paper_std: 0.0055
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.526
    table_ref: Table 1
    source_ref: Frasca 2022
    variant_inference_reason: ''
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 31
    true_value: 0.8003
    true_std: 0.0055
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8003
    sort_std: 0.0055
    is_best: false
  - model: GNN (a)
    model_key: gnn (a)
    model_plain: GNN (a)
    value: 0.7961
    std: 0.0119
    paper_value: 0.7961
    paper_std: 0.0119
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhao 2022
    variant_inference_reason: ''
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 44
    true_value: 0.7961
    true_std: 0.0119
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 44
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7961
    sort_std: 0.0119
    is_best: false
  - model: GNN-SSWL+
    model_key: gnn-sswl+
    model_plain: GNN-SSWL+
    value: 0.7958
    std: 0.0035
    paper_value: 0.7958
    paper_std: 0.0035
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.387
    table_ref: Table 1
    source_ref: Zhang 2023
    variant_inference_reason: ''
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 48
    true_value: 0.7958
    true_std: 0.0035
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 48
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7958
    sort_std: 0.0035
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.7905
    std: 0.0132
    paper_value: 0.7905
    paper_std: 0.0132
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Corso 2020
    variant_inference_reason: ''
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 58
    true_value: 0.7905
    true_std: 0.0132
    value_gap_source_arxiv: '2604.17324'
    value_gap_source_title: 'SigGate-GT: Taming Over-Smoothing in Graph Transformers
      via Sigmoid-Gated Attention'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 58
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7905
    sort_std: 0.0132
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.788
    std: 0.0101
    paper_value: 0.788
    paper_std: 0.0101
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.424
    table_ref: Table 1
    source_ref: Rampásek 2022
    variant_inference_reason: ''
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 70
    true_value: 0.788
    true_std: 0.01
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 70
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.788
    sort_std: 0.01
    is_best: false
  - model: NGNN
    model_key: ngnn
    model_plain: NGNN
    value: 0.7834
    std: 0.0186
    paper_value: 0.7834
    paper_std: 0.0186
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    table_ref: Table 1
    source_ref: Zhang 2021
    variant_inference_reason: ''
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 88
    true_value: 0.7834
    true_std: 0.0186
    value_gap_source_arxiv: '2405.02795'
    value_gap_source_title: Graph as Point Set
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 88
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7834
    sort_std: 0.0186
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.7785
    std: 0.0024
    paper_value: 0.7785
    paper_std: 0.0024
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.509
    table_ref: Table 1
    source_ref: Kreuzer 2021
    variant_inference_reason: ''
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 111
    true_value: 0.7785
    true_std: 0.247
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 111
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7785
    sort_std: 0.247
    is_best: true
  - model: DSS-GNN
    model_key: dss-gnn
    model_plain: DSS-GNN
    value: 0.7678
    std: 0.0166
    paper_value: 0.7678
    paper_std: 0.0166
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.1
    table_ref: Table 1
    source_ref: Bevilacqua 2021
    variant_inference_reason: ''
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 134
    true_value: 0.7678
    true_std: 0.0166
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 134
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7678
    sort_std: 0.0166
    is_best: false
  - model: Recon. GNN
    model_key: recon. gnn
    model_plain: Recon. GNN
    value: 0.7632
    std: 0.014
    paper_value: 0.7632
    paper_std: 0.014
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Cotta 2021
    variant_inference_reason: ''
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 145
    true_value: 0.7632
    true_std: 0.014
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 145
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7632
    sort_std: 0.014
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
- benchmark: LRGB
  datasets:
  - *id002
  - *id003
- benchmark: OGB
  datasets:
  - *id004
- benchmark: MoleculeNet
  datasets:
  - *id005
  - *id006
main_figure: /figures/2402.08450/main_figure.png
---

