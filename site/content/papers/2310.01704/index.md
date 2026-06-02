---
title: Transformers are efficient hierarchical chemical graph learners
arxiv_id: '2310.01704'
source_url: ''
authors: []
published_date: Oct 2, 2023
published_date_iso: '2023-10-02'
published_venue: ''
abstract: Transformers, adapted from natural language processing, are emerging as
  a leading approach for graph representation learning. Contemporary graph transformers
  often treat nodes or edges as separate tokens. This approach leads to computational
  challenges for even moderately-sized graphs due to the quadratic scaling of self-attention
  complexity with token count. In this paper, we introduce SubFormer, a graph transformer
  that operates on subgraphs that aggregate information by a message-passing mechanism.
  This approach reduces the number of tokens and enhances learning long-range interactions.
  We demonstrate SubFormer on benchmarks for predicting molecular properties from
  chemical structures and show that it is competitive with state-of-the-art graph
  transformers at a fraction of the computational cost, with training times on the
  order of minutes on a consumer-grade graphics card. We interpret the attention weights
  in terms of chemical structures. We show that SubFormer exhibits limited over-smoothing
  and avoids over-squashing, which is prevalent in traditional graph neural networks.
codebase_url: ''
extraction_model: Qwen/Qwen3.6-35B-A3B-FP8
has_results: true
paper_type: method
proposed_models:
- MP
- MP (dual readout, slim)
- MP (dual readout, VN)
mrr: 0.0473
adjusted_mrr: 0.0473
mrr_dataset_count: 4
benchmark_categories:
- Classic
- OGB
- MoleculeNet
task_categories:
- graph_classification
- graph_regression
experiment_scopes:
- graph-level
results:
- &id003
  dataset: Tox21
  rows:
  - model: HIMP
    model_key: himp
    model_plain: HIMP
    value: 0.874
    std: 0.005
    paper_value: 0.874
    paper_std: 0.005
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: HIMP2020
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    published_venue: null
    global_rank: 1
    true_value: 0.874
    true_std: 0.005
    value_gap_source_arxiv: '2310.01704'
    value_gap_source_title: Transformers are efficient hierarchical chemical graph
      learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.874
    sort_std: 0.005
    is_best: true
  - model: MP (dual readout, VN)
    model_key: mp (dual readout, vn)
    model_plain: MP (dual readout, VN)
    value: 0.851
    std: 0.008
    paper_value: 0.851
    paper_std: 0.008
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    published_venue: null
    global_rank: 2
    true_value: 0.851
    true_std: 0.008
    value_gap_source_arxiv: '2310.01704'
    value_gap_source_title: Transformers are efficient hierarchical chemical graph
      learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.851
    sort_std: 0.008
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.85
    std: 0.009
    paper_value: 0.85
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
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    published_venue: null
    global_rank: 3
    true_value: 0.85
    true_std: 0.009
    value_gap_source_arxiv: '2310.01704'
    value_gap_source_title: Transformers are efficient hierarchical chemical graph
      learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.85
    sort_std: 0.009
    is_best: false
  - model: GeomGCL
    model_key: geomgcl
    model_plain: GeomGCL
    value: 0.85
    std: null
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2109.11730'
    title: 'GeomGCL: Geometric Graph Contrastive Learning for Molecular Property Prediction'
    date: Sep 2021
    date_display: Sep 2021
    date_iso: 2021-09
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.85
    sort_std: null
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.849
    std: null
    paper_value: 0.849
    paper_std: null
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: rampavsek2022recipe
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    published_venue: null
    global_rank: 6
    true_value: 0.849
    true_std: null
    value_gap_source_arxiv: '2310.01704'
    value_gap_source_title: Transformers are efficient hierarchical chemical graph
      learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.849
    sort_std: null
    is_best: false
  - model: ChemRL-GEM
    model_key: chemrl-gem
    model_plain: ChemRL-GEM
    value: 0.849
    std: 0.003
    paper_value: 0.849
    paper_std: 0.003
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    published_venue: null
    global_rank: 5
    true_value: 0.849
    true_std: 0.003
    value_gap_source_arxiv: '2310.01704'
    value_gap_source_title: Transformers are efficient hierarchical chemical graph
      learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.849
    sort_std: 0.003
    is_best: false
  - model: D-MPNN
    model_key: d-mpnn
    model_plain: D-MPNN
    value: 0.848
    std: null
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2109.11730'
    title: 'GeomGCL: Geometric Graph Contrastive Learning for Molecular Property Prediction'
    date: Sep 2021
    date_display: Sep 2021
    date_iso: 2021-09
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 7
    sort_value: 0.848
    sort_std: null
    is_best: false
  - model: MoLFormer-XL
    model_key: molformer-xl
    model_plain: MoLFormer-XL
    value: 0.847
    std: null
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.09553'
    title: How Much Structural Information Large Scale Molecular Language Representations
      Can Capture?
    date: Jun 2021
    date_display: Jun 2021
    date_iso: 2021-06
    codebase_url: https://github.com/IBM/molformer
    uses_external_data: true
    is_global_top: true
    global_rank: 8
    sort_value: 0.847
    sort_std: null
    is_best: false
  - model: MP
    model_key: mp
    model_plain: MP
    value: 0.841
    std: 0.003
    paper_value: 0.841
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
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    published_venue: null
    global_rank: 10
    true_value: 0.841
    true_std: 0.003
    value_gap_source_arxiv: '2310.01704'
    value_gap_source_title: Transformers are efficient hierarchical chemical graph
      learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.841
    sort_std: 0.003
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.84
    std: 0.004
    paper_value: 0.84
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
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    published_venue: null
    global_rank: 11
    true_value: 0.84
    true_std: 0.004
    value_gap_source_arxiv: '2310.01704'
    value_gap_source_title: Transformers are efficient hierarchical chemical graph
      learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.84
    sort_std: 0.004
    is_best: false
  - model: Kernel SVM
    model_key: kernel svm
    model_plain: Kernel SVM
    value: 0.822
    std: 0.006
    paper_value: 0.822
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
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    published_venue: null
    global_rank: 19
    true_value: 0.822
    true_std: 0.006
    value_gap_source_arxiv: '2310.01704'
    value_gap_source_title: Transformers are efficient hierarchical chemical graph
      learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.822
    sort_std: 0.006
    is_best: false
  - model: XGBoost
    model_key: xgboost
    model_plain: XGBoost
    value: 0.794
    std: 0.014
    paper_value: 0.794
    paper_std: 0.014
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    published_venue: null
    global_rank: 34
    true_value: 0.794
    true_std: 0.014
    value_gap_source_arxiv: '2310.01704'
    value_gap_source_title: Transformers are efficient hierarchical chemical graph
      learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 34
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.794
    sort_std: 0.014
    is_best: false
  - model: Logistic Regression
    model_key: logistic regression
    model_plain: Logistic Regression
    value: 0.794
    std: 0.015
    paper_value: 0.794
    paper_std: 0.015
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    published_venue: null
    global_rank: 35
    true_value: 0.794
    true_std: 0.015
    value_gap_source_arxiv: '2310.01704'
    value_gap_source_title: Transformers are efficient hierarchical chemical graph
      learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.794
    sort_std: 0.015
    is_best: false
  - model: Random Forest
    model_key: random forest
    model_plain: Random Forest
    value: 0.769
    std: 0.015
    paper_value: 0.769
    paper_std: 0.015
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    published_venue: null
    global_rank: 60
    true_value: 0.769
    true_std: 0.015
    value_gap_source_arxiv: '2310.01704'
    value_gap_source_title: Transformers are efficient hierarchical chemical graph
      learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 60
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.769
    sort_std: 0.015
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id004
  dataset: ToxCast
  rows:
  - model: AI
    model_key: ai
    model_plain: AI
    value: 0.824
    std: 0.007
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.05481'
    title: A Molecular Multimodal Foundation Model Associating Molecule Graphs with
      Natural Language
    date: Sep 2022
    date_display: Sep 2022
    date_iso: 2022-09
    codebase_url: https://github.com/BingSu12/MoMu
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.824
    sort_std: 0.007
    is_best: true
  - model: DimeNet++
    model_key: dimenet++
    model_plain: DimeNet++
    value: 0.815
    std: 0.008
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.05481'
    title: A Molecular Multimodal Foundation Model Associating Molecule Graphs with
      Natural Language
    date: Sep 2022
    date_display: Sep 2022
    date_iso: 2022-09
    codebase_url: https://github.com/BingSu12/MoMu
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.815
    sort_std: 0.008
    is_best: true
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.812
    std: 0.006
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1802.00543'
    title: Modeling polypharmacy side effects with graph convolutional networks
    date: Feb 2, 2018
    date_display: Feb 2018
    date_iso: '2018-02-02'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.812
    sort_std: 0.006
    is_best: true
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.741
    std: 0.004
    paper_value: 0.741
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
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    published_venue: null
    global_rank: 7
    true_value: 0.794
    true_std: 0.01
    value_gap_source_arxiv: '2209.05481'
    value_gap_source_title: A Molecular Multimodal Foundation Model Associating Molecule
      Graphs with Natural Language
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05300000000000005
    value_note: ''
    paper_rank: 17
    rank_delta: 10
    rank_delta_abs: 10
    rank_delta_direction: worse
    sort_value: 0.794
    sort_std: 0.01
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.735
    std: 0.002
    paper_value: 0.735
    paper_std: 0.002
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    published_venue: null
    global_rank: 10
    true_value: 0.785
    true_std: 0.012
    value_gap_source_arxiv: '2209.05481'
    value_gap_source_title: A Molecular Multimodal Foundation Model Associating Molecule
      Graphs with Natural Language
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.050000000000000044
    value_note: ''
    paper_rank: 17
    rank_delta: 7
    rank_delta_abs: 7
    rank_delta_direction: worse
    sort_value: 0.785
    sort_std: 0.012
    is_best: false
  - model: MP (dual readout, VN)
    model_key: mp (dual readout, vn)
    model_plain: MP (dual readout, VN)
    value: 0.752
    std: 0.003
    paper_value: 0.752
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
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    published_venue: null
    global_rank: 13
    true_value: 0.752
    true_std: 0.003
    value_gap_source_arxiv: '2310.01704'
    value_gap_source_title: Transformers are efficient hierarchical chemical graph
      learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.752
    sort_std: 0.003
    is_best: false
  - model: ChemRL-GEM
    model_key: chemrl-gem
    model_plain: ChemRL-GEM
    value: 0.742
    std: 0.004
    paper_value: 0.742
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
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    published_venue: null
    global_rank: 17
    true_value: 0.742
    true_std: 0.004
    value_gap_source_arxiv: '2310.01704'
    value_gap_source_title: Transformers are efficient hierarchical chemical graph
      learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.742
    sort_std: 0.004
    is_best: false
  - model: MP
    model_key: mp
    model_plain: MP
    value: 0.733
    std: 0.001
    paper_value: 0.733
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
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    published_venue: null
    global_rank: 20
    true_value: 0.733
    true_std: 0.001
    value_gap_source_arxiv: '2310.01704'
    value_gap_source_title: Transformers are efficient hierarchical chemical graph
      learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.733
    sort_std: 0.001
    is_best: false
  - model: HIMP
    model_key: himp
    model_plain: HIMP
    value: 0.721
    std: 0.004
    paper_value: 0.721
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
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    published_venue: null
    global_rank: 25
    true_value: 0.721
    true_std: 0.004
    value_gap_source_arxiv: '2310.01704'
    value_gap_source_title: Transformers are efficient hierarchical chemical graph
      learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.721
    sort_std: 0.004
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.719
    std: null
    paper_value: 0.719
    paper_std: null
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    published_venue: null
    global_rank: 26
    true_value: 0.719
    true_std: null
    value_gap_source_arxiv: '2310.01704'
    value_gap_source_title: Transformers are efficient hierarchical chemical graph
      learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.719
    sort_std: null
    is_best: false
  - model: Kernel SVM
    model_key: kernel svm
    model_plain: Kernel SVM
    value: 0.669
    std: 0.014
    paper_value: 0.669
    paper_std: 0.014
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    published_venue: null
    global_rank: 46
    true_value: 0.669
    true_std: 0.014
    value_gap_source_arxiv: '2310.01704'
    value_gap_source_title: Transformers are efficient hierarchical chemical graph
      learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 46
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.669
    sort_std: 0.014
    is_best: false
  - model: XGBoost
    model_key: xgboost
    model_plain: XGBoost
    value: 0.64
    std: 0.005
    paper_value: 0.64
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
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    published_venue: null
    global_rank: 70
    true_value: 0.64
    true_std: 0.005
    value_gap_source_arxiv: '2310.01704'
    value_gap_source_title: Transformers are efficient hierarchical chemical graph
      learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 70
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.64
    sort_std: 0.005
    is_best: false
  - model: Logistic Regression
    model_key: logistic regression
    model_plain: Logistic Regression
    value: 0.605
    std: 0.003
    paper_value: 0.605
    paper_std: 0.003
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    published_venue: null
    global_rank: 104
    true_value: 0.605
    true_std: 0.003
    value_gap_source_arxiv: '2310.01704'
    value_gap_source_title: Transformers are efficient hierarchical chemical graph
      learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 104
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.605
    sort_std: 0.003
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id001
  dataset: ZINC
  rows:
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.004
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.03589'
    title: How does over-squashing affect the power of GNNs?
    date: Jun 6, 2023
    date_display: Jun 2023
    date_iso: '2023-06-06'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.004
    sort_std: null
    is_best: true
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.006
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.03589'
    title: How does over-squashing affect the power of GNNs?
    date: Jun 6, 2023
    date_display: Jun 2023
    date_iso: '2023-06-06'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.006
    sort_std: null
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.408
    std: 0.008
    paper_value: 0.408
    paper_std: 0.008
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    published_venue: null
    global_rank: 3
    true_value: 0.014
    true_std: null
    value_gap_source_arxiv: '2306.03589'
    value_gap_source_title: How does over-squashing affect the power of GNNs?
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.39399999999999996
    value_note: ''
    paper_rank: 149
    rank_delta: 146
    rank_delta_abs: 146
    rank_delta_direction: worse
    sort_value: 0.014
    sort_std: null
    is_best: false
  - model: PPGN++(6)
    model_key: ppgn++(6)
    model_plain: PPGN++(6)
    value: 0.02
    std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08450'
    title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via Graph
      Products'
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    codebase_url: https://github.com/BarSGuy/Subgraphormer
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.02
    sort_std: 0.001
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.367
    std: 0.011
    paper_value: 0.367
    paper_std: 0.011
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    published_venue: null
    global_rank: 11
    true_value: 0.024
    true_std: null
    value_gap_source_arxiv: '2306.03589'
    value_gap_source_title: How does over-squashing affect the power of GNNs?
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.34299999999999997
    value_note: ''
    paper_rank: 144
    rank_delta: 133
    rank_delta_abs: 133
    rank_delta_direction: worse
    sort_value: 0.024
    sort_std: null
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
    params_millions: null
    table_ref: Table 1
    source_ref: Graphormer2021
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    published_venue: null
    global_rank: 13
    true_value: 0.025
    true_std: 0.004
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.097
    value_note: ''
    paper_rank: 87
    rank_delta: 74
    rank_delta_abs: 74
    rank_delta_direction: worse
    sort_value: 0.025
    sort_std: 0.004
    is_best: false
  - model: AUTOBAHN
    model_key: autobahn
    model_plain: AUTOBAHN
    value: 0.106
    std: 0.004
    paper_value: 0.106
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: thiede2021autobahn
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    published_venue: null
    global_rank: 22
    true_value: 0.029
    true_std: 0.001
    value_gap_source_arxiv: '2406.08210'
    value_gap_source_title: arXiv:2406.08210
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.077
    value_note: ''
    paper_rank: 77
    rank_delta: 55
    rank_delta_abs: 55
    rank_delta_direction: worse
    sort_value: 0.029
    sort_std: 0.001
    is_best: false
  - model: HIMP
    model_key: himp
    model_plain: HIMP
    value: 0.151
    std: 0.006
    paper_value: 0.151
    paper_std: 0.006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: HIMP2020
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    published_venue: null
    global_rank: 27
    true_value: 0.036
    true_std: 0.002
    value_gap_source_arxiv: '2406.08210'
    value_gap_source_title: arXiv:2406.08210
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11499999999999999
    value_note: ''
    paper_rank: 109
    rank_delta: 82
    rank_delta_abs: 82
    rank_delta_direction: worse
    sort_value: 0.036
    sort_std: 0.002
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
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
    source_ref: GraphGPS2022
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    published_venue: null
    global_rank: 50
    true_value: 0.07
    true_std: 0.004
    value_gap_source_arxiv: '2502.00282'
    value_gap_source_title: 'GraphMinNet: Learning Dependencies in Graphs with Light
      Complexity Minimal Architecture'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 50
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.07
    sort_std: 0.004
    is_best: false
  - model: MP (dual readout, VN)
    model_key: mp (dual readout, vn)
    model_plain: MP (dual readout, VN)
    value: 0.077
    std: 0.003
    paper_value: 0.077
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    published_venue: null
    global_rank: 57
    true_value: 0.077
    true_std: 0.003
    value_gap_source_arxiv: '2310.01704'
    value_gap_source_title: Transformers are efficient hierarchical chemical graph
      learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 57
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.077
    sort_std: 0.003
    is_best: false
  - model: MP (dual readout, slim)
    model_key: mp (dual readout, slim)
    model_plain: MP (dual readout, slim)
    value: 0.084
    std: 0.004
    paper_value: 0.084
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    published_venue: null
    global_rank: 59
    true_value: 0.084
    true_std: 0.004
    value_gap_source_arxiv: '2310.01704'
    value_gap_source_title: Transformers are efficient hierarchical chemical graph
      learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 59
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.084
    sort_std: 0.004
    is_best: false
  - model: MP
    model_key: mp
    model_plain: MP
    value: 0.094
    std: 0.003
    paper_value: 0.094
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    published_venue: null
    global_rank: 71
    true_value: 0.094
    true_std: 0.003
    value_gap_source_arxiv: '2310.01704'
    value_gap_source_title: Transformers are efficient hierarchical chemical graph
      learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 71
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.094
    sort_std: 0.003
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
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    published_venue: null
    global_rank: 80
    true_value: 0.111
    true_std: 0.002
    value_gap_source_arxiv: '2301.09505'
    value_gap_source_title: Rethinking the Expressive Power of GNNs via Graph Biconnectivity
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.273
    value_note: ''
    paper_rank: 147
    rank_delta: 67
    rank_delta_abs: 67
    rank_delta_direction: worse
    sort_value: 0.111
    sort_std: 0.002
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
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    published_venue: null
    global_rank: 97
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
    paper_rank: 100
    rank_delta: 3
    rank_delta_abs: 3
    rank_delta_direction: worse
    sort_value: 0.1341
    sort_std: 0.0063
    is_best: false
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.226
    std: 0.014
    paper_value: 0.226
    paper_std: 0.014
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    published_venue: null
    global_rank: 132
    true_value: 0.226
    true_std: 0.014
    value_gap_source_arxiv: '2110.07875'
    value_gap_source_title: Graph Neural Networks with Learnable Structural and Positional
      Representations
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 132
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.226
    sort_std: 0.014
    is_best: false
  metric: MAE
  higher_is_better: false
- &id002
  dataset: ogbg-molhiv
  rows:
  - model: ML
    model_key: ml
    model_plain: ML
    value: 0.997
    std: 0.002
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.08443'
    title: 'CLEAR: Generative Counterfactual Explanations on Graphs'
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.997
    sort_std: 0.002
    is_best: true
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.862
    std: 0.002
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.862
    sort_std: 0.002
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.788
    std: 0.01
    paper_value: 0.788
    paper_std: 0.01
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: rampavsek2022recipe
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    published_venue: null
    global_rank: 3
    true_value: 0.858
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.06999999999999995
    value_note: ''
    paper_rank: 51
    rank_delta: 48
    rank_delta_abs: 48
    rank_delta_direction: worse
    sort_value: 0.858
    sort_std: 0.002
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.855
    std: 0.002
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.855
    sort_std: 0.002
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.756
    std: 0.014
    paper_value: 0.756
    paper_std: 0.014
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    published_venue: null
    global_rank: 9
    true_value: 0.848
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09199999999999997
    value_note: ''
    paper_rank: 131
    rank_delta: 122
    rank_delta_abs: 122
    rank_delta_direction: worse
    sort_value: 0.848
    sort_std: 0.003
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.761
    std: 0.01
    paper_value: 0.761
    paper_std: 0.01
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    published_venue: null
    global_rank: 13
    true_value: 0.839
    true_std: 0.006
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07799999999999996
    value_note: ''
    paper_rank: 117
    rank_delta: 104
    rank_delta_abs: 104
    rank_delta_direction: worse
    sort_value: 0.839
    sort_std: 0.006
    is_best: false
  - model: MP
    model_key: mp
    model_plain: MP
    value: 0.795
    std: 0.008
    paper_value: 0.795
    paper_std: 0.008
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    published_venue: null
    global_rank: 40
    true_value: 0.795
    true_std: 0.008
    value_gap_source_arxiv: '2310.01704'
    value_gap_source_title: Transformers are efficient hierarchical chemical graph
      learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 40
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.795
    sort_std: 0.008
    is_best: false
  - model: Kernel SVM
    model_key: kernel svm
    model_plain: Kernel SVM
    value: 0.792
    std: 0.0
    paper_value: 0.792
    paper_std: 0.0
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    published_venue: null
    global_rank: 46
    true_value: 0.792
    true_std: 0.0
    value_gap_source_arxiv: '2310.01704'
    value_gap_source_title: Transformers are efficient hierarchical chemical graph
      learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 46
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.792
    sort_std: 0.0
    is_best: false
  - model: HIMP
    model_key: himp
    model_plain: HIMP
    value: 0.788
    std: 0.08
    paper_value: 0.788
    paper_std: 0.08
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: HIMP2020
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    published_venue: null
    global_rank: 54
    true_value: 0.788
    true_std: 0.08
    value_gap_source_arxiv: '2310.01704'
    value_gap_source_title: Transformers are efficient hierarchical chemical graph
      learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 54
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.788
    sort_std: 0.08
    is_best: false
  - model: Random Forest
    model_key: random forest
    model_plain: Random Forest
    value: 0.781
    std: 0.006
    paper_value: 0.781
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
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    published_venue: null
    global_rank: 75
    true_value: 0.781
    true_std: 0.006
    value_gap_source_arxiv: '2310.01704'
    value_gap_source_title: Transformers are efficient hierarchical chemical graph
      learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 75
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.781
    sort_std: 0.006
    is_best: false
  - model: AUTOBAHN
    model_key: autobahn
    model_plain: AUTOBAHN
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
    source_ref: thiede2021autobahn
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    published_venue: null
    global_rank: 78
    true_value: 0.78
    true_std: 0.015
    value_gap_source_arxiv: '2310.01704'
    value_gap_source_title: Transformers are efficient hierarchical chemical graph
      learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 78
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.78
    sort_std: 0.015
    is_best: false
  - model: MP (dual readout, VN)
    model_key: mp (dual readout, vn)
    model_plain: MP (dual readout, VN)
    value: 0.756
    std: 0.007
    paper_value: 0.756
    paper_std: 0.007
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    published_venue: null
    global_rank: 133
    true_value: 0.756
    true_std: 0.007
    value_gap_source_arxiv: '2310.01704'
    value_gap_source_title: Transformers are efficient hierarchical chemical graph
      learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 133
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.756
    sort_std: 0.007
    is_best: false
  - model: XGBoost
    model_key: xgboost
    model_plain: XGBoost
    value: 0.756
    std: 0.0
    paper_value: 0.756
    paper_std: 0.0
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    published_venue: null
    global_rank: 132
    true_value: 0.756
    true_std: 0.0
    value_gap_source_arxiv: '2310.01704'
    value_gap_source_title: Transformers are efficient hierarchical chemical graph
      learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 132
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.756
    sort_std: 0.0
    is_best: false
  - model: Logistic Regression
    model_key: logistic regression
    model_plain: Logistic Regression
    value: 0.702
    std: 0.018
    paper_value: 0.702
    paper_std: 0.018
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    published_venue: null
    global_rank: 167
    true_value: 0.702
    true_std: 0.018
    value_gap_source_arxiv: '2310.01704'
    value_gap_source_title: Transformers are efficient hierarchical chemical graph
      learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 167
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.702
    sort_std: 0.018
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
- benchmark: OGB
  datasets:
  - *id002
- benchmark: MoleculeNet
  datasets:
  - *id003
  - *id004
---

