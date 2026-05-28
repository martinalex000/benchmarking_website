---
title: 'Toward a Graph Foundation Model: Pre-Training Transformers With Random Walks'
arxiv_id: '2506.14098'
source_url: ''
authors: []
published_date: Jun 2025
published_date_iso: 2025-06
abstract: A foundation model like GPT elicits many emergent abilities, owing to the
  pre-training with broad inclusion of data and the use of the powerful Transformer
  architecture. While foundation models in natural languages are prevalent, can we
  build similar models for graphs? This paper describes an approach toward a graph
  foundation model that is pre-trained with diverse graph datasets by adapting the
  Transformer backbone. A central challenge toward this end is how a sequence model
  encodes graphs of varying sizes and from different domains. We propose representing
  a node as multiple random walks, such that the Transformer can extract node representations
  from sequences, which in turn form edge and graph representations. We develop a
  novel context prediction loss for these random walks and theoretically analyze their
  expressive power in distinguishing neighborhoods and graphs. We also demonstrate
  the pre-training of our model and its adaptation to downstream tasks, showcasing
  its potential as a foundation for processing and reasoning with graph-structured
  data.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- RWPT
- RWPT (Pre-Train w/ all)
- RWPT (Pre-Train w/ Arxiv + FB15k237 + ChEMBL)
- RWPT (Pre-Train w/ Arxiv)
- RWPT (Pre-Train w/ FB15k237)
- RWPT (Pre-Train w/ ChEMBL)
- RWPT (Context loss)
- RWPT (Context prediction)
- RWPT (+ Token reconstruction)
- RWPT (+ Position reconstruction)
- Our loss
- RWPT (Pre-Train w/ three)
- RWPT (Walk, k=16, l=2)
- RWPT (Walk, k=4, l=4)
- RWPT (Neighbor, [4,4,2])
- RWPT (Our loss)
- RWPT (Edge feat. input)
- RWPT (Full attn. mask)
mrr: 0.0162
adjusted_mrr: 0.0162
mrr_dataset_count: 5
benchmark_categories:
- Classic
- LRGB
- OGB
- MoleculeNet
- Knowledge Graphs
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
- &id002
  dataset: CiteSeer
  rows:
  - model: FAGCN
    model_key: fagcn
    model_plain: FAGCN
    value: 0.8237
    std: 0.0146
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
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
  - model: RWPT (Context prediction)
    model_key: rwpt (context prediction)
    model_plain: RWPT (Context prediction)
    value: 0.7546
    std: 0.0045
    paper_value: 0.7546
    paper_std: 0.0045
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 80
    true_value: 0.7546
    true_std: 0.0045
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 80
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7546
    sort_std: 0.0045
    is_best: false
  - model: Our loss
    model_key: our loss
    model_plain: Our loss
    value: 0.7546
    std: 0.0045
    paper_value: 0.7546
    paper_std: 0.0045
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 79
    true_value: 0.7546
    true_std: 0.0045
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 79
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7546
    sort_std: 0.0045
    is_best: false
  - model: RWPT (+ Token reconstruction)
    model_key: rwpt (+ token reconstruction)
    model_plain: RWPT (+ Token reconstruction)
    value: 0.7525
    std: 0.0071
    paper_value: 0.7525
    paper_std: 0.0071
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 83
    true_value: 0.7525
    true_std: 0.0071
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 83
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7525
    sort_std: 0.0071
    is_best: false
  - model: MaskGAE
    model_key: maskgae
    model_plain: MaskGAE
    value: 0.7487
    std: 0.0043
    paper_value: 0.7487
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
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 91
    true_value: 0.7487
    true_std: 0.0043
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 91
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7487
    sort_std: 0.0043
    is_best: false
  - model: RWPT (+ Position reconstruction)
    model_key: rwpt (+ position reconstruction)
    model_plain: RWPT (+ Position reconstruction)
    value: 0.7469
    std: 0.0043
    paper_value: 0.7469
    paper_std: 0.0043
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 92
    true_value: 0.7469
    true_std: 0.0043
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 92
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7469
    sort_std: 0.0043
    is_best: false
  - model: GraphPrompt
    model_key: graphprompt
    model_plain: GraphPrompt
    value: 0.7445
    std: 0.006
    paper_value: 0.7445
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
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 97
    true_value: 0.7445
    true_std: 0.006
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 97
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7445
    sort_std: 0.006
    is_best: false
  - model: DGI
    model_key: dgi
    model_plain: DGI
    value: 0.7437
    std: 0.0088
    paper_value: 0.7437
    paper_std: 0.0088
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Velickovic 2019
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 99
    true_value: 0.7437
    true_std: 0.0088
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 99
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7437
    sort_std: 0.0088
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
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.7624
    std: null
    paper_value: 0.7624
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 31
    true_value: 0.8825
    true_std: 0.0053
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.12009999999999998
    value_note: ''
    paper_rank: 190
    rank_delta: 159
    rank_delta_abs: 159
    rank_delta_direction: worse
    sort_value: 0.8825
    sort_std: 0.0053
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7565
    std: null
    paper_value: 0.7565
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 48
    true_value: 0.8778
    true_std: 0.0096
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.12130000000000007
    value_note: ''
    paper_rank: 194
    rank_delta: 146
    rank_delta_abs: 146
    rank_delta_direction: worse
    sort_value: 0.8778
    sort_std: 0.0096
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.5803
    std: null
    paper_value: 0.5803
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 65
    true_value: 0.8709
    true_std: 0.0066
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.29059999999999997
    value_note: ''
    paper_rank: 287
    rank_delta: 222
    rank_delta_abs: 222
    rank_delta_direction: worse
    sort_value: 0.8709
    sort_std: 0.0066
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.7359
    std: null
    paper_value: 0.7359
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 128
    true_value: 0.8303
    true_std: 0.0541
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09440000000000004
    value_note: ''
    paper_rank: 210
    rank_delta: 82
    rank_delta_abs: 82
    rank_delta_direction: worse
    sort_value: 0.8303
    sort_std: 0.0541
    is_best: false
  - model: RWPT
    model_key: rwpt
    model_plain: RWPT
    value: 0.793
    std: null
    paper_value: 0.793
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 162
    true_value: 0.793
    true_std: null
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 162
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.793
    sort_std: null
    is_best: false
  - model: RWPT (Pre-Train w/ all)
    model_key: rwpt (pre-train w/ all)
    model_plain: RWPT (Pre-Train w/ all)
    value: 0.793
    std: null
    paper_value: 0.793
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 163
    true_value: 0.793
    true_std: null
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 163
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.793
    sort_std: null
    is_best: false
  - model: RWPT (Pre-Train w/ Arxiv + FB15k237 + ChEMBL)
    model_key: rwpt (pre-train w/ arxiv + fb15k237 + chembl)
    model_plain: RWPT (Pre-Train w/ Arxiv + FB15k237 + ChEMBL)
    value: 0.7869
    std: null
    paper_value: 0.7869
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 167
    true_value: 0.7869
    true_std: null
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 167
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7869
    sort_std: null
    is_best: false
  - model: GFT
    model_key: gft
    model_plain: GFT
    value: 0.7862
    std: null
    paper_value: 0.7862
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Wang 2024
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 168
    true_value: 0.7862
    true_std: null
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 168
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7862
    sort_std: null
    is_best: false
  - model: RWPT (+ Token reconstruction)
    model_key: rwpt (+ token reconstruction)
    model_plain: RWPT (+ Token reconstruction)
    value: 0.7818
    std: 0.0052
    paper_value: 0.7818
    paper_std: 0.0052
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 174
    true_value: 0.7818
    true_std: 0.0052
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 174
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7818
    sort_std: 0.0052
    is_best: false
  - model: RWPT (Context loss)
    model_key: rwpt (context loss)
    model_plain: RWPT (Context loss)
    value: 0.7802
    std: 0.0037
    paper_value: 0.7802
    paper_std: 0.0037
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 176
    true_value: 0.7802
    true_std: 0.0037
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 176
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7802
    sort_std: 0.0037
    is_best: false
  - model: RWPT (Context prediction)
    model_key: rwpt (context prediction)
    model_plain: RWPT (Context prediction)
    value: 0.7802
    std: 0.0037
    paper_value: 0.7802
    paper_std: 0.0037
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 177
    true_value: 0.7802
    true_std: 0.0037
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 177
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7802
    sort_std: 0.0037
    is_best: false
  - model: MaskGAE
    model_key: maskgae
    model_plain: MaskGAE
    value: 0.7751
    std: 0.0028
    paper_value: 0.7751
    paper_std: 0.0028
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 180
    true_value: 0.7751
    true_std: 0.0028
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 180
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7751
    sort_std: 0.0028
    is_best: false
  - model: RWPT (Pre-Train w/ Arxiv)
    model_key: rwpt (pre-train w/ arxiv)
    model_plain: RWPT (Pre-Train w/ Arxiv)
    value: 0.7663
    std: null
    paper_value: 0.7663
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 186
    true_value: 0.7663
    true_std: null
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 186
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7663
    sort_std: null
    is_best: false
  - model: RWPT (+ Position reconstruction)
    model_key: rwpt (+ position reconstruction)
    model_plain: RWPT (+ Position reconstruction)
    value: 0.7661
    std: 0.0044
    paper_value: 0.7661
    paper_std: 0.0044
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 187
    true_value: 0.7661
    true_std: 0.0044
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 187
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7661
    sort_std: 0.0044
    is_best: false
  - model: GIANT
    model_key: giant
    model_plain: GIANT
    value: 0.7513
    std: null
    paper_value: 0.7513
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 198
    true_value: 0.7513
    true_std: null
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 198
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7513
    sort_std: null
    is_best: false
  - model: GraphPrompt
    model_key: graphprompt
    model_plain: GraphPrompt
    value: 0.7497
    std: 0.0035
    paper_value: 0.7497
    paper_std: 0.0035
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 200
    true_value: 0.7497
    true_std: 0.0035
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 200
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7497
    sort_std: 0.0035
    is_best: false
  - model: RWPT (Pre-Train w/ FB15k237)
    model_key: rwpt (pre-train w/ fb15k237)
    model_plain: RWPT (Pre-Train w/ FB15k237)
    value: 0.7371
    std: null
    paper_value: 0.7371
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 207
    true_value: 0.7371
    true_std: null
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 207
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7371
    sort_std: null
    is_best: false
  - model: GraphMAE
    model_key: graphmae
    model_plain: GraphMAE
    value: 0.731
    std: null
    paper_value: 0.731
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 212
    true_value: 0.731
    true_std: null
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 212
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.731
    sort_std: null
    is_best: false
  - model: DGI
    model_key: dgi
    model_plain: DGI
    value: 0.721
    std: null
    paper_value: 0.721
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 228
    true_value: 0.721
    true_std: null
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 228
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.721
    sort_std: null
    is_best: false
  - model: BGRL
    model_key: bgrl
    model_plain: BGRL
    value: 0.712
    std: null
    paper_value: 0.712
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 236
    true_value: 0.712
    true_std: null
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 236
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.712
    sort_std: null
    is_best: false
  - model: RWPT (Pre-Train w/ ChEMBL)
    model_key: rwpt (pre-train w/ chembl)
    model_plain: RWPT (Pre-Train w/ ChEMBL)
    value: 0.7034
    std: null
    paper_value: 0.7034
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 242
    true_value: 0.7034
    true_std: null
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 242
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7034
    sort_std: null
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id009
  dataset: FB15k-237
  rows:
  - model: RWPT
    model_key: rwpt
    model_plain: RWPT
    value: 0.9523
    std: null
    paper_value: 0.9523
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: null
    sort_value: 0.9523
    sort_std: null
    is_best: true
  - model: GFT
    model_key: gft
    model_plain: GFT
    value: 0.8972
    std: null
    paper_value: 0.8972
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: null
    sort_value: 0.8972
    sort_std: null
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.8893
    std: null
    paper_value: 0.8893
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: null
    sort_value: 0.8893
    sort_std: null
    is_best: false
  - model: GIANT
    model_key: giant
    model_plain: GIANT
    value: 0.8745
    std: null
    paper_value: 0.8745
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: null
    sort_value: 0.8745
    sort_std: null
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.8739
    std: null
    paper_value: 0.8739
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: null
    sort_value: 0.8739
    sort_std: null
    is_best: false
  - model: GraphMAE
    model_key: graphmae
    model_plain: GraphMAE
    value: 0.853
    std: null
    paper_value: 0.853
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: null
    sort_value: 0.853
    sort_std: null
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.8321
    std: null
    paper_value: 0.8321
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: null
    sort_value: 0.8321
    sort_std: null
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.8222
    std: null
    paper_value: 0.8222
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: null
    sort_value: 0.8222
    sort_std: null
    is_best: false
  - model: DGI
    model_key: dgi
    model_plain: DGI
    value: 0.8134
    std: null
    paper_value: 0.8134
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: null
    sort_value: 0.8134
    sort_std: null
    is_best: false
  - model: BGRL
    model_key: bgrl
    model_plain: BGRL
    value: 0.8066
    std: null
    paper_value: 0.8066
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: null
    sort_value: 0.8066
    sort_std: null
    is_best: false
  metric: MRR
  higher_is_better: true
- &id005
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
    value: 0.2421
    std: 0.0016
    metric: MAE
    higher_is_better: false
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
    global_rank: 3
    sort_value: 0.2421
    sort_std: 0.0016
    is_best: false
  - model: RWPT (Walk, k=4, l=4)
    model_key: rwpt (walk, k=4, l=4)
    model_plain: RWPT (Walk, k=4, l=4)
    value: 0.2561
    std: null
    paper_value: 0.2561
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1 (Sampler Ablation)
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 196
    true_value: 0.2561
    true_std: null
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 196
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2561
    sort_std: null
    is_best: false
  metric: MAE
  higher_is_better: false
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
    value: 0.6866
    std: null
    paper_value: 0.6866
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 3
    true_value: 0.9476
    true_std: 0.001
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.261
    value_note: ''
    paper_rank: 155
    rank_delta: 152
    rank_delta_abs: 152
    rank_delta_direction: worse
    sort_value: 0.9476
    sort_std: 0.001
    is_best: true
  - model: ND
    model_key: nd
    model_plain: ND
    value: 0.9256
    std: 0.0071
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
    global_rank: 4
    sort_value: 0.9256
    sort_std: 0.0071
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7561
    std: null
    paper_value: 0.7561
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 5
    true_value: 0.9224
    true_std: 0.0123
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1663
    value_note: ''
    paper_rank: 131
    rank_delta: 126
    rank_delta_abs: 126
    rank_delta_direction: worse
    sort_value: 0.9224
    sort_std: 0.0123
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.7486
    std: null
    paper_value: 0.7486
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 6
    true_value: 0.9201
    true_std: 0.0024
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.17149999999999999
    value_note: ''
    paper_rank: 142
    rank_delta: 136
    rank_delta_abs: 136
    rank_delta_direction: worse
    sort_value: 0.9201
    sort_std: 0.0024
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.6951
    std: null
    paper_value: 0.6951
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 7
    true_value: 0.914
    true_std: 0.0063
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.21889999999999998
    value_note: ''
    paper_rank: 155
    rank_delta: 148
    rank_delta_abs: 148
    rank_delta_direction: worse
    sort_value: 0.914
    sort_std: 0.0063
    is_best: false
  - model: GFT
    model_key: gft
    model_plain: GFT
    value: 0.7719
    std: null
    paper_value: 0.7719
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Wang 2024
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 127
    true_value: 0.7719
    true_std: null
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 127
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7719
    sort_std: null
    is_best: false
  - model: BGRL
    model_key: bgrl
    model_plain: BGRL
    value: 0.7529
    std: null
    paper_value: 0.7529
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 135
    true_value: 0.7529
    true_std: null
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 135
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7529
    sort_std: null
    is_best: false
  - model: RWPT
    model_key: rwpt
    model_plain: RWPT
    value: 0.7497
    std: null
    paper_value: 0.7497
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 142
    true_value: 0.7497
    true_std: null
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 142
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7497
    sort_std: null
    is_best: false
  - model: GraphMAE
    model_key: graphmae
    model_plain: GraphMAE
    value: 0.7432
    std: null
    paper_value: 0.7432
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 146
    true_value: 0.7432
    true_std: null
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 146
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7432
    sort_std: null
    is_best: false
  - model: DGI
    model_key: dgi
    model_plain: DGI
    value: 0.7313
    std: null
    paper_value: 0.7313
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 151
    true_value: 0.7313
    true_std: null
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 151
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7313
    sort_std: null
    is_best: false
  - model: GIANT
    model_key: giant
    model_plain: GIANT
    value: 0.7231
    std: null
    paper_value: 0.7231
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 152
    true_value: 0.7231
    true_std: null
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 152
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7231
    sort_std: null
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id008
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
  - model: RWPT
    model_key: rwpt
    model_plain: RWPT
    value: 0.7449
    std: 0.014
    paper_value: 0.7449
    paper_std: 0.014
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 60
    true_value: 0.7449
    true_std: 0.014
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 60
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7449
    sort_std: 0.014
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id004
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
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.7678
    std: null
    paper_value: 0.7678
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 9
    true_value: 0.8322
    true_std: 0.0078
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.06440000000000001
    value_note: ''
    paper_rank: 49
    rank_delta: 40
    rank_delta_abs: 40
    rank_delta_direction: worse
    sort_value: 0.8322
    sort_std: 0.0078
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7528
    std: null
    paper_value: 0.7528
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 14
    true_value: 0.8232
    true_std: 0.0069
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07040000000000002
    value_note: ''
    paper_rank: 51
    rank_delta: 37
    rank_delta_abs: 37
    rank_delta_direction: worse
    sort_value: 0.8232
    sort_std: 0.0069
    is_best: false
  - model: RWPT (Edge feat. input)
    model_key: rwpt (edge feat. input)
    model_plain: RWPT (Edge feat. input)
    value: 0.8093
    std: 0.0026
    paper_value: 0.8093
    paper_std: 0.0026
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 6
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 17
    true_value: 0.8093
    true_std: 0.0026
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8093
    sort_std: 0.0026
    is_best: false
  - model: RWPT (Walk, k=16, l=2)
    model_key: rwpt (walk, k=16, l=2)
    model_plain: RWPT (Walk, k=16, l=2)
    value: 0.808
    std: null
    paper_value: 0.808
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 18
    true_value: 0.808
    true_std: null
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.808
    sort_std: null
    is_best: false
  - model: RWPT (+ Token reconstruction)
    model_key: rwpt (+ token reconstruction)
    model_plain: RWPT (+ Token reconstruction)
    value: 0.8074
    std: 0.0034
    paper_value: 0.8074
    paper_std: 0.0034
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 19
    true_value: 0.8074
    true_std: 0.0034
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8074
    sort_std: 0.0034
    is_best: false
  - model: MaskGAE
    model_key: maskgae
    model_plain: MaskGAE
    value: 0.8048
    std: 0.0013
    paper_value: 0.8048
    paper_std: 0.0013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 21
    true_value: 0.8048
    true_std: 0.0013
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8048
    sort_std: 0.0013
    is_best: false
  - model: RWPT
    model_key: rwpt
    model_plain: RWPT
    value: 0.8027
    std: 0.0019
    paper_value: 0.8027
    paper_std: 0.0019
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 22
    true_value: 0.8027
    true_std: 0.0019
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8027
    sort_std: 0.0019
    is_best: false
  - model: RWPT (Pre-Train w/ all)
    model_key: rwpt (pre-train w/ all)
    model_plain: RWPT (Pre-Train w/ all)
    value: 0.8027
    std: null
    paper_value: 0.8027
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 23
    true_value: 0.8027
    true_std: null
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8027
    sort_std: null
    is_best: false
  - model: RWPT (Context prediction)
    model_key: rwpt (context prediction)
    model_plain: RWPT (Context prediction)
    value: 0.8027
    std: 0.0019
    paper_value: 0.8027
    paper_std: 0.0019
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 25
    true_value: 0.8027
    true_std: 0.0019
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8027
    sort_std: 0.0019
    is_best: false
  - model: RWPT (Our loss)
    model_key: rwpt (our loss)
    model_plain: RWPT (Our loss)
    value: 0.8027
    std: 0.0019
    paper_value: 0.8027
    paper_std: 0.0019
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 24
    true_value: 0.8027
    true_std: 0.0019
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8027
    sort_std: 0.0019
    is_best: false
  - model: RWPT (+ Position reconstruction)
    model_key: rwpt (+ position reconstruction)
    model_plain: RWPT (+ Position reconstruction)
    value: 0.8025
    std: 0.0023
    paper_value: 0.8025
    paper_std: 0.0023
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 27
    true_value: 0.8025
    true_std: 0.0023
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 27
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8025
    sort_std: 0.0023
    is_best: false
  - model: RWPT (Walk, k=4, l=4)
    model_key: rwpt (walk, k=4, l=4)
    model_plain: RWPT (Walk, k=4, l=4)
    value: 0.8025
    std: null
    paper_value: 0.8025
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 26
    true_value: 0.8025
    true_std: null
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8025
    sort_std: null
    is_best: false
  - model: RWPT (Pre-Train w/ three)
    model_key: rwpt (pre-train w/ three)
    model_plain: RWPT (Pre-Train w/ three)
    value: 0.8015
    std: null
    paper_value: 0.8015
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 29
    true_value: 0.8015
    true_std: null
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8015
    sort_std: null
    is_best: false
  - model: RWPT (Neighbor, [4,4,2])
    model_key: rwpt (neighbor, [4,4,2])
    model_plain: RWPT (Neighbor, [4,4,2])
    value: 0.8002
    std: null
    paper_value: 0.8002
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 30
    true_value: 0.8002
    true_std: null
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 30
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8002
    sort_std: null
    is_best: false
  - model: GraphPrompt
    model_key: graphprompt
    model_plain: GraphPrompt
    value: 0.8001
    std: 0.0029
    paper_value: 0.8001
    paper_std: 0.0029
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 31
    true_value: 0.8001
    true_std: 0.0029
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8001
    sort_std: 0.0029
    is_best: false
  - model: RWPT (Pre-Train w/ Arxiv)
    model_key: rwpt (pre-train w/ arxiv)
    model_plain: RWPT (Pre-Train w/ Arxiv)
    value: 0.7995
    std: null
    paper_value: 0.7995
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 32
    true_value: 0.7995
    true_std: null
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7995
    sort_std: null
    is_best: false
  - model: RWPT (Full attn. mask)
    model_key: rwpt (full attn. mask)
    model_plain: RWPT (Full attn. mask)
    value: 0.7955
    std: 0.0012
    paper_value: 0.7955
    paper_std: 0.0012
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 6
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 33
    true_value: 0.7955
    true_std: 0.0012
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7955
    sort_std: 0.0012
    is_best: false
  - model: RWPT (Pre-Train w/ FB15k237)
    model_key: rwpt (pre-train w/ fb15k237)
    model_plain: RWPT (Pre-Train w/ FB15k237)
    value: 0.795
    std: null
    paper_value: 0.795
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 34
    true_value: 0.795
    true_std: null
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 34
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.795
    sort_std: null
    is_best: false
  - model: GFT
    model_key: gft
    model_plain: GFT
    value: 0.7939
    std: null
    paper_value: 0.7939
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Wang 2024
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 35
    true_value: 0.7939
    true_std: null
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7939
    sort_std: null
    is_best: false
  - model: GraphMAE
    model_key: graphmae
    model_plain: GraphMAE
    value: 0.7761
    std: null
    paper_value: 0.7761
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 37
    true_value: 0.7932
    true_std: 0.0029
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.017100000000000004
    value_note: ''
    paper_rank: 48
    rank_delta: 11
    rank_delta_abs: 11
    rank_delta_direction: worse
    sort_value: 0.7932
    sort_std: 0.0029
    is_best: false
  - model: RWPT (Pre-Train w/ ChEMBL)
    model_key: rwpt (pre-train w/ chembl)
    model_plain: RWPT (Pre-Train w/ ChEMBL)
    value: 0.7927
    std: null
    paper_value: 0.7927
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 38
    true_value: 0.7927
    true_std: null
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7927
    sort_std: null
    is_best: false
  - model: BGRL
    model_key: bgrl
    model_plain: BGRL
    value: 0.7653
    std: null
    paper_value: 0.7653
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 40
    true_value: 0.7902
    true_std: 0.0013
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.024900000000000033
    value_note: ''
    paper_rank: 50
    rank_delta: 10
    rank_delta_abs: 10
    rank_delta_direction: worse
    sort_value: 0.7902
    sort_std: 0.0013
    is_best: false
  - model: GIANT
    model_key: giant
    model_plain: GIANT
    value: 0.7656
    std: null
    paper_value: 0.7656
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 50
    true_value: 0.7656
    true_std: null
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 50
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7656
    sort_std: null
    is_best: false
  - model: DGI
    model_key: dgi
    model_plain: DGI
    value: 0.7532
    std: null
    paper_value: 0.7532
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 51
    true_value: 0.7532
    true_std: null
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 51
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7532
    sort_std: null
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.7036
    std: null
    paper_value: 0.7036
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 52
    true_value: 0.7036
    true_std: null
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 52
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7036
    sort_std: null
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.4977
    std: null
    paper_value: 0.4977
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 53
    true_value: 0.4977
    true_std: null
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 53
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4977
    sort_std: null
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id006
  dataset: ogbg-molhiv
  rows:
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.6637
    std: null
    paper_value: 0.6637
    paper_std: null
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 1
    true_value: 0.9685
    true_std: 0.0001
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.30480000000000007
    value_note: ''
    paper_rank: 215
    rank_delta: 214
    rank_delta_abs: 214
    rank_delta_direction: worse
    sort_value: 0.9685
    sort_std: 0.0001
    is_best: true
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.6554
    std: null
    paper_value: 0.6554
    paper_std: null
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 2
    true_value: 0.9682
    true_std: 0.0003
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.31279999999999997
    value_note: ''
    paper_rank: 215
    rank_delta: 213
    rank_delta_abs: 213
    rank_delta_direction: worse
    sort_value: 0.9682
    sort_std: 0.0003
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.6484
    std: null
    paper_value: 0.6484
    paper_std: null
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 3
    true_value: 0.9681
    true_std: 0.0003
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.3197
    value_note: ''
    paper_rank: 217
    rank_delta: 214
    rank_delta_abs: 214
    rank_delta_direction: worse
    sort_value: 0.9681
    sort_std: 0.0003
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.6686
    std: null
    paper_value: 0.6686
    paper_std: null
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 4
    true_value: 0.968
    true_std: 0.002
    value_gap_source_arxiv: '2502.02379'
    value_gap_source_title: 'No Metric to Rule Them All: Toward Principled Evaluations
      of Graph-Learning Datasets'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.2994
    value_note: ''
    paper_rank: 215
    rank_delta: 211
    rank_delta_abs: 211
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
  - model: G1
    model_key: g1
    model_plain: G1
    value: 0.8247
    std: null
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
    global_rank: 6
    sort_value: 0.8247
    sort_std: null
    is_best: false
  - model: Per-head
    model_key: per-head
    model_plain: Per-head
    value: 0.8247
    std: null
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
    global_rank: 7
    sort_value: 0.8247
    sort_std: null
    is_best: false
  - model: GraphMAE
    model_key: graphmae
    model_plain: GraphMAE
    value: 0.6104
    std: null
    paper_value: 0.6104
    paper_std: null
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 144
    true_value: 0.768
    true_std: 0.006
    value_gap_source_arxiv: '2604.06336'
    value_gap_source_title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale
      Molecular Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.15759999999999996
    value_note: ''
    paper_rank: 220
    rank_delta: 76
    rank_delta_abs: 76
    rank_delta_direction: worse
    sort_value: 0.768
    sort_std: 0.006
    is_best: false
  - model: RWPT (Walk, k=16, l=2)
    model_key: rwpt (walk, k=16, l=2)
    model_plain: RWPT (Walk, k=16, l=2)
    value: 0.7524
    std: null
    paper_value: 0.7524
    paper_std: null
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 179
    true_value: 0.7524
    true_std: null
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 179
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7524
    sort_std: null
    is_best: false
  - model: RWPT
    model_key: rwpt
    model_plain: RWPT
    value: 0.7515
    std: 0.0239
    paper_value: 0.7515
    paper_std: 0.0239
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 181
    true_value: 0.7515
    true_std: 0.0239
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 181
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7515
    sort_std: 0.0239
    is_best: false
  - model: RWPT (Pre-Train w/ all)
    model_key: rwpt (pre-train w/ all)
    model_plain: RWPT (Pre-Train w/ all)
    value: 0.7515
    std: null
    paper_value: 0.7515
    paper_std: null
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 182
    true_value: 0.7515
    true_std: null
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 182
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7515
    sort_std: null
    is_best: false
  - model: RWPT (Walk, k=4, l=4)
    model_key: rwpt (walk, k=4, l=4)
    model_plain: RWPT (Walk, k=4, l=4)
    value: 0.7514
    std: null
    paper_value: 0.7514
    paper_std: null
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 183
    true_value: 0.7514
    true_std: null
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 183
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7514
    sort_std: null
    is_best: false
  - model: RWPT (Pre-Train w/ ChEMBL)
    model_key: rwpt (pre-train w/ chembl)
    model_plain: RWPT (Pre-Train w/ ChEMBL)
    value: 0.7485
    std: null
    paper_value: 0.7485
    paper_std: null
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 189
    true_value: 0.7485
    true_std: null
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 189
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7485
    sort_std: null
    is_best: false
  - model: RWPT (Pre-Train w/ three)
    model_key: rwpt (pre-train w/ three)
    model_plain: RWPT (Pre-Train w/ three)
    value: 0.7403
    std: null
    paper_value: 0.7403
    paper_std: null
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 191
    true_value: 0.7403
    true_std: null
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 191
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7403
    sort_std: null
    is_best: false
  - model: RWPT (Pre-Train w/ FB15k237)
    model_key: rwpt (pre-train w/ fb15k237)
    model_plain: RWPT (Pre-Train w/ FB15k237)
    value: 0.7357
    std: null
    paper_value: 0.7357
    paper_std: null
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 200
    true_value: 0.7357
    true_std: null
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 200
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7357
    sort_std: null
    is_best: false
  - model: RWPT (Pre-Train w/ Arxiv)
    model_key: rwpt (pre-train w/ arxiv)
    model_plain: RWPT (Pre-Train w/ Arxiv)
    value: 0.7346
    std: null
    paper_value: 0.7346
    paper_std: null
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 201
    true_value: 0.7346
    true_std: null
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 201
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7346
    sort_std: null
    is_best: false
  - model: RWPT (Full attn. mask)
    model_key: rwpt (full attn. mask)
    model_plain: RWPT (Full attn. mask)
    value: 0.7342
    std: 0.0343
    paper_value: 0.7342
    paper_std: 0.0343
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 202
    true_value: 0.7342
    true_std: 0.0343
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 202
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7342
    sort_std: 0.0343
    is_best: false
  - model: RWPT (Edge feat. input)
    model_key: rwpt (edge feat. input)
    model_plain: RWPT (Edge feat. input)
    value: 0.7315
    std: 0.0295
    paper_value: 0.7315
    paper_std: 0.0295
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 203
    true_value: 0.7315
    true_std: 0.0295
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 203
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7315
    sort_std: 0.0295
    is_best: false
  - model: RWPT (Neighbor, [4,4,2])
    model_key: rwpt (neighbor, [4,4,2])
    model_plain: RWPT (Neighbor, [4,4,2])
    value: 0.7281
    std: null
    paper_value: 0.7281
    paper_std: null
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 207
    true_value: 0.7281
    true_std: null
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 207
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7281
    sort_std: null
    is_best: false
  - model: GFT
    model_key: gft
    model_plain: GFT
    value: 0.7267
    std: null
    paper_value: 0.7267
    paper_std: null
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Wang 2024
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 208
    true_value: 0.7267
    true_std: null
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 208
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7267
    sort_std: null
    is_best: false
  - model: GIANT
    model_key: giant
    model_plain: GIANT
    value: 0.6544
    std: null
    paper_value: 0.6544
    paper_std: null
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 216
    true_value: 0.6544
    true_std: null
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 216
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6544
    sort_std: null
    is_best: false
  - model: BGRL
    model_key: bgrl
    model_plain: BGRL
    value: 0.6395
    std: null
    paper_value: 0.6395
    paper_std: null
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 218
    true_value: 0.6395
    true_std: null
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 218
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6395
    sort_std: null
    is_best: false
  - model: DGI
    model_key: dgi
    model_plain: DGI
    value: 0.5962
    std: null
    paper_value: 0.5962
    paper_std: null
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 221
    true_value: 0.5962
    true_std: null
    value_gap_source_arxiv: '2506.14098'
    value_gap_source_title: 'Toward a Graph Foundation Model: Pre-Training Transformers
      With Random Walks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 221
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5962
    sort_std: null
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id007
  dataset: ogbg-molpcba
  rows:
  - model: RWPT
    model_key: rwpt
    model_plain: RWPT
    value: 0.8103
    std: null
    paper_value: 0.8103
    paper_std: null
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: null
    sort_value: 0.8103
    sort_std: null
    is_best: true
  - model: GFT
    model_key: gft
    model_plain: GFT
    value: 0.779
    std: null
    paper_value: 0.779
    paper_std: null
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Wang 2024
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: null
    sort_value: 0.779
    sort_std: null
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.7269
    std: null
    paper_value: 0.7269
    paper_std: null
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 57
    sort_value: 0.7269
    sort_std: null
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.723
    std: null
    paper_value: 0.723
    paper_std: null
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: null
    sort_value: 0.723
    sort_std: null
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7132
    std: null
    paper_value: 0.7132
    paper_std: null
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 40
    sort_value: 0.7132
    sort_std: null
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.7012
    std: null
    paper_value: 0.7012
    paper_std: null
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 41
    sort_value: 0.7012
    sort_std: null
    is_best: false
  - model: BGRL
    model_key: bgrl
    model_plain: BGRL
    value: 0.6709
    std: null
    paper_value: 0.6709
    paper_std: null
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: null
    sort_value: 0.6709
    sort_std: null
    is_best: false
  - model: DGI
    model_key: dgi
    model_plain: DGI
    value: 0.6331
    std: null
    paper_value: 0.6331
    paper_std: null
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: null
    sort_value: 0.6331
    sort_std: null
    is_best: false
  - model: GraphMAE
    model_key: graphmae
    model_plain: GraphMAE
    value: 0.633
    std: null
    paper_value: 0.633
    paper_std: null
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: null
    sort_value: 0.633
    sort_std: null
    is_best: false
  - model: GIANT
    model_key: giant
    model_plain: GIANT
    value: 0.6149
    std: null
    paper_value: 0.6149
    paper_std: null
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: null
    sort_value: 0.6149
    sort_std: null
    is_best: false
  - model: GatedGCN + VN
    model_key: gatedgcn + vn
    model_plain: GatedGCN + VN
    value: 0.3141
    std: 0.0019
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.11951'
    title: 'Distinguished In Uniform: Self-Attention Vs. Virtual Nodes'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.3141
    sort_std: 0.0019
    is_best: false
  - model: NeuralWalker
    model_key: neuralwalker
    model_plain: NeuralWalker
    value: 0.3086
    std: 0.0031
    metric: AP
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
    global_rank: 2
    sort_value: 0.3086
    sort_std: 0.0031
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.3066
    std: 0.0013
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.11951'
    title: 'Distinguished In Uniform: Self-Attention Vs. Virtual Nodes'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.3066
    sort_std: 0.0013
    is_best: false
  metric: AP
  higher_is_better: true
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
  - *id002
  - *id003
  - *id004
- benchmark: LRGB
  datasets:
  - *id005
- benchmark: OGB
  datasets:
  - *id006
  - *id007
- benchmark: MoleculeNet
  datasets:
  - *id008
- benchmark: Knowledge Graphs
  datasets:
  - *id009
main_figure: /figures/2506.14098/main_figure.png
---

