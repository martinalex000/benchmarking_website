---
title: An end-to-end attention-based approach for learning on graphs
arxiv_id: '2402.10793'
source_url: ''
authors: []
published_date: Feb 2024
published_date_iso: 2024-02
abstract: There has been a recent surge in transformer-based architectures for learning
  on graphs, mainly motivated by attention as an effective learning mechanism and
  the desire to supersede the hand-crafted operators characteristic of message passing
  schemes. However, concerns over their empirical effectiveness, scalability, and
  complexity of the pre-processing steps have been raised, especially in relation
  to much simpler graph neural networks that typically perform on par with them across
  a wide range of benchmarks. To address these shortcomings, we consider graphs as
  sets of edges and propose a purely attention-based approach consisting of an encoder
  and an attention pooling mechanism. The encoder vertically interleaves masked and
  vanilla self-attention modules to learn an effective representation of edges while
  allowing for tackling possible misspecifications in input graphs. Despite its simplicity,
  the approach outperforms fine-tuned message passing baselines and recently proposed
  transformer-based methods on more than 70 node and graph-level tasks, including
  challenging long-range benchmarks. Moreover, we demonstrate state-of-the-art performance
  across different tasks, ranging from molecular to vision graphs, and heterophilous
  node classification. The approach also outperforms graph neural networks and transformers
  in transfer learning settings and scales much better than alternatives with a similar
  performance level or expressive power.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- ESA
- ESA (3/4)
mrr: 0.4635
adjusted_mrr: 0.4635
mrr_dataset_count: 5
benchmark_categories:
- Classic
- LRGB
- TU Dortmund
- Quantum Chemistry
- Other Graph Benchmarks
task_categories:
- graph_classification
- graph_regression
experiment_scopes:
- graph-level
results:
- &id004
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
  - model: ESA
    model_key: esa
    model_plain: ESA
    value: 0.6968516041247438
    std: 0.0013794417525553372
    paper_value: 0.6968516041247438
    paper_std: 0.0013794417525553372
    metric: R^2
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: null
    sort_value: 0.6968516041247438
    sort_std: 0.0013794417525553372
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.6962037752713723
    std: 0.0017162537128048157
    paper_value: 0.6962037752713723
    paper_std: 0.0017162537128048157
    metric: R^2
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: null
    sort_value: 0.6962037752713723
    sort_std: 0.0017162537128048157
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.675772
    std: 0.0019314683533518953
    paper_value: 0.675772
    paper_std: 0.0019314683533518953
    metric: R^2
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: null
    sort_value: 0.675772
    sort_std: 0.0019314683533518953
    is_best: false
  - model: DropGIN
    model_key: dropgin
    model_plain: DropGIN
    value: 0.6750444425282793
    std: 0.003010065997818225
    paper_value: 0.6750444425282793
    paper_std: 0.003010065997818225
    metric: R^2
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: null
    sort_value: 0.6750444425282793
    sort_std: 0.003010065997818225
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.6659264497946298
    std: 0.0019193275851867547
    paper_value: 0.6659264497946298
    paper_std: 0.0019193275851867547
    metric: R^2
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 35
    sort_value: 0.6659264497946298
    sort_std: 0.0019193275851867547
    is_best: false
  - model: GATv2
    model_key: gatv2
    model_plain: GATv2
    value: 0.65472612254266
    std: 0.004456977663883839
    paper_value: 0.65472612254266
    paper_std: 0.004456977663883839
    metric: R^2
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 76
    sort_value: 0.65472612254266
    sort_std: 0.004456977663883839
    is_best: false
  - model: TokenGT
    model_key: tokengt
    model_plain: TokenGT
    value: 0.6407549500465393
    std: 0.008498306711241119
    paper_value: 0.6407549500465393
    paper_std: 0.008498306711241119
    metric: R^2
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: null
    sort_value: 0.6407549500465393
    sort_std: 0.008498306711241119
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id007
  dataset: MalNet-Tiny
  rows:
  - model: ESA
    model_key: esa
    model_plain: ESA
    value: 0.948
    std: 0.00424
    paper_value: 0.948
    paper_std: 0.00424
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 1
    true_value: 0.948
    true_std: 0.00424
    value_gap_source_arxiv: '2402.10793'
    value_gap_source_title: An end-to-end attention-based approach for learning on
      graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.948
    sort_std: 0.00424
    is_best: true
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.946
    std: 0.0057
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09263'
    title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks? Simple Architectures
      Meet Excellence
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.946
    sort_std: 0.0057
    is_best: true
  - model: GSM++ (MoT)
    model_key: gsm++ (mot)
    model_plain: GSM++ (MoT)
    value: 0.9437
    std: 0.0058
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
    global_rank: 3
    sort_value: 0.9437
    sort_std: 0.0058
    is_best: true
  - model: GSM++ (BFS)
    model_key: gsm++ (bfs)
    model_plain: GSM++ (BFS)
    value: 0.9417
    std: 0.002
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
    global_rank: 4
    sort_value: 0.9417
    sort_std: 0.002
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id005
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
    metric: Accuracy
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
  - model: ESA
    model_key: esa
    model_plain: ESA
    value: 0.7546
    std: 0.0115
    paper_value: 0.7546
    paper_std: 0.0115
    metric: MCC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: null
    sort_value: 0.7546
    sort_std: 0.0115
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.7009
    std: 0.0181
    paper_value: 0.7009
    paper_std: 0.0181
    metric: MCC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 47
    sort_value: 0.7009
    sort_std: 0.0181
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.6969
    std: 0.0252
    paper_value: 0.6969
    paper_std: 0.0252
    metric: MCC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: null
    sort_value: 0.6969
    sort_std: 0.0252
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.6967
    std: 0.0268
    paper_value: 0.6967
    paper_std: 0.0268
    metric: MCC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 84
    sort_value: 0.6967
    sort_std: 0.0268
    is_best: false
  - model: DropGIN
    model_key: dropgin
    model_plain: DropGIN
    value: 0.6857
    std: 0.0274
    paper_value: 0.6857
    paper_std: 0.0274
    metric: MCC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: null
    sort_value: 0.6857
    sort_std: 0.0274
    is_best: false
  - model: GATv2
    model_key: gatv2
    model_plain: GATv2
    value: 0.6463
    std: 0.0293
    paper_value: 0.6463
    paper_std: 0.0293
    metric: MCC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: null
    sort_value: 0.6463
    sort_std: 0.0293
    is_best: false
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.5401
    std: 0.0245
    paper_value: 0.5401
    paper_std: 0.0245
    metric: MCC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: null
    sort_value: 0.5401
    sort_std: 0.0245
    is_best: false
  - model: TokenGT
    model_key: tokengt
    model_plain: TokenGT
    value: 0.5316
    std: 0.0337
    paper_value: 0.5316
    paper_std: 0.0337
    metric: MCC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: null
    sort_value: 0.5316
    sort_std: 0.0337
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
    value: 0.686
    std: 0.005
    paper_value: 0.686
    paper_std: 0.005
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Tonshoff 2023
    variant_inference_reason: ''
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
    value_gap: 0.040099999999999913
    value_note: ''
    paper_rank: 86
    rank_delta: 77
    rank_delta_abs: 77
    rank_delta_direction: worse
    sort_value: 0.7261
    sort_std: 0.0067
    is_best: false
  - model: ESA
    model_key: esa
    model_plain: ESA
    value: 0.7071
    std: 0.0015
    paper_value: 0.7071
    paper_std: 0.0015
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 39
    true_value: 0.7071
    true_std: 0.0015
    value_gap_source_arxiv: '2402.10793'
    value_gap_source_title: An end-to-end attention-based approach for learning on
      graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7071
    sort_std: 0.0015
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.6621
    std: 0.0067
    paper_value: 0.6621
    paper_std: 0.0067
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Tonshoff 2023
    variant_inference_reason: ''
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
    value_gap: 0.04379999999999995
    value_note: ''
    paper_rank: 140
    rank_delta: 100
    rank_delta_abs: 100
    rank_delta_direction: worse
    sort_value: 0.7059
    sort_std: 0.0089
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.6534
    std: 0.0091
    paper_value: 0.6534
    paper_std: 0.0091
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Tonshoff 2023
    variant_inference_reason: ''
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 152
    true_value: 0.6601
    true_std: 0.0061
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.006700000000000039
    value_note: global 0.6601 within std
    paper_rank: 170
    rank_delta: 18
    rank_delta_abs: 18
    rank_delta_direction: worse
    sort_value: 0.6601
    sort_std: 0.0061
    is_best: false
  - model: TokenGT
    model_key: tokengt
    model_plain: TokenGT
    value: 0.6263
    std: 0.0117
    paper_value: 0.6263
    paper_std: 0.0117
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Tonshoff 2023
    variant_inference_reason: ''
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 227
    true_value: 0.6263
    true_std: 0.0117
    value_gap_source_arxiv: '2402.10793'
    value_gap_source_title: An end-to-end attention-based approach for learning on
      graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 227
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6263
    sort_std: 0.0117
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
    paper_value: 0.2393
    paper_std: 0.0004
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 1
    true_value: 0.2393
    true_std: 0.0004
    value_gap_source_arxiv: '2402.10793'
    value_gap_source_title: An end-to-end attention-based approach for learning on
      graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
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
    value: 0.246
    std: 0.0007
    paper_value: 0.246
    paper_std: 0.0007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Tonshoff 2023
    variant_inference_reason: ''
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
    value_gap: 0.003899999999999987
    value_note: ''
    paper_rank: 53
    rank_delta: 50
    rank_delta_abs: 50
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
  - model: IPR-MPNN
    model_key: ipr-mpnn
    model_plain: IPR-MPNN
    value: 0.2422
    std: 0.0007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.16560'
    title: Algorithmic Graph Tasks
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    codebase_url: https://github.com/nec-research/Adaptive-Message-Passing
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    sort_value: 0.2422
    sort_std: 0.0007
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.2473
    std: 0.0017
    paper_value: 0.2473
    paper_std: 0.0017
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Tonshoff 2023
    variant_inference_reason: ''
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
    value_gap: 0.004399999999999987
    value_note: ''
    paper_rank: 77
    rank_delta: 68
    rank_delta_abs: 68
    rank_delta_direction: worse
    sort_value: 0.2429
    sort_std: 0.0019
    is_best: false
  - model: ESA (3/4)
    model_key: esa (3/4)
    model_plain: ESA (3/4)
    value: 0.245329301
    std: 0.000297453
    paper_value: 0.245329301
    paper_std: 0.000297453
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Tonshoff 2023
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 40
    true_value: 0.245329301
    true_std: 0.000297453
    value_gap_source_arxiv: '2402.10793'
    value_gap_source_title: An end-to-end attention-based approach for learning on
      graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 40
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.245329301
    sort_std: 0.000297453
    is_best: false
  - model: GCN (6/6)
    model_key: gcn (6/6)
    model_plain: GCN (6/6)
    value: 0.246
    std: 0.0007
    paper_value: 0.246
    paper_std: 0.0007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Tonshoff 2023
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 56
    true_value: 0.246
    true_std: 0.0007
    value_gap_source_arxiv: '2402.10793'
    value_gap_source_title: An end-to-end attention-based approach for learning on
      graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 56
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.246
    sort_std: 0.0007
    is_best: false
  - model: GIN (10/8)
    model_key: gin (10/8)
    model_plain: GIN (10/8)
    value: 0.2473
    std: 0.0017
    paper_value: 0.2473
    paper_std: 0.0017
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Tonshoff 2023
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 82
    true_value: 0.2473
    true_std: 0.0017
    value_gap_source_arxiv: '2402.10793'
    value_gap_source_title: An end-to-end attention-based approach for learning on
      graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 82
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2473
    sort_std: 0.0017
    is_best: false
  - model: TokenGT
    model_key: tokengt
    model_plain: TokenGT
    value: 0.24888524548573923
    std: 0.0013272721664974406
    paper_value: 0.24888524548573923
    paper_std: 0.0013272721664974406
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Tonshoff 2023
    variant_inference_reason: ''
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 120
    true_value: 0.24888524548573923
    true_std: 0.0013272721664974406
    value_gap_source_arxiv: '2402.10793'
    value_gap_source_title: An end-to-end attention-based approach for learning on
      graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 120
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.24888524548573923
    sort_std: 0.0013272721664974406
    is_best: false
  - model: TokenGT (10/10)
    model_key: tokengt (10/10)
    model_plain: TokenGT (10/10)
    value: 0.24888524548573923
    std: 0.0013272721664974406
    paper_value: 0.24888524548573923
    paper_std: 0.0013272721664974406
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Tonshoff 2023
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 121
    true_value: 0.24888524548573923
    true_std: 0.0013272721664974406
    value_gap_source_arxiv: '2402.10793'
    value_gap_source_title: An end-to-end attention-based approach for learning on
      graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 121
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.24888524548573923
    sort_std: 0.0013272721664974406
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.2509
    std: 0.0014
    paper_value: 0.2509
    paper_std: 0.0014
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Tonshoff 2023
    variant_inference_reason: ''
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
    has_value_note: true
    value_gap: 0.0009000000000000119
    value_note: global 0.2500 within std
    paper_rank: 145
    rank_delta: 13
    rank_delta_abs: 13
    rank_delta_direction: worse
    sort_value: 0.25
    sort_std: 0.0005
    is_best: false
  - model: GPS (8/6)
    model_key: gps (8/6)
    model_plain: GPS (8/6)
    value: 0.2509
    std: 0.0014
    paper_value: 0.2509
    paper_std: 0.0014
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Tonshoff 2023
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 149
    true_value: 0.2509
    true_std: 0.0014
    value_gap_source_arxiv: '2402.10793'
    value_gap_source_title: An end-to-end attention-based approach for learning on
      graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 149
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2509
    sort_std: 0.0014
    is_best: false
  metric: MAE
  higher_is_better: false
- &id006
  dataset: QM9
  is_multi_metric: true
  rows:
  - model: Mace
    model_key: mace
    model_plain: Mace
    metric_values:
    - 0.02
    - null
    metric_stds:
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.22259'
    title: Rotary Position Encodings for Graphs
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    codebase_url: https://github.com/google-research/scenic
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
    sort_value: 0.02
    sort_std: null
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: PST
    model_key: pst
    model_plain: PST
    metric_values:
    - 0.023
    - null
    metric_stds:
    - 0.001
    - null
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
    global_rank: 2
    is_best: false
    sort_value: 0.023
    sort_std: 0.001
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: DropGIN
    model_key: dropgin
    model_plain: DropGIN
    metric_values:
    - 0.02578744427174226
    - 0.16229444581483676
    metric_stds:
    - 0.000867405321348238
    - 0.0017203168654583633
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.02578744427174226
    sort_std: 0.000867405321348238
    true_value: 0.02578744427174226
    true_std: 0.000867405321348238
    paper_value: 0.02578744427174226
    paper_std: 0.000867405321348238
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2402.10793'
    value_gap_source_title: An end-to-end attention-based approach for learning on
      graphs
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 3
  - model: ESA
    model_key: esa
    model_plain: ESA
    metric_values:
    - 0.02578744427174226
    - 0.15244936051398003
    metric_stds:
    - 0.000867405321348238
    - 0.0029945876029935353
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.02578744427174226
    sort_std: 0.000867405321348238
    true_value: 0.02578744427174226
    true_std: 0.000867405321348238
    paper_value: 0.02578744427174226
    paper_std: 0.000867405321348238
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2402.10793'
    value_gap_source_title: An end-to-end attention-based approach for learning on
      graphs
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 4
  - model: SchNet
    model_key: schnet
    model_plain: SchNet
    metric_values:
    - 0.026
    - null
    metric_stds:
    - 0.002
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.002
    arxiv_id: '2509.22259'
    title: Rotary Position Encodings for Graphs
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    codebase_url: https://github.com/google-research/scenic
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    is_best: false
    sort_value: 0.026
    sort_std: 0.002
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: TokenGT
    model_key: tokengt
    model_plain: TokenGT
    metric_values:
    - 0.030389001220464663
    - 0.20003333687782282
    metric_stds:
    - 0.0005953300476479862
    - 0.00828174606274421
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.030389001220464663
    sort_std: 0.0005953300476479862
    true_value: 0.030389001220464663
    true_std: 0.0005953300476479862
    paper_value: 0.030389001220464663
    paper_std: 0.0005953300476479862
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2402.10793'
    value_gap_source_title: An end-to-end attention-based approach for learning on
      graphs
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 7
  - model: PNA
    model_key: pna
    model_plain: PNA
    metric_values:
    - 0.0317492975167588
    - 0.15115694898675025
    metric_stds:
    - 0.0028074830084290074
    - 0.0012178706316662376
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.0317492975167588
    sort_std: 0.0028074830084290074
    true_value: 0.0317492975167588
    true_std: 0.0028074830084290074
    paper_value: 0.0317492975167588
    paper_std: 0.0028074830084290074
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2402.10793'
    value_gap_source_title: An end-to-end attention-based approach for learning on
      graphs
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 8
  - model: GATv2
    model_key: gatv2
    model_plain: GATv2
    metric_values:
    - 0.03219783138040288
    - 0.15725115601797318
    metric_stds:
    - 0.0008736508385477724
    - 0.0023134325943648688
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.03219783138040288
    sort_std: 0.0008736508385477724
    true_value: 0.03219783138040288
    true_std: 0.0008736508385477724
    paper_value: 0.03219783138040288
    paper_std: 0.0008736508385477724
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2402.10793'
    value_gap_source_title: An end-to-end attention-based approach for learning on
      graphs
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 9
  - model: GAT
    model_key: gat
    model_plain: GAT
    metric_values:
    - 0.03290000183733416
    - 0.1594100643906536
    metric_stds:
    - 0.0014504048065470119
    - 0.00274523474824748
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.03290000183733416
    sort_std: 0.0014504048065470119
    true_value: 0.03290000183733416
    true_std: 0.0014504048065470119
    paper_value: 0.03290000183733416
    paper_std: 0.0014504048065470119
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2402.10793'
    value_gap_source_title: An end-to-end attention-based approach for learning on
      graphs
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 10
  - model: GPS
    model_key: gps
    model_plain: GPS
    metric_values:
    - 0.033075999999999994
    - 0.178406
    metric_stds:
    - 0.005936661014408688
    - 0.0020226477696326695
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.033075999999999994
    sort_std: 0.005936661014408688
    true_value: 0.033075999999999994
    true_std: 0.005936661014408688
    paper_value: 0.033075999999999994
    paper_std: 0.005936661014408688
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2402.10793'
    value_gap_source_title: An end-to-end attention-based approach for learning on
      graphs
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 12
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    metric_values:
    - 0.05862095989286895
    - 0.17889551252591157
    metric_stds:
    - 0.03095901400991143
    - 0.008689612096286428
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.05862095989286895
    sort_std: 0.03095901400991143
    true_value: 0.05862095989286895
    true_std: 0.03095901400991143
    paper_value: 0.05862095989286895
    paper_std: 0.03095901400991143
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2402.10793'
    value_gap_source_title: An end-to-end attention-based approach for learning on
      graphs
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 14
  - model: GIN
    model_key: gin
    model_plain: GIN
    metric_values:
    - null
    - 0.16187201431047754
    metric_stds:
    - null
    - 0.0016597907171188395
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.16187201431047754
    sort_std: 0.0016597907171188395
    true_value: null
    true_std: null
    paper_value: 0.16187201431047754
    paper_std: 0.0016597907171188395
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 18
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    metric_values:
    - null
    - 0.161956
    metric_stds:
    - null
    - 0.0015081326201631
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.161956
    sort_std: 0.0015081326201631
    true_value: null
    true_std: null
    paper_value: 0.161956
    paper_std: 0.0015081326201631
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: GCN
    model_key: gcn
    model_plain: GCN
    metric_values:
    - null
    - 0.17144381081131788
    metric_stds:
    - null
    - 0.003676356368918919
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.17144381081131788
    sort_std: 0.003676356368918919
    true_value: null
    true_std: null
    paper_value: 0.17144381081131788
    paper_std: 0.003676356368918919
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: Grph.
    model_key: grph.
    model_plain: Grph.
    metric_values:
    - null
    - 0.19038245203081353
    metric_stds:
    - null
    - 0.005813449852960949
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.19038245203081353
    sort_std: 0.005813449852960949
    true_value: null
    true_std: null
    paper_value: 0.19038245203081353
    paper_std: 0.005813449852960949
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  metrics:
  - MAE
  - RMSE
  primary_metric: MAE
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
    paper_value: 0.017331929457918168
    paper_std: 0.0009253668251948539
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback <= 0.06'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 2
    true_value: 0.017331929457918168
    true_std: 0.0009253668251948539
    value_gap_source_arxiv: '2402.10793'
    value_gap_source_title: An end-to-end attention-based approach for learning on
      graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
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
    value: 0.02
    std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    arxiv_id: '2402.08450'
    title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via Graph
      Products'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.02
    sort_std: 0.001
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.023842
    std: 0.0069779309254248125
    paper_value: 0.023842
    paper_std: 0.0069779309254248125
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback <= 0.06'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 13
    true_value: 0.023842
    true_std: 0.0069779309254248125
    value_gap_source_arxiv: '2402.10793'
    value_gap_source_title: An end-to-end attention-based approach for learning on
      graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.023842
    sort_std: 0.0069779309254248125
    is_best: false
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.036005993400000005
    std: 0.002019173876825075
    paper_value: 0.036005993400000005
    paper_std: 0.002019173876825075
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback <= 0.06'
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
    value_gap: 0.011005993400000004
    value_note: ''
    paper_rank: 37
    rank_delta: 19
    rank_delta_abs: 19
    rank_delta_direction: worse
    sort_value: 0.025
    sort_std: 0.004
    is_best: false
  - model: ESA
    model_key: esa
    model_plain: ESA
    value: 0.02683207359883397
    std: 0.0007197092487851843
    paper_value: 0.02683207359883397
    paper_std: 0.0007197092487851843
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback <= 0.06'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 24
    true_value: 0.02683207359883397
    true_std: 0.0007197092487851843
    value_gap_source_arxiv: '2402.10793'
    value_gap_source_title: An end-to-end attention-based approach for learning on
      graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.02683207359883397
    sort_std: 0.0007197092487851843
    is_best: false
  - model: TokenGT
    model_key: tokengt
    model_plain: TokenGT
    value: 0.0467565117234533
    std: 0.01010544569636761
    paper_value: 0.0467565117234533
    paper_std: 0.01010544569636761
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback <= 0.06'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 40
    true_value: 0.0467565117234533
    true_std: 0.01010544569636761
    value_gap_source_arxiv: '2402.10793'
    value_gap_source_title: An end-to-end attention-based approach for learning on
      graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 40
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.0467565117234533
    sort_std: 0.01010544569636761
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.05727021078890476
    std: 0.006639614126119909
    paper_value: 0.05727021078890476
    paper_std: 0.006639614126119909
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback <= 0.06'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 48
    true_value: 0.05727021078890476
    true_std: 0.006639614126119909
    value_gap_source_arxiv: '2402.10793'
    value_gap_source_title: An end-to-end attention-based approach for learning on
      graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 48
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.05727021078890476
    sort_std: 0.006639614126119909
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.06763977903440473
    std: 0.00412784873186527
    paper_value: 0.06763977903440473
    paper_std: 0.00412784873186527
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'zinc: default subset fallback'
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
    has_value_gap: false
    has_value_note: true
    value_gap: 0.002639779034404724
    value_note: global 0.0650 within std
    paper_rank: 85
    rank_delta: 12
    rank_delta_abs: 12
    rank_delta_direction: worse
    sort_value: 0.065
    sort_std: 0.004
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.06763977903440473
    std: 0.00412784873186527
    paper_value: 0.06763977903440473
    paper_std: 0.00412784873186527
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
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
    has_value_gap: false
    has_value_note: true
    value_gap: 0.002639779034404724
    value_note: global 0.0650 within std
    paper_rank: 85
    rank_delta: 12
    rank_delta_abs: 12
    rank_delta_direction: worse
    sort_value: 0.065
    sort_std: 0.004
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.1517617683115362
    std: 0.02268571908117693
    paper_value: 0.1517617683115362
    paper_std: 0.02268571908117693
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 126
    true_value: 0.076
    true_std: 0.009
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0757617683115362
    value_note: ''
    paper_rank: 221
    rank_delta: 95
    rank_delta_abs: 95
    rank_delta_direction: worse
    sort_value: 0.076
    sort_std: 0.009
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.1517617683115362
    std: 0.02268571908117693
    paper_value: 0.1517617683115362
    paper_std: 0.02268571908117693
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 126
    true_value: 0.076
    true_std: 0.009
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0757617683115362
    value_note: ''
    paper_rank: 221
    rank_delta: 95
    rank_delta_abs: 95
    rank_delta_direction: worse
    sort_value: 0.076
    sort_std: 0.009
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.0776354896230479
    std: 0.005512609666895327
    paper_value: 0.0776354896230479
    paper_std: 0.005512609666895327
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 135
    true_value: 0.0776354896230479
    true_std: 0.005512609666895327
    value_gap_source_arxiv: '2402.10793'
    value_gap_source_title: An end-to-end attention-based approach for learning on
      graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 135
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.0776354896230479
    sort_std: 0.005512609666895327
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.0776354896230479
    std: 0.005512609666895327
    paper_value: 0.0776354896230479
    paper_std: 0.005512609666895327
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 135
    true_value: 0.0776354896230479
    true_std: 0.005512609666895327
    value_gap_source_arxiv: '2402.10793'
    value_gap_source_title: An end-to-end attention-based approach for learning on
      graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 135
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.0776354896230479
    sort_std: 0.005512609666895327
    is_best: false
  - model: GATv2
    model_key: gatv2
    model_plain: GATv2
    value: 0.0794978814609628
    std: 0.003649727726331984
    paper_value: 0.0794978814609628
    paper_std: 0.003649727726331984
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 139
    true_value: 0.0794978814609628
    true_std: 0.003649727726331984
    value_gap_source_arxiv: '2402.10793'
    value_gap_source_title: An end-to-end attention-based approach for learning on
      graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 139
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.0794978814609628
    sort_std: 0.003649727726331984
    is_best: false
  - model: GATv2
    model_key: gatv2
    model_plain: GATv2
    value: 0.0794978814609628
    std: 0.003649727726331984
    paper_value: 0.0794978814609628
    paper_std: 0.003649727726331984
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    global_rank: 139
    true_value: 0.0794978814609628
    true_std: 0.003649727726331984
    value_gap_source_arxiv: '2402.10793'
    value_gap_source_title: An end-to-end attention-based approach for learning on
      graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 139
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.0794978814609628
    sort_std: 0.003649727726331984
    is_best: false
  metric: MAE
  higher_is_better: false
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
- benchmark: Quantum Chemistry
  datasets:
  - *id006
- benchmark: Other Graph Benchmarks
  datasets:
  - *id007
main_figure: /figures/2402.10793/main_figure.png
---

