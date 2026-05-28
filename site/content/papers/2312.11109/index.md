---
title: Graph Transformers for Large Graphs
arxiv_id: '2312.11109'
source_url: ''
authors: []
published_date: Dec 2023
published_date_iso: 2023-12
abstract: 'Transformers have recently emerged as powerful neural networks for graph
  learning, showcasing state-of-the-art performance on several graph property prediction
  tasks. However, these results have been limited to small-scale graphs, such as ligand
  molecules with fewer than a hundred atoms, where the computational feasibility of
  the global attention mechanism is possible. The next goal is to scale up these architectures
  to handle very large graphs on the scale of millions or even billions of nodes.
  With large-scale graphs, global attention learning is proven impractical due to
  its quadratic complexity w.r.t. the number of nodes. On the other hand, neighborhood
  sampling techniques become essential to manage large graph sizes, yet finding the
  optimal trade-off between speed and accuracy with sampling techniques remains challenging.
  This work advances representation learning on single large-scale graphs with a focus
  on identifying model characteristics and critical design constraints for developing
  scalable graph transformer (GT) architectures. We argue such GT requires layers
  that can adeptly learn both local and global graph representations while swiftly
  sampling the graph topology. As such, a key innovation of this work lies in the
  creation of a fast neighborhood sampling technique coupled with a local attention
  mechanism that encompasses a 4-hop reception field, but achieved through just 2-hop
  operations. This local node embedding is then integrated with a global node embedding,
  acquired via another self-attention layer with an approximate global codebook, before
  finally sent through a downstream layer for node predictions. The proposed GT framework,
  named, overcomes previous computational bottlenecks and is validated on three large-scale
  node classification benchmarks. We report a $3 $ speedup and $16.8\ Source code
  available at: https://github.com/snap-research/LargeGT'
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- LargeGT-local
- LargeGT-full
mrr: 0.1208
adjusted_mrr: 0.0806
mrr_dataset_count: 2
benchmark_categories:
- OGB
- LINKX Benchmarks
task_categories:
- node_classification
experiment_scopes:
- node-level
results:
- &id002
  dataset: ogbn-papers100M
  rows:
  - model: GT + HDSE
    model_key: gt + hdse
    model_plain: GT + HDSE
    value: 0.6604
    std: 0.0015
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
    global_rank: 1
    sort_value: 0.6604
    sort_std: 0.0015
    is_best: true
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.6601
    std: 0.0037
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
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
    global_rank: 2
    sort_value: 0.6601
    sort_std: 0.0037
    is_best: true
  - model: SIGN
    model_key: sign
    model_plain: SIGN
    value: 0.6511
    std: 0.0014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
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
    global_rank: 3
    sort_value: 0.6511
    sort_std: 0.0014
    is_best: false
  - model: LargeGT-full
    model_key: largegt-full
    model_plain: LargeGT-full
    value: 0.6473
    std: 0.0005
    paper_value: 0.6473
    paper_std: 0.0005
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 5
    true_value: 0.6473
    true_std: 0.0005
    value_gap_source_arxiv: '2312.11109'
    value_gap_source_title: Graph Transformers for Large Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6473
    sort_std: 0.0005
    is_best: false
  - model: GOAT-full-δ
    model_key: goat-full-δ
    model_plain: GOAT-full-δ
    value: 0.6112
    std: 0.001
    paper_value: 0.6112
    paper_std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 10
    true_value: 0.6112
    true_std: 0.001
    value_gap_source_arxiv: '2312.11109'
    value_gap_source_title: Graph Transformers for Large Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6112
    sort_std: 0.001
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id001
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
    value: 0.9115
    std: 0.0004
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
    global_rank: 2
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
  - model: GOAT-local-δ
    model_key: goat-local-δ
    model_plain: GOAT-local-δ
    value: 0.8117
    std: 0.0012
    paper_value: 0.8117
    paper_std: 0.0012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 10
    true_value: 0.8117
    true_std: 0.0012
    value_gap_source_arxiv: '2312.11109'
    value_gap_source_title: Graph Transformers for Large Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8117
    sort_std: 0.0012
    is_best: false
  - model: GOAT-full-δ
    model_key: goat-full-δ
    model_plain: GOAT-full-δ
    value: 0.7988
    std: 0.002
    paper_value: 0.7988
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 16
    true_value: 0.7988
    true_std: 0.002
    value_gap_source_arxiv: '2312.11109'
    value_gap_source_title: Graph Transformers for Large Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7988
    sort_std: 0.002
    is_best: false
  - model: LargeGT-full
    model_key: largegt-full
    model_plain: LargeGT-full
    value: 0.7981
    std: 0.0025
    paper_value: 0.7981
    paper_std: 0.0025
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 18
    true_value: 0.7981
    true_std: 0.0025
    value_gap_source_arxiv: '2312.11109'
    value_gap_source_title: Graph Transformers for Large Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7981
    sort_std: 0.0025
    is_best: false
  - model: LargeGT-local
    model_key: largegt-local
    model_plain: LargeGT-local
    value: 0.7895
    std: 0.008
    paper_value: 0.7895
    paper_std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 24
    true_value: 0.7895
    true_std: 0.008
    value_gap_source_arxiv: '2312.11109'
    value_gap_source_title: Graph Transformers for Large Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7895
    sort_std: 0.008
    is_best: false
  - model: GAT-δ
    model_key: gat-δ
    model_plain: GAT-δ
    value: 0.7738
    std: 0.0059
    paper_value: 0.7738
    paper_std: 0.0059
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 31
    true_value: 0.7738
    true_std: 0.0059
    value_gap_source_arxiv: '2312.11109'
    value_gap_source_title: Graph Transformers for Large Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7738
    sort_std: 0.0059
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.7662
    std: 0.0093
    paper_value: 0.7662
    paper_std: 0.0093
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 32
    true_value: 0.7662
    true_std: 0.0093
    value_gap_source_arxiv: '2312.11109'
    value_gap_source_title: Graph Transformers for Large Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7662
    sort_std: 0.0093
    is_best: false
  - model: Nagphormer
    model_key: nagphormer
    model_plain: Nagphormer
    value: 0.7528
    std: 0.0004
    paper_value: 0.7528
    paper_std: 0.0004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 37
    true_value: 0.7528
    true_std: 0.0004
    value_gap_source_arxiv: '2312.11109'
    value_gap_source_title: Graph Transformers for Large Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 37
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7528
    sort_std: 0.0004
    is_best: false
  - model: GOAT-global-δ
    model_key: goat-global-δ
    model_plain: GOAT-global-δ
    value: 0.7028
    std: 0.0195
    paper_value: 0.7028
    paper_std: 0.0195
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 47
    true_value: 0.7028
    true_std: 0.0195
    value_gap_source_arxiv: '2312.11109'
    value_gap_source_title: Graph Transformers for Large Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 47
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7028
    sort_std: 0.0195
    is_best: false
  - model: GT-sparse-δ
    model_key: gt-sparse-δ
    model_plain: GT-sparse-δ
    value: 0.6076
    std: 0.0
    paper_value: 0.6076
    paper_std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 50
    true_value: 0.6076
    true_std: 0.0
    value_gap_source_arxiv: '2312.11109'
    value_gap_source_title: Graph Transformers for Large Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 50
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6076
    sort_std: 0.0
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id003
  dataset: snap-patents
  rows:
  - model: MRS-Dir-GCN_DA
    model_key: mrs-dir-gcn_da
    model_plain: MRS-Dir-GCN_DA
    value: 0.7472
    std: 0.0005
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
    sort_value: 0.7472
    sort_std: 0.0005
    is_best: true
  - model: Dir-GNN
    model_key: dir-gnn
    model_plain: Dir-GNN
    value: 0.7395
    std: 0.0005
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
    sort_value: 0.7395
    sort_std: 0.0005
    is_best: false
  - model: LargeGT-full
    model_key: largegt-full
    model_plain: LargeGT-full
    value: 0.7021
    std: 0.0012
    paper_value: 0.7021
    paper_std: 0.0012
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 3
    true_value: 0.7021
    true_std: 0.0012
    value_gap_source_arxiv: '2312.11109'
    value_gap_source_title: Graph Transformers for Large Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7021
    sort_std: 0.0012
    is_best: false
  - model: Grad. Gating
    model_key: grad. gating
    model_plain: Grad. Gating
    value: 0.695
    std: 0.0039
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
    global_rank: 4
    sort_value: 0.695
    sort_std: 0.0039
    is_best: false
  - model: LargeGT-local
    model_key: largegt-local
    model_plain: LargeGT-local
    value: 0.6819
    std: 0.0311
    paper_value: 0.6819
    paper_std: 0.0311
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 5
    true_value: 0.6819
    true_std: 0.0311
    value_gap_source_arxiv: '2312.11109'
    value_gap_source_title: Graph Transformers for Large Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6819
    sort_std: 0.0311
    is_best: false
  - model: Nagphormer
    model_key: nagphormer
    model_plain: Nagphormer
    value: 0.6011
    std: 0.0005
    paper_value: 0.6011
    paper_std: 0.0005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 9
    true_value: 0.6011
    true_std: 0.0005
    value_gap_source_arxiv: '2312.11109'
    value_gap_source_title: Graph Transformers for Large Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6011
    sort_std: 0.0005
    is_best: false
  - model: GOAT-full-δ
    model_key: goat-full-δ
    model_plain: GOAT-full-δ
    value: 0.5028
    std: 0.0014
    paper_value: 0.5028
    paper_std: 0.0014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 12
    true_value: 0.5028
    true_std: 0.0014
    value_gap_source_arxiv: '2312.11109'
    value_gap_source_title: Graph Transformers for Large Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5028
    sort_std: 0.0014
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.4843
    std: 0.0021
    paper_value: 0.4843
    paper_std: 0.0021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 13
    true_value: 0.4843
    true_std: 0.0021
    value_gap_source_arxiv: '2312.11109'
    value_gap_source_title: Graph Transformers for Large Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4843
    sort_std: 0.0021
    is_best: false
  - model: GT-sparse-δ
    model_key: gt-sparse-δ
    model_plain: GT-sparse-δ
    value: 0.4781
    std: 0.0
    paper_value: 0.4781
    paper_std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 14
    true_value: 0.4781
    true_std: 0.0
    value_gap_source_arxiv: '2312.11109'
    value_gap_source_title: Graph Transformers for Large Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4781
    sort_std: 0.0
    is_best: false
  - model: GAT-δ
    model_key: gat-δ
    model_plain: GAT-δ
    value: 0.4592
    std: 0.0022
    paper_value: 0.4592
    paper_std: 0.0022
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 16
    true_value: 0.4592
    true_std: 0.0022
    value_gap_source_arxiv: '2312.11109'
    value_gap_source_title: Graph Transformers for Large Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4592
    sort_std: 0.0022
    is_best: false
  - model: GOAT-global-δ
    model_key: goat-global-δ
    model_plain: GOAT-global-δ
    value: 0.4265
    std: 0.0007
    paper_value: 0.4265
    paper_std: 0.0007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 17
    true_value: 0.4265
    true_std: 0.0007
    value_gap_source_arxiv: '2312.11109'
    value_gap_source_title: Graph Transformers for Large Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4265
    sort_std: 0.0007
    is_best: false
  - model: GOAT-local-δ
    model_key: goat-local-δ
    model_plain: GOAT-local-δ
    value: 0.4095
    std: 0.0016
    paper_value: 0.4095
    paper_std: 0.0016
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    global_rank: 18
    true_value: 0.4095
    true_std: 0.0016
    value_gap_source_arxiv: '2312.11109'
    value_gap_source_title: Graph Transformers for Large Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4095
    sort_std: 0.0016
    is_best: false
  metric: Accuracy
  higher_is_better: true
results_grouped:
- benchmark: OGB
  datasets:
  - *id001
  - *id002
- benchmark: LINKX Benchmarks
  datasets:
  - *id003
main_figure: /figures/2312.11109/main_figure.png
---

