---
title: Revisiting Heterophily For Graph Neural Networks
arxiv_id: '2210.07606'
source_url: ''
authors: []
published_date: Oct 2022
published_date_iso: 2022-10
abstract: Graph Neural Networks (GNNs) extend basic Neural Networks (NNs) by using
  graph structures based on the relational inductive bias (homophily assumption).
  While GNNs have been commonly believed to outperform NNs in real-world tasks, recent
  work has identified a non-trivial set of datasets where their performance compared
  to NNs is not satisfactory. Heterophily has been considered the main cause of this
  empirical observation and numerous works have been put forward to address it. In
  this paper, we first revisit the widely used homophily metrics and point out that
  their consideration of only graph-label consistency is a shortcoming. Then, we study
  heterophily from the perspective of post-aggregation node similarity and define
  new homophily metrics, which are potentially advantageous compared to existing ones.
  Based on this investigation, we prove that some harmful cases of heterophily can
  be effectively addressed by local diversification operation. Then, we propose the
  Adaptive Channel Mixing (ACM), a framework to adaptively exploit aggregation, diversification
  and identity channels node-wisely to extract richer localized information for diverse
  node heterophily situations. ACM is more powerful than the commonly used uni-channel
  framework for node classification tasks on heterophilic graphs and is easy to be
  implemented in baseline GNN layers. When evaluated on $10$ benchmark node classification
  tasks, ACM-augmented baselines consistently achieve significant performance gain,
  exceeding state-of-the-art GNNs on most tasks without incurring significant computational
  burden.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: dataset
proposed_models: []
mrr: null
adjusted_mrr: null
mrr_dataset_count: 0
benchmark_categories:
- Classic
- Heterophilic Graphs
task_categories:
- node_classification
experiment_scopes:
- node-level
results:
- &id006
  dataset: Chameleon
  rows:
  - model: GraphMAE
    model_key: graphmae
    model_plain: GraphMAE
    value: 0.8051
    std: 0.0125
    metric: Accuracy
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
    sort_value: 0.8051
    sort_std: 0.0125
    is_best: true
  - model: MRS-Dir-GCN_DA
    model_key: mrs-dir-gcn_da
    model_plain: MRS-Dir-GCN_DA
    value: 0.8017
    std: 0.0188
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.11504'
    title: Preventing Representational Rank Collapse in MPNNs by Splitting the Computational
      Graph
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.8017
    sort_std: 0.0188
    is_best: true
  - model: Supervised
    model_key: supervised
    model_plain: Supervised
    value: 0.8002
    std: 0.0087
    metric: Accuracy
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
    global_rank: 3
    sort_value: 0.8002
    sort_std: 0.0087
    is_best: true
  - model: ACMII-GCN
    model_key: acmii-gcn
    model_plain: ACMII-GCN
    value: 0.7593
    std: 0.0171
    paper_value: 0.7593
    paper_std: 0.0171
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 9
    true_value: 0.7593
    true_std: 0.0171
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7593
    sort_std: 0.0171
    is_best: false
  - model: ACMGCN
    model_key: acmgcn
    model_plain: ACMGCN
    value: 0.7523
    std: 0.0172
    paper_value: 0.7523
    paper_std: 0.0172
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 12
    true_value: 0.7523
    true_std: 0.0172
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7523
    sort_std: 0.0172
    is_best: false
  - model: ACM-Snowball-2
    model_key: acm-snowball-2
    model_plain: ACM-Snowball-2
    value: 0.6851
    std: 0.017
    paper_value: 0.6851
    paper_std: 0.017
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 28
    true_value: 0.6851
    true_std: 0.017
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 28
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6851
    sort_std: 0.017
    is_best: false
  - model: BernNet
    model_key: bernnet
    model_plain: BernNet
    value: 0.6829
    std: 0.0158
    paper_value: 0.6829
    paper_std: 0.0158
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 31
    true_value: 0.6829
    true_std: 0.0158
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6829
    sort_std: 0.0158
    is_best: false
  - model: GAT+JK
    model_key: gat+jk
    model_plain: GAT+JK
    value: 0.6814
    std: 0.0118
    paper_value: 0.6814
    paper_std: 0.0118
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 32
    true_value: 0.6814
    true_std: 0.0118
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6814
    sort_std: 0.0118
    is_best: false
  - model: ACMII-Snowball-3
    model_key: acmii-snowball-3
    model_plain: ACMII-Snowball-3
    value: 0.6753
    std: 0.0283
    paper_value: 0.6753
    paper_std: 0.0283
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 35
    true_value: 0.6753
    true_std: 0.0283
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6753
    sort_std: 0.0283
    is_best: false
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.6748
    std: 0.004
    paper_value: 0.6748
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 36
    true_value: 0.6748
    true_std: 0.004
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 36
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6748
    sort_std: 0.004
    is_best: false
  - model: Snowball-2
    model_key: snowball-2
    model_plain: Snowball-2
    value: 0.6549
    std: 0.0164
    paper_value: 0.6549
    paper_std: 0.0164
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 42
    true_value: 0.6549
    true_std: 0.0164
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 42
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6549
    sort_std: 0.0164
    is_best: false
  - model: SGC-1
    model_key: sgc-1
    model_plain: SGC-1
    value: 0.6486
    std: 0.0181
    paper_value: 0.6486
    paper_std: 0.0181
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 47
    true_value: 0.6486
    true_std: 0.0181
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 47
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6486
    sort_std: 0.0181
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.6418
    std: 0.0262
    paper_value: 0.6418
    paper_std: 0.0262
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 48
    true_value: 0.6482
    true_std: 0.0224
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.006399999999999961
    value_note: global 0.6482 within std
    paper_rank: 49
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.6482
    sort_std: 0.0224
    is_best: false
  - model: GCN+JK
    model_key: gcn+jk
    model_plain: GCN+JK
    value: 0.6468
    std: 0.0285
    paper_value: 0.6468
    paper_std: 0.0285
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 49
    true_value: 0.6468
    true_std: 0.0285
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 49
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6468
    sort_std: 0.0285
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.639
    std: 0.0046
    paper_value: 0.639
    paper_std: 0.0046
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 50
    true_value: 0.639
    true_std: 0.0046
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 50
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.639
    sort_std: 0.0046
    is_best: false
  - model: GCNII
    model_key: gcnii
    model_plain: GCNII
    value: 0.628
    std: 0.0287
    paper_value: 0.628
    paper_std: 0.0287
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 51
    true_value: 0.6386
    true_std: 0.0304
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.010599999999999943
    value_note: global 0.6386 within std
    paper_rank: 54
    rank_delta: 3
    rank_delta_abs: 3
    rank_delta_direction: worse
    sort_value: 0.6386
    sort_std: 0.0304
    is_best: false
  - model: SGC-2
    model_key: sgc-2
    model_plain: SGC-2
    value: 0.6267
    std: 0.0241
    paper_value: 0.6267
    paper_std: 0.0241
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 55
    true_value: 0.6267
    true_std: 0.0241
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 55
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6267
    sort_std: 0.0241
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.6215
    std: 0.0042
    paper_value: 0.6215
    paper_std: 0.0042
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 60
    true_value: 0.6215
    true_std: 0.0042
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 60
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6215
    sort_std: 0.0042
    is_best: false
  - model: ACM-GCNII
    model_key: acm-gcnii
    model_plain: ACM-GCNII
    value: 0.6166
    std: 0.0229
    paper_value: 0.6166
    paper_std: 0.0229
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 61
    true_value: 0.6166
    true_std: 0.0229
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 61
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6166
    sort_std: 0.0229
    is_best: false
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.523
    std: 0.0048
    paper_value: 0.523
    paper_std: 0.0048
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 64
    true_value: 0.612
    true_std: 0.0428
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08899999999999997
    value_note: ''
    paper_rank: 94
    rank_delta: 30
    rank_delta_abs: 30
    rank_delta_direction: worse
    sort_value: 0.612
    sort_std: 0.0428
    is_best: false
  - model: Geom-GCN
    model_key: geom-gcn
    model_plain: Geom-GCN
    value: 0.609
    std: null
    paper_value: 0.609
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: pei2020geom
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 65
    true_value: 0.609
    true_std: null
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 65
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.609
    sort_std: null
    is_best: false
  - model: MixHop
    model_key: mixhop
    model_plain: MixHop
    value: 0.3628
    std: 0.1022
    paper_value: 0.3628
    paper_std: 0.1022
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 67
    true_value: 0.605
    true_std: 0.0253
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.24219999999999997
    value_note: ''
    paper_rank: 127
    rank_delta: 60
    rank_delta_abs: 60
    rank_delta_direction: worse
    sort_value: 0.605
    sort_std: 0.0253
    is_best: false
  - model: ACM-SGC-1
    model_key: acm-sgc-1
    model_plain: ACM-SGC-1
    value: 0.6048
    std: 0.0155
    paper_value: 0.6048
    paper_std: 0.0155
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 68
    true_value: 0.6048
    true_std: 0.0155
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 68
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6048
    sort_std: 0.0155
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.5191
    std: 0.0056
    paper_value: 0.5191
    paper_std: 0.0056
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 96
    true_value: 0.5191
    true_std: 0.0056
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 96
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5191
    sort_std: 0.0056
    is_best: false
  - model: FAGCN
    model_key: fagcn
    model_plain: FAGCN
    value: 0.4947
    std: 0.0284
    paper_value: 0.4947
    paper_std: 0.0284
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 102
    true_value: 0.4947
    true_std: 0.0284
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 102
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4947
    sort_std: 0.0284
    is_best: false
  - model: MLP-2
    model_key: mlp-2
    model_plain: MLP-2
    value: 0.4672
    std: 0.0046
    paper_value: 0.4672
    paper_std: 0.0046
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 110
    true_value: 0.4672
    true_std: 0.0046
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 110
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4672
    sort_std: 0.0046
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id002
  dataset: CiteSeer
  rows:
  - model: FAGCN
    model_key: fagcn
    model_plain: FAGCN
    value: 0.8237
    std: 0.0146
    paper_value: 0.8237
    paper_std: 0.0146
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 1
    true_value: 0.8237
    true_std: 0.0146
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8237
    sort_std: 0.0146
    is_best: true
  - model: ANS-GT-AnchorGT
    model_key: ans-gt-anchorgt
    model_plain: ANS-GT-AnchorGT
    value: 0.8201
    std: 0.0021
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.03481'
    title: 'AnchorGT: Efficient and Flexible Attention Architecture for Scalable Graph
      Transformers'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.8201
    sort_std: 0.0021
    is_best: true
  - model: GrokFormer
    model_key: grokformer
    model_plain: GrokFormer
    value: 0.8192
    std: 0.0125
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.8192
    sort_std: 0.0125
    is_best: true
  - model: GCNII
    model_key: gcnii
    model_plain: GCNII
    value: 0.8183
    std: 0.0178
    paper_value: 0.8183
    paper_std: 0.0178
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 4
    true_value: 0.8183
    true_std: 0.0178
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8183
    sort_std: 0.0178
    is_best: true
  - model: ACMGCN
    model_key: acmgcn
    model_plain: ACMGCN
    value: 0.8183
    std: 0.0165
    paper_value: 0.8183
    paper_std: 0.0165
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 5
    true_value: 0.8183
    true_std: 0.0165
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8183
    sort_std: 0.0165
    is_best: true
  - model: Polynormer
    model_key: polynormer
    model_plain: Polynormer
    value: 0.818
    std: 0.0076
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 6
    sort_value: 0.818
    sort_std: 0.0076
    is_best: true
  - model: ACMII-GCN
    model_key: acmii-gcn
    model_plain: ACMII-GCN
    value: 0.8176
    std: 0.0125
    paper_value: 0.8176
    paper_std: 0.0125
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 7
    true_value: 0.8176
    true_std: 0.0125
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8176
    sort_std: 0.0125
    is_best: true
  - model: ACM-GCNII
    model_key: acm-gcnii
    model_plain: ACM-GCNII
    value: 0.8169
    std: 0.0125
    paper_value: 0.8169
    paper_std: 0.0125
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 8
    true_value: 0.8169
    true_std: 0.0125
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8169
    sort_std: 0.0125
    is_best: true
  - model: ACM-Snowball-2
    model_key: acm-snowball-2
    model_plain: ACM-Snowball-2
    value: 0.8158
    std: 0.0123
    paper_value: 0.8158
    paper_std: 0.0123
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 9
    true_value: 0.8158
    true_std: 0.0123
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8158
    sort_std: 0.0123
    is_best: true
  - model: ACMII-Snowball-3
    model_key: acmii-snowball-3
    model_plain: ACMII-Snowball-3
    value: 0.8156
    std: 0.0115
    paper_value: 0.8156
    paper_std: 0.0115
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 10
    true_value: 0.8156
    true_std: 0.0115
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8156
    sort_std: 0.0115
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.8139
    std: 0.0123
    paper_value: 0.8139
    paper_std: 0.0123
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 12
    true_value: 0.8139
    true_std: 0.0123
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8139
    sort_std: 0.0123
    is_best: true
  - model: Snowball-2
    model_key: snowball-2
    model_plain: Snowball-2
    value: 0.8093
    std: 0.0132
    paper_value: 0.8093
    paper_std: 0.0132
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 14
    true_value: 0.8093
    true_std: 0.0132
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8093
    sort_std: 0.0132
    is_best: true
  - model: ACM-SGC-1
    model_key: acm-sgc-1
    model_plain: ACM-SGC-1
    value: 0.8093
    std: 0.0116
    paper_value: 0.8093
    paper_std: 0.0116
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 15
    true_value: 0.8093
    true_std: 0.0116
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8093
    sort_std: 0.0116
    is_best: true
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.7997
    std: 0.0069
    paper_value: 0.7997
    paper_std: 0.0069
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 16
    true_value: 0.809
    true_std: 0.0121
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.009300000000000086
    value_note: global 0.8090 within std
    paper_rank: 27
    rank_delta: 11
    rank_delta_abs: 11
    rank_delta_direction: worse
    sort_value: 0.809
    sort_std: 0.0121
    is_best: true
  - model: SGC-2
    model_key: sgc-2
    model_plain: SGC-2
    value: 0.8075
    std: 0.0115
    paper_value: 0.8075
    paper_std: 0.0115
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 18
    true_value: 0.8075
    true_std: 0.0115
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8075
    sort_std: 0.0115
    is_best: true
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.672
    std: 0.0046
    paper_value: 0.672
    paper_std: 0.0046
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 19
    true_value: 0.8052
    true_std: 0.0071
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.13319999999999999
    value_note: ''
    paper_rank: 151
    rank_delta: 132
    rank_delta_abs: 132
    rank_delta_direction: worse
    sort_value: 0.8052
    sort_std: 0.0071
    is_best: true
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.6763
    std: 0.0038
    paper_value: 0.6763
    paper_std: 0.0038
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 25
    true_value: 0.8012
    true_std: 0.0083
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.12490000000000001
    value_note: ''
    paper_rank: 150
    rank_delta: 125
    rank_delta_abs: 125
    rank_delta_direction: worse
    sort_value: 0.8012
    sort_std: 0.0083
    is_best: true
  - model: BernNet
    model_key: bernnet
    model_plain: BernNet
    value: 0.8009
    std: 0.0079
    paper_value: 0.8009
    paper_std: 0.0079
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 27
    true_value: 0.8009
    true_std: 0.0079
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 27
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8009
    sort_std: 0.0079
    is_best: false
  - model: SGC-1
    model_key: sgc-1
    model_plain: SGC-1
    value: 0.7966
    std: 0.0075
    paper_value: 0.7966
    paper_std: 0.0075
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 28
    true_value: 0.7966
    true_std: 0.0075
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 28
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7966
    sort_std: 0.0075
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.6859
    std: 0.003
    paper_value: 0.6859
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 32
    true_value: 0.7933
    true_std: 0.0035
    value_gap_source_arxiv: '2405.03481'
    value_gap_source_title: 'AnchorGT: Efficient and Flexible Attention Architecture
      for Scalable Graph Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10740000000000005
    value_note: ''
    paper_rank: 142
    rank_delta: 110
    rank_delta_abs: 110
    rank_delta_direction: worse
    sort_value: 0.7933
    sort_std: 0.0035
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.7824
    std: 0.003
    paper_value: 0.7824
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 34
    true_value: 0.7923
    true_std: 0.0053
    value_gap_source_arxiv: '2405.03481'
    value_gap_source_title: 'AnchorGT: Efficient and Flexible Attention Architecture
      for Scalable Graph Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.00990000000000002
    value_note: ''
    paper_rank: 36
    rank_delta: 2
    rank_delta_abs: 2
    rank_delta_direction: worse
    sort_value: 0.7923
    sort_std: 0.0053
    is_best: false
  - model: Geom-GCN
    model_key: geom-gcn
    model_plain: Geom-GCN
    value: 0.7799
    std: null
    paper_value: 0.7799
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: pei2020geom
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 37
    true_value: 0.7799
    true_std: null
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 37
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7799
    sort_std: null
    is_best: false
  - model: MixHop
    model_key: mixhop
    model_plain: MixHop
    value: 0.4952
    std: 0.1335
    paper_value: 0.4952
    paper_std: 0.1335
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 63
    true_value: 0.7626000000000001
    true_std: 0.013300000000000001
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.2674000000000001
    value_note: ''
    paper_rank: 213
    rank_delta: 150
    rank_delta_abs: 150
    rank_delta_direction: worse
    sort_value: 0.7626000000000001
    sort_std: 0.013300000000000001
    is_best: false
  - model: MLP-2
    model_key: mlp-2
    model_plain: MLP-2
    value: 0.7625
    std: 0.0028
    paper_value: 0.7625
    paper_std: 0.0028
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 64
    true_value: 0.7625
    true_std: 0.0028
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 64
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7625
    sort_std: 0.0028
    is_best: false
  - model: GCN+JK
    model_key: gcn+jk
    model_plain: GCN+JK
    value: 0.7377
    std: 0.0185
    paper_value: 0.7377
    paper_std: 0.0185
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 94
    true_value: 0.7451000000000001
    true_std: 0.0175
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.007400000000000073
    value_note: global 0.7451 within std
    paper_rank: 103
    rank_delta: 9
    rank_delta_abs: 9
    rank_delta_direction: worse
    sort_value: 0.7451000000000001
    sort_std: 0.0175
    is_best: false
  - model: GAT+JK
    model_key: gat+jk
    model_plain: GAT+JK
    value: 0.7449
    std: 0.0276
    paper_value: 0.7449
    paper_std: 0.0276
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 96
    true_value: 0.7449
    true_std: 0.0276
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 96
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7449
    sort_std: 0.0276
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id001
  dataset: Cora
  rows:
  - model: TRIGON
    model_key: trigon
    model_plain: TRIGON
    value: 0.9170999999999999
    std: 0.0029
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.9170999999999999
    sort_std: 0.0029
    is_best: true
  - model: DR
    model_key: dr
    model_plain: DR
    value: 0.9139
    std: 0.0024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.9139
    sort_std: 0.0024
    is_best: true
  - model: LLP
    model_key: llp
    model_plain: LLP
    value: 0.8995
    std: 0.0201
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
    uses_external_data: null
    is_global_top: true
    global_rank: 3
    sort_value: 0.8995
    sort_std: 0.0201
    is_best: true
  - model: GAT+JK
    model_key: gat+jk
    model_plain: GAT+JK
    value: 0.8952
    std: 0.0043
    paper_value: 0.8952
    paper_std: 0.0043
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 6
    true_value: 0.8952
    true_std: 0.0043
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8952
    sort_std: 0.0043
    is_best: false
  - model: ACMII-GCN
    model_key: acmii-gcn
    model_plain: ACMII-GCN
    value: 0.8947
    std: 0.0108
    paper_value: 0.8947
    paper_std: 0.0108
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 7
    true_value: 0.8947
    true_std: 0.0108
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8947
    sort_std: 0.0108
    is_best: false
  - model: ACMII-Snowball-3
    model_key: acmii-snowball-3
    model_plain: ACMII-Snowball-3
    value: 0.8936
    std: 0.0126
    paper_value: 0.8936
    paper_std: 0.0126
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 9
    true_value: 0.8936
    true_std: 0.0126
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8936
    sort_std: 0.0126
    is_best: false
  - model: ACMGCN
    model_key: acmgcn
    model_plain: ACMGCN
    value: 0.8933
    std: 0.0081
    paper_value: 0.8933
    paper_std: 0.0081
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 11
    true_value: 0.8933
    true_std: 0.0081
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8933
    sort_std: 0.0081
    is_best: false
  - model: Snowball-2
    model_key: snowball-2
    model_plain: Snowball-2
    value: 0.8933
    std: 0.013
    paper_value: 0.8933
    paper_std: 0.013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 10
    true_value: 0.8933
    true_std: 0.013
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8933
    sort_std: 0.013
    is_best: false
  - model: ACM-GCNII
    model_key: acm-gcnii
    model_plain: ACM-GCNII
    value: 0.89
    std: 0.0135
    paper_value: 0.89
    paper_std: 0.0135
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 13
    true_value: 0.89
    true_std: 0.0135
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.89
    sort_std: 0.0135
    is_best: false
  - model: GCNII
    model_key: gcnii
    model_plain: GCNII
    value: 0.8893
    std: 0.0137
    paper_value: 0.8893
    paper_std: 0.0137
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 16
    true_value: 0.8893
    true_std: 0.0137
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8893
    sort_std: 0.0137
    is_best: false
  - model: FAGCN
    model_key: fagcn
    model_plain: FAGCN
    value: 0.8885
    std: 0.0136
    paper_value: 0.8885
    paper_std: 0.0136
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 18
    true_value: 0.8885
    true_std: 0.0136
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8885
    sort_std: 0.0136
    is_best: false
  - model: ACM-Snowball-2
    model_key: acm-snowball-2
    model_plain: ACM-Snowball-2
    value: 0.8883
    std: 0.0149
    paper_value: 0.8883
    paper_std: 0.0149
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 19
    true_value: 0.8883
    true_std: 0.0149
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8883
    sort_std: 0.0149
    is_best: false
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.7951
    std: 0.0036
    paper_value: 0.7951
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
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 25
    true_value: 0.8857
    true_std: 0.0069
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09060000000000001
    value_note: ''
    paper_rank: 158
    rank_delta: 133
    rank_delta_abs: 133
    rank_delta_direction: worse
    sort_value: 0.8857
    sort_std: 0.0069
    is_best: false
  - model: BernNet
    model_key: bernnet
    model_plain: BernNet
    value: 0.8852
    std: 0.0095
    paper_value: 0.8852
    paper_std: 0.0095
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 28
    true_value: 0.8852
    true_std: 0.0095
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 28
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8852
    sort_std: 0.0095
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.767
    std: 0.0042
    paper_value: 0.767
    paper_std: 0.0042
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 31
    true_value: 0.8825
    true_std: 0.0053
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11549999999999994
    value_note: ''
    paper_rank: 183
    rank_delta: 152
    rank_delta_abs: 152
    rank_delta_direction: worse
    sort_value: 0.8825
    sort_std: 0.0053
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.7941
    std: 0.0038
    paper_value: 0.7941
    paper_std: 0.0038
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 39
    true_value: 0.88
    true_std: 0.002
    value_gap_source_arxiv: '2512.14619'
    value_gap_source_title: 'ParaFormer: A Generalized PageRank Graph Transformer
      for Graph Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08589999999999998
    value_note: ''
    paper_rank: 159
    rank_delta: 120
    rank_delta_abs: 120
    rank_delta_direction: worse
    sort_value: 0.88
    sort_std: 0.002
    is_best: false
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.8752
    std: 0.0061
    paper_value: 0.8752
    paper_std: 0.0061
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 41
    true_value: 0.8796
    true_std: 0.0037
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0044000000000000705
    value_note: global 0.8796 within std
    paper_rank: 58
    rank_delta: 17
    rank_delta_abs: 17
    rank_delta_direction: worse
    sort_value: 0.8796
    sort_std: 0.0037
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.8778
    std: 0.0096
    paper_value: 0.8778
    paper_std: 0.0096
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 48
    true_value: 0.8778
    true_std: 0.0096
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 48
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8778
    sort_std: 0.0096
    is_best: false
  - model: ACM-SGC-1
    model_key: acm-sgc-1
    model_plain: ACM-SGC-1
    value: 0.8764
    std: 0.0099
    paper_value: 0.8764
    paper_std: 0.0099
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 54
    true_value: 0.8764
    true_std: 0.0099
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 54
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8764
    sort_std: 0.0099
    is_best: false
  - model: MixHop
    model_key: mixhop
    model_plain: MixHop
    value: 0.6565
    std: 0.1131
    paper_value: 0.6565
    paper_std: 0.1131
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 55
    true_value: 0.8761
    true_std: 0.0085
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.21960000000000002
    value_note: ''
    paper_rank: 272
    rank_delta: 217
    rank_delta_abs: 217
    rank_delta_direction: worse
    sort_value: 0.8761
    sort_std: 0.0085
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.8658
    std: 0.0026
    paper_value: 0.8658
    paper_std: 0.0026
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 71
    true_value: 0.8690000000000001
    true_std: 0.0104
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0032000000000000917
    value_note: global 0.8690 within std
    paper_rank: 82
    rank_delta: 11
    rank_delta_abs: 11
    rank_delta_direction: worse
    sort_value: 0.8690000000000001
    sort_std: 0.0104
    is_best: false
  - model: GCN+JK
    model_key: gcn+jk
    model_plain: GCN+JK
    value: 0.869
    std: 0.0151
    paper_value: 0.869
    paper_std: 0.0151
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 72
    true_value: 0.869
    true_std: 0.0151
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 72
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.869
    sort_std: 0.0151
    is_best: false
  - model: SGC-2
    model_key: sgc-2
    model_plain: SGC-2
    value: 0.8548
    std: 0.0148
    paper_value: 0.8548
    paper_std: 0.0148
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 95
    true_value: 0.8548
    true_std: 0.0148
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 95
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8548
    sort_std: 0.0148
    is_best: false
  - model: Geom-GCN
    model_key: geom-gcn
    model_plain: Geom-GCN
    value: 0.8527
    std: null
    paper_value: 0.8527
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Pei 2020
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 100
    true_value: 0.8527
    true_std: null
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 100
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8527
    sort_std: null
    is_best: false
  - model: SGC-1
    model_key: sgc-1
    model_plain: SGC-1
    value: 0.8512
    std: 0.0164
    paper_value: 0.8512
    paper_std: 0.0164
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 101
    true_value: 0.8512
    true_std: 0.0164
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 101
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8512
    sort_std: 0.0164
    is_best: false
  - model: MLP-2
    model_key: mlp-2
    model_plain: MLP-2
    value: 0.7644
    std: 0.003
    paper_value: 0.7644
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 189
    true_value: 0.7644
    true_std: 0.003
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 189
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7644
    sort_std: 0.003
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id005
  dataset: Cornell
  rows:
  - model: ACM-Snowball-2
    model_key: acm-snowball-2
    model_plain: ACM-Snowball-2
    value: 0.9525
    std: 0.0155
    paper_value: 0.9525
    paper_std: 0.0155
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 1
    true_value: 0.9525
    true_std: 0.0155
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9525
    sort_std: 0.0155
    is_best: true
  - model: ACMGCN
    model_key: acmgcn
    model_plain: ACMGCN
    value: 0.9393
    std: 0.0105
    paper_value: 0.9393
    paper_std: 0.0105
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 2
    true_value: 0.9393
    true_std: 0.0105
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9393
    sort_std: 0.0105
    is_best: true
  - model: ACM-SGC-1
    model_key: acm-sgc-1
    model_plain: ACM-SGC-1
    value: 0.9377
    std: 0.0217
    paper_value: 0.9377
    paper_std: 0.0217
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 3
    true_value: 0.9377
    true_std: 0.0217
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9377
    sort_std: 0.0217
    is_best: true
  - model: ACMII-Snowball-3
    model_key: acmii-snowball-3
    model_plain: ACMII-Snowball-3
    value: 0.9361
    std: 0.0279
    paper_value: 0.9361
    paper_std: 0.0279
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 4
    true_value: 0.9361
    true_std: 0.0279
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9361
    sort_std: 0.0279
    is_best: true
  - model: ACM-GCNII
    model_key: acm-gcnii
    model_plain: ACM-GCNII
    value: 0.9344
    std: 0.0274
    paper_value: 0.9344
    paper_std: 0.0274
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 5
    true_value: 0.9344
    true_std: 0.0274
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9344
    sort_std: 0.0274
    is_best: true
  - model: ACMII-GCN
    model_key: acmii-gcn
    model_plain: ACMII-GCN
    value: 0.9262
    std: 0.0257
    paper_value: 0.9262
    paper_std: 0.0257
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 6
    true_value: 0.9262
    true_std: 0.0257
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9262
    sort_std: 0.0257
    is_best: true
  - model: BernNet
    model_key: bernnet
    model_plain: BernNet
    value: 0.9213
    std: 0.0164
    paper_value: 0.9213
    paper_std: 0.0164
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 7
    true_value: 0.9213
    true_std: 0.0164
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9213
    sort_std: 0.0164
    is_best: true
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.918
    std: 0.0063
    paper_value: 0.918
    paper_std: 0.0063
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 8
    true_value: 0.918
    true_std: 0.0063
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.918
    sort_std: 0.0063
    is_best: false
  - model: DMD++
    model_key: dmd++
    model_plain: DMD++
    value: 0.914
    std: 0.017
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 9
    sort_value: 0.914
    sort_std: 0.017
    is_best: false
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.9136
    std: 0.007
    paper_value: 0.9136
    paper_std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 10
    true_value: 0.9136
    true_std: 0.007
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9136
    sort_std: 0.007
    is_best: false
  - model: MLP-2
    model_key: mlp-2
    model_plain: MLP-2
    value: 0.913
    std: 0.007
    paper_value: 0.913
    paper_std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 12
    true_value: 0.913
    true_std: 0.007
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.913
    sort_std: 0.007
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.913
    std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 11
    sort_value: 0.913
    sort_std: 0.007
    is_best: false
  - model: GCNII
    model_key: gcnii
    model_plain: GCNII
    value: 0.9049
    std: 0.0445
    paper_value: 0.9049
    paper_std: 0.0445
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 13
    true_value: 0.9049
    true_std: 0.0445
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9049
    sort_std: 0.0445
    is_best: true
  - model: DMD-ACMP
    model_key: dmd-acmp
    model_plain: DMD-ACMP
    value: 0.881
    std: 0.024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 14
    sort_value: 0.881
    sort_std: 0.024
    is_best: false
  - model: FAGCN
    model_key: fagcn
    model_plain: FAGCN
    value: 0.8803
    std: 0.056
    paper_value: 0.8803
    paper_std: 0.056
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 15
    true_value: 0.8803
    true_std: 0.056
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8803
    sort_std: 0.056
    is_best: false
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.8623
    std: 0.0471
    paper_value: 0.8623
    paper_std: 0.0471
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 18
    true_value: 0.8623
    true_std: 0.0471
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8623
    sort_std: 0.0471
    is_best: false
  - model: Snowball-2
    model_key: snowball-2
    model_plain: Snowball-2
    value: 0.8295
    std: 0.021
    paper_value: 0.8295
    paper_std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 26
    true_value: 0.8295
    true_std: 0.021
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8295
    sort_std: 0.021
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.8246
    std: 0.0311
    paper_value: 0.8246
    paper_std: 0.0311
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 27
    true_value: 0.8246
    true_std: 0.0311
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 27
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8246
    sort_std: 0.0311
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.7141
    std: 0.0124
    paper_value: 0.7141
    paper_std: 0.0124
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 30
    true_value: 0.8008
    true_std: 0.0296
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0867
    value_note: ''
    paper_rank: 53
    rank_delta: 23
    rank_delta_abs: 23
    rank_delta_direction: worse
    sort_value: 0.8008
    sort_std: 0.0296
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.76
    std: 0.0101
    paper_value: 0.76
    paper_std: 0.0101
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 37
    true_value: 0.76
    true_std: 0.0101
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 37
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.76
    sort_std: 0.0101
    is_best: false
  - model: GAT+JK
    model_key: gat+jk
    model_plain: GAT+JK
    value: 0.7443
    std: 0.1024
    paper_value: 0.7443
    paper_std: 0.1024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 42
    true_value: 0.7443
    true_std: 0.1024
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 42
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7443
    sort_std: 0.1024
    is_best: false
  - model: MixHop
    model_key: mixhop
    model_plain: MixHop
    value: 0.6033
    std: 0.2853
    paper_value: 0.6033
    paper_std: 0.2853
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 45
    true_value: 0.7351000000000001
    true_std: 0.0634
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.13180000000000014
    value_note: global 0.7351 within std
    paper_rank: 99
    rank_delta: 54
    rank_delta_abs: 54
    rank_delta_direction: worse
    sort_value: 0.7351000000000001
    sort_std: 0.0634
    is_best: false
  - model: SGC-2
    model_key: sgc-2
    model_plain: SGC-2
    value: 0.7262
    std: 0.0992
    paper_value: 0.7262
    paper_std: 0.0992
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 49
    true_value: 0.7262
    true_std: 0.0992
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 49
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7262
    sort_std: 0.0992
    is_best: false
  - model: SGC-1
    model_key: sgc-1
    model_plain: SGC-1
    value: 0.7098
    std: 0.0839
    paper_value: 0.7098
    paper_std: 0.0839
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 60
    true_value: 0.7098
    true_std: 0.0839
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 60
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7098
    sort_std: 0.0839
    is_best: false
  - model: GCN+JK
    model_key: gcn+jk
    model_plain: GCN+JK
    value: 0.6656
    std: 0.1382
    paper_value: 0.6656
    paper_std: 0.1382
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 81
    true_value: 0.6656
    true_std: 0.1382
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 81
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6656
    sort_std: 0.1382
    is_best: false
  - model: Geom-GCN
    model_key: geom-gcn
    model_plain: Geom-GCN
    value: 0.6081
    std: null
    paper_value: 0.6081
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: pei2020geom
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 99
    true_value: 0.6081
    true_std: null
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 99
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6081
    sort_std: null
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id008
  dataset: Film
  rows:
  - model: ACMGCN
    model_key: acmgcn
    model_plain: ACMGCN
    value: 0.4186
    std: 0.0148
    paper_value: 0.4186
    paper_std: 0.0148
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 1
    true_value: 0.4186
    true_std: 0.0148
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4186
    sort_std: 0.0148
    is_best: true
  - model: BernNet
    model_key: bernnet
    model_plain: BernNet
    value: 0.4179
    std: 0.0101
    paper_value: 0.4179
    paper_std: 0.0101
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 2
    true_value: 0.4179
    true_std: 0.0101
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4179
    sort_std: 0.0101
    is_best: true
  - model: ACMII-GCN
    model_key: acmii-gcn
    model_plain: ACMII-GCN
    value: 0.4166
    std: 0.0142
    paper_value: 0.4166
    paper_std: 0.0142
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 3
    true_value: 0.4166
    true_std: 0.0142
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4166
    sort_std: 0.0142
    is_best: true
  - model: GCNII
    model_key: gcnii
    model_plain: GCNII
    value: 0.4154
    std: 0.0099
    paper_value: 0.4154
    paper_std: 0.0099
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 4
    true_value: 0.4154
    true_std: 0.0099
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4154
    sort_std: 0.0099
    is_best: true
  - model: ACM-Snowball-2
    model_key: acm-snowball-2
    model_plain: ACM-Snowball-2
    value: 0.414
    std: 0.0123
    paper_value: 0.414
    paper_std: 0.0123
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 5
    true_value: 0.414
    true_std: 0.0123
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.414
    sort_std: 0.0123
    is_best: true
  - model: ACM-GCNII
    model_key: acm-gcnii
    model_plain: ACM-GCNII
    value: 0.4127
    std: 0.0124
    paper_value: 0.4127
    paper_std: 0.0124
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 6
    true_value: 0.4127
    true_std: 0.0124
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4127
    sort_std: 0.0124
    is_best: true
  - model: ACMII-Snowball-3
    model_key: acmii-snowball-3
    model_plain: ACMII-Snowball-3
    value: 0.4031
    std: 0.016
    paper_value: 0.4031
    paper_std: 0.016
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 7
    true_value: 0.4031
    true_std: 0.016
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4031
    sort_std: 0.016
    is_best: true
  - model: ACM-SGC-1
    model_key: acm-sgc-1
    model_plain: ACM-SGC-1
    value: 0.4013
    std: 0.0121
    paper_value: 0.4013
    paper_std: 0.0121
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 8
    true_value: 0.4013
    true_std: 0.0121
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4013
    sort_std: 0.0121
    is_best: true
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.393
    std: 0.0027
    paper_value: 0.393
    paper_std: 0.0027
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 9
    true_value: 0.393
    true_std: 0.0027
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.393
    sort_std: 0.0027
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.3886
    std: 0.0024
    paper_value: 0.3886
    paper_std: 0.0024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 10
    true_value: 0.3886
    true_std: 0.0024
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3886
    sort_std: 0.0024
    is_best: false
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.3885
    std: 0.0117
    paper_value: 0.3885
    paper_std: 0.0117
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 11
    true_value: 0.3885
    true_std: 0.0117
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3885
    sort_std: 0.0117
    is_best: false
  - model: MLP-2
    model_key: mlp-2
    model_plain: MLP-2
    value: 0.3858
    std: 0.0025
    paper_value: 0.3858
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
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 12
    true_value: 0.3858
    true_std: 0.0025
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3858
    sort_std: 0.0025
    is_best: false
  - model: CSNN
    model_key: csnn
    model_plain: CSNN
    value: 0.3803
    std: 0.011200000000000002
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 13
    sort_value: 0.3803
    sort_std: 0.011200000000000002
    is_best: false
  - model: ParaFormer_GCN
    model_key: paraformer_gcn
    model_plain: ParaFormer_GCN
    value: 0.38
    std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.14619'
    title: 'ParaFormer: A Generalized PageRank Graph Transformer for Graph Representation
      Learning'
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 14
    sort_value: 0.38
    sort_std: 0.012
    is_best: false
  - model: O(d)-NSD
    model_key: o(d)-nsd
    model_plain: O(d)-NSD
    value: 0.37810000000000005
    std: 0.0115
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 15
    sort_value: 0.37810000000000005
    sort_std: 0.0115
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.3637
    std: 0.0021
    paper_value: 0.3637
    paper_std: 0.0021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 27
    true_value: 0.3637
    true_std: 0.0021
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 27
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3637
    sort_std: 0.0021
    is_best: false
  - model: Snowball-2
    model_key: snowball-2
    model_plain: Snowball-2
    value: 0.36
    std: 0.0136
    paper_value: 0.36
    paper_std: 0.0136
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 29
    true_value: 0.36
    true_std: 0.0136
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.36
    sort_std: 0.0136
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.3598
    std: 0.0023
    paper_value: 0.3598
    paper_std: 0.0023
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 30
    true_value: 0.3598
    true_std: 0.0023
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 30
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3598
    sort_std: 0.0023
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.3551
    std: 0.0099
    paper_value: 0.3551
    paper_std: 0.0099
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 32
    true_value: 0.3551
    true_std: 0.0099
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3551
    sort_std: 0.0099
    is_best: false
  - model: GAT+JK
    model_key: gat+jk
    model_plain: GAT+JK
    value: 0.3541
    std: 0.0097
    paper_value: 0.3541
    paper_std: 0.0097
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 33
    true_value: 0.3541
    true_std: 0.0097
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3541
    sort_std: 0.0097
    is_best: false
  - model: FAGCN
    model_key: fagcn
    model_plain: FAGCN
    value: 0.3159
    std: 0.0137
    paper_value: 0.3159
    paper_std: 0.0137
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 35
    true_value: 0.34869999999999995
    true_std: 0.0125
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.03279999999999994
    value_note: ''
    paper_rank: 41
    rank_delta: 6
    rank_delta_abs: 6
    rank_delta_direction: worse
    sort_value: 0.34869999999999995
    sort_std: 0.0125
    is_best: false
  - model: MixHop
    model_key: mixhop
    model_plain: MixHop
    value: 0.3313
    std: 0.024
    paper_value: 0.3313
    paper_std: 0.024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 38
    true_value: 0.3313
    true_std: 0.024
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3313
    sort_std: 0.024
    is_best: false
  - model: GCN+JK
    model_key: gcn+jk
    model_plain: GCN+JK
    value: 0.3272
    std: 0.0262
    paper_value: 0.3272
    paper_std: 0.0262
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 39
    true_value: 0.3272
    true_std: 0.0262
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3272
    sort_std: 0.0262
    is_best: false
  - model: Geom-GCN
    model_key: geom-gcn
    model_plain: Geom-GCN
    value: 0.3163
    std: null
    paper_value: 0.3163
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: pei2020geom
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 41
    true_value: 0.3163
    true_std: null
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 41
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3163
    sort_std: null
    is_best: false
  - model: SGC-2
    model_key: sgc-2
    model_plain: SGC-2
    value: 0.2881
    std: 0.0111
    paper_value: 0.2881
    paper_std: 0.0111
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 43
    true_value: 0.2881
    true_std: 0.0111
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 43
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2881
    sort_std: 0.0111
    is_best: false
  - model: SGC-1
    model_key: sgc-1
    model_plain: SGC-1
    value: 0.2526
    std: 0.0118
    paper_value: 0.2526
    paper_std: 0.0118
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 46
    true_value: 0.2526
    true_std: 0.0118
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 46
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2526
    sort_std: 0.0118
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id003
  dataset: PubMed
  rows:
  - model: CO
    model_key: co
    model_plain: CO
    value: 0.9484
    std: 0.0004
    metric: Accuracy
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
    uses_external_data: null
    is_global_top: true
    global_rank: 1
    sort_value: 0.9484
    sort_std: 0.0004
    is_best: true
  - model: HN-1
    model_key: hn-1
    model_plain: HN-1
    value: 0.948
    std: 0.0017
    metric: Accuracy
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
    uses_external_data: null
    is_global_top: true
    global_rank: 2
    sort_value: 0.948
    sort_std: 0.0017
    is_best: true
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.9476
    std: 0.001
    metric: Accuracy
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
    uses_external_data: null
    is_global_top: true
    global_rank: 3
    sort_value: 0.9476
    sort_std: 0.001
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.889
    std: 0.0032
    paper_value: 0.889
    paper_std: 0.0032
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 5
    true_value: 0.9224
    true_std: 0.0123
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.033399999999999985
    value_note: ''
    paper_rank: 45
    rank_delta: 40
    rank_delta_abs: 40
    rank_delta_direction: worse
    sort_value: 0.9224
    sort_std: 0.0123
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.8328
    std: 0.0012
    paper_value: 0.8328
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
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 6
    true_value: 0.9201
    true_std: 0.0024
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08730000000000004
    value_note: ''
    paper_rank: 104
    rank_delta: 98
    rank_delta_abs: 98
    rank_delta_direction: worse
    sort_value: 0.9201
    sort_std: 0.0024
    is_best: false
  - model: ACMII-Snowball-3
    model_key: acmii-snowball-3
    model_plain: ACMII-Snowball-3
    value: 0.9131
    std: 0.006
    paper_value: 0.9131
    paper_std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 9
    true_value: 0.9131
    true_std: 0.006
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9131
    sort_std: 0.006
    is_best: false
  - model: ACM-Snowball-2
    model_key: acm-snowball-2
    model_plain: ACM-Snowball-2
    value: 0.9081
    std: 0.0052
    paper_value: 0.9081
    paper_std: 0.0052
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 10
    true_value: 0.9081
    true_std: 0.0052
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9081
    sort_std: 0.0052
    is_best: false
  - model: ACMII-GCN
    model_key: acmii-gcn
    model_plain: ACMII-GCN
    value: 0.9063
    std: 0.0056
    paper_value: 0.9063
    paper_std: 0.0056
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 12
    true_value: 0.9063
    true_std: 0.0056
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9063
    sort_std: 0.0056
    is_best: false
  - model: ACMGCN
    model_key: acmgcn
    model_plain: ACMGCN
    value: 0.9039
    std: 0.0033
    paper_value: 0.9039
    paper_std: 0.0033
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 14
    true_value: 0.9039
    true_std: 0.0033
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9039
    sort_std: 0.0033
    is_best: false
  - model: ACM-GCNII
    model_key: acm-gcnii
    model_plain: ACM-GCNII
    value: 0.9018
    std: 0.0051
    paper_value: 0.9018
    paper_std: 0.0051
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 17
    true_value: 0.9018
    true_std: 0.0051
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9018
    sort_std: 0.0051
    is_best: false
  - model: GCN+JK
    model_key: gcn+jk
    model_plain: GCN+JK
    value: 0.9009
    std: 0.0068
    paper_value: 0.9009
    paper_std: 0.0068
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 19
    true_value: 0.9009
    true_std: 0.0068
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9009
    sort_std: 0.0068
    is_best: false
  - model: Geom-GCN
    model_key: geom-gcn
    model_plain: Geom-GCN
    value: 0.9005
    std: null
    paper_value: 0.9005
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Chien 2021, Lim 2021
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 20
    true_value: 0.9005
    true_std: null
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9005
    sort_std: null
    is_best: false
  - model: GCNII
    model_key: gcnii
    model_plain: GCNII
    value: 0.8998
    std: 0.0052
    paper_value: 0.8998
    paper_std: 0.0052
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 22
    true_value: 0.8998
    true_std: 0.0052
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8998
    sort_std: 0.0052
    is_best: false
  - model: FAGCN
    model_key: fagcn
    model_plain: FAGCN
    value: 0.8998
    std: 0.0054
    paper_value: 0.8998
    paper_std: 0.0054
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 23
    true_value: 0.8998
    true_std: 0.0054
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8998
    sort_std: 0.0054
    is_best: false
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.8778
    std: 0.0028
    paper_value: 0.8778
    paper_std: 0.0028
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 34
    true_value: 0.895
    true_std: 0.004
    value_gap_source_arxiv: '2512.14619'
    value_gap_source_title: 'ParaFormer: A Generalized PageRank Graph Transformer
      for Graph Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.017199999999999993
    value_note: ''
    paper_rank: 74
    rank_delta: 40
    rank_delta_abs: 40
    rank_delta_direction: worse
    sort_value: 0.895
    sort_std: 0.004
    is_best: false
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.8507
    std: 0.0009
    paper_value: 0.8507
    paper_std: 0.0009
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 37
    true_value: 0.8934
    true_std: 0.0025
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04269999999999996
    value_note: ''
    paper_rank: 100
    rank_delta: 63
    rank_delta_abs: 63
    rank_delta_direction: worse
    sort_value: 0.8934
    sort_std: 0.0025
    is_best: false
  - model: GAT+JK
    model_key: gat+jk
    model_plain: GAT+JK
    value: 0.8915
    std: 0.0087
    paper_value: 0.8915
    paper_std: 0.0087
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 39
    true_value: 0.8915
    true_std: 0.0087
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8915
    sort_std: 0.0087
    is_best: false
  - model: Snowball-2
    model_key: snowball-2
    model_plain: Snowball-2
    value: 0.888
    std: 0.0082
    paper_value: 0.888
    paper_std: 0.0082
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 47
    true_value: 0.888
    true_std: 0.0082
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 47
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.888
    sort_std: 0.0082
    is_best: false
  - model: ACM-SGC-1
    model_key: acm-sgc-1
    model_plain: ACM-SGC-1
    value: 0.8879
    std: 0.005
    paper_value: 0.8879
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 48
    true_value: 0.8879
    true_std: 0.005
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 48
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8879
    sort_std: 0.005
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.8685
    std: 0.0011
    paper_value: 0.8685
    paper_std: 0.0011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 54
    true_value: 0.8864
    true_std: 0.003
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.017899999999999916
    value_note: ''
    paper_rank: 92
    rank_delta: 38
    rank_delta_abs: 38
    rank_delta_direction: worse
    sort_value: 0.8864
    sort_std: 0.003
    is_best: false
  - model: BernNet
    model_key: bernnet
    model_plain: BernNet
    value: 0.8848
    std: 0.0041
    paper_value: 0.8848
    paper_std: 0.0041
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 56
    true_value: 0.8848
    true_std: 0.0041
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 56
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8848
    sort_std: 0.0041
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.8502
    std: 0.0009
    paper_value: 0.8502
    paper_std: 0.0009
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 58
    true_value: 0.8843
    true_std: 0.0015
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.03410000000000002
    value_note: ''
    paper_rank: 100
    rank_delta: 42
    rank_delta_abs: 42
    rank_delta_direction: worse
    sort_value: 0.8843
    sort_std: 0.0015
    is_best: false
  - model: MixHop
    model_key: mixhop
    model_plain: MixHop
    value: 0.8704
    std: 0.041
    paper_value: 0.8704
    paper_std: 0.041
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 90
    true_value: 0.8704
    true_std: 0.041
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 90
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8704
    sort_std: 0.041
    is_best: false
  - model: MLP-2
    model_key: mlp-2
    model_plain: MLP-2
    value: 0.8643
    std: 0.0013
    paper_value: 0.8643
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
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 96
    true_value: 0.8643
    true_std: 0.0013
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 96
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8643
    sort_std: 0.0013
    is_best: false
  - model: SGC-1
    model_key: sgc-1
    model_plain: SGC-1
    value: 0.855
    std: 0.0076
    paper_value: 0.855
    paper_std: 0.0076
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 99
    true_value: 0.855
    true_std: 0.0076
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 99
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.855
    sort_std: 0.0076
    is_best: false
  - model: SGC-2
    model_key: sgc-2
    model_plain: SGC-2
    value: 0.8536
    std: 0.0052
    paper_value: 0.8536
    paper_std: 0.0052
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 100
    true_value: 0.8536
    true_std: 0.0052
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 100
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8536
    sort_std: 0.0052
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id007
  dataset: Squirrel
  rows:
  - model: MRS-Dir-GCN_DA
    model_key: mrs-dir-gcn_da
    model_plain: MRS-Dir-GCN_DA
    value: 0.7601
    std: 0.019
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.11504'
    title: Preventing Representational Rank Collapse in MPNNs by Splitting the Computational
      Graph
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.7601
    sort_std: 0.019
    is_best: true
  - model: Dir-GNN
    model_key: dir-gnn
    model_plain: Dir-GNN
    value: 0.7531
    std: 0.0192
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.11504'
    title: Preventing Representational Rank Collapse in MPNNs by Splitting the Computational
      Graph
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.7531
    sort_std: 0.0192
    is_best: true
  - model: FSGNN
    model_key: fsgnn
    model_plain: FSGNN
    value: 0.741
    std: 0.0189
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.11504'
    title: Preventing Representational Rank Collapse in MPNNs by Splitting the Computational
      Graph
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.741
    sort_std: 0.0189
    is_best: true
  - model: ACMII-GCN
    model_key: acmii-gcn
    model_plain: ACMII-GCN
    value: 0.6998
    std: 0.0153
    paper_value: 0.6998
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
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 8
    true_value: 0.6998
    true_std: 0.0153
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6998
    sort_std: 0.0153
    is_best: false
  - model: ACMGCN
    model_key: acmgcn
    model_plain: ACMGCN
    value: 0.6856
    std: 0.0133
    paper_value: 0.6856
    paper_std: 0.0133
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 10
    true_value: 0.6856
    true_std: 0.0133
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6856
    sort_std: 0.0133
    is_best: false
  - model: ACM-Snowball-2
    model_key: acm-snowball-2
    model_plain: ACM-Snowball-2
    value: 0.5597
    std: 0.0203
    paper_value: 0.5597
    paper_std: 0.0203
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 27
    true_value: 0.5597
    true_std: 0.0203
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 27
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5597
    sort_std: 0.0203
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.4476
    std: 0.0139
    paper_value: 0.4476
    paper_std: 0.0139
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kipf & Welling 2016
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 31
    true_value: 0.5343
    true_std: 0.0201
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0867
    value_note: ''
    paper_rank: 50
    rank_delta: 19
    rank_delta_abs: 19
    rank_delta_direction: worse
    sort_value: 0.5343
    sort_std: 0.0201
    is_best: false
  - model: GCN+JK
    model_key: gcn+jk
    model_plain: GCN+JK
    value: 0.534
    std: 0.019
    paper_value: 0.534
    paper_std: 0.019
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 32
    true_value: 0.534
    true_std: 0.019
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.534
    sort_std: 0.019
    is_best: false
  - model: ACMII-Snowball-3
    model_key: acmii-snowball-3
    model_plain: ACMII-Snowball-3
    value: 0.5231
    std: 0.0157
    paper_value: 0.5231
    paper_std: 0.0157
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 35
    true_value: 0.5231
    true_std: 0.0157
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5231
    sort_std: 0.0157
    is_best: false
  - model: GAT+JK
    model_key: gat+jk
    model_plain: GAT+JK
    value: 0.5228
    std: 0.0361
    paper_value: 0.5228
    paper_std: 0.0361
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 36
    true_value: 0.5228
    true_std: 0.0361
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 36
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5228
    sort_std: 0.0361
    is_best: false
  - model: BernNet
    model_key: bernnet
    model_plain: BernNet
    value: 0.5135
    std: 0.0073
    paper_value: 0.5135
    paper_std: 0.0073
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 38
    true_value: 0.5135
    true_std: 0.0073
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5135
    sort_std: 0.0073
    is_best: false
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.4993
    std: 0.0053
    paper_value: 0.4993
    paper_std: 0.0053
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 41
    true_value: 0.5015
    true_std: 0.0192
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0021999999999999242
    value_note: global 0.5015 within std
    paper_rank: 41
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5015
    sort_std: 0.0192
    is_best: false
  - model: Snowball-2
    model_key: snowball-2
    model_plain: Snowball-2
    value: 0.4825
    std: 0.0094
    paper_value: 0.4825
    paper_std: 0.0094
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 44
    true_value: 0.4825
    true_std: 0.0094
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 44
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4825
    sort_std: 0.0094
    is_best: false
  - model: SGC-1
    model_key: sgc-1
    model_plain: SGC-1
    value: 0.4762
    std: 0.0127
    paper_value: 0.4762
    paper_std: 0.0127
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Wu et al. 2019
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 45
    true_value: 0.4762
    true_std: 0.0127
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 45
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4762
    sort_std: 0.0127
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.4272
    std: 0.0033
    paper_value: 0.4272
    paper_std: 0.0033
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 51
    true_value: 0.4449
    true_std: 0.0088
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.017699999999999994
    value_note: ''
    paper_rank: 62
    rank_delta: 11
    rank_delta_abs: 11
    rank_delta_direction: worse
    sort_value: 0.4449
    sort_std: 0.0088
    is_best: false
  - model: MixHop
    model_key: mixhop
    model_plain: MixHop
    value: 0.2455
    std: 0.026
    paper_value: 0.2455
    paper_std: 0.026
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 54
    true_value: 0.438
    true_std: 0.0148
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1925
    value_note: ''
    paper_rank: 111
    rank_delta: 57
    rank_delta_abs: 57
    rank_delta_direction: worse
    sort_value: 0.438
    sort_std: 0.0148
    is_best: false
  - model: FAGCN
    model_key: fagcn
    model_plain: FAGCN
    value: 0.4224
    std: 0.012
    paper_value: 0.4224
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 67
    true_value: 0.4224
    true_std: 0.012
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 67
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4224
    sort_std: 0.012
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.4126
    std: 0.0026
    paper_value: 0.4126
    paper_std: 0.0026
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 69
    true_value: 0.41609999999999997
    true_std: 0.0074
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0034999999999999476
    value_note: global 0.4161 within std
    paper_rank: 69
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.41609999999999997
    sort_std: 0.0074
    is_best: false
  - model: SGC-2
    model_key: sgc-2
    model_plain: SGC-2
    value: 0.4125
    std: 0.014
    paper_value: 0.4125
    paper_std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 70
    true_value: 0.4125
    true_std: 0.014
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 70
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4125
    sort_std: 0.014
    is_best: false
  - model: ACM-SGC-1
    model_key: acm-sgc-1
    model_plain: ACM-SGC-1
    value: 0.4091
    std: 0.0139
    paper_value: 0.4091
    paper_std: 0.0139
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 72
    true_value: 0.4091
    true_std: 0.0139
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 72
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4091
    sort_std: 0.0139
    is_best: false
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.3039
    std: 0.0122
    paper_value: 0.3039
    paper_std: 0.0122
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 78
    true_value: 0.3953
    true_std: 0.0088
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09139999999999998
    value_note: ''
    paper_rank: 109
    rank_delta: 31
    rank_delta_abs: 31
    rank_delta_direction: worse
    sort_value: 0.3953
    sort_std: 0.0088
    is_best: false
  - model: GCNII
    model_key: gcnii
    model_plain: GCNII
    value: 0.3831
    std: 0.013
    paper_value: 0.3831
    paper_std: 0.013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 83
    true_value: 0.3847
    true_std: 0.0158
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0015999999999999903
    value_note: global 0.3847 within std
    paper_rank: 84
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.3847
    sort_std: 0.0158
    is_best: false
  - model: ACM-GCNII
    model_key: acm-gcnii
    model_plain: ACM-GCNII
    value: 0.3832
    std: 0.015
    paper_value: 0.3832
    paper_std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 84
    true_value: 0.3832
    true_std: 0.015
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 84
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3832
    sort_std: 0.015
    is_best: false
  - model: Geom-GCN
    model_key: geom-gcn
    model_plain: Geom-GCN
    value: 0.3814
    std: null
    paper_value: 0.3814
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Chien et al. 2021
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 85
    true_value: 0.3815
    true_std: 0.0092
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 9.999999999998899e-05
    value_note: global 0.3815 within std
    paper_rank: 85
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3815
    sort_std: 0.0092
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.3477
    std: 0.0034
    paper_value: 0.3477
    paper_std: 0.0034
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 101
    true_value: 0.353
    true_std: 0.019
    value_gap_source_arxiv: '2512.14619'
    value_gap_source_title: 'ParaFormer: A Generalized PageRank Graph Transformer
      for Graph Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.005299999999999971
    value_note: global 0.3530 within std
    paper_rank: 103
    rank_delta: 2
    rank_delta_abs: 2
    rank_delta_direction: worse
    sort_value: 0.353
    sort_std: 0.019
    is_best: false
  - model: MLP-2
    model_key: mlp-2
    model_plain: MLP-2
    value: 0.3128
    std: 0.0027
    paper_value: 0.3128
    paper_std: 0.0027
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 109
    true_value: 0.3128
    true_std: 0.0027
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 109
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3128
    sort_std: 0.0027
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: Texas
  rows:
  - model: ACMGCN
    model_key: acmgcn
    model_plain: ACMGCN
    value: 0.9656
    std: 0.02
    paper_value: 0.9656
    paper_std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 1
    true_value: 0.9656
    true_std: 0.02
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9656
    sort_std: 0.02
    is_best: true
  - model: ACM-Snowball-2
    model_key: acm-snowball-2
    model_plain: ACM-Snowball-2
    value: 0.9574
    std: 0.0222
    paper_value: 0.9574
    paper_std: 0.0222
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 2
    true_value: 0.9574
    true_std: 0.0222
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9574
    sort_std: 0.0222
    is_best: true
  - model: ACMII-GCN
    model_key: acmii-gcn
    model_plain: ACMII-GCN
    value: 0.9475
    std: 0.0291
    paper_value: 0.9475
    paper_std: 0.0291
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 4
    true_value: 0.9475
    true_std: 0.0291
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9475
    sort_std: 0.0291
    is_best: true
  - model: ACMII-Snowball-3
    model_key: acmii-snowball-3
    model_plain: ACMII-Snowball-3
    value: 0.9475
    std: 0.0309
    paper_value: 0.9475
    paper_std: 0.0309
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 3
    true_value: 0.9475
    true_std: 0.0309
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9475
    sort_std: 0.0309
    is_best: true
  - model: GrokFormer
    model_key: grokformer
    model_plain: GrokFormer
    value: 0.9459
    std: 0.0208
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    sort_value: 0.9459
    sort_std: 0.0208
    is_best: true
  - model: GrokFilter
    model_key: grokfilter
    model_plain: GrokFilter
    value: 0.9362
    std: 0.0304
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 6
    sort_value: 0.9362
    sort_std: 0.0304
    is_best: true
  - model: ACM-SGC-1
    model_key: acm-sgc-1
    model_plain: ACM-SGC-1
    value: 0.9344
    std: 0.0254
    paper_value: 0.9344
    paper_std: 0.0254
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 7
    true_value: 0.9344
    true_std: 0.0254
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9344
    sort_std: 0.0254
    is_best: true
  - model: JacobiConv
    model_key: jacobiconv
    model_plain: JacobiConv
    value: 0.9344
    std: 0.0213
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 8
    sort_value: 0.9344
    sort_std: 0.0213
    is_best: true
  - model: ACM-GCNII
    model_key: acm-gcnii
    model_plain: ACM-GCNII
    value: 0.9328
    std: 0.0279
    paper_value: 0.9328
    paper_std: 0.0279
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 9
    true_value: 0.9328
    true_std: 0.0279
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9328
    sort_std: 0.0279
    is_best: true
  - model: BernNet
    model_key: bernnet
    model_plain: BernNet
    value: 0.9312
    std: 0.0065
    paper_value: 0.9312
    paper_std: 0.0065
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: lim2021new
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 10
    true_value: 0.9312
    true_std: 0.0065
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9312
    sort_std: 0.0065
    is_best: false
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.9292
    std: 0.0061
    paper_value: 0.9292
    paper_std: 0.0061
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 11
    true_value: 0.9295
    true_std: 0.0131
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.00029999999999996696
    value_note: global 0.9295 within std
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9295
    sort_std: 0.0131
    is_best: false
  - model: MLP-2
    model_key: mlp-2
    model_plain: MLP-2
    value: 0.9226
    std: 0.0071
    paper_value: 0.9226
    paper_std: 0.0071
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 15
    true_value: 0.9226
    true_std: 0.0071
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9226
    sort_std: 0.0071
    is_best: false
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.859
    std: 0.0353
    paper_value: 0.859
    paper_std: 0.0353
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 17
    true_value: 0.9189
    true_std: 0.0393
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.059900000000000064
    value_note: ''
    paper_rank: 33
    rank_delta: 16
    rank_delta_abs: 16
    rank_delta_direction: worse
    sort_value: 0.9189
    sort_std: 0.0393
    is_best: true
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.9118
    std: 0.007
    paper_value: 0.9118
    paper_std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 19
    true_value: 0.9118
    true_std: 0.007
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9118
    sort_std: 0.007
    is_best: false
  - model: FAGCN
    model_key: fagcn
    model_plain: FAGCN
    value: 0.8885
    std: 0.0439
    paper_value: 0.8885
    paper_std: 0.0439
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 25
    true_value: 0.8885
    true_std: 0.0439
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8885
    sort_std: 0.0439
    is_best: false
  - model: GCNII
    model_key: gcnii
    model_plain: GCNII
    value: 0.8852
    std: 0.0302
    paper_value: 0.8852
    paper_std: 0.0302
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 28
    true_value: 0.8852
    true_std: 0.0302
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 28
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8852
    sort_std: 0.0302
    is_best: false
  - model: SGC-1
    model_key: sgc-1
    model_plain: SGC-1
    value: 0.8328
    std: 0.0543
    paper_value: 0.8328
    paper_std: 0.0543
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 45
    true_value: 0.8328
    true_std: 0.0543
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 45
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8328
    sort_std: 0.0543
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.8311
    std: 0.032
    paper_value: 0.8311
    paper_std: 0.032
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 46
    true_value: 0.8311
    true_std: 0.032
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 46
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8311
    sort_std: 0.032
    is_best: false
  - model: Snowball-2
    model_key: snowball-2
    model_plain: Snowball-2
    value: 0.8311
    std: 0.032
    paper_value: 0.8311
    paper_std: 0.032
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 47
    true_value: 0.8311
    true_std: 0.032
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 47
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8311
    sort_std: 0.032
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.7903
    std: 0.012
    paper_value: 0.7903
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 51
    true_value: 0.8243
    true_std: 0.061399999999999996
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.03400000000000003
    value_note: global 0.8243 within std
    paper_rank: 66
    rank_delta: 15
    rank_delta_abs: 15
    rank_delta_direction: worse
    sort_value: 0.8243
    sort_std: 0.061399999999999996
    is_best: false
  - model: SGC-2
    model_key: sgc-2
    model_plain: SGC-2
    value: 0.8131
    std: 0.033
    paper_value: 0.8131
    paper_std: 0.033
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 58
    true_value: 0.8131
    true_std: 0.033
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 58
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8131
    sort_std: 0.033
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.7887
    std: 0.0086
    paper_value: 0.7887
    paper_std: 0.0086
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 61
    true_value: 0.8082
    true_std: 0.0213
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.019500000000000073
    value_note: global 0.8082 within std
    paper_rank: 67
    rank_delta: 6
    rank_delta_abs: 6
    rank_delta_direction: worse
    sort_value: 0.8082
    sort_std: 0.0213
    is_best: false
  - model: GCN+JK
    model_key: gcn+jk
    model_plain: GCN+JK
    value: 0.8066
    std: 0.0191
    paper_value: 0.8066
    paper_std: 0.0191
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 63
    true_value: 0.8066
    true_std: 0.0191
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 63
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8066
    sort_std: 0.0191
    is_best: false
  - model: MixHop
    model_key: mixhop
    model_plain: MixHop
    value: 0.7639
    std: 0.0766
    paper_value: 0.7639
    paper_std: 0.0766
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 70
    true_value: 0.7784
    true_std: 0.07730000000000001
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.014499999999999957
    value_note: global 0.7784 within std
    paper_rank: 86
    rank_delta: 16
    rank_delta_abs: 16
    rank_delta_direction: worse
    sort_value: 0.7784
    sort_std: 0.07730000000000001
    is_best: false
  - model: GAT+JK
    model_key: gat+jk
    model_plain: GAT+JK
    value: 0.7541
    std: 0.0718
    paper_value: 0.7541
    paper_std: 0.0718
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 89
    true_value: 0.7541
    true_std: 0.0718
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 89
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7541
    sort_std: 0.0718
    is_best: false
  - model: Geom-GCN
    model_key: geom-gcn
    model_plain: Geom-GCN
    value: 0.6757
    std: null
    paper_value: 0.6757
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: pei2020geom
    variant_inference_reason: ''
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    global_rank: 119
    true_value: 0.676
    true_std: null
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.000300000000000078
    value_note: ''
    paper_rank: 119
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.676
    sort_std: null
    is_best: false
  metric: Accuracy
  higher_is_better: true
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
  - *id002
  - *id003
- benchmark: Heterophilic Graphs
  datasets:
  - *id004
  - *id005
  - *id006
  - *id007
  - *id008
main_figure: /figures/2210.07606/main_figure.png
---

