---
title: 'Beyond Message Passing: Neural Graph Pattern Machine'
arxiv_id: '2501.18739'
source_url: ''
authors: []
published_date: Jan 30, 2025
published_date_iso: '2025-01-30'
abstract: 'Graph learning tasks often hinge on identifying key substructure patterns
  -- such as triadic closures in social networks or benzene rings in molecular graphs
  -- that underpin downstream performance. However, most existing graph neural networks
  (GNNs) rely on message passing, which aggregates local neighborhood information
  iteratively and struggles to explicitly capture such fundamental motifs, like triangles,
  k-cliques, and rings. This limitation hinders both expressiveness and long-range
  dependency modeling. In this paper, we introduce the Neural Graph Pattern Machine
  (GPM), a novel framework that bypasses message passing by learning directly from
  graph substructures. GPM efficiently extracts, encodes, and prioritizes task-relevant
  graph patterns, offering greater expressivity and improved ability to capture long-range
  dependencies. Empirical evaluations across four standard tasks -- node classification,
  link prediction, graph classification, and graph regression -- demonstrate that
  GPM outperforms state-of-the-art baselines. Further analysis reveals that GPM exhibits
  strong out-of-distribution generalization, desirable scalability, and enhanced interpretability.
  Code and datasets are available at: https://github.com/Zehong-Wang/GPM.'
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- GPM
- GPM + DANN
- GPM + SSReg
mrr: 0.1581
adjusted_mrr: 0.1581
mrr_dataset_count: 11
benchmark_categories:
- Classic
- Heterophilic Graphs
- TU Dortmund
- GNNBenchmark
- OGB
- LINKX Benchmarks
- PyG Imported Datasets
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
- &id006
  dataset: Amazon-Computers
  rows:
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.9078
    std: 0.0013
    paper_value: 0.9078
    paper_std: 0.0013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: velickovic2018graph
    variant_inference_reason: 'dataset: fuzzy match to amazon-computers (score=90)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 1
    true_value: 0.9409
    true_std: 0.0037
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.03309999999999991
    value_note: ''
    paper_rank: 20
    rank_delta: 19
    rank_delta_abs: 19
    rank_delta_direction: worse
    sort_value: 0.9409
    sort_std: 0.0037
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.8965
    std: 0.0052
    paper_value: 0.8965
    paper_std: 0.0052
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: kipf2017semisupervised
    variant_inference_reason: 'dataset: fuzzy match to amazon-computers (score=90)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 2
    true_value: 0.9399
    true_std: 0.0012
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.043399999999999994
    value_note: ''
    paper_rank: 25
    rank_delta: 23
    rank_delta_abs: 23
    rank_delta_direction: worse
    sort_value: 0.9399
    sort_std: 0.0012
    is_best: true
  - model: Polynormer
    model_key: polynormer
    model_plain: Polynormer
    value: 0.9378
    std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08993'
    title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for Node Classification'
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.9378
    sort_std: 0.001
    is_best: true
  - model: GCN* (-) Dropout
    model_key: gcn* (-) dropout
    model_plain: GCN* (-) Dropout
    value: 0.9378
    std: 0.0026
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08993'
    title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for Node Classification'
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.9378
    sort_std: 0.0026
    is_best: true
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.9325
    std: 0.0014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08993'
    title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for Node Classification'
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    sort_value: 0.9325
    sort_std: 0.0014
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.9163
    std: 0.0018
    paper_value: 0.9163
    paper_std: 0.0018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: chen2024leveraging
    variant_inference_reason: 'dataset: fuzzy match to amazon-computers (score=90)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 8
    true_value: 0.9242
    true_std: 0.0066
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.007900000000000018
    value_note: ''
    paper_rank: 17
    rank_delta: 9
    rank_delta_abs: 9
    rank_delta_direction: worse
    sort_value: 0.9242
    sort_std: 0.0066
    is_best: false
  - model: GOAT
    model_key: goat
    model_plain: GOAT
    value: 0.9096
    std: 0.009
    paper_value: 0.9096
    paper_std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: kong2023goat
    variant_inference_reason: 'dataset: fuzzy match to amazon-computers (score=90)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 9
    true_value: 0.9229
    true_std: 0.0037
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.01330000000000009
    value_note: ''
    paper_rank: 20
    rank_delta: 11
    rank_delta_abs: 11
    rank_delta_direction: worse
    sort_value: 0.9229
    sort_std: 0.0037
    is_best: false
  - model: GPM
    model_key: gpm
    model_plain: GPM
    value: 0.9228
    std: 0.0039
    paper_value: 0.9228
    paper_std: 0.0039
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to amazon-computers (score=90)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 10
    true_value: 0.9228
    true_std: 0.0039
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9228
    sort_std: 0.0039
    is_best: false
  - model: OrderedGNN
    model_key: orderedgnn
    model_plain: OrderedGNN
    value: 0.9203
    std: 0.0013
    paper_value: 0.9203
    paper_std: 0.0013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: song2023ordered
    variant_inference_reason: 'dataset: fuzzy match to amazon-computers (score=90)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 13
    true_value: 0.9203
    true_std: 0.0013
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9203
    sort_std: 0.0013
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.9119
    std: 0.0054
    paper_value: 0.9119
    paper_std: 0.0054
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: rampasek2022recipe
    variant_inference_reason: 'dataset: fuzzy match to amazon-computers (score=90)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 16
    true_value: 0.9179
    true_std: 0.0063
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.006000000000000005
    value_note: global 0.9179 within std
    paper_rank: 18
    rank_delta: 2
    rank_delta_abs: 2
    rank_delta_direction: worse
    sort_value: 0.9179
    sort_std: 0.0063
    is_best: false
  - model: Nagphormer
    model_key: nagphormer
    model_plain: Nagphormer
    value: 0.9122
    std: 0.0014
    paper_value: 0.9122
    paper_std: 0.0014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: chen2023nagphormer
    variant_inference_reason: 'dataset: fuzzy match to amazon-computers (score=90)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 17
    true_value: 0.9169
    true_std: 0.003
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0047000000000000375
    value_note: ''
    paper_rank: 18
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.9169
    sort_std: 0.003
    is_best: false
  - model: VCR-Graphormer
    model_key: vcr-graphormer
    model_plain: VCR-Graphormer
    value: 0.9104
    std: 0.0012
    paper_value: 0.9104
    paper_std: 0.0012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: fu2024vcrgraphormer
    variant_inference_reason: 'dataset: fuzzy match to amazon-computers (score=90)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 19
    true_value: 0.9104
    true_std: 0.0012
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9104
    sort_std: 0.0012
    is_best: false
  - model: RAW-GNN
    model_key: raw-gnn
    model_plain: RAW-GNN
    value: 0.9098
    std: 0.0073
    paper_value: 0.9098
    paper_std: 0.0073
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: jin2022raw
    variant_inference_reason: 'dataset: fuzzy match to amazon-computers (score=90)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 20
    true_value: 0.9098
    true_std: 0.0073
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9098
    sort_std: 0.0073
    is_best: false
  - model: RUM
    model_key: rum
    model_plain: RUM
    value: 0.9062
    std: 0.0024
    paper_value: 0.9062
    paper_std: 0.0024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wang2024nonconvolutional
    variant_inference_reason: 'dataset: fuzzy match to amazon-computers (score=90)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 22
    true_value: 0.9062
    true_std: 0.0024
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9062
    sort_std: 0.0024
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.9018
    std: 0.0017
    paper_value: 0.9018
    paper_std: 0.0017
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: gasteiger2018combining
    variant_inference_reason: 'dataset: fuzzy match to amazon-computers (score=90)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 23
    true_value: 0.9018
    true_std: 0.0017
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9018
    sort_std: 0.0017
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.8983
    std: 0.0016
    paper_value: 0.8983
    paper_std: 0.0016
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: kreuzer2021rethinking
    variant_inference_reason: 'dataset: fuzzy match to amazon-computers (score=90)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 25
    true_value: 0.8983
    true_std: 0.0016
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8983
    sort_std: 0.0016
    is_best: false
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.8932
    std: 0.0029
    paper_value: 0.8932
    paper_std: 0.0029
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: chien2021adaptive
    variant_inference_reason: 'dataset: fuzzy match to amazon-computers (score=90)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 27
    true_value: 0.8932
    true_std: 0.0029
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 27
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8932
    sort_std: 0.0029
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.8698
    std: 0.0062
    paper_value: 0.8698
    paper_std: 0.0062
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu2022nodeformer
    variant_inference_reason: 'dataset: fuzzy match to amazon-computers (score=90)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 31
    true_value: 0.8785
    true_std: 0.0024
    value_gap_source_arxiv: '2512.14619'
    value_gap_source_title: 'ParaFormer: A Generalized PageRank Graph Transformer
      for Graph Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.00869999999999993
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8785
    sort_std: 0.0024
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id016
  dataset: Blog
  rows:
  - model: GPM
    model_key: gpm
    model_plain: GPM
    value: 0.9671
    std: 0.0059
    paper_value: 0.9671
    paper_std: 0.0059
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 1
    true_value: 0.9671
    true_std: 0.0059
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9671
    sort_std: 0.0059
    is_best: true
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.9603
    std: 0.0044
    paper_value: 0.9603
    paper_std: 0.0044
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: chen2024leveraging
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 2
    true_value: 0.9603
    true_std: 0.0044
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9603
    sort_std: 0.0044
    is_best: true
  - model: OrderedGNN
    model_key: orderedgnn
    model_plain: OrderedGNN
    value: 0.959
    std: 0.0044
    paper_value: 0.959
    paper_std: 0.0044
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: song2023ordered
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 3
    true_value: 0.959
    true_std: 0.0044
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.959
    sort_std: 0.0044
    is_best: true
  - model: RAW-GNN
    model_key: raw-gnn
    model_plain: RAW-GNN
    value: 0.9496
    std: 0.007
    paper_value: 0.9496
    paper_std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: jin2022raw
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 4
    true_value: 0.9496
    true_std: 0.007
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9496
    sort_std: 0.007
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.9477
    std: 0.0019
    paper_value: 0.9477
    paper_std: 0.0019
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: gasteiger2018combining
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 5
    true_value: 0.9477
    true_std: 0.0019
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9477
    sort_std: 0.0019
    is_best: false
  - model: Nagphormer
    model_key: nagphormer
    model_plain: Nagphormer
    value: 0.9442
    std: 0.0063
    paper_value: 0.9442
    paper_std: 0.0063
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: chen2023nagphormer
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 6
    true_value: 0.9442
    true_std: 0.0063
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9442
    sort_std: 0.0063
    is_best: false
  - model: GOAT
    model_key: goat
    model_plain: GOAT
    value: 0.944
    std: 0.0008
    paper_value: 0.944
    paper_std: 0.0008
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: kong2023goat
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 7
    true_value: 0.944
    true_std: 0.0008
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.944
    sort_std: 0.0008
    is_best: false
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.9436
    std: 0.0029
    paper_value: 0.9436
    paper_std: 0.0029
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: chien2021adaptive
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 8
    true_value: 0.9436
    true_std: 0.0029
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9436
    sort_std: 0.0029
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.9435
    std: 0.0052
    paper_value: 0.9435
    paper_std: 0.0052
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: rampasek2022recipe
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 9
    true_value: 0.9435
    true_std: 0.0052
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9435
    sort_std: 0.0052
    is_best: false
  - model: RUM
    model_key: rum
    model_plain: RUM
    value: 0.9416
    std: 0.0035
    paper_value: 0.9416
    paper_std: 0.0035
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wang2024nonconvolutional
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 10
    true_value: 0.9416
    true_std: 0.0035
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9416
    sort_std: 0.0035
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.9412
    std: 0.0079
    paper_value: 0.9412
    paper_std: 0.0079
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: kipf2017semisupervised
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 11
    true_value: 0.9412
    true_std: 0.0079
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9412
    sort_std: 0.0079
    is_best: false
  - model: VCR-Graphormer
    model_key: vcr-graphormer
    model_plain: VCR-Graphormer
    value: 0.9392
    std: 0.0037
    paper_value: 0.9392
    paper_std: 0.0037
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: fu2024vcrgraphormer
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 12
    true_value: 0.9392
    true_std: 0.0037
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9392
    sort_std: 0.0037
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.9379
    std: 0.0076
    paper_value: 0.9379
    paper_std: 0.0076
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu2022nodeformer
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 13
    true_value: 0.9379
    true_std: 0.0076
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9379
    sort_std: 0.0076
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.9347
    std: 0.0063
    paper_value: 0.9347
    paper_std: 0.0063
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: velickovic2018graph
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 14
    true_value: 0.9347
    true_std: 0.0063
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9347
    sort_std: 0.0063
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.9021
    std: 0.002
    paper_value: 0.9021
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: kreuzer2021rethinking
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 15
    true_value: 0.9021
    true_std: 0.002
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9021
    sort_std: 0.002
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id009
  dataset: COLLAB
  rows:
  - model: CoCN expanded
    model_key: cocn expanded
    model_plain: CoCN expanded
    value: 0.8722
    std: 0.0013
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
    global_rank: 1
    sort_value: 0.8722
    sort_std: 0.0013
    is_best: true
  - model: nsqure~
    model_key: nsqure~
    model_plain: nsqure~
    value: 0.8672
    std: 0.0162
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
    global_rank: 2
    sort_value: 0.8672
    sort_std: 0.0162
    is_best: true
  - model: CoCN
    model_key: cocn
    model_plain: CoCN
    value: 0.8615
    std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
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
    sort_value: 0.8615
    sort_std: 0.001
    is_best: false
  - model: GMT
    model_key: gmt
    model_plain: GMT
    value: 0.7894
    std: 0.0044
    paper_value: 0.7894
    paper_std: 0.0044
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: baek2021accurate
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 12
    true_value: 0.8074
    true_std: 0.0054
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.018000000000000016
    value_note: ''
    paper_rank: 15
    rank_delta: 3
    rank_delta_abs: 3
    rank_delta_direction: worse
    sort_value: 0.8074
    sort_std: 0.0054
    is_best: false
  - model: GPM
    model_key: gpm
    model_plain: GPM
    value: 0.807
    std: 0.0074
    paper_value: 0.807
    paper_std: 0.0074
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 13
    true_value: 0.807
    true_std: 0.0074
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.807
    sort_std: 0.0074
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.8059
    std: 0.0027
    paper_value: 0.8059
    paper_std: 0.0027
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: xu2018how
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 14
    true_value: 0.8059
    true_std: 0.0027
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8059
    sort_std: 0.0027
    is_best: false
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.7882
    std: 0.0121
    paper_value: 0.7882
    paper_std: 0.0121
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ying2021transformers
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 16
    true_value: 0.7882
    true_std: 0.0121
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7882
    sort_std: 0.0121
    is_best: false
  - model: Graph ViT
    model_key: graph vit
    model_plain: Graph ViT
    value: 0.7879
    std: 0.0074
    paper_value: 0.7879
    paper_std: 0.0074
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: he2023generalization
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 17
    true_value: 0.7879
    true_std: 0.0074
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7879
    sort_std: 0.0074
    is_best: false
  - model: SAT
    model_key: sat
    model_plain: SAT
    value: 0.7835
    std: 0.0085
    paper_value: 0.7835
    paper_std: 0.0085
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: chen2022structure
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 20
    true_value: 0.7835
    true_std: 0.0085
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7835
    sort_std: 0.0085
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.7741
    std: 0.0056
    paper_value: 0.7741
    paper_std: 0.0056
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: rampasek2022recipe
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 26
    true_value: 0.7741
    true_std: 0.0056
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7741
    sort_std: 0.0056
    is_best: false
  - model: GNN (a)
    model_key: gnn (a)
    model_plain: GNN (a)
    value: 0.7735
    std: 0.0093
    paper_value: 0.7735
    paper_std: 0.0093
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: zhao2022from
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 27
    true_value: 0.7735
    true_std: 0.0093
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 27
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7735
    sort_std: 0.0093
    is_best: false
  - model: AgentNet
    model_key: agentnet
    model_plain: AgentNet
    value: 0.773
    std: 0.0198
    paper_value: 0.773
    paper_std: 0.0198
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: martinkus2023agentbased
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 28
    true_value: 0.773
    true_std: 0.0198
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 28
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.773
    sort_std: 0.0198
    is_best: false
  - model: CRaWl
    model_key: crawl
    model_plain: CRaWl
    value: 0.7717
    std: 0.0078
    paper_value: 0.7717
    paper_std: 0.0078
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: tonshoff2023walking
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 31
    true_value: 0.7717
    true_std: 0.0078
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7717
    sort_std: 0.0078
    is_best: false
  - model: RUM
    model_key: rum
    model_plain: RUM
    value: 0.755
    std: 0.0058
    paper_value: 0.755
    paper_std: 0.0058
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wang2024nonconvolutional
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 34
    true_value: 0.755
    true_std: 0.0058
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 34
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.755
    sort_std: 0.0058
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.7473
    std: 0.0109
    paper_value: 0.7473
    paper_std: 0.0109
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: corso2020principal
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 39
    true_value: 0.7473
    true_std: 0.0109
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7473
    sort_std: 0.0109
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.7445
    std: 0.0246
    paper_value: 0.7445
    paper_std: 0.0246
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: kreuzer2021rethinking
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 40
    true_value: 0.7445
    true_std: 0.0246
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 40
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7445
    sort_std: 0.0246
    is_best: false
  - model: AWE
    model_key: awe
    model_plain: AWE
    value: 0.7393
    std: 0.0194
    paper_value: 0.7393
    paper_std: 0.0194
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ivanov2018anonymous
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 44
    true_value: 0.7393
    true_std: 0.0194
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 44
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7393
    sort_std: 0.0194
    is_best: false
  - model: DGK
    model_key: dgk
    model_plain: DGK
    value: 0.7309
    std: 0.0025
    paper_value: 0.7309
    paper_std: 0.0025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: yanardag2015deep
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 50
    true_value: 0.7309
    true_std: 0.0025
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 50
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7309
    sort_std: 0.0025
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id011
  dataset: CSL
  rows:
  - model: Graph ViT
    model_key: graph vit
    model_plain: Graph ViT
    value: 1.0
    std: null
    paper_value: 1.0
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: He 2023
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 19
    true_value: 1.0
    true_std: null
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.0
    sort_std: null
    is_best: true
  - model: GPM
    model_key: gpm
    model_plain: GPM
    value: 1.0
    std: null
    paper_value: 1.0
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 21
    true_value: 1.0
    true_std: null
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.0
    sort_std: null
    is_best: true
  - model: ESC-GNN
    model_key: esc-gnn
    model_plain: ESC-GNN
    value: 1.0
    std: null
    paper_value: 1.0
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Yan 2024
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 20
    true_value: 1.0
    true_std: null
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.0
    sort_std: null
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
  - model: 3-GNN
    model_key: 3-gnn
    model_plain: 3-GNN
    value: 0.957
    std: null
    paper_value: 0.957
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Morris 2019
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 29
    true_value: 0.957
    true_std: null
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.957
    sort_std: null
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.1
    std: null
    paper_value: 0.1
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kipf 2017
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 41
    true_value: 0.1
    true_std: null
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 41
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1
    sort_std: null
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.1
    std: null
    paper_value: 0.1
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Bresson 2017
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 42
    true_value: 0.1
    true_std: null
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 42
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1
    sort_std: null
    is_best: false
  - model: GraphTrans
    model_key: graphtrans
    model_plain: GraphTrans
    value: 0.1
    std: null
    paper_value: 0.1
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Dwivedi 2020
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 43
    true_value: 0.1
    true_std: null
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 43
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1
    sort_std: null
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id002
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
    paper_value: 0.8995
    paper_std: 0.0201
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: guo2023linkless
    variant_inference_reason: ''
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 3
    true_value: 0.8995
    true_std: 0.0201
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8995
    sort_std: 0.0201
    is_best: true
  - model: ANS-GT + HDSE
    model_key: ans-gt + hdse
    model_plain: ANS-GT + HDSE
    value: 0.8967
    std: 0.0039
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_display: Aug 2023
    date_iso: 2023-08
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.8967
    sort_std: 0.0039
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.7101
    std: 0.0014
    paper_value: 0.7101
    paper_std: 0.0014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu2022nodeformer
    variant_inference_reason: 'dataset: fuzzy match to cora (score=90)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 20
    true_value: 0.887
    true_std: 0.002
    value_gap_source_arxiv: '2512.14619'
    value_gap_source_title: 'ParaFormer: A Generalized PageRank Graph Transformer
      for Graph Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.17690000000000006
    value_note: ''
    paper_rank: 238
    rank_delta: 218
    rank_delta_abs: 218
    rank_delta_direction: worse
    sort_value: 0.887
    sort_std: 0.002
    is_best: false
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.6712
    std: 0.0031
    paper_value: 0.6712
    paper_std: 0.0031
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: chien2021adaptive
    variant_inference_reason: 'dataset: fuzzy match to cora (score=90)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 25
    true_value: 0.8857
    true_std: 0.0069
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.21450000000000002
    value_note: ''
    paper_rank: 263
    rank_delta: 238
    rank_delta_abs: 238
    rank_delta_direction: worse
    sort_value: 0.8857
    sort_std: 0.0069
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.6447
    std: 0.0018
    paper_value: 0.6447
    paper_std: 0.0018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: velickovic2018graph
    variant_inference_reason: 'dataset: fuzzy match to cora (score=90)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 31
    true_value: 0.8825
    true_std: 0.0053
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.2377999999999999
    value_note: ''
    paper_rank: 274
    rank_delta: 243
    rank_delta_abs: 243
    rank_delta_direction: worse
    sort_value: 0.8825
    sort_std: 0.0053
    is_best: false
  - model: Nagphormer
    model_key: nagphormer
    model_plain: Nagphormer
    value: 0.7151
    std: 0.0013
    paper_value: 0.7151
    paper_std: 0.0013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: chen2023nagphormer
    variant_inference_reason: 'dataset: fuzzy match to cora (score=90)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 33
    true_value: 0.882
    true_std: 0.005
    value_gap_source_arxiv: '2512.14619'
    value_gap_source_title: 'ParaFormer: A Generalized PageRank Graph Transformer
      for Graph Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.16690000000000005
    value_note: ''
    paper_rank: 233
    rank_delta: 200
    rank_delta_abs: 200
    rank_delta_direction: worse
    sort_value: 0.882
    sort_std: 0.005
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.697
    std: 0.0054
    paper_value: 0.697
    paper_std: 0.0054
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: chen2024leveraging
    variant_inference_reason: 'dataset: fuzzy match to cora (score=90)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 37
    true_value: 0.8809999999999999
    true_std: 0.006999999999999999
    value_gap_source_arxiv: '2512.14619'
    value_gap_source_title: 'ParaFormer: A Generalized PageRank Graph Transformer
      for Graph Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.18399999999999994
    value_note: ''
    paper_rank: 246
    rank_delta: 209
    rank_delta_abs: 209
    rank_delta_direction: worse
    sort_value: 0.8809999999999999
    sort_std: 0.006999999999999999
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.6516
    std: 0.0028
    paper_value: 0.6516
    paper_std: 0.0028
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: gasteiger2018combining
    variant_inference_reason: 'dataset: fuzzy match to cora (score=90)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 39
    true_value: 0.88
    true_std: 0.002
    value_gap_source_arxiv: '2512.14619'
    value_gap_source_title: 'ParaFormer: A Generalized PageRank Graph Transformer
      for Graph Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.22840000000000005
    value_note: ''
    paper_rank: 273
    rank_delta: 234
    rank_delta_abs: 234
    rank_delta_direction: worse
    sort_value: 0.88
    sort_std: 0.002
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.6176
    std: 0.0014
    paper_value: 0.6176
    paper_std: 0.0014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: kipf2017semisupervised
    variant_inference_reason: 'dataset: fuzzy match to cora (score=90)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 48
    true_value: 0.8778
    true_std: 0.0096
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.2602
    value_note: ''
    paper_rank: 279
    rank_delta: 231
    rank_delta_abs: 231
    rank_delta_direction: worse
    sort_value: 0.8778
    sort_std: 0.0096
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.5576
    std: 0.0023
    paper_value: 0.5576
    paper_std: 0.0023
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: rampasek2022recipe
    variant_inference_reason: 'dataset: fuzzy match to cora (score=90)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 114
    true_value: 0.8387
    true_std: 0.0096
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.2811
    value_note: ''
    paper_rank: 293
    rank_delta: 179
    rank_delta_abs: 179
    rank_delta_direction: worse
    sort_value: 0.8387
    sort_std: 0.0096
    is_best: false
  - model: GOAT
    model_key: goat
    model_plain: GOAT
    value: 0.6855
    std: 0.0034
    paper_value: 0.6855
    paper_std: 0.0034
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: kong2023goat
    variant_inference_reason: 'dataset: fuzzy match to cora (score=90)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 125
    true_value: 0.8326
    true_std: 0.0124
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1471
    value_note: ''
    paper_rank: 253
    rank_delta: 128
    rank_delta_abs: 128
    rank_delta_direction: worse
    sort_value: 0.8326
    sort_std: 0.0124
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.5901
    std: 0.0034
    paper_value: 0.5901
    paper_std: 0.0034
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: kreuzer2021rethinking
    variant_inference_reason: 'dataset: fuzzy match to cora (score=90)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 143
    true_value: 0.8191
    true_std: 0.0342
    value_gap_source_arxiv: '2311.04653'
    value_gap_source_title: Hybrid Focal and Full-Range Attention Based Graph Transformers
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.2290000000000001
    value_note: ''
    paper_rank: 286
    rank_delta: 143
    rank_delta_abs: 143
    rank_delta_direction: worse
    sort_value: 0.8191
    sort_std: 0.0342
    is_best: false
  - model: VCR-Graphormer
    model_key: vcr-graphormer
    model_plain: VCR-Graphormer
    value: 0.6878
    std: 0.0029
    paper_value: 0.6878
    paper_std: 0.0029
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: fu2024vcrgraphormer
    variant_inference_reason: 'dataset: fuzzy match to cora (score=90)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 233
    true_value: 0.7167
    true_std: 0.001
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.028900000000000037
    value_note: ''
    paper_rank: 252
    rank_delta: 19
    rank_delta_abs: 19
    rank_delta_direction: worse
    sort_value: 0.7167
    sort_std: 0.001
    is_best: false
  - model: GPM
    model_key: gpm
    model_plain: GPM
    value: 0.7123
    std: 0.0051
    paper_value: 0.7123
    paper_std: 0.0051
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to cora (score=90)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 235
    true_value: 0.7123
    true_std: 0.0051
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 235
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7123
    sort_std: 0.0051
    is_best: false
  - model: RUM
    model_key: rum
    model_plain: RUM
    value: 0.7042
    std: 0.0008
    paper_value: 0.7042
    paper_std: 0.0008
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wang2024nonconvolutional
    variant_inference_reason: 'dataset: fuzzy match to cora (score=90)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 241
    true_value: 0.7042
    true_std: 0.0008
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 241
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7042
    sort_std: 0.0008
    is_best: false
  - model: OrderedGNN
    model_key: orderedgnn
    model_plain: OrderedGNN
    value: 0.6921
    std: 0.0023
    paper_value: 0.6921
    paper_std: 0.0023
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: song2023ordered
    variant_inference_reason: 'dataset: fuzzy match to cora (score=90)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 251
    true_value: 0.6921
    true_std: 0.0023
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 251
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6921
    sort_std: 0.0023
    is_best: false
  - model: RAW-GNN
    model_key: raw-gnn
    model_plain: RAW-GNN
    value: 0.6864
    std: 0.0055
    paper_value: 0.6864
    paper_std: 0.0055
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: jin2022raw
    variant_inference_reason: 'dataset: fuzzy match to cora (score=90)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 253
    true_value: 0.6864
    true_std: 0.0055
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 253
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6864
    sort_std: 0.0055
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id007
  dataset: Deezer
  rows:
  - model: GPM
    model_key: gpm
    model_plain: GPM
    value: 0.6726
    std: 0.0022
    paper_value: 0.6726
    paper_std: 0.0022
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: null
    sort_value: 0.6726
    sort_std: 0.0022
    is_best: true
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.664
    std: 0.007
    paper_value: 0.664
    paper_std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu2022nodeformer
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: null
    sort_value: 0.664
    sort_std: 0.007
    is_best: true
  - model: OrderedGNN
    model_key: orderedgnn
    model_plain: OrderedGNN
    value: 0.6612
    std: 0.0075
    paper_value: 0.6612
    paper_std: 0.0075
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: song2023ordered
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: null
    sort_value: 0.6612
    sort_std: 0.0075
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.661
    std: 0.006
    paper_value: 0.661
    paper_std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: gasteiger2018combining
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: null
    sort_value: 0.661
    sort_std: 0.006
    is_best: false
  - model: Nagphormer
    model_key: nagphormer
    model_plain: Nagphormer
    value: 0.6554
    std: 0.0057
    paper_value: 0.6554
    paper_std: 0.0057
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: chen2023nagphormer
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: null
    sort_value: 0.6554
    sort_std: 0.0057
    is_best: false
  - model: GOAT
    model_key: goat
    model_plain: GOAT
    value: 0.6531
    std: 0.0024
    paper_value: 0.6531
    paper_std: 0.0024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: kong2023goat
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: null
    sort_value: 0.6531
    sort_std: 0.0024
    is_best: false
  - model: VCR-Graphormer
    model_key: vcr-graphormer
    model_plain: VCR-Graphormer
    value: 0.6528
    std: 0.0051
    paper_value: 0.6528
    paper_std: 0.0051
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: fu2024vcrgraphormer
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: null
    sort_value: 0.6528
    sort_std: 0.0051
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.6516
    std: 0.0033
    paper_value: 0.6516
    paper_std: 0.0033
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: chen2024leveraging
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: null
    sort_value: 0.6516
    sort_std: 0.0033
    is_best: false
  - model: RAW-GNN
    model_key: raw-gnn
    model_plain: RAW-GNN
    value: 0.6511
    std: 0.0064
    paper_value: 0.6511
    paper_std: 0.0064
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: jin2022raw
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: null
    sort_value: 0.6511
    sort_std: 0.0064
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.6429
    std: 0.0035
    paper_value: 0.6429
    paper_std: 0.0035
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: kreuzer2021rethinking
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: null
    sort_value: 0.6429
    sort_std: 0.0035
    is_best: false
  - model: RUM
    model_key: rum
    model_plain: RUM
    value: 0.6425
    std: 0.0062
    paper_value: 0.6425
    paper_std: 0.0062
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wang2024nonconvolutional
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: null
    sort_value: 0.6425
    sort_std: 0.0062
    is_best: false
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.632
    std: 0.0084
    paper_value: 0.632
    paper_std: 0.0084
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: chien2021adaptive
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: null
    sort_value: 0.632
    sort_std: 0.0084
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.627
    std: 0.007
    paper_value: 0.627
    paper_std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: kipf2017semisupervised
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: null
    sort_value: 0.627
    sort_std: 0.007
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.617
    std: 0.008
    paper_value: 0.617
    paper_std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: velickovic2018graph
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: null
    sort_value: 0.617
    sort_std: 0.008
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.6056
    std: 0.0062
    paper_value: 0.6056
    paper_std: 0.0062
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: rampasek2022recipe
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: null
    sort_value: 0.6056
    sort_std: 0.0062
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id017
  dataset: Flickr
  rows:
  - model: GPM
    model_key: gpm
    model_plain: GPM
    value: 0.8941
    std: 0.0047
    paper_value: 0.8941
    paper_std: 0.0047
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to flickr (score=95)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 1
    true_value: 0.8941
    true_std: 0.0047
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8941
    sort_std: 0.0047
    is_best: true
  - model: OrderedGNN
    model_key: orderedgnn
    model_plain: OrderedGNN
    value: 0.8868
    std: 0.0054
    paper_value: 0.8868
    paper_std: 0.0054
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Song 2023
    variant_inference_reason: 'dataset: fuzzy match to flickr (score=95)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 2
    true_value: 0.8868
    true_std: 0.0054
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8868
    sort_std: 0.0054
    is_best: true
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.883
    std: 0.0022
    paper_value: 0.883
    paper_std: 0.0022
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Wu 2022
    variant_inference_reason: 'dataset: fuzzy match to flickr (score=95)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 3
    true_value: 0.883
    true_std: 0.0022
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.883
    sort_std: 0.0022
    is_best: false
  - model: GOAT
    model_key: goat
    model_plain: GOAT
    value: 0.8816
    std: 0.0095
    paper_value: 0.8816
    paper_std: 0.0095
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kong 2023
    variant_inference_reason: 'dataset: fuzzy match to flickr (score=95)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 4
    true_value: 0.8816
    true_std: 0.0095
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8816
    sort_std: 0.0095
    is_best: true
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.879
    std: 0.0045
    paper_value: 0.879
    paper_std: 0.0045
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Chen 2024
    variant_inference_reason: 'dataset: fuzzy match to flickr (score=95)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 5
    true_value: 0.879
    true_std: 0.0045
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.879
    sort_std: 0.0045
    is_best: false
  - model: RUM
    model_key: rum
    model_plain: RUM
    value: 0.8725
    std: 0.0066
    paper_value: 0.8725
    paper_std: 0.0066
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Wang 2024
    variant_inference_reason: 'dataset: fuzzy match to flickr (score=95)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 6
    true_value: 0.8725
    true_std: 0.0066
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8725
    sort_std: 0.0066
    is_best: false
  - model: Nagphormer
    model_key: nagphormer
    model_plain: Nagphormer
    value: 0.8685
    std: 0.0085
    paper_value: 0.8685
    paper_std: 0.0085
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Chen 2023
    variant_inference_reason: 'dataset: fuzzy match to flickr (score=95)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 7
    true_value: 0.8685
    true_std: 0.0085
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8685
    sort_std: 0.0085
    is_best: false
  - model: RAW-GNN
    model_key: raw-gnn
    model_plain: RAW-GNN
    value: 0.8653
    std: 0.0065
    paper_value: 0.8653
    paper_std: 0.0065
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Jin 2022
    variant_inference_reason: 'dataset: fuzzy match to flickr (score=95)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 8
    true_value: 0.8653
    true_std: 0.0065
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8653
    sort_std: 0.0065
    is_best: false
  - model: VCR-Graphormer
    model_key: vcr-graphormer
    model_plain: VCR-Graphormer
    value: 0.8623
    std: 0.0074
    paper_value: 0.8623
    paper_std: 0.0074
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Fu 2024
    variant_inference_reason: 'dataset: fuzzy match to flickr (score=95)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 9
    true_value: 0.8623
    true_std: 0.0074
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8623
    sort_std: 0.0074
    is_best: false
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.8591
    std: 0.0051
    paper_value: 0.8591
    paper_std: 0.0051
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Chien 2021
    variant_inference_reason: 'dataset: fuzzy match to flickr (score=95)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 10
    true_value: 0.8591
    true_std: 0.0051
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8591
    sort_std: 0.0051
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.8511
    std: 0.0067
    paper_value: 0.8511
    paper_std: 0.0067
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Veličković 2018
    variant_inference_reason: 'dataset: fuzzy match to flickr (score=95)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 11
    true_value: 0.8511
    true_std: 0.0067
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8511
    sort_std: 0.0067
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.8466
    std: 0.0031
    paper_value: 0.8466
    paper_std: 0.0031
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Gasteiger 2018
    variant_inference_reason: 'dataset: fuzzy match to flickr (score=95)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 12
    true_value: 0.8466
    true_std: 0.0031
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8466
    sort_std: 0.0031
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.8458
    std: 0.0049
    paper_value: 0.8458
    paper_std: 0.0049
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kipf 2017
    variant_inference_reason: 'dataset: fuzzy match to flickr (score=95)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 13
    true_value: 0.8458
    true_std: 0.0049
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8458
    sort_std: 0.0049
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.8361
    std: 0.007
    paper_value: 0.8361
    paper_std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Rampasek 2022
    variant_inference_reason: 'dataset: fuzzy match to flickr (score=95)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 14
    true_value: 0.8361
    true_std: 0.007
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8361
    sort_std: 0.007
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id008
  dataset: IMDB-BINARY
  rows:
  - model: GPM
    model_key: gpm
    model_plain: GPM
    value: 0.8267
    std: 0.0047
    paper_value: 0.8267
    paper_std: 0.0047
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 1
    true_value: 0.8267
    true_std: 0.0047
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8267
    sort_std: 0.0047
    is_best: true
  - model: RUM
    model_key: rum
    model_plain: RUM
    value: 0.811
    std: 0.045
    paper_value: 0.811
    paper_std: 0.045
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wang2024nonconvolutional
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 2
    true_value: 0.811
    true_std: 0.045
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
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
  - model: SAT
    model_key: sat
    model_plain: SAT
    value: 0.7829
    std: 0.0126
    paper_value: 0.7829
    paper_std: 0.0126
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: chen2022structure
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 4
    true_value: 0.7829
    true_std: 0.0126
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7829
    sort_std: 0.0126
    is_best: false
  - model: Graph ViT
    model_key: graph vit
    model_plain: Graph ViT
    value: 0.7805
    std: 0.01
    paper_value: 0.7805
    paper_std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: he2023generalization
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 5
    true_value: 0.7805
    true_std: 0.01
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7805
    sort_std: 0.01
    is_best: false
  - model: CoCN expanded
    model_key: cocn expanded
    model_plain: CoCN expanded
    value: 0.7794
    std: 0.0033
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
    global_rank: 6
    sort_value: 0.7794
    sort_std: 0.0033
    is_best: false
  - model: GSN
    model_key: gsn
    model_plain: GSN
    value: 0.778
    std: 0.033
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
    global_rank: 7
    sort_value: 0.778
    sort_std: 0.033
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.7776
    std: 0.0098
    paper_value: 0.7776
    paper_std: 0.0098
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: rampasek2022recipe
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 8
    true_value: 0.7776
    true_std: 0.0098
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7776
    sort_std: 0.0098
    is_best: false
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.7674
    std: 0.0086
    paper_value: 0.7674
    paper_std: 0.0086
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ying2021transformers
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 15
    true_value: 0.7674
    true_std: 0.0086
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7674
    sort_std: 0.0086
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.76
    std: 0.019
    paper_value: 0.76
    paper_std: 0.019
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: kreuzer2021rethinking
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 16
    true_value: 0.76
    true_std: 0.019
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.76
    sort_std: 0.019
    is_best: false
  - model: AgentNet
    model_key: agentnet
    model_plain: AgentNet
    value: 0.7588
    std: 0.036
    paper_value: 0.7588
    paper_std: 0.036
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: martinkus2023agentbased
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 18
    true_value: 0.7588
    true_std: 0.036
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7588
    sort_std: 0.036
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.7326
    std: 0.0046
    paper_value: 0.7326
    paper_std: 0.0046
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: xu2018how
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 25
    true_value: 0.751
    true_std: 0.051
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.018399999999999972
    value_note: global 0.7510 within std
    paper_rank: 44
    rank_delta: 19
    rank_delta_abs: 19
    rank_delta_direction: worse
    sort_value: 0.751
    sort_std: 0.051
    is_best: false
  - model: GNN (a)
    model_key: gnn (a)
    model_plain: GNN (a)
    value: 0.75
    std: 0.042
    paper_value: 0.75
    paper_std: 0.042
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: zhao2022from
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 26
    true_value: 0.75
    true_std: 0.042
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.75
    sort_std: 0.042
    is_best: false
  - model: AWE
    model_key: awe
    model_plain: AWE
    value: 0.7445
    std: 0.0583
    paper_value: 0.7445
    paper_std: 0.0583
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ivanov2018anonymous
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 28
    true_value: 0.7445
    true_std: 0.0583
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 28
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7445
    sort_std: 0.0583
    is_best: false
  - model: CRaWl
    model_key: crawl
    model_plain: CRaWl
    value: 0.7369
    std: 0.0205
    paper_value: 0.7369
    paper_std: 0.0205
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: tonshoff2023walking
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 35
    true_value: 0.7369
    true_std: 0.0205
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7369
    sort_std: 0.0205
    is_best: false
  - model: GMT
    model_key: gmt
    model_plain: GMT
    value: 0.7348
    std: 0.0076
    paper_value: 0.7348
    paper_std: 0.0076
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: baek2021accurate
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 43
    true_value: 0.7348
    true_std: 0.0076
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 43
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7348
    sort_std: 0.0076
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.7231
    std: 0.0367
    paper_value: 0.7231
    paper_std: 0.0367
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: corso2020principal
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 60
    true_value: 0.7231
    true_std: 0.0367
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 60
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7231
    sort_std: 0.0367
    is_best: false
  - model: DGK
    model_key: dgk
    model_plain: DGK
    value: 0.6696
    std: 0.0056
    paper_value: 0.6696
    paper_std: 0.0056
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: yanardag2015deep
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 120
    true_value: 0.6696
    true_std: 0.0056
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 120
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6696
    sort_std: 0.0056
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
    value: 0.8506
    std: 0.0379
    paper_value: 0.8506
    paper_std: 0.0379
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: kipf2017semisupervised
    variant_inference_reason: ''
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 5
    true_value: 0.9224
    true_std: 0.0123
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07179999999999997
    value_note: ''
    paper_rank: 100
    rank_delta: 95
    rank_delta_abs: 95
    rank_delta_direction: worse
    sort_value: 0.9224
    sort_std: 0.0123
    is_best: false
  - model: Nagphormer
    model_key: nagphormer
    model_plain: Nagphormer
    value: 0.8646
    std: 0.0409
    paper_value: 0.8646
    paper_std: 0.0409
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: chen2023nagphormer
    variant_inference_reason: ''
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 27
    true_value: 0.897
    true_std: 0.002
    value_gap_source_arxiv: '2512.14619'
    value_gap_source_title: 'ParaFormer: A Generalized PageRank Graph Transformer
      for Graph Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.032399999999999984
    value_note: global 0.8970 within std
    paper_rank: 95
    rank_delta: 68
    rank_delta_abs: 68
    rank_delta_direction: worse
    sort_value: 0.897
    sort_std: 0.002
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.8393
    std: 0.0472
    paper_value: 0.8393
    paper_std: 0.0472
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu2022nodeformer
    variant_inference_reason: ''
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 38
    true_value: 0.8932
    true_std: 0.0025
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05389999999999995
    value_note: ''
    paper_rank: 103
    rank_delta: 65
    rank_delta_abs: 65
    rank_delta_direction: worse
    sort_value: 0.8932
    sort_std: 0.0025
    is_best: false
  - model: GPM
    model_key: gpm
    model_plain: GPM
    value: 0.8829
    std: 0.0515
    paper_value: 0.8829
    paper_std: 0.0515
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 63
    true_value: 0.8829
    true_std: 0.0515
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 63
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8829
    sort_std: 0.0515
    is_best: false
  - model: LLP
    model_key: llp
    model_plain: LLP
    value: 0.8723
    std: 0.0492
    paper_value: 0.8723
    paper_std: 0.0492
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: guo2023linkless
    variant_inference_reason: ''
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 87
    true_value: 0.8723
    true_std: 0.0492
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 87
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8723
    sort_std: 0.0492
    is_best: false
  - model: RUM
    model_key: rum
    model_plain: RUM
    value: 0.8587
    std: 0.0393
    paper_value: 0.8587
    paper_std: 0.0393
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wang2024nonconvolutional
    variant_inference_reason: ''
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 98
    true_value: 0.8587
    true_std: 0.0393
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 98
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8587
    sort_std: 0.0393
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id010
  dataset: REDDIT-MULTI-5K
  rows:
  - model: R-method
    model_key: r-method
    model_plain: R-method
    value: 0.606
    std: 0.003
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
    sort_value: 0.606
    sort_std: 0.003
    is_best: true
  - model: GIN + rand id
    model_key: gin + rand id
    model_plain: GIN + rand id
    value: 0.57
    std: 0.021
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
    sort_value: 0.57
    sort_std: 0.021
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.3937
    std: 0.014
    paper_value: 0.3937
    paper_std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xu et al. 2018
    variant_inference_reason: 'dataset: fuzzy match to reddit-multi-5k (score=90)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 3
    true_value: 0.569
    true_std: 0.02
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.17529999999999996
    value_note: ''
    paper_rank: 28
    rank_delta: 25
    rank_delta_abs: 25
    rank_delta_direction: worse
    sort_value: 0.569
    sort_std: 0.02
    is_best: false
  - model: Graph-JEPA
    model_key: graph-jepa
    model_plain: Graph-JEPA
    value: 0.5673
    std: 0.0196
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 19.22
    arxiv_id: '2309.16014'
    title: Graph-level Representation Learning with Joint-Embedding Predictive Architectures
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.5673
    sort_std: 0.0196
    is_best: false
  - model: GPM
    model_key: gpm
    model_plain: GPM
    value: 0.4307
    std: 0.0029
    paper_value: 0.4307
    paper_std: 0.0029
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to reddit-multi-5k (score=90)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 18
    true_value: 0.4307
    true_std: 0.0029
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4307
    sort_std: 0.0029
    is_best: false
  - model: AgentNet
    model_key: agentnet
    model_plain: AgentNet
    value: 0.4215
    std: 0.0013
    paper_value: 0.4215
    paper_std: 0.0013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Martinkus et al. 2023
    variant_inference_reason: 'dataset: fuzzy match to reddit-multi-5k (score=90)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 19
    true_value: 0.4215
    true_std: 0.0013
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4215
    sort_std: 0.0013
    is_best: false
  - model: SAT
    model_key: sat
    model_plain: SAT
    value: 0.4214
    std: 0.0007
    paper_value: 0.4214
    paper_std: 0.0007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Chen et al. 2022
    variant_inference_reason: 'dataset: fuzzy match to reddit-multi-5k (score=90)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 20
    true_value: 0.4214
    true_std: 0.0007
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4214
    sort_std: 0.0007
    is_best: false
  - model: RUM
    model_key: rum
    model_plain: RUM
    value: 0.4166
    std: 0.0015
    paper_value: 0.4166
    paper_std: 0.0015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Wang et al. 2024
    variant_inference_reason: 'dataset: fuzzy match to reddit-multi-5k (score=90)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 21
    true_value: 0.4166
    true_std: 0.0015
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4166
    sort_std: 0.0015
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.4155
    std: 0.0016
    paper_value: 0.4155
    paper_std: 0.0016
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Rampasek et al. 2022
    variant_inference_reason: 'dataset: fuzzy match to reddit-multi-5k (score=90)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 22
    true_value: 0.4155
    true_std: 0.0016
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4155
    sort_std: 0.0016
    is_best: false
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.4142
    std: 0.0042
    paper_value: 0.4142
    paper_std: 0.0042
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Ying et al. 2021
    variant_inference_reason: 'dataset: fuzzy match to reddit-multi-5k (score=90)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 23
    true_value: 0.4142
    true_std: 0.0042
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4142
    sort_std: 0.0042
    is_best: false
  - model: CRaWl
    model_key: crawl
    model_plain: CRaWl
    value: 0.4072
    std: 0.0065
    paper_value: 0.4072
    paper_std: 0.0065
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tonshoff et al. 2023
    variant_inference_reason: 'dataset: fuzzy match to reddit-multi-5k (score=90)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 24
    true_value: 0.4072
    true_std: 0.0065
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4072
    sort_std: 0.0065
    is_best: false
  - model: GMT
    model_key: gmt
    model_plain: GMT
    value: 0.4063
    std: 0.0094
    paper_value: 0.4063
    paper_std: 0.0094
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Baek et al. 2021
    variant_inference_reason: 'dataset: fuzzy match to reddit-multi-5k (score=90)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 25
    true_value: 0.4063
    true_std: 0.0094
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4063
    sort_std: 0.0094
    is_best: false
  - model: GNN (a)
    model_key: gnn (a)
    model_plain: GNN (a)
    value: 0.406
    std: 0.0099
    paper_value: 0.406
    paper_std: 0.0099
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhao et al. 2022
    variant_inference_reason: 'dataset: fuzzy match to reddit-multi-5k (score=90)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 26
    true_value: 0.406
    true_std: 0.0099
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.406
    sort_std: 0.0099
    is_best: false
  - model: Graph ViT
    model_key: graph vit
    model_plain: Graph ViT
    value: 0.4017
    std: 0.0052
    paper_value: 0.4017
    paper_std: 0.0052
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: He et al. 2023
    variant_inference_reason: 'dataset: fuzzy match to reddit-multi-5k (score=90)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 27
    true_value: 0.4017
    true_std: 0.0052
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 27
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4017
    sort_std: 0.0052
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.3992
    std: 0.0102
    paper_value: 0.3992
    paper_std: 0.0102
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kreuzer et al. 2021
    variant_inference_reason: 'dataset: fuzzy match to reddit-multi-5k (score=90)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 28
    true_value: 0.3992
    true_std: 0.0102
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 28
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3992
    sort_std: 0.0102
    is_best: false
  - model: AWE
    model_key: awe
    model_plain: AWE
    value: 0.392
    std: 0.0209
    paper_value: 0.392
    paper_std: 0.0209
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Ivanov et al. 2018
    variant_inference_reason: 'dataset: fuzzy match to reddit-multi-5k (score=90)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 29
    true_value: 0.392
    true_std: 0.0209
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.392
    sort_std: 0.0209
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.3857
    std: 0.0186
    paper_value: 0.3857
    paper_std: 0.0186
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Corso et al. 2020
    variant_inference_reason: 'dataset: fuzzy match to reddit-multi-5k (score=90)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 30
    true_value: 0.3857
    true_std: 0.0186
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 30
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3857
    sort_std: 0.0186
    is_best: false
  - model: DGK
    model_key: dgk
    model_plain: DGK
    value: 0.3222
    std: 0.001
    paper_value: 0.3222
    paper_std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Yanardag and Vishwanathan 2015
    variant_inference_reason: 'dataset: fuzzy match to reddit-multi-5k (score=90)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 31
    true_value: 0.3222
    true_std: 0.001
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3222
    sort_std: 0.001
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: Reddit
  rows:
  - model: GCN (LCP-ORC)
    model_key: gcn (lcp-orc)
    model_plain: GCN (LCP-ORC)
    value: 0.8719
    std: 0.0156
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information in Relational Learning
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.8719
    sort_std: 0.0156
    is_best: true
  - model: GIN (HCP-ORC)
    model_key: gin (hcp-orc)
    model_plain: GIN (HCP-ORC)
    value: 0.8482
    std: 0.0162
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information in Relational Learning
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.8482
    sort_std: 0.0162
    is_best: true
  - model: GPS (EN H-19-RWPE)
    model_key: gps (en h-19-rwpe)
    model_plain: GPS (EN H-19-RWPE)
    value: 0.8425
    std: 0.0113
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information in Relational Learning
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.8425
    sort_std: 0.0113
    is_best: false
  - model: GPM
    model_key: gpm
    model_plain: GPM
    value: 0.4307
    std: 0.0029
    paper_value: 0.4307
    paper_std: 0.0029
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: null
    sort_value: 0.4307
    sort_std: 0.0029
    is_best: false
  - model: AgentNet
    model_key: agentnet
    model_plain: AgentNet
    value: 0.4215
    std: 0.0013
    paper_value: 0.4215
    paper_std: 0.0013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: martinkus2023agentbased
    variant_inference_reason: ''
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: null
    sort_value: 0.4215
    sort_std: 0.0013
    is_best: false
  - model: SAT
    model_key: sat
    model_plain: SAT
    value: 0.4214
    std: 0.0007
    paper_value: 0.4214
    paper_std: 0.0007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: chen2022structure
    variant_inference_reason: ''
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: null
    sort_value: 0.4214
    sort_std: 0.0007
    is_best: false
  - model: RUM
    model_key: rum
    model_plain: RUM
    value: 0.4166
    std: 0.0015
    paper_value: 0.4166
    paper_std: 0.0015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wang2024nonconvolutional
    variant_inference_reason: ''
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: null
    sort_value: 0.4166
    sort_std: 0.0015
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.4155
    std: 0.0016
    paper_value: 0.4155
    paper_std: 0.0016
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: rampasek2022recipe
    variant_inference_reason: ''
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: null
    sort_value: 0.4155
    sort_std: 0.0016
    is_best: false
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.4142
    std: 0.0042
    paper_value: 0.4142
    paper_std: 0.0042
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ying2021transformers
    variant_inference_reason: ''
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: null
    sort_value: 0.4142
    sort_std: 0.0042
    is_best: false
  - model: CRaWl
    model_key: crawl
    model_plain: CRaWl
    value: 0.4072
    std: 0.0065
    paper_value: 0.4072
    paper_std: 0.0065
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: tonshoff2023walking
    variant_inference_reason: ''
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: null
    sort_value: 0.4072
    sort_std: 0.0065
    is_best: false
  - model: GMT
    model_key: gmt
    model_plain: GMT
    value: 0.4063
    std: 0.0094
    paper_value: 0.4063
    paper_std: 0.0094
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: baek2021accurate
    variant_inference_reason: ''
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: null
    sort_value: 0.4063
    sort_std: 0.0094
    is_best: false
  - model: GNN (a)
    model_key: gnn (a)
    model_plain: GNN (a)
    value: 0.406
    std: 0.0099
    paper_value: 0.406
    paper_std: 0.0099
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: zhao2022from
    variant_inference_reason: ''
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: null
    sort_value: 0.406
    sort_std: 0.0099
    is_best: false
  - model: Graph ViT
    model_key: graph vit
    model_plain: Graph ViT
    value: 0.4017
    std: 0.0052
    paper_value: 0.4017
    paper_std: 0.0052
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: he2023generalization
    variant_inference_reason: ''
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: null
    sort_value: 0.4017
    sort_std: 0.0052
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.3992
    std: 0.0102
    paper_value: 0.3992
    paper_std: 0.0102
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: kreuzer2021rethinking
    variant_inference_reason: ''
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: null
    sort_value: 0.3992
    sort_std: 0.0102
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.3937
    std: 0.014
    paper_value: 0.3937
    paper_std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: xu2018how
    variant_inference_reason: ''
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: null
    sort_value: 0.3937
    sort_std: 0.014
    is_best: false
  - model: AWE
    model_key: awe
    model_plain: AWE
    value: 0.392
    std: 0.0209
    paper_value: 0.392
    paper_std: 0.0209
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ivanov2018anonymous
    variant_inference_reason: ''
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: null
    sort_value: 0.392
    sort_std: 0.0209
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.3857
    std: 0.0186
    paper_value: 0.3857
    paper_std: 0.0186
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: corso2020principal
    variant_inference_reason: ''
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: null
    sort_value: 0.3857
    sort_std: 0.0186
    is_best: false
  - model: DGK
    model_key: dgk
    model_plain: DGK
    value: 0.3222
    std: 0.001
    paper_value: 0.3222
    paper_std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: yanardag2015deep
    variant_inference_reason: ''
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: null
    sort_value: 0.3222
    sort_std: 0.001
    is_best: false
  metric: F1
  higher_is_better: true
- &id005
  dataset: WikiCS
  rows:
  - model: GrokFormer
    model_key: grokformer
    model_plain: GrokFormer
    value: 0.8557
    std: 0.0065
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
    global_rank: 1
    sort_value: 0.8557
    sort_std: 0.0065
    is_best: true
  - model: SpecFormer
    model_key: specformer
    model_plain: SpecFormer
    value: 0.8515
    std: 0.0063
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
    global_rank: 2
    sort_value: 0.8515
    sort_std: 0.0063
    is_best: true
  - model: HopGNN
    model_key: hopgnn
    model_plain: HopGNN
    value: 0.8473
    std: 0.0059
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
    global_rank: 3
    sort_value: 0.8473
    sort_std: 0.0059
    is_best: true
  - model: Nagphormer
    model_key: nagphormer
    model_plain: Nagphormer
    value: 0.7716
    std: 0.0072
    paper_value: 0.7716
    paper_std: 0.0072
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: chen2023nagphormer
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 8
    true_value: 0.8341
    true_std: 0.0034
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0625
    value_note: ''
    paper_rank: 49
    rank_delta: 41
    rank_delta_abs: 41
    rank_delta_direction: worse
    sort_value: 0.8341
    sort_std: 0.0034
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.7691
    std: 0.0082
    paper_value: 0.7691
    paper_std: 0.0082
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: velickovic2018graph
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 9
    true_value: 0.8322
    true_std: 0.0078
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.06310000000000004
    value_note: ''
    paper_rank: 49
    rank_delta: 40
    rank_delta_abs: 40
    rank_delta_direction: worse
    sort_value: 0.8322
    sort_std: 0.0078
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.7812
    std: 0.005
    paper_value: 0.7812
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: chen2024leveraging
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 12
    true_value: 0.8271
    true_std: 0.0056
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04589999999999994
    value_note: ''
    paper_rank: 45
    rank_delta: 33
    rank_delta_abs: 33
    rank_delta_direction: worse
    sort_value: 0.8271
    sort_std: 0.0056
    is_best: false
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.7812
    std: 0.0023
    paper_value: 0.7812
    paper_std: 0.0023
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: chien2021adaptive
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 13
    true_value: 0.8258
    true_std: 0.0089
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04459999999999997
    value_note: ''
    paper_rank: 45
    rank_delta: 32
    rank_delta_abs: 32
    rank_delta_direction: worse
    sort_value: 0.8258
    sort_std: 0.0089
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7747
    std: 0.0085
    paper_value: 0.7747
    paper_std: 0.0085
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: kipf2017semisupervised
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 14
    true_value: 0.8232
    true_std: 0.0069
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04849999999999999
    value_note: ''
    paper_rank: 48
    rank_delta: 34
    rank_delta_abs: 34
    rank_delta_direction: worse
    sort_value: 0.8232
    sort_std: 0.0069
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.7473
    std: 0.0094
    paper_value: 0.7473
    paper_std: 0.0094
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu2022nodeformer
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 16
    true_value: 0.8103
    true_std: 0.0094
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.06300000000000006
    value_note: ''
    paper_rank: 51
    rank_delta: 35
    rank_delta_abs: 35
    rank_delta_direction: worse
    sort_value: 0.8103
    sort_std: 0.0094
    is_best: false
  - model: GPM
    model_key: gpm
    model_plain: GPM
    value: 0.8019
    std: 0.0041
    paper_value: 0.8019
    paper_std: 0.0041
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 28
    true_value: 0.8019
    true_std: 0.0041
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 28
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8019
    sort_std: 0.0041
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.7866
    std: 0.0049
    paper_value: 0.7866
    paper_std: 0.0049
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: rampasek2022recipe
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 39
    true_value: 0.7926
    true_std: 0.0057
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.006000000000000005
    value_note: ''
    paper_rank: 43
    rank_delta: 4
    rank_delta_abs: 4
    rank_delta_direction: worse
    sort_value: 0.7926
    sort_std: 0.0057
    is_best: false
  - model: OrderedGNN
    model_key: orderedgnn
    model_plain: OrderedGNN
    value: 0.7901
    std: 0.0068
    paper_value: 0.7901
    paper_std: 0.0068
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: song2023ordered
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 41
    true_value: 0.7901
    true_std: 0.0068
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 41
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7901
    sort_std: 0.0068
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.7887
    std: 0.0011
    paper_value: 0.7887
    paper_std: 0.0011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: gasteiger2018combining
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 42
    true_value: 0.7887
    true_std: 0.0011
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 42
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7887
    sort_std: 0.0011
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.7846
    std: 0.0099
    paper_value: 0.7846
    paper_std: 0.0099
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: kreuzer2021rethinking
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 44
    true_value: 0.7846
    true_std: 0.0099
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 44
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7846
    sort_std: 0.0099
    is_best: false
  - model: RUM
    model_key: rum
    model_plain: RUM
    value: 0.782
    std: 0.0029
    paper_value: 0.782
    paper_std: 0.0029
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wang2024nonconvolutional
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 45
    true_value: 0.782
    true_std: 0.0029
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 45
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.782
    sort_std: 0.0029
    is_best: false
  - model: RAW-GNN
    model_key: raw-gnn
    model_plain: RAW-GNN
    value: 0.7801
    std: 0.0058
    paper_value: 0.7801
    paper_std: 0.0058
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: jin2022raw
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 46
    true_value: 0.7801
    true_std: 0.0058
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 46
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7801
    sort_std: 0.0058
    is_best: false
  - model: GOAT
    model_key: goat
    model_plain: GOAT
    value: 0.77
    std: 0.0077
    paper_value: 0.77
    paper_std: 0.0077
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: kong2023goat
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 47
    true_value: 0.7796
    true_std: 0.0003
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.009599999999999942
    value_note: ''
    paper_rank: 49
    rank_delta: 2
    rank_delta_abs: 2
    rank_delta_direction: worse
    sort_value: 0.7796
    sort_std: 0.0003
    is_best: false
  - model: VCR-Graphormer
    model_key: vcr-graphormer
    model_plain: VCR-Graphormer
    value: 0.7769
    std: 0.0033
    paper_value: 0.7769
    paper_std: 0.0033
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: fu2024vcrgraphormer
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 48
    true_value: 0.7769
    true_std: 0.0033
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 48
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7769
    sort_std: 0.0033
    is_best: false
  metric: Accuracy
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
  - model: GPM
    model_key: gpm
    model_plain: GPM
    value: 0.064
    std: 0.004
    paper_value: 0.064
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: default subset fallback'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 5
    true_value: 0.021
    true_std: 0.002
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 0.043
    value_note: ''
    paper_rank: 69
    rank_delta: 64
    rank_delta_abs: 64
    rank_delta_direction: worse
    sort_value: 0.021
    sort_std: 0.002
    is_best: false
  - model: GPM
    model_key: gpm
    model_plain: GPM
    value: 0.021
    std: 0.002
    paper_value: 0.021
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 5
    true_value: 0.021
    true_std: 0.002
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.021
    sort_std: 0.002
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
    params_millions: null
    table_ref: Table 1
    source_ref: Rampásek et al. 2022
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
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
    paper_rank: 107
    rank_delta: 94
    rank_delta_abs: 94
    rank_delta_direction: worse
    sort_value: 0.023842
    sort_std: 0.0069779309254248125
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
    source_ref: Ying et al. 2021
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 18
    true_value: 0.025
    true_std: 0.004
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 0.097
    value_note: ''
    paper_rank: 210
    rank_delta: 192
    rank_delta_abs: 192
    rank_delta_direction: worse
    sort_value: 0.025
    sort_std: 0.004
    is_best: false
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.025
    std: 0.004
    paper_value: 0.025
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ying2021transformers
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 18
    true_value: 0.025
    true_std: 0.004
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.025
    sort_std: 0.004
    is_best: false
  - model: GNN (a)
    model_key: gnn (a)
    model_plain: GNN (a)
    value: 0.08
    std: 0.001
    paper_value: 0.08
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhao et al. 2022
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 33
    true_value: 0.034
    true_std: 0.007
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 0.046
    value_note: ''
    paper_rank: 146
    rank_delta: 113
    rank_delta_abs: 113
    rank_delta_direction: worse
    sort_value: 0.034
    sort_std: 0.007
    is_best: false
  - model: GNN (a)
    model_key: gnn (a)
    model_plain: GNN (a)
    value: 0.034
    std: 0.007
    paper_value: 0.034
    paper_std: 0.007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: zhao2022from
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 33
    true_value: 0.034
    true_std: 0.007
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.034
    sort_std: 0.007
    is_best: false
  - model: Graph ViT
    model_key: graph vit
    model_plain: Graph ViT
    value: 0.073
    std: 0.001
    paper_value: 0.073
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: He et al. 2023
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 34
    true_value: 0.035
    true_std: 0.005
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 0.03799999999999999
    value_note: ''
    paper_rank: 116
    rank_delta: 82
    rank_delta_abs: 82
    rank_delta_direction: worse
    sort_value: 0.035
    sort_std: 0.005
    is_best: false
  - model: Graph ViT
    model_key: graph vit
    model_plain: Graph ViT
    value: 0.035
    std: 0.005
    paper_value: 0.035
    paper_std: 0.005
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: he2023generalization
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 34
    true_value: 0.035
    true_std: 0.005
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 34
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.035
    sort_std: 0.005
    is_best: false
  - model: CRaWl
    model_key: crawl
    model_plain: CRaWl
    value: 0.085
    std: 0.004
    paper_value: 0.085
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tonshoff et al. 2023
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 36
    true_value: 0.036
    true_std: 0.005
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04900000000000001
    value_note: ''
    paper_rank: 159
    rank_delta: 123
    rank_delta_abs: 123
    rank_delta_direction: worse
    sort_value: 0.036
    sort_std: 0.005
    is_best: false
  - model: CRaWl
    model_key: crawl
    model_plain: CRaWl
    value: 0.036
    std: 0.005
    paper_value: 0.036
    paper_std: 0.005
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: tonshoff2023walking
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 36
    true_value: 0.036
    true_std: 0.005
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 36
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.036
    sort_std: 0.005
    is_best: false
  - model: SAT
    model_key: sat
    model_plain: SAT
    value: 0.094
    std: 0.008
    paper_value: 0.094
    paper_std: 0.008
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Chen et al. 2022
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 35
    true_value: 0.036
    true_std: 0.002
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 0.058
    value_note: ''
    paper_rank: 181
    rank_delta: 146
    rank_delta_abs: 146
    rank_delta_direction: worse
    sort_value: 0.036
    sort_std: 0.002
    is_best: false
  - model: SAT
    model_key: sat
    model_plain: SAT
    value: 0.036
    std: 0.002
    paper_value: 0.036
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: chen2022structure
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 35
    true_value: 0.036
    true_std: 0.002
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.036
    sort_std: 0.002
    is_best: false
  - model: AgentNet
    model_key: agentnet
    model_plain: AgentNet
    value: 0.144
    std: 0.016
    paper_value: 0.144
    paper_std: 0.016
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Martinkus et al. 2023
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 38
    true_value: 0.04
    true_std: 0.006
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10399999999999998
    value_note: ''
    paper_rank: 230
    rank_delta: 192
    rank_delta_abs: 192
    rank_delta_direction: worse
    sort_value: 0.04
    sort_std: 0.006
    is_best: false
  - model: AgentNet
    model_key: agentnet
    model_plain: AgentNet
    value: 0.04
    std: 0.006
    paper_value: 0.04
    paper_std: 0.006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: martinkus2023agentbased
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 38
    true_value: 0.04
    true_std: 0.006
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.04
    sort_std: 0.006
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.142
    std: 0.01
    paper_value: 0.142
    paper_std: 0.01
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Corso et al. 2020
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 48
    true_value: 0.05727021078890476
    true_std: 0.006639614126119909
    value_gap_source_arxiv: '2402.10793'
    value_gap_source_title: An end-to-end attention-based approach for learning on
      graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08472978921109522
    value_note: ''
    paper_rank: 230
    rank_delta: 182
    rank_delta_abs: 182
    rank_delta_direction: worse
    sort_value: 0.05727021078890476
    sort_std: 0.006639614126119909
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.067
    std: 0.009
    paper_value: 0.067
    paper_std: 0.009
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: corso2020principal
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 48
    true_value: 0.05727021078890476
    true_std: 0.006639614126119909
    value_gap_source_arxiv: '2402.10793'
    value_gap_source_title: An end-to-end attention-based approach for learning on
      graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.009729789211095241
    value_note: ''
    paper_rank: 81
    rank_delta: 33
    rank_delta_abs: 33
    rank_delta_direction: worse
    sort_value: 0.05727021078890476
    sort_std: 0.006639614126119909
    is_best: false
  - model: AWE
    model_key: awe
    model_plain: AWE
    value: 0.094
    std: 0.005
    paper_value: 0.094
    paper_std: 0.005
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Ivanov et al. 2018
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 56
    true_value: 0.059
    true_std: 0.005
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 0.035
    value_note: ''
    paper_rank: 181
    rank_delta: 125
    rank_delta_abs: 125
    rank_delta_direction: worse
    sort_value: 0.059
    sort_std: 0.005
    is_best: false
  - model: AWE
    model_key: awe
    model_plain: AWE
    value: 0.059
    std: 0.005
    paper_value: 0.059
    paper_std: 0.005
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ivanov2018anonymous
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 56
    true_value: 0.059
    true_std: 0.005
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 56
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.059
    sort_std: 0.005
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
    source_ref: Xu et al. 2018
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
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
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.088
    std: 0.002
    paper_value: 0.088
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: xu2018how
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 75
    true_value: 0.065
    true_std: 0.004
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.022999999999999993
    value_note: ''
    paper_rank: 170
    rank_delta: 95
    rank_delta_abs: 95
    rank_delta_direction: worse
    sort_value: 0.065
    sort_std: 0.004
    is_best: false
  - model: DeepGraph
    model_key: deepgraph
    model_plain: DeepGraph
    value: 0.072
    std: 0.004
    paper_value: 0.072
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhao et al. 2023
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 114
    true_value: 0.072
    true_std: 0.004
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 114
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.072
    sort_std: 0.004
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
    source_ref: Kreuzer et al. 2021
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 224
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
    paper_rank: 225
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.1341
    sort_std: 0.0063
    is_best: false
  - model: GEAET
    model_key: geaet
    model_plain: GEAET
    value: 0.193
    std: 0.001
    paper_value: 0.193
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Liang et al. 2024
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 255
    true_value: 0.193
    true_std: 0.001
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 255
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.193
    sort_std: 0.001
    is_best: false
  metric: MAE
  higher_is_better: false
- &id014
  dataset: ogbl-collab
  rows:
  - model: QGAT
    model_key: qgat
    model_plain: QGAT
    value: 0.512
    std: 0.0192
    metric: Hits@50
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
    sort_value: 0.512
    sort_std: 0.0192
    is_best: true
  - model: Graph transformer
    model_key: graph transformer
    model_plain: Graph transformer
    value: 0.497
    std: 0.0059
    paper_value: 0.497
    paper_std: 0.0059
    metric: Hits@50
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 3
    true_value: 0.497
    true_std: 0.0059
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.497
    sort_std: 0.0059
    is_best: true
  - model: GPM
    model_key: gpm
    model_plain: GPM
    value: 0.497
    std: 0.0059
    paper_value: 0.497
    paper_std: 0.0059
    metric: Hits@50
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 2
    true_value: 0.497
    true_std: 0.0059
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.497
    sort_std: 0.0059
    is_best: true
  - model: GATv2
    model_key: gatv2
    model_plain: GATv2
    value: 0.497
    std: 0.0308
    metric: Hits@50
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
    global_rank: 4
    sort_value: 0.497
    sort_std: 0.0308
    is_best: true
  - model: GPM w/o PE
    model_key: gpm w/o pe
    model_plain: GPM w/o PE
    value: 0.4959
    std: 0.0065
    paper_value: 0.4959
    paper_std: 0.0065
    metric: Hits@50
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 5
    true_value: 0.4959
    true_std: 0.0065
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4959
    sort_std: 0.0065
    is_best: true
  - model: LLP
    model_key: llp
    model_plain: LLP
    value: 0.491
    std: 0.0057
    paper_value: 0.491
    paper_std: 0.0057
    metric: Hits@50
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: guo2023linkless
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 6
    true_value: 0.491
    true_std: 0.0057
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.491
    sort_std: 0.0057
    is_best: true
  - model: GPM w/o AP
    model_key: gpm w/o ap
    model_plain: GPM w/o AP
    value: 0.4843
    std: 0.0097
    paper_value: 0.4843
    paper_std: 0.0097
    metric: Hits@50
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 7
    true_value: 0.4843
    true_std: 0.0097
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4843
    sort_std: 0.0097
    is_best: true
  - model: GPM w/o PE & AP
    model_key: gpm w/o pe & ap
    model_plain: GPM w/o PE & AP
    value: 0.4824
    std: 0.0097
    paper_value: 0.4824
    paper_std: 0.0097
    metric: Hits@50
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 8
    true_value: 0.4824
    true_std: 0.0097
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4824
    sort_std: 0.0097
    is_best: false
  - model: RUM
    model_key: rum
    model_plain: RUM
    value: 0.4819
    std: 0.0094
    paper_value: 0.4819
    paper_std: 0.0094
    metric: Hits@50
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wang2024nonconvolutional
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 9
    true_value: 0.4819
    true_std: 0.0094
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4819
    sort_std: 0.0094
    is_best: false
  - model: GPM GRU
    model_key: gpm gru
    model_plain: GPM GRU
    value: 0.4812
    std: 0.0055
    paper_value: 0.4812
    paper_std: 0.0055
    metric: Hits@50
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 10
    true_value: 0.4812
    true_std: 0.0055
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4812
    sort_std: 0.0055
    is_best: false
  - model: GPM Mean
    model_key: gpm mean
    model_plain: GPM Mean
    value: 0.4783
    std: 0.01
    paper_value: 0.4783
    paper_std: 0.01
    metric: Hits@50
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 11
    true_value: 0.4783
    true_std: 0.01
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4783
    sort_std: 0.01
    is_best: false
  - model: Nagphormer
    model_key: nagphormer
    model_plain: Nagphormer
    value: 0.4756
    std: 0.0052
    paper_value: 0.4756
    paper_std: 0.0052
    metric: Hits@50
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: chen2023nagphormer
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 12
    true_value: 0.4756
    true_std: 0.0052
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4756
    sort_std: 0.0052
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.4663
    std: 0.028
    metric: Hits@50
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
    global_rank: 13
    sort_value: 0.4663
    sort_std: 0.028
    is_best: true
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.4656
    std: 0.0062
    paper_value: 0.4656
    paper_std: 0.0062
    metric: Hits@50
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu2022nodeformer
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 14
    true_value: 0.4656
    true_std: 0.0062
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4656
    sort_std: 0.0062
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.4475
    std: 0.0107
    paper_value: 0.4475
    paper_std: 0.0107
    metric: Hits@50
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: kipf2017semisupervised
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 15
    true_value: 0.4475
    true_std: 0.0107
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4475
    sort_std: 0.0107
    is_best: false
  metric: Hits@50
  higher_is_better: true
- &id012
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
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7174
    std: 0.0029
    paper_value: 0.7174
    paper_std: 0.0029
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: kipf2017semisupervised
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 14
    true_value: 0.7353
    true_std: 0.0012
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.017899999999999916
    value_note: ''
    paper_rank: 64
    rank_delta: 50
    rank_delta_abs: 50
    rank_delta_direction: worse
    sort_value: 0.7353
    sort_std: 0.0012
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.7201
    std: 0.002
    paper_value: 0.7201
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: velickovic2018graph
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 17
    true_value: 0.733
    true_std: 0.0018
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.012900000000000023
    value_note: ''
    paper_rank: 50
    rank_delta: 33
    rank_delta_abs: 33
    rank_delta_direction: worse
    sort_value: 0.733
    sort_std: 0.0018
    is_best: false
  - model: GPM
    model_key: gpm
    model_plain: GPM
    value: 0.7289
    std: 0.0068
    paper_value: 0.7289
    paper_std: 0.0068
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 27
    true_value: 0.7289
    true_std: 0.0068
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 27
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7289
    sort_std: 0.0068
    is_best: false
  - model: GOAT
    model_key: goat
    model_plain: GOAT
    value: 0.7241
    std: 0.004
    paper_value: 0.7241
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: kong2023goat
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 33
    true_value: 0.7276
    true_std: 0.0029
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0035000000000000586
    value_note: global 0.7276 within std
    paper_rank: 42
    rank_delta: 9
    rank_delta_abs: 9
    rank_delta_direction: worse
    sort_value: 0.7276
    sort_std: 0.0029
    is_best: false
  - model: Graph-Mamba
    model_key: graph-mamba
    model_plain: Graph-Mamba
    value: 0.7248
    std: 0.0
    paper_value: 0.7248
    paper_std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: behrouz2024graph
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 38
    true_value: 0.7248
    true_std: 0.0
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7248
    sort_std: 0.0
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.694
    std: 0.005
    paper_value: 0.694
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: gasteiger2018combining
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 58
    true_value: 0.719
    true_std: 0.0025
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.025000000000000022
    value_note: ''
    paper_rank: 79
    rank_delta: 21
    rank_delta_abs: 21
    rank_delta_direction: worse
    sort_value: 0.719
    sort_std: 0.0025
    is_best: false
  - model: Nagphormer
    model_key: nagphormer
    model_plain: Nagphormer
    value: 0.7013
    std: 0.0055
    paper_value: 0.7013
    paper_std: 0.0055
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: chen2023nagphormer
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 67
    true_value: 0.7152
    true_std: 0.0024
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.013899999999999912
    value_note: ''
    paper_rank: 77
    rank_delta: 10
    rank_delta_abs: 10
    rank_delta_direction: worse
    sort_value: 0.7152
    sort_std: 0.0024
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.7097
    std: 0.0041
    paper_value: 0.7097
    paper_std: 0.0041
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: rampasek2022recipe
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 71
    true_value: 0.7123
    true_std: 0.0059
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0026000000000000467
    value_note: global 0.7123 within std
    paper_rank: 75
    rank_delta: 4
    rank_delta_abs: 4
    rank_delta_direction: worse
    sort_value: 0.7123
    sort_std: 0.0059
    is_best: false
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.711
    std: 0.0012
    paper_value: 0.711
    paper_std: 0.0012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: chien2021adaptive
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 75
    true_value: 0.711
    true_std: 0.0012
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 75
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.711
    sort_std: 0.0012
    is_best: false
  - model: RUM
    model_key: rum
    model_plain: RUM
    value: 0.7054
    std: 0.003
    paper_value: 0.7054
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wang2024nonconvolutional
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 76
    true_value: 0.7054
    true_std: 0.003
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 76
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7054
    sort_std: 0.003
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.6719
    std: 0.0083
    paper_value: 0.6719
    paper_std: 0.0083
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu2022nodeformer
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 89
    true_value: 0.6778
    true_std: 0.0028
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.005899999999999905
    value_note: global 0.6778 within std
    paper_rank: 90
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.6778
    sort_std: 0.0028
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id013
  dataset: ogbn-products
  rows:
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.9334
    std: 0.0006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05697'
    title: 'Diffusing to the Top: Boost Graph Neural Networks with Minimal Hyperparameter
      Tuning'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.9334
    sort_std: 0.0006
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7564
    std: 0.0021
    paper_value: 0.7564
    paper_std: 0.0021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: kipf2017semisupervised
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 2
    true_value: 0.9115
    true_std: 0.0004
    value_gap_source_arxiv: '2410.05697'
    value_gap_source_title: 'Diffusing to the Top: Boost Graph Neural Networks with
      Minimal Hyperparameter Tuning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.15510000000000002
    value_note: ''
    paper_rank: 35
    rank_delta: 33
    rank_delta_abs: 33
    rank_delta_direction: worse
    sort_value: 0.9115
    sort_std: 0.0004
    is_best: false
  - model: GLEM-GNN
    model_key: glem-gnn
    model_plain: GLEM-GNN
    value: 0.8736
    std: 0.0007
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
    global_rank: 3
    sort_value: 0.8736
    sort_std: 0.0007
    is_best: false
  - model: GLEM-LM
    model_key: glem-lm
    model_plain: GLEM-LM
    value: 0.8483
    std: 0.0004
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
    global_rank: 4
    sort_value: 0.8483
    sort_std: 0.0004
    is_best: false
  - model: GPM
    model_key: gpm
    model_plain: GPM
    value: 0.8262
    std: 0.0039
    paper_value: 0.8262
    paper_std: 0.0039
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 6
    true_value: 0.8262
    true_std: 0.0039
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8262
    sort_std: 0.0039
    is_best: false
  - model: GOAT
    model_key: goat
    model_plain: GOAT
    value: 0.82
    std: 0.0043
    paper_value: 0.82
    paper_std: 0.0043
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: kong2023goat
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 9
    true_value: 0.82
    true_std: 0.0043
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.82
    sort_std: 0.0043
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.7945
    std: 0.0059
    paper_value: 0.7945
    paper_std: 0.0059
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: velickovic2018graph
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 19
    true_value: 0.798
    true_std: 0.003
    value_gap_source_arxiv: '2405.19121'
    value_gap_source_title: Spatio-Spectral Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0035000000000000586
    value_note: global 0.7980 within std
    paper_rank: 20
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.798
    sort_std: 0.003
    is_best: false
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.7976
    std: 0.0059
    paper_value: 0.7976
    paper_std: 0.0059
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: chien2021adaptive
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 20
    true_value: 0.7976
    true_std: 0.0059
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7976
    sort_std: 0.0059
    is_best: false
  - model: RUM
    model_key: rum
    model_plain: RUM
    value: 0.7868
    std: 0.014
    paper_value: 0.7868
    paper_std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wang2024nonconvolutional
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 25
    true_value: 0.7868
    true_std: 0.014
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7868
    sort_std: 0.014
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.7758
    std: 0.0047
    paper_value: 0.7758
    paper_std: 0.0047
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: gasteiger2018combining
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 29
    true_value: 0.7758
    true_std: 0.0047
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7758
    sort_std: 0.0047
    is_best: false
  - model: Nagphormer
    model_key: nagphormer
    model_plain: Nagphormer
    value: 0.7355
    std: 0.0021
    paper_value: 0.7355
    paper_std: 0.0021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: chen2023nagphormer
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 37
    true_value: 0.7528
    true_std: 0.0004
    value_gap_source_arxiv: '2312.11109'
    value_gap_source_title: Graph Transformers for Large Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.017299999999999982
    value_note: ''
    paper_rank: 40
    rank_delta: 3
    rank_delta_abs: 3
    rank_delta_direction: worse
    sort_value: 0.7528
    sort_std: 0.0004
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.7293
    std: 0.0013
    paper_value: 0.7293
    paper_std: 0.0013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu2022nodeformer
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 42
    true_value: 0.7293
    true_std: 0.0013
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 42
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7293
    sort_std: 0.0013
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id015
  dataset: twitch-gamers
  rows:
  - model: GPM + DANN
    model_key: gpm + dann
    model_plain: GPM + DANN
    value: 0.6298
    std: null
    paper_value: 0.6298
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 1
    true_value: 0.6298
    true_std: null
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6298
    sort_std: null
    is_best: true
  - model: GPM + SSReg
    model_key: gpm + ssreg
    model_plain: GPM + SSReg
    value: 0.6277
    std: null
    paper_value: 0.6277
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 2
    true_value: 0.6277
    true_std: null
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6277
    sort_std: null
    is_best: false
  - model: GPM
    model_key: gpm
    model_plain: GPM
    value: 0.6163
    std: null
    paper_value: 0.6163
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 3
    true_value: 0.6163
    true_std: null
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6163
    sort_std: null
    is_best: false
  - model: StruRW
    model_key: strurw
    model_plain: StruRW
    value: 0.6146
    std: null
    paper_value: 0.6146
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: liu2023structural
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 4
    true_value: 0.6146
    true_std: null
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6146
    sort_std: null
    is_best: false
  - model: DAGNN
    model_key: dagnn
    model_plain: DAGNN
    value: 0.6071
    std: null
    paper_value: 0.6071
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ganin2016domain
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 5
    true_value: 0.6071
    true_std: null
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6071
    sort_std: null
    is_best: false
  - model: SSReg
    model_key: ssreg
    model_plain: SSReg
    value: 0.6043
    std: null
    paper_value: 0.6043
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: you2023graph
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 6
    true_value: 0.6043
    true_std: null
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6043
    sort_std: null
    is_best: false
  - model: SR-GNN
    model_key: sr-gnn
    model_plain: SR-GNN
    value: 0.5965
    std: null
    paper_value: 0.5965
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: zhu2021shift
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 7
    true_value: 0.5965
    true_std: null
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5965
    sort_std: null
    is_best: false
  - model: RUM
    model_key: rum
    model_plain: RUM
    value: 0.5859
    std: null
    paper_value: 0.5859
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wang2024nonconvolutional
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 8
    true_value: 0.5859
    true_std: null
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5859
    sort_std: null
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.5686
    std: null
    paper_value: 0.5686
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: velickovic2018graph
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 9
    true_value: 0.5686
    true_std: null
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5686
    sort_std: null
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.5668
    std: null
    paper_value: 0.5668
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: kipf2017semisupervised
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 10
    true_value: 0.5668
    true_std: null
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5668
    sort_std: null
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.5426
    std: null
    paper_value: 0.5426
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: gasteiger2018combining
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 11
    true_value: 0.5426
    true_std: null
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5426
    sort_std: null
    is_best: false
  - model: Nagphormer
    model_key: nagphormer
    model_plain: Nagphormer
    value: 0.5419
    std: null
    paper_value: 0.5419
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: chen2023nagphormer
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 12
    true_value: 0.5419
    true_std: null
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5419
    sort_std: null
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.5417
    std: null
    paper_value: 0.5417
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu2022nodeformer
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 13
    true_value: 0.5417
    true_std: null
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5417
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
  - *id004
  - *id005
  - *id006
- benchmark: Heterophilic Graphs
  datasets:
  - *id007
- benchmark: TU Dortmund
  datasets:
  - *id008
  - *id009
  - *id010
- benchmark: GNNBenchmark
  datasets:
  - *id011
- benchmark: OGB
  datasets:
  - *id012
  - *id013
  - *id014
- benchmark: LINKX Benchmarks
  datasets:
  - *id015
- benchmark: PyG Imported Datasets
  datasets:
  - *id016
  - *id017
main_figure: /figures/2501.18739/main_figure.png
---

