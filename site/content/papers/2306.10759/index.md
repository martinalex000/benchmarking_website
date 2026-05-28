---
title: 'SGFormer: Simplifying and Empowering Transformers for Large-Graph Representations'
arxiv_id: '2306.10759'
source_url: ''
authors: []
published_date: Jun 2023
published_date_iso: 2023-06
abstract: Learning representations on large-sized graphs is a long-standing challenge
  due to the inter-dependence nature involved in massive data points. Transformers,
  as an emerging class of foundation encoders for graph-structured data, have shown
  promising performance on small graphs due to its global attention capable of capturing
  all-pair influence beyond neighboring nodes. Even so, existing approaches tend to
  inherit the spirit of Transformers in language and vision tasks, and embrace complicated
  models by stacking deep multi-head attentions. In this paper, we critically demonstrate
  that even using a one-layer attention can bring up surprisingly competitive performance
  across node property prediction benchmarks where node numbers range from thousand-level
  to billion-level. This encourages us to rethink the design philosophy for Transformers
  on large graphs, where the quadratic global attention is a computation overhead
  hindering the scalability. We frame the proposed scheme as Simplified Graph Transformers
  (SGFormer), which is empowered by a simple attention model that can efficiently
  propagate information among arbitrary nodes at the minimal cost of one propagation
  layer and linear complexity w.r.t. node numbers. Moreover, SGFormer requires none
  of positional encodings, feature/graph pre-processing or extra loss. Empirically,
  SGFormer successfully scales to the web-scale graph ogbn-papers100M and yields up
  to 141x inference acceleration over SOTA Transformers on medium-sized graphs. Beyond
  current results, we believe the proposed methodology alone enlightens a new technical
  path of independent interest for building Transformers on large graphs. The codes
  are publicly available at https://github.com/qitianwu/SGFormer.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- SGFormer
mrr: 0.1161
adjusted_mrr: 0.0774
mrr_dataset_count: 2
benchmark_categories:
- OGB
task_categories:
- node_classification
experiment_scopes:
- node-level
results:
- &id001
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
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
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.7263
    std: 0.0013
    paper_value: 0.7263
    paper_std: 0.0013
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 31
    true_value: 0.7276
    true_std: 0.0033
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0013000000000000789
    value_note: global 0.7276 within std
    paper_rank: 35
    rank_delta: 4
    rank_delta_abs: 4
    rank_delta_direction: worse
    sort_value: 0.7276
    sort_std: 0.0033
    is_best: false
  - model: SIGN
    model_key: sign
    model_plain: SIGN
    value: 0.7028
    std: 0.0025
    paper_value: 0.7028
    paper_std: 0.0025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 56
    true_value: 0.7195
    true_std: 0.0011
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.016700000000000048
    value_note: ''
    paper_rank: 77
    rank_delta: 21
    rank_delta_abs: 21
    rank_delta_direction: worse
    sort_value: 0.7195
    sort_std: 0.0011
    is_best: false
  - model: GCN-Nsampler
    model_key: gcn-nsampler
    model_plain: GCN-Nsampler
    value: 0.685
    std: 0.0023
    paper_value: 0.685
    paper_std: 0.0023
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 82
    true_value: 0.685
    true_std: 0.0023
    value_gap_source_arxiv: '2512.14619'
    value_gap_source_title: 'ParaFormer: A Generalized PageRank Graph Transformer
      for Graph Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 82
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.685
    sort_std: 0.0023
    is_best: false
  - model: SGC
    model_key: sgc
    model_plain: SGC
    value: 0.6779
    std: 0.0027
    paper_value: 0.6779
    paper_std: 0.0027
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 88
    true_value: 0.6779000000000001
    true_std: 0.0027
    value_gap_source_arxiv: '2512.14619'
    value_gap_source_title: 'ParaFormer: A Generalized PageRank Graph Transformer
      for Graph Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 88
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6779000000000001
    sort_std: 0.0027
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.599
    std: 0.0042
    paper_value: 0.599
    paper_std: 0.0042
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 89
    true_value: 0.6778
    true_std: 0.0028
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07879999999999998
    value_note: ''
    paper_rank: 96
    rank_delta: 7
    rank_delta_abs: 7
    rank_delta_direction: worse
    sort_value: 0.6778
    sort_std: 0.0028
    is_best: false
  - model: GAT-NSampler
    model_key: gat-nsampler
    model_plain: GAT-NSampler
    value: 0.6763
    std: 0.0023
    paper_value: 0.6763
    paper_std: 0.0023
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 90
    true_value: 0.6763
    true_std: 0.0023
    value_gap_source_arxiv: '2306.10759'
    value_gap_source_title: 'SGFormer: Simplifying and Empowering Transformers for
      Large-Graph Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 90
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6763
    sort_std: 0.0023
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.555
    std: 0.0023
    paper_value: 0.555
    paper_std: 0.0023
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 91
    true_value: 0.666
    true_std: 0.0025
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11099999999999999
    value_note: ''
    paper_rank: 98
    rank_delta: 7
    rank_delta_abs: 7
    rank_delta_direction: worse
    sort_value: 0.666
    sort_std: 0.0025
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id002
  dataset: ogbn-proteins
  rows:
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.8501
    std: 0.0046
    metric: ROC-AUC
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
    global_rank: 1
    sort_value: 0.8501
    sort_std: 0.0046
    is_best: true
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.8221
    std: 0.0032
    metric: ROC-AUC
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
    global_rank: 2
    sort_value: 0.8221
    sort_std: 0.0032
    is_best: false
  - model: HGODE
    model_key: hgode
    model_plain: HGODE
    value: 0.8124
    std: 0.0063
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.24293'
    title: 'Latent-Hysteresis Graph ODEs: Modeling Coupled Topology-Feature Evolution
      via Continuous Phase Transitions'
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.8124
    sort_std: 0.0063
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.7953
    std: 0.0038
    paper_value: 0.7953
    paper_std: 0.0038
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 5
    true_value: 0.7992
    true_std: 0.0048
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0039000000000000146
    value_note: global 0.7992 within std
    paper_rank: 6
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.7992
    sort_std: 0.0048
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.7745
    std: 0.0115
    paper_value: 0.7745
    paper_std: 0.0115
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: nodeformer
    variant_inference_reason: ''
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 14
    true_value: 0.7786
    true_std: 0.0084
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0040999999999999925
    value_note: global 0.7786 within std
    paper_rank: 15
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.7786
    sort_std: 0.0084
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7251
    std: 0.0035
    paper_value: 0.7251
    paper_std: 0.0035
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 16
    true_value: 0.7729
    true_std: 0.0046
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.047800000000000065
    value_note: ''
    paper_rank: 20
    rank_delta: 4
    rank_delta_abs: 4
    rank_delta_direction: worse
    sort_value: 0.7729
    sort_std: 0.0046
    is_best: false
  - model: GAT-NSampler
    model_key: gat-nsampler
    model_plain: GAT-NSampler
    value: 0.7463
    std: 0.0124
    paper_value: 0.7463
    paper_std: 0.0124
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 19
    true_value: 0.7463
    true_std: 0.0124
    value_gap_source_arxiv: '2306.10759'
    value_gap_source_title: 'SGFormer: Simplifying and Empowering Transformers for
      Large-Graph Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7463
    sort_std: 0.0124
    is_best: false
  - model: GCN-Nsampler
    model_key: gcn-nsampler
    model_plain: GCN-Nsampler
    value: 0.7351
    std: 0.0131
    paper_value: 0.7351
    paper_std: 0.0131
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 20
    true_value: 0.7351
    true_std: 0.0131
    value_gap_source_arxiv: '2306.10759'
    value_gap_source_title: 'SGFormer: Simplifying and Empowering Transformers for
      Large-Graph Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7351
    sort_std: 0.0131
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.7204
    std: 0.0048
    paper_value: 0.7204
    paper_std: 0.0048
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 22
    true_value: 0.7204
    true_std: 0.0048
    value_gap_source_arxiv: '2306.10759'
    value_gap_source_title: 'SGFormer: Simplifying and Empowering Transformers for
      Large-Graph Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7204
    sort_std: 0.0048
    is_best: false
  - model: SIGN
    model_key: sign
    model_plain: SIGN
    value: 0.7124
    std: 0.0046
    paper_value: 0.7124
    paper_std: 0.0046
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 23
    true_value: 0.7124
    true_std: 0.0046
    value_gap_source_arxiv: '2306.10759'
    value_gap_source_title: 'SGFormer: Simplifying and Empowering Transformers for
      Large-Graph Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7124
    sort_std: 0.0046
    is_best: false
  - model: SGC
    model_key: sgc
    model_plain: SGC
    value: 0.7031
    std: 0.0023
    paper_value: 0.7031
    paper_std: 0.0023
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    global_rank: 24
    true_value: 0.7031
    true_std: 0.0023
    value_gap_source_arxiv: '2306.10759'
    value_gap_source_title: 'SGFormer: Simplifying and Empowering Transformers for
      Large-Graph Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7031
    sort_std: 0.0023
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
results_grouped:
- benchmark: OGB
  datasets:
  - *id001
  - *id002
single_proposed_model: SGFormer
main_figure: /figures/2306.10759/main_figure.png
---

