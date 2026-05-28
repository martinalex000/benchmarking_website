---
title: 'L2G-Net: Local to Global Spectral Graph Neural Networks via Cauchy Factorizations'
arxiv_id: '2602.18837'
source_url: ''
authors: []
published_date: Feb 2026
published_date_iso: 2026-02
abstract: Despite their theoretical advantages, spectral methods based on the graph
  Fourier transform (GFT) are seldom used in graph neural networks (GNNs) due to the
  cost of computing the eigenbasis and the lack of vertex-domain locality in spectral
  representations. As a result, most GNNs rely on local approximations such as polynomial
  Laplacian filters or message passing, which limit their ability to model long-range
  dependencies. In this paper, we introduce a novel factorization of the GFT into
  operators acting on subgraphs, which are then combined via a sequence of Cauchy
  matrices. We use this factorization to propose a new class of spectral GNNs, which
  we term L2G-Net (Local-to-Global Net). Unlike existing spectral methods, which are
  either fully global (when they use the GFT) or local (when they use polynomial filters),
  L2G-Net operates by processing the spectral representations of subgraphs and then
  combining them via structured matrices. Our algorithm avoids full eigendecompositions,
  exploiting graph topology to construct the factorization with quadratic complexity
  in the number of nodes, scaled by the subgraph interface size. Experiments on benchmarks
  stressing non-local dependencies show that L2G-Net outperforms existing spectral
  techniques and is competitive with the state-of-the-art with orders of magnitude
  fewer learnable parameters.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- Ours
mrr: 0.1239
adjusted_mrr: 0.1239
mrr_dataset_count: 4
benchmark_categories:
- Heterophilic Graphs
task_categories:
- node_classification
experiment_scopes:
- node-level
results:
- &id002
  dataset: Amazon-ratings
  rows:
  - model: GENs
    model_key: gens
    model_plain: GENs
    value: 0.5592
    std: 0.0043
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.5592
    sort_std: 0.0043
    is_best: true
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.4909
    std: 0.0063
    paper_value: 0.4909
    paper_std: 0.0063
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 2
    true_value: 0.5554
    true_std: 0.0051
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0645
    value_note: ''
    paper_rank: 53
    rank_delta: 51
    rank_delta_abs: 51
    rank_delta_direction: worse
    sort_value: 0.5554
    sort_std: 0.0051
    is_best: true
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.554
    std: 0.0021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.554
    sort_std: 0.0021
    is_best: true
  - model: Polynormer
    model_key: polynormer
    model_plain: Polynormer
    value: 0.5481
    std: 0.0049
    paper_value: 0.5481
    paper_std: 0.0049
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 4
    true_value: 0.5496
    true_std: 0.0222
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0014999999999999458
    value_note: global 0.5496 within std
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5496
    sort_std: 0.0222
    is_best: true
  - model: NeuralWalker
    model_key: neuralwalker
    model_plain: NeuralWalker
    value: 0.5458
    std: 0.0036
    metric: Accuracy
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
    global_rank: 5
    sort_value: 0.5458
    sort_std: 0.0036
    is_best: false
  - model: CO-GNN(\mu, \mu)
    model_key: co-gnn($\mu$, $\mu$)
    model_plain: CO-GNN(\mu, \mu)
    value: 0.5417
    std: 0.0037
    paper_value: 0.5417
    paper_std: 0.0037
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 8
    true_value: 0.5417
    true_std: 0.0037
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5417
    sort_std: 0.0037
    is_best: false
  - model: GMN
    model_key: gmn
    model_plain: GMN
    value: 0.5407
    std: 0.0031
    paper_value: 0.5407
    paper_std: 0.0031
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 11
    true_value: 0.5407
    true_std: 0.0031
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5407
    sort_std: 0.0031
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.487
    std: 0.0063
    paper_value: 0.487
    paper_std: 0.0063
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 17
    true_value: 0.538
    true_std: 0.0
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.051000000000000045
    value_note: ''
    paper_rank: 58
    rank_delta: 41
    rank_delta_abs: 41
    rank_delta_direction: worse
    sort_value: 0.538
    sort_std: 0.0
    is_best: false
  - model: MP-SSM
    model_key: mp-ssm
    model_plain: MP-SSM
    value: 0.5365
    std: 0.0071
    paper_value: 0.5365
    paper_std: 0.0071
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 19
    true_value: 0.5365
    true_std: 0.0071
    value_gap_source_arxiv: '2602.18837'
    value_gap_source_title: 'L2G-Net: Local to Global Spectral Graph Neural Networks
      via Cauchy Factorizations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5365
    sort_std: 0.0071
    is_best: false
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.5363
    std: 0.0039
    paper_value: 0.5363
    paper_std: 0.0039
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 20
    true_value: 0.5363
    true_std: 0.0039
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5363
    sort_std: 0.0039
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.5351
    std: 0.0046
    paper_value: 0.5351
    paper_std: 0.0046
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 22
    true_value: 0.5351
    true_std: 0.0046
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5351
    sort_std: 0.0046
    is_best: false
  - model: GRAMA
    model_key: grama
    model_plain: GRAMA
    value: 0.5348
    std: 0.0062
    paper_value: 0.5348
    paper_std: 0.0062
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 23
    true_value: 0.5348
    true_std: 0.0062
    value_gap_source_arxiv: '2602.18837'
    value_gap_source_title: 'L2G-Net: Local to Global Spectral Graph Neural Networks
      via Cauchy Factorizations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5348
    sort_std: 0.0062
    is_best: false
  - model: Ours
    model_key: ours
    model_plain: Ours
    value: 0.5341
    std: 0.0134
    paper_value: 0.5341
    paper_std: 0.0134
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 24
    true_value: 0.5341
    true_std: 0.0134
    value_gap_source_arxiv: '2602.18837'
    value_gap_source_title: 'L2G-Net: Local to Global Spectral Graph Neural Networks
      via Cauchy Factorizations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5341
    sort_std: 0.0134
    is_best: false
  - model: Stable-ChebNet
    model_key: stable-chebnet
    model_plain: Stable-ChebNet
    value: 0.5315
    std: 0.0021
    paper_value: 0.5315
    paper_std: 0.0021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 26
    true_value: 0.5315
    true_std: 0.0021
    value_gap_source_arxiv: '2602.18837'
    value_gap_source_title: 'L2G-Net: Local to Global Spectral Graph Neural Networks
      via Cauchy Factorizations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5315
    sort_std: 0.0021
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.531
    std: 0.0042
    paper_value: 0.531
    paper_std: 0.0042
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 29
    true_value: 0.531
    true_std: 0.0042
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.531
    sort_std: 0.0042
    is_best: false
  - model: FSGNN
    model_key: fsgnn
    model_plain: FSGNN
    value: 0.5274
    std: 0.0083
    paper_value: 0.5274
    paper_std: 0.0083
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 33
    true_value: 0.5274
    true_std: 0.0083
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5274
    sort_std: 0.0083
    is_best: false
  - model: GAT-sep
    model_key: gat-sep
    model_plain: GAT-sep
    value: 0.5218
    std: 0.008
    paper_value: 0.5218
    paper_std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 34
    true_value: 0.527
    true_std: 0.0062
    value_gap_source_arxiv: '2505.23185'
    value_gap_source_title: Improving the Effective Receptive Field of Message-Passing
      Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.005199999999999982
    value_note: global 0.5270 within std
    paper_rank: 36
    rank_delta: 2
    rank_delta_abs: 2
    rank_delta_direction: worse
    sort_value: 0.527
    sort_std: 0.0062
    is_best: false
  - model: CO-GNN(\Sigma, \Sigma)
    model_key: co-gnn($\sigma$, $\sigma$)
    model_plain: CO-GNN(\Sigma, \Sigma)
    value: 0.5128
    std: 0.0056
    paper_value: 0.5128
    paper_std: 0.0056
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 40
    true_value: 0.5128
    true_std: 0.0056
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 40
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5128
    sort_std: 0.0056
    is_best: false
  - model: Nagphormer
    model_key: nagphormer
    model_plain: Nagphormer
    value: 0.5126
    std: 0.0072
    paper_value: 0.5126
    paper_std: 0.0072
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 42
    true_value: 0.5126
    true_std: 0.0072
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 42
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5126
    sort_std: 0.0072
    is_best: false
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.5117
    std: 0.0066
    paper_value: 0.5117
    paper_std: 0.0066
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 43
    true_value: 0.5117
    true_std: 0.0066
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 43
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5117
    sort_std: 0.0066
    is_best: false
  - model: Gated + RWSE
    model_key: gated + rwse
    model_plain: Gated + RWSE
    value: 0.4858
    std: 0.0041
    paper_value: 0.4858
    paper_std: 0.0041
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 60
    true_value: 0.4858
    true_std: 0.0041
    value_gap_source_arxiv: '2602.18837'
    value_gap_source_title: 'L2G-Net: Local to Global Spectral Graph Neural Networks
      via Cauchy Factorizations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 60
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4858
    sort_std: 0.0041
    is_best: false
  - model: GPSGCN+Performer (LapPE)
    model_key: gpsgcn+performer (lappe)
    model_plain: GPSGCN+Performer (LapPE)
    value: 0.482
    std: 0.0067
    paper_value: 0.482
    paper_std: 0.0067
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 63
    true_value: 0.482
    true_std: 0.0067
    value_gap_source_arxiv: '2602.18837'
    value_gap_source_title: 'L2G-Net: Local to Global Spectral Graph Neural Networks
      via Cauchy Factorizations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 63
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.482
    sort_std: 0.0067
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.43
    std: 0.0032
    paper_value: 0.43
    paper_std: 0.0032
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 64
    true_value: 0.481
    true_std: 0.0071
    value_gap_source_arxiv: '2602.17893'
    value_gap_source_title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs
      with Context Gating State Space Models'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05099999999999999
    value_note: ''
    paper_rank: 84
    rank_delta: 20
    rank_delta_abs: 20
    rank_delta_direction: worse
    sort_value: 0.481
    sort_std: 0.0071
    is_best: false
  - model: GPS₃₂GCN+Performer (RWSE)
    model_key: gps₃₂gcn+performer (rwse)
    model_plain: GPS₃₂GCN+Performer (RWSE)
    value: 0.4808
    std: 0.0085
    paper_value: 0.4808
    paper_std: 0.0085
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 65
    true_value: 0.4808
    true_std: 0.0085
    value_gap_source_arxiv: '2505.23185'
    value_gap_source_title: Improving the Effective Receptive Field of Message-Passing
      Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 65
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4808
    sort_std: 0.0085
    is_best: false
  - model: R-GCN (RWSE)
    model_key: r-gcn (rwse)
    model_plain: R-GCN (RWSE)
    value: 0.464
    std: 0.0055
    paper_value: 0.464
    paper_std: 0.0055
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 72
    true_value: 0.464
    true_std: 0.0055
    value_gap_source_arxiv: '2602.18837'
    value_gap_source_title: 'L2G-Net: Local to Global Spectral Graph Neural Networks
      via Cauchy Factorizations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 72
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.464
    sort_std: 0.0055
    is_best: false
  - model: GBK-GNN
    model_key: gbk-gnn
    model_plain: GBK-GNN
    value: 0.4598
    std: 0.0071
    paper_value: 0.4598
    paper_std: 0.0071
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 73
    true_value: 0.4598
    true_std: 0.0071
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 73
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4598
    sort_std: 0.0071
    is_best: false
  - model: GPS + Mamba
    model_key: gps + mamba
    model_plain: GPS + Mamba
    value: 0.4513
    std: 0.0097
    paper_value: 0.4513
    paper_std: 0.0097
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 74
    true_value: 0.45130000000000003
    true_std: 0.0097
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 74
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.45130000000000003
    sort_std: 0.0097
    is_best: false
  - model: GAT (LapPE)
    model_key: gat (lappe)
    model_plain: GAT (LapPE)
    value: 0.449
    std: 0.0073
    paper_value: 0.449
    paper_std: 0.0073
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 75
    true_value: 0.449
    true_std: 0.0073
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 75
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.449
    sort_std: 0.0073
    is_best: false
  - model: GPR-GNN
    model_key: gpr-gnn
    model_plain: GPR-GNN
    value: 0.4488
    std: 0.0034
    paper_value: 0.4488
    paper_std: 0.0034
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 76
    true_value: 0.4488
    true_std: 0.0034
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 76
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4488
    sort_std: 0.0034
    is_best: false
  - model: GOAT
    model_key: goat
    model_plain: GOAT
    value: 0.4461
    std: 0.005
    paper_value: 0.4461
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 79
    true_value: 0.4461
    true_std: 0.005
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 79
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4461
    sort_std: 0.005
    is_best: false
  - model: GCN+LapPE
    model_key: gcn+lappe
    model_plain: GCN+LapPE
    value: 0.4435
    std: 0.0036
    paper_value: 0.4435
    paper_std: 0.0036
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 80
    true_value: 0.4435
    true_std: 0.0036
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 80
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4435
    sort_std: 0.0036
    is_best: false
  - model: FAGCN
    model_key: fagcn
    model_plain: FAGCN
    value: 0.4412
    std: 0.003
    paper_value: 0.4412
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 81
    true_value: 0.4412
    true_std: 0.003
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 81
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4412
    sort_std: 0.003
    is_best: false
  - model: JacobiConv
    model_key: jacobiconv
    model_plain: JacobiConv
    value: 0.4355
    std: 0.0048
    paper_value: 0.4355
    paper_std: 0.0048
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 83
    true_value: 0.4355
    true_std: 0.0048
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 83
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4355
    sort_std: 0.0048
    is_best: false
  - model: CPGNN
    model_key: cpgnn
    model_plain: CPGNN
    value: 0.3979
    std: 0.0077
    paper_value: 0.3979
    paper_std: 0.0077
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 91
    true_value: 0.3979
    true_std: 0.0077
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 91
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3979
    sort_std: 0.0077
    is_best: false
  - model: GLoGNN
    model_key: glognn
    model_plain: GLoGNN
    value: 0.3689
    std: 0.0014
    paper_value: 0.3689
    paper_std: 0.0014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 93
    true_value: 0.3689
    true_std: 0.0014
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 93
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3689
    sort_std: 0.0014
    is_best: false
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.3647
    std: 0.0023
    paper_value: 0.3647
    paper_std: 0.0023
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 94
    true_value: 0.3647
    true_std: 0.0023
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 94
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3647
    sort_std: 0.0023
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id003
  dataset: Minesweeper
  rows:
  - model: CSNN
    model_key: csnn
    model_plain: CSNN
    value: 0.9906999999999999
    std: 0.0025
    metric: ROC-AUC
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
    global_rank: 1
    sort_value: 0.9906999999999999
    sort_std: 0.0025
    is_best: true
  - model: BuNN
    model_key: bunn
    model_plain: BuNN
    value: 0.9899
    std: 0.0016
    metric: ROC-AUC
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
    global_rank: 2
    sort_value: 0.9899
    sort_std: 0.0016
    is_best: true
  - model: Tango<sub>GPS</sub>
    model_key: tango\textsubscript{gps}
    model_plain: TangoGPS
    value: 0.9839
    std: 0.0054
    metric: ROC-AUC
    higher_is_better: true
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
    global_rank: 3
    sort_value: 0.9839
    sort_std: 0.0054
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.8975
    std: 0.0052
    paper_value: 0.8975
    paper_std: 0.0052
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 5
    true_value: 0.9786
    true_std: 0.0024
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08110000000000006
    value_note: ''
    paper_rank: 76
    rank_delta: 71
    rank_delta_abs: 71
    rank_delta_direction: worse
    sort_value: 0.9786
    sort_std: 0.0024
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.9201
    std: 0.0068
    paper_value: 0.9201
    paper_std: 0.0068
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 8
    true_value: 0.9773
    true_std: 0.0073
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05719999999999992
    value_note: ''
    paper_rank: 50
    rank_delta: 42
    rank_delta_abs: 42
    rank_delta_direction: worse
    sort_value: 0.9773
    sort_std: 0.0073
    is_best: false
  - model: Ours
    model_key: ours
    model_plain: Ours
    value: 0.975
    std: 0.0026
    paper_value: 0.975
    paper_std: 0.0026
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 9
    true_value: 0.975
    true_std: 0.0026
    value_gap_source_arxiv: '2602.18837'
    value_gap_source_title: 'L2G-Net: Local to Global Spectral Graph Neural Networks
      via Cauchy Factorizations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.975
    sort_std: 0.0026
    is_best: false
  - model: Polynormer
    model_key: polynormer
    model_plain: Polynormer
    value: 0.9746
    std: 0.0036
    paper_value: 0.9746
    paper_std: 0.0036
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 10
    true_value: 0.9749
    true_std: 0.0048
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.00029999999999996696
    value_note: global 0.9749 within std
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9749
    sort_std: 0.0048
    is_best: false
  - model: CO-GNN(\mu, \mu)
    model_key: co-gnn($\mu$, $\mu$)
    model_plain: CO-GNN(\mu, \mu)
    value: 0.9731
    std: 0.0041
    paper_value: 0.9731
    paper_std: 0.0041
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 14
    true_value: 0.9731
    true_std: 0.0041
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9731
    sort_std: 0.0041
    is_best: false
  - model: Stable-ChebNet
    model_key: stable-chebnet
    model_plain: Stable-ChebNet
    value: 0.9571
    std: 0.0226
    paper_value: 0.9571
    paper_std: 0.0226
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 20
    true_value: 0.9571
    true_std: 0.0226
    value_gap_source_arxiv: '2602.18837'
    value_gap_source_title: 'L2G-Net: Local to Global Spectral Graph Neural Networks
      via Cauchy Factorizations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9571
    sort_std: 0.0226
    is_best: false
  - model: MP-SSM
    model_key: mp-ssm
    model_plain: MP-SSM
    value: 0.9533
    std: 0.0072
    paper_value: 0.9533
    paper_std: 0.0072
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 21
    true_value: 0.9533
    true_std: 0.0072
    value_gap_source_arxiv: '2602.18837'
    value_gap_source_title: 'L2G-Net: Local to Global Spectral Graph Neural Networks
      via Cauchy Factorizations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9533
    sort_std: 0.0072
    is_best: false
  - model: GRAMA<sub>GCN</sub>
    model_key: grama$_{gcn}$
    model_plain: GRAMAGCN
    value: 0.9527
    std: 0.0071
    paper_value: 0.9527
    paper_std: 0.0071
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 24
    true_value: 0.9527
    true_std: 0.0071
    value_gap_source_arxiv: '2602.18837'
    value_gap_source_title: 'L2G-Net: Local to Global Spectral Graph Neural Networks
      via Cauchy Factorizations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9527
    sort_std: 0.0071
    is_best: false
  - model: CO-GNN(\Sigma, \Sigma)
    model_key: co-gnn($\sigma$, $\sigma$)
    model_plain: CO-GNN(\Sigma, \Sigma)
    value: 0.9509
    std: 0.0118
    paper_value: 0.9509
    paper_std: 0.0118
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 26
    true_value: 0.9509
    true_std: 0.0118
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9509
    sort_std: 0.0118
    is_best: false
  - model: GCN+LapPE
    model_key: gcn+lappe
    model_plain: GCN+LapPE
    value: 0.9426
    std: 0.0049
    paper_value: 0.9426
    paper_std: 0.0049
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 29
    true_value: 0.9426
    true_std: 0.0049
    value_gap_source_arxiv: '2505.23185'
    value_gap_source_title: Improving the Effective Receptive Field of Message-Passing
      Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9426
    sort_std: 0.0049
    is_best: false
  - model: GAT-sep
    model_key: gat-sep
    model_plain: GAT-sep
    value: 0.9229
    std: 0.0047
    paper_value: 0.9229
    paper_std: 0.0047
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 32
    true_value: 0.9391
    true_std: 0.0035
    value_gap_source_arxiv: '2505.23185'
    value_gap_source_title: Improving the Effective Receptive Field of Message-Passing
      Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.016199999999999992
    value_note: ''
    paper_rank: 48
    rank_delta: 16
    rank_delta_abs: 16
    rank_delta_direction: worse
    sort_value: 0.9391
    sort_std: 0.0035
    is_best: false
  - model: GPSGCN+Performer (LapPE)
    model_key: gpsgcn+performer (lappe)
    model_plain: GPSGCN+Performer (LapPE)
    value: 0.9385
    std: 0.0041
    paper_value: 0.9385
    paper_std: 0.0041
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 34
    true_value: 0.9385
    true_std: 0.0041
    value_gap_source_arxiv: '2602.18837'
    value_gap_source_title: 'L2G-Net: Local to Global Spectral Graph Neural Networks
      via Cauchy Factorizations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 34
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9385
    sort_std: 0.0041
    is_best: false
  - model: R-GCN (RWSE)
    model_key: r-gcn (rwse)
    model_plain: R-GCN (RWSE)
    value: 0.9384
    std: 0.0048
    paper_value: 0.9384
    paper_std: 0.0048
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 37
    true_value: 0.9384
    true_std: 0.0048
    value_gap_source_arxiv: '2602.18837'
    value_gap_source_title: 'L2G-Net: Local to Global Spectral Graph Neural Networks
      via Cauchy Factorizations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 37
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9384
    sort_std: 0.0048
    is_best: false
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.9351
    std: 0.0057
    paper_value: 0.9351
    paper_std: 0.0057
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 39
    true_value: 0.9351
    true_std: 0.0057
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9351
    sort_std: 0.0057
    is_best: false
  - model: GAT (LapPE)
    model_key: gat (lappe)
    model_plain: GAT (LapPE)
    value: 0.935
    std: 0.0054
    paper_value: 0.935
    paper_std: 0.0054
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 40
    true_value: 0.935
    true_std: 0.0054
    value_gap_source_arxiv: '2505.23185'
    value_gap_source_title: Improving the Effective Receptive Field of Message-Passing
      Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 40
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.935
    sort_std: 0.0054
    is_best: false
  - model: GPS₃₂GCN+Performer (RWSE)
    model_key: gps₃₂gcn+performer (rwse)
    model_plain: GPS₃₂GCN+Performer (RWSE)
    value: 0.9288
    std: 0.005
    paper_value: 0.9288
    paper_std: 0.005
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 42
    true_value: 0.9288
    true_std: 0.005
    value_gap_source_arxiv: '2505.23185'
    value_gap_source_title: Improving the Effective Receptive Field of Message-Passing
      Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 42
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9288
    sort_std: 0.005
    is_best: false
  - model: Gated + RWSE
    model_key: gated + rwse
    model_plain: Gated + RWSE
    value: 0.9253
    std: 0.0065
    paper_value: 0.9253
    paper_std: 0.0065
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 48
    true_value: 0.9253
    true_std: 0.0065
    value_gap_source_arxiv: '2602.18837'
    value_gap_source_title: 'L2G-Net: Local to Global Spectral Graph Neural Networks
      via Cauchy Factorizations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 48
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9253
    sort_std: 0.0065
    is_best: false
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.9185
    std: 0.0076
    paper_value: 0.9185
    paper_std: 0.0076
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 52
    true_value: 0.9185
    true_std: 0.0076
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 52
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9185
    sort_std: 0.0076
    is_best: false
  - model: GPSGCN+Transformer (LapPE)
    model_key: gpsgcn+transformer (lappe)
    model_plain: GPSGCN+Transformer (LapPE)
    value: 0.9182
    std: 0.0041
    paper_value: 0.9182
    paper_std: 0.0041
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 53
    true_value: 0.9182
    true_std: 0.0041
    value_gap_source_arxiv: '2602.18837'
    value_gap_source_title: 'L2G-Net: Local to Global Spectral Graph Neural Networks
      via Cauchy Factorizations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 53
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9182
    sort_std: 0.0041
    is_best: false
  - model: GPSGCN+Transformer (RWSE)
    model_key: gpsgcn+transformer (rwse)
    model_plain: GPSGCN+Transformer (RWSE)
    value: 0.9117
    std: 0.0051
    paper_value: 0.9117
    paper_std: 0.0051
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 59
    true_value: 0.9117
    true_std: 0.0051
    value_gap_source_arxiv: '2602.18837'
    value_gap_source_title: 'L2G-Net: Local to Global Spectral Graph Neural Networks
      via Cauchy Factorizations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 59
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9117
    sort_std: 0.0051
    is_best: false
  - model: GMN
    model_key: gmn
    model_plain: GMN
    value: 0.9101
    std: 0.0023
    paper_value: 0.9101
    paper_std: 0.0023
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 63
    true_value: 0.9101
    true_std: 0.0023
    value_gap_source_arxiv: '2402.08678'
    value_gap_source_title: 'Graph Mamba: Towards Learning on Graphs with State Space
      Models'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 63
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9101
    sort_std: 0.0023
    is_best: false
  - model: GBK-GNN
    model_key: gbk-gnn
    model_plain: GBK-GNN
    value: 0.9085
    std: 0.0058
    paper_value: 0.9085
    paper_std: 0.0058
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 65
    true_value: 0.9085
    true_std: 0.0058
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 65
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9085
    sort_std: 0.0058
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.9074
    std: 0.0053
    paper_value: 0.9074
    paper_std: 0.0053
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 67
    true_value: 0.9074
    true_std: 0.0053
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 67
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9074
    sort_std: 0.0053
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.9063
    std: 0.0067
    paper_value: 0.9063
    paper_std: 0.0067
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 68
    true_value: 0.9063
    true_std: 0.0067
    value_gap_source_arxiv: '2505.23185'
    value_gap_source_title: Improving the Effective Receptive Field of Message-Passing
      Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 68
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9063
    sort_std: 0.0067
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.8754
    std: 0.0122
    paper_value: 0.8754
    paper_std: 0.0122
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 69
    true_value: 0.905
    true_std: 0.0016
    value_gap_source_arxiv: '2602.17893'
    value_gap_source_title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs
      with Context Gating State Space Models'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.02960000000000007
    value_note: ''
    paper_rank: 83
    rank_delta: 14
    rank_delta_abs: 14
    rank_delta_direction: worse
    sort_value: 0.905
    sort_std: 0.0016
    is_best: false
  - model: Nagphormer
    model_key: nagphormer
    model_plain: Nagphormer
    value: 0.8419
    std: 0.0066
    paper_value: 0.8419
    paper_std: 0.0066
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 70
    true_value: 0.903
    true_std: 0.0006
    value_gap_source_arxiv: '2602.17893'
    value_gap_source_title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs
      with Context Gating State Space Models'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.06110000000000004
    value_note: ''
    paper_rank: 86
    rank_delta: 16
    rank_delta_abs: 16
    rank_delta_direction: worse
    sort_value: 0.903
    sort_std: 0.0006
    is_best: false
  - model: FSGNN
    model_key: fsgnn
    model_plain: FSGNN
    value: 0.9008
    std: 0.007
    paper_value: 0.9008
    paper_std: 0.007
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 73
    true_value: 0.9008
    true_std: 0.007
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 73
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9008
    sort_std: 0.007
    is_best: false
  - model: GPS + Mamba
    model_key: gps + mamba
    model_plain: GPS + Mamba
    value: 0.8993
    std: 0.0054
    paper_value: 0.8993
    paper_std: 0.0054
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 74
    true_value: 0.8993
    true_std: 0.0054
    value_gap_source_arxiv: '2402.08678'
    value_gap_source_title: 'Graph Mamba: Towards Learning on Graphs with State Space
      Models'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 74
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8993
    sort_std: 0.0054
    is_best: false
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.8971
    std: 0.0031
    paper_value: 0.8971
    paper_std: 0.0031
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 77
    true_value: 0.8971
    true_std: 0.0031
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 77
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8971
    sort_std: 0.0031
    is_best: false
  - model: JacobiConv
    model_key: jacobiconv
    model_plain: JacobiConv
    value: 0.8966
    std: 0.004
    paper_value: 0.8966
    paper_std: 0.004
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 79
    true_value: 0.8966
    true_std: 0.004
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 79
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8966
    sort_std: 0.004
    is_best: false
  - model: FAGCN
    model_key: fagcn
    model_plain: FAGCN
    value: 0.8817
    std: 0.0073
    paper_value: 0.8817
    paper_std: 0.0073
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 82
    true_value: 0.8817
    true_std: 0.0073
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 82
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8817
    sort_std: 0.0073
    is_best: false
  - model: GPR-GNN
    model_key: gpr-gnn
    model_plain: GPR-GNN
    value: 0.8624
    std: 0.0061
    paper_value: 0.8624
    paper_std: 0.0061
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 84
    true_value: 0.8624
    true_std: 0.0061
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 84
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8624
    sort_std: 0.0061
    is_best: false
  - model: GOAT
    model_key: goat
    model_plain: GOAT
    value: 0.8109
    std: 0.0102
    paper_value: 0.8109
    paper_std: 0.0102
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 88
    true_value: 0.8109
    true_std: 0.0102
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 88
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8109
    sort_std: 0.0102
    is_best: false
  - model: CPGNN
    model_key: cpgnn
    model_plain: CPGNN
    value: 0.5203
    std: 0.0546
    paper_value: 0.5203
    paper_std: 0.0546
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 92
    true_value: 0.5203
    true_std: 0.0546
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 92
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5203
    sort_std: 0.0546
    is_best: false
  - model: GLoGNN
    model_key: glognn
    model_plain: GLoGNN
    value: 0.5108
    std: 0.0123
    paper_value: 0.5108
    paper_std: 0.0123
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 93
    true_value: 0.5108
    true_std: 0.0123
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 93
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5108
    sort_std: 0.0123
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id001
  dataset: Roman-empire
  rows:
  - model: NeuralWalker
    model_key: neuralwalker
    model_plain: NeuralWalker
    value: 0.9292
    std: 0.0036
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
    global_rank: 1
    sort_value: 0.9292
    sort_std: 0.0036
    is_best: true
  - model: Polynormer
    model_key: polynormer
    model_plain: Polynormer
    value: 0.9255
    std: 0.003
    paper_value: 0.9255
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 2
    true_value: 0.9266
    true_std: 0.006
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0010999999999999899
    value_note: global 0.9266 within std
    paper_rank: 3
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.9266
    sort_std: 0.006
    is_best: true
  - model: CSNN
    model_key: csnn
    model_plain: CSNN
    value: 0.9262999999999999
    std: 0.005
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
    global_rank: 3
    sort_value: 0.9262999999999999
    sort_std: 0.005
    is_best: true
  - model: GENs
    model_key: gens
    model_plain: GENs
    value: 0.9252
    std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.9252
    sort_std: 0.005
    is_best: true
  - model: Ours
    model_key: ours
    model_plain: Ours
    value: 0.9212
    std: 0.0112
    paper_value: 0.9212
    paper_std: 0.0112
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 5
    true_value: 0.9212
    true_std: 0.0112
    value_gap_source_arxiv: '2602.18837'
    value_gap_source_title: 'L2G-Net: Local to Global Spectral Graph Neural Networks
      via Cauchy Factorizations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9212
    sort_std: 0.0112
    is_best: true
  - model: Stable-ChebNet
    model_key: stable-chebnet
    model_plain: Stable-ChebNet
    value: 0.9203
    std: 0.0085
    paper_value: 0.9203
    paper_std: 0.0085
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 7
    true_value: 0.9203
    true_std: 0.0085
    value_gap_source_arxiv: '2602.18837'
    value_gap_source_title: 'L2G-Net: Local to Global Spectral Graph Neural Networks
      via Cauchy Factorizations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9203
    sort_std: 0.0085
    is_best: true
  - model: CO-GNN(\Sigma, \Sigma)
    model_key: co-gnn($\sigma$, $\sigma$)
    model_plain: CO-GNN(\Sigma, \Sigma)
    value: 0.9157
    std: 0.0032
    paper_value: 0.9157
    paper_std: 0.0032
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 14
    true_value: 0.9157
    true_std: 0.0032
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9157
    sort_std: 0.0032
    is_best: false
  - model: CO-GNN(\mu, \mu)
    model_key: co-gnn($\mu$, $\mu$)
    model_plain: CO-GNN(\mu, \mu)
    value: 0.9137
    std: 0.0035
    paper_value: 0.9137
    paper_std: 0.0035
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 16
    true_value: 0.9137
    true_std: 0.0035
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9137
    sort_std: 0.0035
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7369
    std: 0.0074
    paper_value: 0.7369
    paper_std: 0.0074
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 19
    true_value: 0.9127
    true_std: 0.002
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.17579999999999996
    value_note: ''
    paper_rank: 79
    rank_delta: 60
    rank_delta_abs: 60
    rank_delta_direction: worse
    sort_value: 0.9127
    sort_std: 0.002
    is_best: false
  - model: MP-SSM
    model_key: mp-ssm
    model_plain: MP-SSM
    value: 0.9091
    std: 0.0048
    paper_value: 0.9091
    paper_std: 0.0048
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 24
    true_value: 0.9091
    true_std: 0.0048
    value_gap_source_arxiv: '2602.18837'
    value_gap_source_title: 'L2G-Net: Local to Global Spectral Graph Neural Networks
      via Cauchy Factorizations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9091
    sort_std: 0.0048
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.8087
    std: 0.003
    paper_value: 0.8087
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 26
    true_value: 0.9063
    true_std: 0.0014
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09760000000000002
    value_note: ''
    paper_rank: 67
    rank_delta: 41
    rank_delta_abs: 41
    rank_delta_direction: worse
    sort_value: 0.9063
    sort_std: 0.0014
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.8903
    std: 0.0037
    paper_value: 0.8903
    paper_std: 0.0037
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 31
    true_value: 0.8903
    true_std: 0.0037
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8903
    sort_std: 0.0037
    is_best: false
  - model: GAT-sep
    model_key: gat-sep
    model_plain: GAT-sep
    value: 0.8732
    std: 0.0039
    paper_value: 0.8732
    paper_std: 0.0039
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 32
    true_value: 0.8875
    true_std: 0.0041
    value_gap_source_arxiv: '2505.23185'
    value_gap_source_title: Improving the Effective Receptive Field of Message-Passing
      Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.01429999999999998
    value_note: ''
    paper_rank: 36
    rank_delta: 4
    rank_delta_abs: 4
    rank_delta_direction: worse
    sort_value: 0.8875
    sort_std: 0.0041
    is_best: false
  - model: GRAMA
    model_key: grama
    model_plain: GRAMA
    value: 0.8861
    std: 0.0043
    paper_value: 0.8861
    paper_std: 0.0043
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 33
    true_value: 0.8861
    true_std: 0.0043
    value_gap_source_arxiv: '2602.18837'
    value_gap_source_title: 'L2G-Net: Local to Global Spectral Graph Neural Networks
      via Cauchy Factorizations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8861
    sort_std: 0.0043
    is_best: false
  - model: GMN
    model_key: gmn
    model_plain: GMN
    value: 0.8769
    std: 0.005
    paper_value: 0.8769
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 36
    true_value: 0.8769
    true_std: 0.005
    value_gap_source_arxiv: '2602.18837'
    value_gap_source_title: 'L2G-Net: Local to Global Spectral Graph Neural Networks
      via Cauchy Factorizations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 36
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8769
    sort_std: 0.005
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.82
    std: 0.0061
    paper_value: 0.82
    paper_std: 0.0061
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 38
    true_value: 0.8704000000000001
    true_std: 0.0058
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05040000000000011
    value_note: ''
    paper_rank: 66
    rank_delta: 28
    rank_delta_abs: 28
    rank_delta_direction: worse
    sort_value: 0.8704000000000001
    sort_std: 0.0058
    is_best: false
  - model: Gated + RWSE
    model_key: gated + rwse
    model_plain: Gated + RWSE
    value: 0.8662
    std: 0.0053
    paper_value: 0.8662
    paper_std: 0.0053
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 43
    true_value: 0.8662
    true_std: 0.0053
    value_gap_source_arxiv: '2602.18837'
    value_gap_source_title: 'L2G-Net: Local to Global Spectral Graph Neural Networks
      via Cauchy Factorizations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 43
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8662
    sort_std: 0.0053
    is_best: false
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.8651
    std: 0.0073
    paper_value: 0.8651
    paper_std: 0.0073
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 44
    true_value: 0.8651000000000001
    true_std: 0.0073
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 44
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8651000000000001
    sort_std: 0.0073
    is_best: false
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.8574
    std: 0.0067
    paper_value: 0.8574
    paper_std: 0.0067
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 47
    true_value: 0.8574
    true_std: 0.0067
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 47
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8574
    sort_std: 0.0067
    is_best: false
  - model: R-GCN (RWSE)
    model_key: r-gcn (rwse)
    model_plain: R-GCN (RWSE)
    value: 0.8484
    std: 0.0055
    paper_value: 0.8484
    paper_std: 0.0055
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 52
    true_value: 0.8484
    true_std: 0.0055
    value_gap_source_arxiv: '2602.18837'
    value_gap_source_title: 'L2G-Net: Local to Global Spectral Graph Neural Networks
      via Cauchy Factorizations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 52
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8484
    sort_std: 0.0055
    is_best: false
  - model: GAT (LapPE)
    model_key: gat (lappe)
    model_plain: GAT (LapPE)
    value: 0.848
    std: 0.0046
    paper_value: 0.848
    paper_std: 0.0046
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 53
    true_value: 0.848
    true_std: 0.0046
    value_gap_source_arxiv: '2505.23185'
    value_gap_source_title: Improving the Effective Receptive Field of Message-Passing
      Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 53
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.848
    sort_std: 0.0046
    is_best: false
  - model: GPS₃₂GCN+Performer (RWSE)
    model_key: gps₃₂gcn+performer (rwse)
    model_plain: GPS₃₂GCN+Performer (RWSE)
    value: 0.8472
    std: 0.0065
    paper_value: 0.8472
    paper_std: 0.0065
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 54
    true_value: 0.8472
    true_std: 0.0065
    value_gap_source_arxiv: '2505.23185'
    value_gap_source_title: Improving the Effective Receptive Field of Message-Passing
      Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 54
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8472
    sort_std: 0.0065
    is_best: false
  - model: GPSGCN+Performer (LapPE)
    model_key: gpsgcn+performer (lappe)
    model_plain: GPSGCN+Performer (LapPE)
    value: 0.8396
    std: 0.0053
    paper_value: 0.8396
    paper_std: 0.0053
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 57
    true_value: 0.8396
    true_std: 0.0053
    value_gap_source_arxiv: '2602.18837'
    value_gap_source_title: 'L2G-Net: Local to Global Spectral Graph Neural Networks
      via Cauchy Factorizations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 57
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8396
    sort_std: 0.0053
    is_best: false
  - model: GCN+LapPE
    model_key: gcn+lappe
    model_plain: GCN+LapPE
    value: 0.8337
    std: 0.0055
    paper_value: 0.8337
    paper_std: 0.0055
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 62
    true_value: 0.8337
    true_std: 0.0055
    value_gap_source_arxiv: '2505.23185'
    value_gap_source_title: Improving the Effective Receptive Field of Message-Passing
      Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 62
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8337
    sort_std: 0.0055
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.7446
    std: 0.0054
    paper_value: 0.7446
    paper_std: 0.0054
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 63
    true_value: 0.833
    true_std: 0.0079
    value_gap_source_arxiv: '2602.17893'
    value_gap_source_title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs
      with Context Gating State Space Models'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08839999999999992
    value_note: ''
    paper_rank: 79
    rank_delta: 16
    rank_delta_abs: 16
    rank_delta_direction: worse
    sort_value: 0.833
    sort_std: 0.0079
    is_best: false
  - model: GPS + Mamba
    model_key: gps + mamba
    model_plain: GPS + Mamba
    value: 0.831
    std: 0.0028
    paper_value: 0.831
    paper_std: 0.0028
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 64
    true_value: 0.831
    true_std: 0.0028
    value_gap_source_arxiv: '2602.18837'
    value_gap_source_title: 'L2G-Net: Local to Global Spectral Graph Neural Networks
      via Cauchy Factorizations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 64
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.831
    sort_std: 0.0028
    is_best: false
  - model: Nagphormer
    model_key: nagphormer
    model_plain: Nagphormer
    value: 0.7434
    std: 0.0077
    paper_value: 0.7434
    paper_std: 0.0077
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 72
    true_value: 0.8
    true_std: 0.0043
    value_gap_source_arxiv: '2602.17893'
    value_gap_source_title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs
      with Context Gating State Space Models'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.056600000000000095
    value_note: ''
    paper_rank: 79
    rank_delta: 7
    rank_delta_abs: 7
    rank_delta_direction: worse
    sort_value: 0.8
    sort_std: 0.0043
    is_best: false
  - model: FSGNN
    model_key: fsgnn
    model_plain: FSGNN
    value: 0.7992
    std: 0.0056
    paper_value: 0.7992
    paper_std: 0.0056
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 74
    true_value: 0.7992
    true_std: 0.0056
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 74
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7992
    sort_std: 0.0056
    is_best: false
  - model: GBK-GNN
    model_key: gbk-gnn
    model_plain: GBK-GNN
    value: 0.7457
    std: 0.0047
    paper_value: 0.7457
    paper_std: 0.0047
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 79
    true_value: 0.7457
    true_std: 0.0047
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 79
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7457
    sort_std: 0.0047
    is_best: false
  - model: GOAT
    model_key: goat
    model_plain: GOAT
    value: 0.7159
    std: 0.0125
    paper_value: 0.7159
    paper_std: 0.0125
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 81
    true_value: 0.7159
    true_std: 0.0125
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 81
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7159
    sort_std: 0.0125
    is_best: false
  - model: JacobiConv
    model_key: jacobiconv
    model_plain: JacobiConv
    value: 0.7114
    std: 0.0042
    paper_value: 0.7114
    paper_std: 0.0042
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 82
    true_value: 0.7114
    true_std: 0.0042
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 82
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7114
    sort_std: 0.0042
    is_best: false
  - model: FAGCN
    model_key: fagcn
    model_plain: FAGCN
    value: 0.6522
    std: 0.0056
    paper_value: 0.6522
    paper_std: 0.0056
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 86
    true_value: 0.6522
    true_std: 0.0056
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 86
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6522
    sort_std: 0.0056
    is_best: false
  - model: GPR-GNN
    model_key: gpr-gnn
    model_plain: GPR-GNN
    value: 0.6485
    std: 0.0027
    paper_value: 0.6485
    paper_std: 0.0027
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 87
    true_value: 0.6485
    true_std: 0.0027
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 87
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6485
    sort_std: 0.0027
    is_best: false
  - model: CPGNN
    model_key: cpgnn
    model_plain: CPGNN
    value: 0.6396
    std: 0.0062
    paper_value: 0.6396
    paper_std: 0.0062
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 88
    true_value: 0.6396
    true_std: 0.0062
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 88
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6396
    sort_std: 0.0062
    is_best: false
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.6011
    std: 0.0052
    paper_value: 0.6011
    paper_std: 0.0052
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 89
    true_value: 0.6363
    true_std: 0.023
    value_gap_source_arxiv: '2410.05697'
    value_gap_source_title: 'Diffusing to the Top: Boost Graph Neural Networks with
      Minimal Hyperparameter Tuning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.03520000000000001
    value_note: ''
    paper_rank: 90
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.6363
    sort_std: 0.023
    is_best: false
  - model: GLoGNN
    model_key: glognn
    model_plain: GLoGNN
    value: 0.5963
    std: 0.0069
    paper_value: 0.5963
    paper_std: 0.0069
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 93
    true_value: 0.5963
    true_std: 0.0069
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 93
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5963
    sort_std: 0.0069
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: Tolokers
  rows:
  - model: GRAMA<sub>GCN</sub>
    model_key: grama$_{gcn}$
    model_plain: GRAMAGCN
    value: 0.8623
    std: 0.011
    paper_value: 0.8623
    paper_std: 0.011
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 1
    true_value: 0.8623
    true_std: 0.011
    value_gap_source_arxiv: '2602.18837'
    value_gap_source_title: 'L2G-Net: Local to Global Spectral Graph Neural Networks
      via Cauchy Factorizations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8623
    sort_std: 0.011
    is_best: true
  - model: GRAMA
    model_key: grama
    model_plain: GRAMA
    value: 0.8623
    std: 0.011
    metric: ROC-AUC
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.8623
    sort_std: 0.011
    is_best: true
  - model: Polynormer
    model_key: polynormer
    model_plain: Polynormer
    value: 0.8591
    std: 0.0074
    paper_value: 0.8591
    paper_std: 0.0074
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 3
    true_value: 0.8591
    true_std: 0.0074
    value_gap_source_arxiv: '2406.03386'
    value_gap_source_title: Learning Long Range Dependencies on Graphs via Random
      Walks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8591
    sort_std: 0.0074
    is_best: true
  - model: IM-CO-GNN(μ,μ)
    model_key: im-co-gnn(μ,μ)
    model_plain: IM-CO-GNN(μ,μ)
    value: 0.8577
    std: 0.0105
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: May 29, 2025
    date_display: May 2025
    date_iso: '2025-05-29'
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 4
    sort_value: 0.8577
    sort_std: 0.0105
    is_best: true
  - model: Tango_GPS
    model_key: tango_gps
    model_plain: Tango_GPS
    value: 0.8566
    std: 0.0101
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
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
    global_rank: 5
    sort_value: 0.8566
    sort_std: 0.0101
    is_best: true
  - model: Ours
    model_key: ours
    model_plain: Ours
    value: 0.8557
    std: 0.0061
    paper_value: 0.8557
    paper_std: 0.0061
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 7
    true_value: 0.8557
    true_std: 0.0061
    value_gap_source_arxiv: '2602.18837'
    value_gap_source_title: 'L2G-Net: Local to Global Spectral Graph Neural Networks
      via Cauchy Factorizations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8557
    sort_std: 0.0061
    is_best: true
  - model: Stable-ChebNet
    model_key: stable-chebnet
    model_plain: Stable-ChebNet
    value: 0.8555
    std: 0.0335
    paper_value: 0.8555
    paper_std: 0.0335
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 9
    true_value: 0.8555
    true_std: 0.0335
    value_gap_source_arxiv: '2602.18837'
    value_gap_source_title: 'L2G-Net: Local to Global Spectral Graph Neural Networks
      via Cauchy Factorizations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8555
    sort_std: 0.0335
    is_best: true
  - model: MP-SSM
    model_key: mp-ssm
    model_plain: MP-SSM
    value: 0.8526
    std: 0.0093
    paper_value: 0.8526
    paper_std: 0.0093
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 14
    true_value: 0.8526
    true_std: 0.0093
    value_gap_source_arxiv: '2602.18837'
    value_gap_source_title: 'L2G-Net: Local to Global Spectral Graph Neural Networks
      via Cauchy Factorizations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8526
    sort_std: 0.0093
    is_best: true
  - model: R-GCN (RWSE)
    model_key: r-gcn (rwse)
    model_plain: R-GCN (RWSE)
    value: 0.8511
    std: 0.0077
    paper_value: 0.8511
    paper_std: 0.0077
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 19
    true_value: 0.8511
    true_std: 0.0077
    value_gap_source_arxiv: '2602.18837'
    value_gap_source_title: 'L2G-Net: Local to Global Spectral Graph Neural Networks
      via Cauchy Factorizations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8511
    sort_std: 0.0077
    is_best: true
  - model: Gated + RWSE
    model_key: gated + rwse
    model_plain: Gated + RWSE
    value: 0.8502
    std: 0.0067
    paper_value: 0.8502
    paper_std: 0.0067
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 22
    true_value: 0.8502
    true_std: 0.0067
    value_gap_source_arxiv: '2602.18837'
    value_gap_source_title: 'L2G-Net: Local to Global Spectral Graph Neural Networks
      via Cauchy Factorizations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8502
    sort_std: 0.0067
    is_best: true
  - model: GAT (LapPE)
    model_key: gat (lappe)
    model_plain: GAT (LapPE)
    value: 0.8499
    std: 0.0054
    paper_value: 0.8499
    paper_std: 0.0054
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 23
    true_value: 0.8499
    true_std: 0.0054
    value_gap_source_arxiv: '2505.23185'
    value_gap_source_title: Improving the Effective Receptive Field of Message-Passing
      Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8499
    sort_std: 0.0054
    is_best: true
  - model: GCN+LapPE
    model_key: gcn+lappe
    model_plain: GCN+LapPE
    value: 0.8495
    std: 0.0078
    paper_value: 0.8495
    paper_std: 0.0078
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 24
    true_value: 0.8495
    true_std: 0.0078
    value_gap_source_arxiv: '2505.23185'
    value_gap_source_title: Improving the Effective Receptive Field of Message-Passing
      Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8495
    sort_std: 0.0078
    is_best: true
  - model: GPS₃₂GCN+Performer (RWSE)
    model_key: gps₃₂gcn+performer (rwse)
    model_plain: GPS₃₂GCN+Performer (RWSE)
    value: 0.8481
    std: 0.0086
    paper_value: 0.8481
    paper_std: 0.0086
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 27
    true_value: 0.8481
    true_std: 0.0086
    value_gap_source_arxiv: '2505.23185'
    value_gap_source_title: Improving the Effective Receptive Field of Message-Passing
      Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 27
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8481
    sort_std: 0.0086
    is_best: true
  - model: GPSGCN+Performer (LapPE)
    model_key: gpsgcn+performer (lappe)
    model_plain: GPSGCN+Performer (LapPE)
    value: 0.8472
    std: 0.0077
    paper_value: 0.8472
    paper_std: 0.0077
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 31
    true_value: 0.8472
    true_std: 0.0077
    value_gap_source_arxiv: '2602.18837'
    value_gap_source_title: 'L2G-Net: Local to Global Spectral Graph Neural Networks
      via Cauchy Factorizations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8472
    sort_std: 0.0077
    is_best: true
  - model: GMN
    model_key: gmn
    model_plain: GMN
    value: 0.8452
    std: 0.0021
    paper_value: 0.8452
    paper_std: 0.0021
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 34
    true_value: 0.8452
    true_std: 0.0021
    value_gap_source_arxiv: '2402.08678'
    value_gap_source_title: 'Graph Mamba: Towards Learning on Graphs with State Space
      Models'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 34
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8452
    sort_std: 0.0021
    is_best: false
  - model: CO-GNN(\mu, \mu)
    model_key: co-gnn($\mu$, $\mu$)
    model_plain: CO-GNN(\mu, \mu)
    value: 0.8445
    std: 0.0117
    paper_value: 0.8445
    paper_std: 0.0117
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 37
    true_value: 0.8445
    true_std: 0.0117
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 37
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8445
    sort_std: 0.0117
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.8364
    std: 0.0067
    paper_value: 0.8364
    paper_std: 0.0067
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 44
    true_value: 0.838
    true_std: 0.0034
    value_gap_source_arxiv: '2602.17893'
    value_gap_source_title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs
      with Context Gating State Space Models'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0015999999999999348
    value_note: global 0.8380 within std
    paper_rank: 49
    rank_delta: 5
    rank_delta_abs: 5
    rank_delta_direction: worse
    sort_value: 0.838
    sort_std: 0.0034
    is_best: false
  - model: GAT-sep
    model_key: gat-sep
    model_plain: GAT-sep
    value: 0.8252
    std: 0.0092
    paper_value: 0.8252
    paper_std: 0.0092
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 45
    true_value: 0.8378
    true_std: 0.0043
    value_gap_source_arxiv: '2505.23185'
    value_gap_source_title: Improving the Effective Receptive Field of Message-Passing
      Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.012599999999999945
    value_note: ''
    paper_rank: 58
    rank_delta: 13
    rank_delta_abs: 13
    rank_delta_direction: worse
    sort_value: 0.8378
    sort_std: 0.0043
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.8377
    std: 0.0078
    paper_value: 0.8377
    paper_std: 0.0078
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 46
    true_value: 0.8377
    true_std: 0.0078
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 46
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8377
    sort_std: 0.0078
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.8371
    std: 0.0048
    paper_value: 0.8371
    paper_std: 0.0048
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 47
    true_value: 0.8371
    true_std: 0.0048
    value_gap_source_arxiv: '2505.23185'
    value_gap_source_title: Improving the Effective Receptive Field of Message-Passing
      Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 47
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8371
    sort_std: 0.0048
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.837
    std: 0.0047
    paper_value: 0.837
    paper_std: 0.0047
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 48
    true_value: 0.8370000000000001
    true_std: 0.004699999999999999
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 48
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8370000000000001
    sort_std: 0.004699999999999999
    is_best: false
  - model: GPS + Mamba
    model_key: gps + mamba
    model_plain: GPS + Mamba
    value: 0.837
    std: 0.0105
    paper_value: 0.837
    paper_std: 0.0105
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 49
    true_value: 0.837
    true_std: 0.0105
    value_gap_source_arxiv: '2402.08678'
    value_gap_source_title: 'Graph Mamba: Towards Learning on Graphs with State Space
      Models'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 49
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.837
    sort_std: 0.0105
    is_best: false
  - model: GPSGCN+Transformer (RWSE)
    model_key: gpsgcn+transformer (rwse)
    model_plain: GPSGCN+Transformer (RWSE)
    value: 0.8353
    std: 0.0106
    paper_value: 0.8353
    paper_std: 0.0106
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 50
    true_value: 0.8353
    true_std: 0.0106
    value_gap_source_arxiv: '2602.18837'
    value_gap_source_title: 'L2G-Net: Local to Global Spectral Graph Neural Networks
      via Cauchy Factorizations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 50
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8353
    sort_std: 0.0106
    is_best: false
  - model: GPSGCN+Transformer (LapPE)
    model_key: gpsgcn+transformer (lappe)
    model_plain: GPSGCN+Transformer (LapPE)
    value: 0.8351
    std: 0.0093
    paper_value: 0.8351
    paper_std: 0.0093
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 51
    true_value: 0.8351
    true_std: 0.0093
    value_gap_source_arxiv: '2602.18837'
    value_gap_source_title: 'L2G-Net: Local to Global Spectral Graph Neural Networks
      via Cauchy Factorizations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 51
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8351
    sort_std: 0.0093
    is_best: false
  - model: Nagphormer
    model_key: nagphormer
    model_plain: Nagphormer
    value: 0.7832
    std: 0.0095
    paper_value: 0.7832
    paper_std: 0.0095
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 52
    true_value: 0.834
    true_std: 0.0045
    value_gap_source_arxiv: '2602.17893'
    value_gap_source_title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs
      with Context Gating State Space Models'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.050799999999999956
    value_note: ''
    paper_rank: 68
    rank_delta: 16
    rank_delta_abs: 16
    rank_delta_direction: worse
    sort_value: 0.834
    sort_std: 0.0045
    is_best: false
  - model: CO-GNN(\Sigma, \Sigma)
    model_key: co-gnn($\sigma$, $\sigma$)
    model_plain: CO-GNN(\Sigma, \Sigma)
    value: 0.8336
    std: 0.0089
    paper_value: 0.8336
    paper_std: 0.0089
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 53
    true_value: 0.8336
    true_std: 0.0089
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 53
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8336
    sort_std: 0.0089
    is_best: false
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.8323
    std: 0.0064
    paper_value: 0.8323
    paper_std: 0.0064
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 55
    true_value: 0.8323
    true_std: 0.0064
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 55
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8323
    sort_std: 0.0064
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.7731
    std: 0.0114
    paper_value: 0.7731
    paper_std: 0.0114
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 56
    true_value: 0.832
    true_std: 0.009
    value_gap_source_arxiv: '2602.17893'
    value_gap_source_title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs
      with Context Gating State Space Models'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05889999999999995
    value_note: ''
    paper_rank: 69
    rank_delta: 13
    rank_delta_abs: 13
    rank_delta_direction: worse
    sort_value: 0.832
    sort_std: 0.009
    is_best: false
  - model: GOAT
    model_key: goat
    model_plain: GOAT
    value: 0.8311
    std: 0.0104
    paper_value: 0.8311
    paper_std: 0.0104
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 57
    true_value: 0.8311
    true_std: 0.0104
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 57
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8311
    sort_std: 0.0104
    is_best: false
  - model: FSGNN
    model_key: fsgnn
    model_plain: FSGNN
    value: 0.8276
    std: 0.0061
    paper_value: 0.8276
    paper_std: 0.0061
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 58
    true_value: 0.8276
    true_std: 0.0061
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 58
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8276
    sort_std: 0.0061
    is_best: false
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.8243
    std: 0.0044
    paper_value: 0.8243
    paper_std: 0.0044
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 61
    true_value: 0.8243
    true_std: 0.0044
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 61
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8243
    sort_std: 0.0044
    is_best: false
  - model: GBK-GNN
    model_key: gbk-gnn
    model_plain: GBK-GNN
    value: 0.8101
    std: 0.0067
    paper_value: 0.8101
    paper_std: 0.0067
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 63
    true_value: 0.8101
    true_std: 0.0067
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 63
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8101
    sort_std: 0.0067
    is_best: false
  - model: FAGCN
    model_key: fagcn
    model_plain: FAGCN
    value: 0.7775
    std: 0.0105
    paper_value: 0.7775
    paper_std: 0.0105
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 69
    true_value: 0.7775
    true_std: 0.0105
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 69
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7775
    sort_std: 0.0105
    is_best: false
  - model: GLoGNN
    model_key: glognn
    model_plain: GLoGNN
    value: 0.7339
    std: 0.0117
    paper_value: 0.7339
    paper_std: 0.0117
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 73
    true_value: 0.7339
    true_std: 0.0117
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 73
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7339
    sort_std: 0.0117
    is_best: false
  - model: CPGNN
    model_key: cpgnn
    model_plain: CPGNN
    value: 0.7336
    std: 0.0101
    paper_value: 0.7336
    paper_std: 0.0101
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 74
    true_value: 0.7336
    true_std: 0.0101
    value_gap_source_arxiv: '2505.23185'
    value_gap_source_title: Improving the Effective Receptive Field of Message-Passing
      Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 74
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7336
    sort_std: 0.0101
    is_best: false
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.7335
    std: 0.0101
    paper_value: 0.7335
    paper_std: 0.0101
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 75
    true_value: 0.7335
    true_std: 0.0101
    value_gap_source_arxiv: '2505.23185'
    value_gap_source_title: Improving the Effective Receptive Field of Message-Passing
      Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 75
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7335
    sort_std: 0.0101
    is_best: false
  - model: GPR-GNN
    model_key: gpr-gnn
    model_plain: GPR-GNN
    value: 0.7294
    std: 0.0097
    paper_value: 0.7294
    paper_std: 0.0097
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 76
    true_value: 0.7294
    true_std: 0.0097
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 76
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7294
    sort_std: 0.0097
    is_best: false
  - model: JacobiConv
    model_key: jacobiconv
    model_plain: JacobiConv
    value: 0.6866
    std: 0.0065
    paper_value: 0.6866
    paper_std: 0.0065
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    global_rank: 78
    true_value: 0.6866
    true_std: 0.0065
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 78
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6866
    sort_std: 0.0065
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
results_grouped:
- benchmark: Heterophilic Graphs
  datasets:
  - *id001
  - *id002
  - *id003
  - *id004
single_proposed_model: Ours
main_figure: /figures/2602.18837/main_figure.png
---

