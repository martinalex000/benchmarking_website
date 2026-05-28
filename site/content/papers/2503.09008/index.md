---
title: City-Networks
arxiv_id: '2503.09008'
source_url: ''
authors: []
published_date: Mar 2025
published_date_iso: 2025-03
abstract: Long-range dependencies are critical for effective graph representation
  learning, yet most existing datasets focus on small graphs tailored to inductive
  tasks, offering limited insight into long-range interactions. Current evaluations
  primarily compare models employing global attention (e.g., graph transformers) with
  those using local neighborhood aggregation (e.g., message-passing neural networks)
  without a direct measurement of long-range dependency. In this work, we introduce
  City-Networks, a novel large-scale transductive learning dataset derived from real-world
  city road networks. This dataset features graphs with over $10^5$ nodes and significantly
  larger diameters than those in existing benchmarks, naturally embodying long-range
  information. We annotate the graphs based on local node eccentricities, ensuring
  that the classification task inherently requires information from distant nodes.
  Furthermore, we propose a generic measurement based on the Jacobians of neighbors
  from distant hops, offering a principled quantification of long-range dependencies.
  Finally, we provide theoretical justifications for both our dataset design and the
  proposed measurement—particularly by focusing on over-smoothing and influence score
  dilution, which establishes a robust foundation for further exploration of long-range
  interactions in graph neural networks. Our https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.CityNetwork.html#torch_geometric.datasets.CityNetwork
  dataset and https://pytorch-geometric.readthedocs.io/en/latest/modules/utils.html#torch_geometric.utils.total_influence
  measurement are available on https://pytorch-geometric.readthedocs.io/en/latest/index.html
  PyTorch Geometric, and the code for reproducing the experimental results can be
  found at https://github.com/LeonResearch/City-Networks github.com/LeonResearch/City-Networks.
codebase_url: ''
extraction_model: MiniMaxAI/MiniMax-M2.5
has_results: true
paper_type: dataset
proposed_models: []
mrr: null
adjusted_mrr: null
mrr_dataset_count: 0
benchmark_categories:
- TU Dortmund
- City-Networks
task_categories:
- graph_classification
- node_classification
experiment_scopes:
- graph-level
- node-level
results:
- &id001
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
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.52
    std: 0.003
    paper_value: 0.52
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
    date: Mar 2025
    date_display: Mar 2025
    date_iso: 2025-03
    global_rank: 35
    true_value: 0.762
    true_std: null
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.242
    value_note: ''
    paper_rank: 67
    rank_delta: 32
    rank_delta_abs: 32
    rank_delta_direction: worse
    sort_value: 0.762
    sort_std: null
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.501
    std: 0.007
    paper_value: 0.501
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
    date: Mar 2025
    date_display: Mar 2025
    date_iso: 2025-03
    global_rank: 39
    true_value: 0.7546
    true_std: null
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.25360000000000005
    value_note: ''
    paper_rank: 67
    rank_delta: 28
    rank_delta_abs: 28
    rank_delta_direction: worse
    sort_value: 0.7546
    sort_std: null
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.483
    std: 0.003
    paper_value: 0.483
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
    date: Mar 2025
    date_display: Mar 2025
    date_iso: 2025-03
    global_rank: 49
    true_value: 0.6709999999999999
    true_std: 0.011000000000000001
    value_gap_source_arxiv: '2512.14619'
    value_gap_source_title: 'ParaFormer: A Generalized PageRank Graph Transformer
      for Graph Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.18799999999999994
    value_note: ''
    paper_rank: 68
    rank_delta: 19
    rank_delta_abs: 19
    rank_delta_direction: worse
    sort_value: 0.6709999999999999
    sort_std: 0.011000000000000001
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.279
    std: 0.001
    paper_value: 0.279
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
    date: Mar 2025
    date_display: Mar 2025
    date_iso: 2025-03
    global_rank: 51
    true_value: 0.6659999999999999
    true_std: 0.006999999999999999
    value_gap_source_arxiv: '2512.14619'
    value_gap_source_title: 'ParaFormer: A Generalized PageRank Graph Transformer
      for Graph Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.3869999999999999
    value_note: ''
    paper_rank: 76
    rank_delta: 25
    rank_delta_abs: 25
    rank_delta_direction: worse
    sort_value: 0.6659999999999999
    sort_std: 0.006999999999999999
    is_best: false
  - model: ChebNet
    model_key: chebnet
    model_plain: ChebNet
    value: 0.547
    std: 0.002
    paper_value: 0.547
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2025
    date_display: Mar 2025
    date_iso: 2025-03
    global_rank: 64
    true_value: 0.5907
    true_std: null
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04369999999999996
    value_note: ''
    paper_rank: 66
    rank_delta: 2
    rank_delta_abs: 2
    rank_delta_direction: worse
    sort_value: 0.5907
    sort_std: null
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.554
    std: 0.002
    paper_value: 0.554
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2025
    date_display: Mar 2025
    date_iso: 2025-03
    global_rank: 66
    true_value: 0.554
    true_std: 0.002
    value_gap_source_arxiv: '2503.09008'
    value_gap_source_title: City-Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 66
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.554
    sort_std: 0.002
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.495
    std: 0.004
    paper_value: 0.495
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
    date: Mar 2025
    date_display: Mar 2025
    date_iso: 2025-03
    global_rank: 68
    true_value: 0.495
    true_std: 0.004
    value_gap_source_arxiv: '2503.09008'
    value_gap_source_title: City-Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 68
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.495
    sort_std: 0.004
    is_best: false
  - model: GCNII
    model_key: gcnii
    model_plain: GCNII
    value: 0.482
    std: 0.003
    paper_value: 0.482
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
    date: Mar 2025
    date_display: Mar 2025
    date_iso: 2025-03
    global_rank: 69
    true_value: 0.482
    true_std: 0.003
    value_gap_source_arxiv: '2503.09008'
    value_gap_source_title: City-Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 69
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.482
    sort_std: 0.003
    is_best: false
  - model: + DropEdge
    model_key: + dropedge
    model_plain: + DropEdge
    value: 0.45
    std: 0.003
    paper_value: 0.45
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
    date: Mar 2025
    date_display: Mar 2025
    date_iso: 2025-03
    global_rank: 71
    true_value: 0.45
    true_std: 0.003
    value_gap_source_arxiv: '2503.09008'
    value_gap_source_title: City-Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 71
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.45
    sort_std: 0.003
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id005
  dataset: London
  rows:
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.554
    std: 0.002
    paper_value: 0.554
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2025
    date_display: Mar 2025
    date_iso: 2025-03
    global_rank: 1
    true_value: 0.554
    true_std: 0.002
    value_gap_source_arxiv: '2503.09008'
    value_gap_source_title: City-Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.554
    sort_std: 0.002
    is_best: true
  - model: ChebNet
    model_key: chebnet
    model_plain: ChebNet
    value: 0.547
    std: 0.002
    paper_value: 0.547
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2025
    date_display: Mar 2025
    date_iso: 2025-03
    global_rank: 2
    true_value: 0.547
    true_std: 0.002
    value_gap_source_arxiv: '2503.09008'
    value_gap_source_title: City-Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.547
    sort_std: 0.002
    is_best: false
  - model: IM-GCN
    model_key: im-gcn
    model_plain: IM-GCN
    value: 0.538
    std: 0.003
    metric: Accuracy
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
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.538
    sort_std: 0.003
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.52
    std: 0.003
    paper_value: 0.52
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
    date: Mar 2025
    date_display: Mar 2025
    date_iso: 2025-03
    global_rank: 4
    true_value: 0.52
    true_std: 0.003
    value_gap_source_arxiv: '2503.09008'
    value_gap_source_title: City-Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.52
    sort_std: 0.003
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.501
    std: 0.007
    paper_value: 0.501
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
    date: Mar 2025
    date_display: Mar 2025
    date_iso: 2025-03
    global_rank: 5
    true_value: 0.501
    true_std: 0.007
    value_gap_source_arxiv: '2503.09008'
    value_gap_source_title: City-Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.501
    sort_std: 0.007
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.495
    std: 0.004
    paper_value: 0.495
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
    date: Mar 2025
    date_display: Mar 2025
    date_iso: 2025-03
    global_rank: 6
    true_value: 0.495
    true_std: 0.004
    value_gap_source_arxiv: '2503.09008'
    value_gap_source_title: City-Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.495
    sort_std: 0.004
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.483
    std: 0.003
    paper_value: 0.483
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
    date: Mar 2025
    date_display: Mar 2025
    date_iso: 2025-03
    global_rank: 7
    true_value: 0.483
    true_std: 0.003
    value_gap_source_arxiv: '2503.09008'
    value_gap_source_title: City-Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.483
    sort_std: 0.003
    is_best: false
  - model: GCNII
    model_key: gcnii
    model_plain: GCNII
    value: 0.482
    std: 0.003
    paper_value: 0.482
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
    date: Mar 2025
    date_display: Mar 2025
    date_iso: 2025-03
    global_rank: 8
    true_value: 0.482
    true_std: 0.003
    value_gap_source_arxiv: '2503.09008'
    value_gap_source_title: City-Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.482
    sort_std: 0.003
    is_best: false
  - model: + DropEdge
    model_key: + dropedge
    model_plain: + DropEdge
    value: 0.45
    std: 0.003
    paper_value: 0.45
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
    date: Mar 2025
    date_display: Mar 2025
    date_iso: 2025-03
    global_rank: 9
    true_value: 0.45
    true_std: 0.003
    value_gap_source_arxiv: '2503.09008'
    value_gap_source_title: City-Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.45
    sort_std: 0.003
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.279
    std: 0.001
    paper_value: 0.279
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
    date: Mar 2025
    date_display: Mar 2025
    date_iso: 2025-03
    global_rank: 10
    true_value: 0.279
    true_std: 0.001
    value_gap_source_arxiv: '2503.09008'
    value_gap_source_title: City-Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.279
    sort_std: 0.001
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: Los Angeles
  rows:
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.638
    std: 0.006
    paper_value: 0.638
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
    date: Mar 2025
    date_display: Mar 2025
    date_iso: 2025-03
    global_rank: 1
    true_value: 0.638
    true_std: 0.006
    value_gap_source_arxiv: '2503.09008'
    value_gap_source_title: City-Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.638
    sort_std: 0.006
    is_best: true
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.614
    std: 0.003
    paper_value: 0.614
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
    date: Mar 2025
    date_display: Mar 2025
    date_iso: 2025-03
    global_rank: 3
    true_value: 0.614
    true_std: 0.003
    value_gap_source_arxiv: '2503.09008'
    value_gap_source_title: City-Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.614
    sort_std: 0.003
    is_best: false
  - model: ChebNet
    model_key: chebnet
    model_plain: ChebNet
    value: 0.614
    std: 0.004
    paper_value: 0.614
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
    date: Mar 2025
    date_display: Mar 2025
    date_iso: 2025-03
    global_rank: 2
    true_value: 0.614
    true_std: 0.004
    value_gap_source_arxiv: '2503.09008'
    value_gap_source_title: City-Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.614
    sort_std: 0.004
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.601
    std: 0.007
    paper_value: 0.601
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
    date: Mar 2025
    date_display: Mar 2025
    date_iso: 2025-03
    global_rank: 4
    true_value: 0.601
    true_std: 0.007
    value_gap_source_arxiv: '2503.09008'
    value_gap_source_title: City-Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.601
    sort_std: 0.007
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.598
    std: 0.005
    paper_value: 0.598
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
    date: Mar 2025
    date_display: Mar 2025
    date_iso: 2025-03
    global_rank: 5
    true_value: 0.598
    true_std: 0.005
    value_gap_source_arxiv: '2503.09008'
    value_gap_source_title: City-Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.598
    sort_std: 0.005
    is_best: false
  - model: IM-GCN
    model_key: im-gcn
    model_plain: IM-GCN
    value: 0.598
    std: 0.002
    metric: Accuracy
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
    uses_external_data: false
    is_global_top: true
    global_rank: 6
    sort_value: 0.598
    sort_std: 0.002
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.595
    std: 0.003
    paper_value: 0.595
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
    date: Mar 2025
    date_display: Mar 2025
    date_iso: 2025-03
    global_rank: 7
    true_value: 0.595
    true_std: 0.003
    value_gap_source_arxiv: '2503.09008'
    value_gap_source_title: City-Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.595
    sort_std: 0.003
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.583
    std: 0.003
    paper_value: 0.583
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
    date: Mar 2025
    date_display: Mar 2025
    date_iso: 2025-03
    global_rank: 8
    true_value: 0.583
    true_std: 0.003
    value_gap_source_arxiv: '2503.09008'
    value_gap_source_title: City-Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.583
    sort_std: 0.003
    is_best: false
  - model: GCNII
    model_key: gcnii
    model_plain: GCNII
    value: 0.56
    std: 0.003
    paper_value: 0.56
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
    date: Mar 2025
    date_display: Mar 2025
    date_iso: 2025-03
    global_rank: 9
    true_value: 0.56
    true_std: 0.003
    value_gap_source_arxiv: '2503.09008'
    value_gap_source_title: City-Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.56
    sort_std: 0.003
    is_best: false
  - model: + DropEdge
    model_key: + dropedge
    model_plain: + DropEdge
    value: 0.555
    std: 0.003
    paper_value: 0.555
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
    date: Mar 2025
    date_display: Mar 2025
    date_iso: 2025-03
    global_rank: 10
    true_value: 0.555
    true_std: 0.003
    value_gap_source_arxiv: '2503.09008'
    value_gap_source_title: City-Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.555
    sort_std: 0.003
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.241
    std: 0.005
    paper_value: 0.241
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
    date: Mar 2025
    date_display: Mar 2025
    date_iso: 2025-03
    global_rank: 11
    true_value: 0.241
    true_std: 0.005
    value_gap_source_arxiv: '2503.09008'
    value_gap_source_title: City-Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.241
    sort_std: 0.005
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id002
  dataset: Paris
  rows:
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.551
    std: 0.008
    paper_value: 0.551
    paper_std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2025
    date_display: Mar 2025
    date_iso: 2025-03
    global_rank: 1
    true_value: 0.551
    true_std: 0.008
    value_gap_source_arxiv: '2503.09008'
    value_gap_source_title: City-Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.551
    sort_std: 0.008
    is_best: true
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.546
    std: 0.002
    paper_value: 0.546
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2025
    date_display: Mar 2025
    date_iso: 2025-03
    global_rank: 2
    true_value: 0.546
    true_std: 0.002
    value_gap_source_arxiv: '2503.09008'
    value_gap_source_title: City-Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.546
    sort_std: 0.002
    is_best: true
  - model: IM-GCN
    model_key: im-gcn
    model_plain: IM-GCN
    value: 0.544
    std: 0.002
    metric: Accuracy
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
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.544
    sort_std: 0.002
    is_best: true
  - model: ChebNet
    model_key: chebnet
    model_plain: ChebNet
    value: 0.541
    std: 0.002
    paper_value: 0.541
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2025
    date_display: Mar 2025
    date_iso: 2025-03
    global_rank: 4
    true_value: 0.541
    true_std: 0.002
    value_gap_source_arxiv: '2503.09008'
    value_gap_source_title: City-Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.541
    sort_std: 0.002
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.532
    std: 0.003
    paper_value: 0.532
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
    date: Mar 2025
    date_display: Mar 2025
    date_iso: 2025-03
    global_rank: 5
    true_value: 0.532
    true_std: 0.003
    value_gap_source_arxiv: '2503.09008'
    value_gap_source_title: City-Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.532
    sort_std: 0.003
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.521
    std: 0.006
    paper_value: 0.521
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
    date: Mar 2025
    date_display: Mar 2025
    date_iso: 2025-03
    global_rank: 6
    true_value: 0.521
    true_std: 0.006
    value_gap_source_arxiv: '2503.09008'
    value_gap_source_title: City-Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.521
    sort_std: 0.006
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.52
    std: 0.008
    paper_value: 0.52
    paper_std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2025
    date_display: Mar 2025
    date_iso: 2025-03
    global_rank: 7
    true_value: 0.52
    true_std: 0.008
    value_gap_source_arxiv: '2503.09008'
    value_gap_source_title: City-Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.52
    sort_std: 0.008
    is_best: false
  - model: GCNII
    model_key: gcnii
    model_plain: GCNII
    value: 0.513
    std: 0.002
    paper_value: 0.513
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2025
    date_display: Mar 2025
    date_iso: 2025-03
    global_rank: 8
    true_value: 0.513
    true_std: 0.002
    value_gap_source_arxiv: '2503.09008'
    value_gap_source_title: City-Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.513
    sort_std: 0.002
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.511
    std: 0.003
    paper_value: 0.511
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
    date: Mar 2025
    date_display: Mar 2025
    date_iso: 2025-03
    global_rank: 9
    true_value: 0.511
    true_std: 0.003
    value_gap_source_arxiv: '2503.09008'
    value_gap_source_title: City-Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.511
    sort_std: 0.003
    is_best: false
  - model: + DropEdge
    model_key: + dropedge
    model_plain: + DropEdge
    value: 0.482
    std: 0.002
    paper_value: 0.482
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2025
    date_display: Mar 2025
    date_iso: 2025-03
    global_rank: 10
    true_value: 0.482
    true_std: 0.002
    value_gap_source_arxiv: '2503.09008'
    value_gap_source_title: City-Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.482
    sort_std: 0.002
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.255
    std: 0.004
    paper_value: 0.255
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
    date: Mar 2025
    date_display: Mar 2025
    date_iso: 2025-03
    global_rank: 11
    true_value: 0.255
    true_std: 0.004
    value_gap_source_arxiv: '2503.09008'
    value_gap_source_title: City-Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.255
    sort_std: 0.004
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id003
  dataset: Shanghai
  rows:
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.702
    std: 0.004
    paper_value: 0.702
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
    date: Mar 2025
    date_display: Mar 2025
    date_iso: 2025-03
    global_rank: 1
    true_value: 0.702
    true_std: 0.004
    value_gap_source_arxiv: '2503.09008'
    value_gap_source_title: City-Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.702
    sort_std: 0.004
    is_best: true
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.683
    std: 0.005
    paper_value: 0.683
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
    date: Mar 2025
    date_display: Mar 2025
    date_iso: 2025-03
    global_rank: 2
    true_value: 0.683
    true_std: 0.005
    value_gap_source_arxiv: '2503.09008'
    value_gap_source_title: City-Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.683
    sort_std: 0.005
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.68
    std: 0.005
    paper_value: 0.68
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
    date: Mar 2025
    date_display: Mar 2025
    date_iso: 2025-03
    global_rank: 3
    true_value: 0.68
    true_std: 0.005
    value_gap_source_arxiv: '2503.09008'
    value_gap_source_title: City-Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.68
    sort_std: 0.005
    is_best: false
  - model: ChebNet
    model_key: chebnet
    model_plain: ChebNet
    value: 0.665
    std: 0.001
    paper_value: 0.665
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
    date: Mar 2025
    date_display: Mar 2025
    date_iso: 2025-03
    global_rank: 4
    true_value: 0.665
    true_std: 0.001
    value_gap_source_arxiv: '2503.09008'
    value_gap_source_title: City-Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.665
    sort_std: 0.001
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.641
    std: 0.003
    paper_value: 0.641
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
    date: Mar 2025
    date_display: Mar 2025
    date_iso: 2025-03
    global_rank: 5
    true_value: 0.641
    true_std: 0.003
    value_gap_source_arxiv: '2503.09008'
    value_gap_source_title: City-Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.641
    sort_std: 0.003
    is_best: false
  - model: IM-GCN
    model_key: im-gcn
    model_plain: IM-GCN
    value: 0.634
    std: 0.008
    metric: Accuracy
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
    uses_external_data: false
    is_global_top: true
    global_rank: 6
    sort_value: 0.634
    sort_std: 0.008
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.63
    std: 0.005
    paper_value: 0.63
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
    date: Mar 2025
    date_display: Mar 2025
    date_iso: 2025-03
    global_rank: 7
    true_value: 0.63
    true_std: 0.005
    value_gap_source_arxiv: '2503.09008'
    value_gap_source_title: City-Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.63
    sort_std: 0.005
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.621
    std: 0.002
    paper_value: 0.621
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2025
    date_display: Mar 2025
    date_iso: 2025-03
    global_rank: 8
    true_value: 0.621
    true_std: 0.002
    value_gap_source_arxiv: '2503.09008'
    value_gap_source_title: City-Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.621
    sort_std: 0.002
    is_best: false
  - model: GCNII
    model_key: gcnii
    model_plain: GCNII
    value: 0.615
    std: 0.004
    paper_value: 0.615
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
    date: Mar 2025
    date_display: Mar 2025
    date_iso: 2025-03
    global_rank: 9
    true_value: 0.615
    true_std: 0.004
    value_gap_source_arxiv: '2503.09008'
    value_gap_source_title: City-Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.615
    sort_std: 0.004
    is_best: false
  - model: + DropEdge
    model_key: + dropedge
    model_plain: + DropEdge
    value: 0.608
    std: 0.004
    paper_value: 0.608
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
    date: Mar 2025
    date_display: Mar 2025
    date_iso: 2025-03
    global_rank: 10
    true_value: 0.608
    true_std: 0.004
    value_gap_source_arxiv: '2503.09008'
    value_gap_source_title: City-Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.608
    sort_std: 0.004
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.284
    std: 0.006
    paper_value: 0.284
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
    date: Mar 2025
    date_display: Mar 2025
    date_iso: 2025-03
    global_rank: 11
    true_value: 0.284
    true_std: 0.006
    value_gap_source_arxiv: '2503.09008'
    value_gap_source_title: City-Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.284
    sort_std: 0.006
    is_best: false
  metric: Accuracy
  higher_is_better: true
results_grouped:
- benchmark: TU Dortmund
  datasets:
  - *id001
- benchmark: City-Networks
  datasets:
  - *id002
  - *id003
  - *id004
  - *id005
main_figure: /figures/2503.09008/main_figure.png
---

