---
title: Exploring the Potential of Large Language Models (LLMs) in Learning on Graphs
arxiv_id: '2307.03393'
source_url: ''
authors: []
published_date: Jul 2023
published_date_iso: 2023-07
abstract: 'Learning on Graphs has attracted immense attention due to its wide real-world
  applications. The most popular pipeline for learning on graphs with textual node
  attributes primarily relies on Graph Neural Networks (GNNs), and utilizes shallow
  text embedding as initial node representations, which has limitations in general
  knowledge and profound semantic understanding. In recent years, Large Language Models
  (LLMs) have been proven to possess extensive common knowledge and powerful semantic
  comprehension abilities that have revolutionized existing workflows to handle text
  data. In this paper, we aim to explore the potential of LLMs in graph machine learning,
  especially the node classification task, and investigate two possible pipelines:
  LLMs-as-Enhancers and LLMs-as-Predictors. The former leverages LLMs to enhance nodes''
  text attributes with their massive knowledge and then generate predictions through
  GNNs. The latter attempts to directly employ LLMs as standalone predictors. We conduct
  comprehensive and systematical studies on these two pipelines under various settings.
  From comprehensive empirical results, we make original observations and find new
  insights that open new possibilities and suggest promising directions to leverage
  LLMs for learning on graphs. Our codes and datasets are available at: https://github.com/CurryTang/Graph-LLM'
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- GLEM-GNN
- GLEM-LM
- TAPE
- LLM Zero-shot
- LLM Few-shot
- LLM Zero-shot with COT
- LLM Few-shot with COT
- LLM Zero-Shot with 2-hop info
- LLM Few-Shot with 2-hop info
- Zero-shot
- Few-shot
mrr: 0.0076
adjusted_mrr: 0.0051
mrr_dataset_count: 2
benchmark_categories:
- Classic
- OGB
task_categories:
- node_classification
experiment_scopes:
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
  - model: GCN/SAGE
    model_key: gcn/sage
    model_plain: GCN/SAGE
    value: 0.7119
    std: 0.011
    paper_value: 0.7119
    paper_std: 0.011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 126
    true_value: 0.7119
    true_std: 0.011
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 126
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7119
    sort_std: 0.011
    is_best: false
  - model: LLM Few-Shot with 2-hop info
    model_key: llm few-shot with 2-hop info
    model_plain: LLM Few-Shot with 2-hop info
    value: 0.67
    std: 0.0494
    paper_value: 0.67
    paper_std: 0.0494
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 154
    true_value: 0.67
    true_std: 0.0494
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 154
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.67
    sort_std: 0.0494
    is_best: false
  - model: LLM Zero-shot with COT
    model_key: llm zero-shot with cot
    model_plain: LLM Zero-shot with COT
    value: 0.665
    std: 0.0282
    paper_value: 0.665
    paper_std: 0.0282
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 157
    true_value: 0.665
    true_std: 0.0282
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 157
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.665
    sort_std: 0.0282
    is_best: false
  - model: Few-shot
    model_key: few-shot
    model_plain: Few-shot
    value: 0.66
    std: 0.0566
    paper_value: 0.66
    paper_std: 0.0566
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 162
    true_value: 0.66
    true_std: 0.0566
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 162
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.66
    sort_std: 0.0566
    is_best: false
  - model: Zero-shot
    model_key: zero-shot
    model_plain: Zero-shot
    value: 0.655
    std: 0.0353
    paper_value: 0.655
    paper_std: 0.0353
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 163
    true_value: 0.655
    true_std: 0.0353
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 163
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.655
    sort_std: 0.0353
    is_best: false
  - model: LLM Zero-Shot with 2-hop info
    model_key: llm zero-shot with 2-hop info
    model_plain: LLM Zero-Shot with 2-hop info
    value: 0.62
    std: 0.0141
    paper_value: 0.62
    paper_std: 0.0141
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 186
    true_value: 0.62
    true_std: 0.0141
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 186
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.62
    sort_std: 0.0141
    is_best: false
  - model: LLM Few-shot with COT
    model_key: llm few-shot with cot
    model_plain: LLM Few-shot with COT
    value: 0.605
    std: 0.0494
    paper_value: 0.605
    paper_std: 0.0494
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 196
    true_value: 0.605
    true_std: 0.0494
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 196
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.605
    sort_std: 0.0494
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
  - model: TAPE (E (e5))
    model_key: tape (e (e5))
    model_plain: TAPE (E (e5))
    value: 0.8438
    std: 0.0036
    paper_value: 0.8438
    paper_std: 0.0036
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 108
    true_value: 0.8438
    true_std: 0.0036
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 108
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8438
    sort_std: 0.0036
    is_best: false
  - model: text-ada-embedding-002
    model_key: text-ada-embedding-002
    model_plain: text-ada-embedding-002
    value: 0.8272
    std: 0.0069
    paper_value: 0.8272
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
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 132
    true_value: 0.8272
    true_std: 0.0069
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 132
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8272
    sort_std: 0.0069
    is_best: false
  - model: e5-large
    model_key: e5-large
    model_plain: e5-large
    value: 0.8256
    std: 0.0073
    paper_value: 0.8256
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
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 135
    true_value: 0.8256
    true_std: 0.0073
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 135
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8256
    sort_std: 0.0073
    is_best: false
  - model: TAPE (TA + E (e5))
    model_key: tape (ta + e (e5))
    model_plain: TAPE (TA + E (e5))
    value: 0.8256
    std: 0.0073
    paper_value: 0.8256
    paper_std: 0.0073
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 136
    true_value: 0.8256
    true_std: 0.0073
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 136
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8256
    sort_std: 0.0073
    is_best: false
  - model: Sentence-BERT(MiniLM)
    model_key: sentence-bert(minilm)
    model_plain: Sentence-BERT(MiniLM)
    value: 0.822
    std: 0.0049
    paper_value: 0.822
    paper_std: 0.0049
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 141
    true_value: 0.822
    true_std: 0.0049
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 141
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.822
    sort_std: 0.0049
    is_best: false
  - model: TF-IDF
    model_key: tf-idf
    model_plain: TF-IDF
    value: 0.8199
    std: 0.0063
    paper_value: 0.8199
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
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 142
    true_value: 0.8199
    true_std: 0.0063
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 142
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8199
    sort_std: 0.0063
    is_best: false
  - model: Google Palm Cortex 001
    model_key: google palm cortex 001
    model_plain: Google Palm Cortex 001
    value: 0.8115
    std: 0.0101
    paper_value: 0.8115
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
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 151
    true_value: 0.8115
    true_std: 0.0101
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 151
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8115
    sort_std: 0.0101
    is_best: false
  - model: TAPE (E (PLM))
    model_key: tape (e (plm))
    model_plain: TAPE (E (PLM))
    value: 0.7946
    std: 0.011
    paper_value: 0.7946
    paper_std: 0.011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 159
    true_value: 0.7946
    true_std: 0.011
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 159
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7946
    sort_std: 0.011
    is_best: false
  - model: TAPE
    model_key: tape
    model_plain: TAPE
    value: 0.7456
    std: 0.0203
    paper_value: 0.7456
    paper_std: 0.0203
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 203
    true_value: 0.7456
    true_std: 0.0203
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 203
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7456
    sort_std: 0.0203
    is_best: false
  - model: Word2Vec
    model_key: word2vec
    model_plain: Word2Vec
    value: 0.7401
    std: 0.0124
    paper_value: 0.7401
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
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 206
    true_value: 0.7401
    true_std: 0.0124
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 206
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7401
    sort_std: 0.0124
    is_best: false
  - model: LLama 7B
    model_key: llama 7b
    model_plain: LLama 7B
    value: 0.668
    std: 0.022
    paper_value: 0.668
    paper_std: 0.022
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 267
    true_value: 0.668
    true_std: 0.022
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 267
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.668
    sort_std: 0.022
    is_best: false
  - model: Fine-tuned Deberta-base
    model_key: fine-tuned deberta-base
    model_plain: Fine-tuned Deberta-base
    value: 0.5923
    std: 0.0116
    paper_value: 0.5923
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
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 284
    true_value: 0.5923
    true_std: 0.0116
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 284
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5923
    sort_std: 0.0116
    is_best: false
  - model: GLEM-LM
    model_key: glem-lm
    model_plain: GLEM-LM
    value: 0.5923
    std: 0.0116
    paper_value: 0.5923
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
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 285
    true_value: 0.5923
    true_std: 0.0116
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 285
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5923
    sort_std: 0.0116
    is_best: false
  - model: TAPE (TA + E (PLM))
    model_key: tape (ta + e (plm))
    model_plain: TAPE (TA + E (PLM))
    value: 0.5923
    std: 0.0116
    paper_value: 0.5923
    paper_std: 0.0116
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 286
    true_value: 0.5923
    true_std: 0.0116
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 286
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5923
    sort_std: 0.0116
    is_best: false
  - model: TAPE (P)
    model_key: tape (p)
    model_plain: TAPE (P)
    value: 0.5279
    std: 0.0147
    paper_value: 0.5279
    paper_std: 0.0147
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 296
    true_value: 0.5279
    true_std: 0.0147
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 296
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5279
    sort_std: 0.0147
    is_best: false
  - model: Deberta-base
    model_key: deberta-base
    model_plain: Deberta-base
    value: 0.4849
    std: 0.0186
    paper_value: 0.4849
    paper_std: 0.0186
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 298
    true_value: 0.4849
    true_std: 0.0186
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 298
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4849
    sort_std: 0.0186
    is_best: false
  - model: GLEM-GNN
    model_key: glem-gnn
    model_plain: GLEM-GNN
    value: 0.4849
    std: 0.0186
    paper_value: 0.4849
    paper_std: 0.0186
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 299
    true_value: 0.4849
    true_std: 0.0186
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 299
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4849
    sort_std: 0.0186
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
  - model: TAPE
    model_key: tape
    model_plain: TAPE
    value: 0.8597
    std: 0.0031
    paper_value: 0.8597
    paper_std: 0.0031
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 97
    true_value: 0.8597
    true_std: 0.0031
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 97
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8597
    sort_std: 0.0031
    is_best: false
  - model: e5-large
    model_key: e5-large
    model_plain: e5-large
    value: 0.8263
    std: 0.0113
    paper_value: 0.8263
    paper_std: 0.0113
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 107
    true_value: 0.8263
    true_std: 0.0113
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 107
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8263
    sort_std: 0.0113
    is_best: false
  - model: TAPE (TA + E (e5))
    model_key: tape (ta + e (e5))
    model_plain: TAPE (TA + E (e5))
    value: 0.8263
    std: 0.0113
    paper_value: 0.8263
    paper_std: 0.0113
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 108
    true_value: 0.8263
    true_std: 0.0113
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 108
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8263
    sort_std: 0.0113
    is_best: false
  - model: TAPE (E (e5))
    model_key: tape (e (e5))
    model_plain: TAPE (E (e5))
    value: 0.8223
    std: 0.0078
    paper_value: 0.8223
    paper_std: 0.0078
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 109
    true_value: 0.8223
    true_std: 0.0078
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 109
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8223
    sort_std: 0.0078
    is_best: false
  - model: TAPE (P)
    model_key: tape (p)
    model_plain: TAPE (P)
    value: 0.8192
    std: 0.0189
    paper_value: 0.8192
    paper_std: 0.0189
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 111
    true_value: 0.8192
    true_std: 0.0189
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 111
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8192
    sort_std: 0.0189
    is_best: false
  - model: TAPE (E (PLM))
    model_key: tape (e (plm))
    model_plain: TAPE (E (PLM))
    value: 0.8188
    std: 0.0005
    paper_value: 0.8188
    paper_std: 0.0005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 112
    true_value: 0.8188
    true_std: 0.0005
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 112
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8188
    sort_std: 0.0005
    is_best: false
  - model: Sentence-BERT(MiniLM)
    model_key: sentence-bert(minilm)
    model_plain: Sentence-BERT(MiniLM)
    value: 0.8101
    std: 0.0132
    paper_value: 0.8101
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
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 115
    true_value: 0.8101
    true_std: 0.0132
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 115
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8101
    sort_std: 0.0132
    is_best: false
  - model: Google Palm Cortex 001
    model_key: google palm cortex 001
    model_plain: Google Palm Cortex 001
    value: 0.8091
    std: 0.0019
    paper_value: 0.8091
    paper_std: 0.0019
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 116
    true_value: 0.8091
    true_std: 0.0019
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 116
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8091
    sort_std: 0.0019
    is_best: false
  - model: text-ada-embedding-002
    model_key: text-ada-embedding-002
    model_plain: text-ada-embedding-002
    value: 0.7909
    std: 0.0151
    paper_value: 0.7909
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
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 123
    true_value: 0.7909
    true_std: 0.0151
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 123
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7909
    sort_std: 0.0151
    is_best: false
  - model: TF-IDF
    model_key: tf-idf
    model_plain: TF-IDF
    value: 0.7886
    std: 0.02
    paper_value: 0.7886
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
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 124
    true_value: 0.7886
    true_std: 0.02
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 124
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7886
    sort_std: 0.02
    is_best: false
  - model: LLama 7B
    model_key: llama 7b
    model_plain: LLama 7B
    value: 0.7353
    std: 0.0006
    paper_value: 0.7353
    paper_std: 0.0006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 149
    true_value: 0.7353
    true_std: 0.0006
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 149
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7353
    sort_std: 0.0006
    is_best: false
  - model: Word2Vec
    model_key: word2vec
    model_plain: Word2Vec
    value: 0.701
    std: 0.018
    paper_value: 0.701
    paper_std: 0.018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 154
    true_value: 0.701
    true_std: 0.018
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 154
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.701
    sort_std: 0.018
    is_best: false
  - model: Fine-tuned Deberta-base
    model_key: fine-tuned deberta-base
    model_plain: Fine-tuned Deberta-base
    value: 0.6212
    std: 0.0007
    paper_value: 0.6212
    paper_std: 0.0007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 164
    true_value: 0.6212
    true_std: 0.0007
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 164
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6212
    sort_std: 0.0007
    is_best: false
  - model: GLEM-LM
    model_key: glem-lm
    model_plain: GLEM-LM
    value: 0.6212
    std: 0.0007
    paper_value: 0.6212
    paper_std: 0.0007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 165
    true_value: 0.6212
    true_std: 0.0007
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 165
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6212
    sort_std: 0.0007
    is_best: false
  - model: TAPE (TA + E (PLM))
    model_key: tape (ta + e (plm))
    model_plain: TAPE (TA + E (PLM))
    value: 0.6212
    std: 0.0007
    paper_value: 0.6212
    paper_std: 0.0007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 166
    true_value: 0.6212
    true_std: 0.0007
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 166
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6212
    sort_std: 0.0007
    is_best: false
  - model: Deberta-base
    model_key: deberta-base
    model_plain: Deberta-base
    value: 0.6208
    std: 0.0006
    paper_value: 0.6208
    paper_std: 0.0006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 167
    true_value: 0.6208
    true_std: 0.0006
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 167
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6208
    sort_std: 0.0006
    is_best: false
  - model: GLEM-GNN
    model_key: glem-gnn
    model_plain: GLEM-GNN
    value: 0.6208
    std: 0.0006
    paper_value: 0.6208
    paper_std: 0.0006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 168
    true_value: 0.6208
    true_std: 0.0006
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 168
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6208
    sort_std: 0.0006
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: ogbn-arxiv
  rows:
  - model: GLEM-GNN
    model_key: glem-gnn
    model_plain: GLEM-GNN
    value: 0.7593
    std: 0.0019
    paper_value: 0.7593
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
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 1
    true_value: 0.7593
    true_std: 0.0019
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
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
    paper_value: 0.7571
    paper_std: 0.0024
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 3
    true_value: 0.7571
    true_std: 0.0024
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7571
    sort_std: 0.0024
    is_best: true
  - model: DMD-ACMP
    model_key: dmd-acmp
    model_plain: DMD-ACMP
    value: 0.755
    std: 0.008
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
    global_rank: 4
    sort_value: 0.755
    sort_std: 0.008
    is_best: true
  - model: RevGAT
    model_key: revgat
    model_plain: RevGAT
    value: 0.7516
    std: 0.0014
    paper_value: 0.7516
    paper_std: 0.0014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 5
    true_value: 0.7516
    true_std: 0.0014
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7516
    sort_std: 0.0014
    is_best: false
  - model: Fine-tuned Deberta-base
    model_key: fine-tuned deberta-base
    model_plain: Fine-tuned Deberta-base
    value: 0.7465
    std: 0.0012
    paper_value: 0.7465
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
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 6
    true_value: 0.7465
    true_std: 0.0012
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7465
    sort_std: 0.0012
    is_best: false
  - model: DMD++
    model_key: dmd++
    model_plain: DMD++
    value: 0.744
    std: 0.015
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
    global_rank: 7
    sort_value: 0.744
    sort_std: 0.015
    is_best: true
  - model: e5-large
    model_key: e5-large
    model_plain: e5-large
    value: 0.7374
    std: 0.0012
    paper_value: 0.7374
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
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 12
    true_value: 0.7374
    true_std: 0.0012
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7374
    sort_std: 0.0012
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.731
    std: 0.0025
    paper_value: 0.731
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
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 14
    true_value: 0.7353
    true_std: 0.0012
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0042999999999999705
    value_note: ''
    paper_rank: 22
    rank_delta: 8
    rank_delta_abs: 8
    rank_delta_direction: worse
    sort_value: 0.7353
    sort_std: 0.0012
    is_best: false
  - model: GIANT
    model_key: giant
    model_plain: GIANT
    value: 0.7329
    std: 0.001
    paper_value: 0.7329
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
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 19
    true_value: 0.7329
    true_std: 0.001
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7329
    sort_std: 0.001
    is_best: false
  - model: Sentence-BERT(MiniLM)
    model_key: sentence-bert(minilm)
    model_plain: Sentence-BERT(MiniLM)
    value: 0.731
    std: 0.0025
    paper_value: 0.731
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
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 24
    true_value: 0.731
    true_std: 0.0025
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.731
    sort_std: 0.0025
    is_best: false
  - model: text-ada-embedding-002
    model_key: text-ada-embedding-002
    model_plain: text-ada-embedding-002
    value: 0.7276
    std: 0.0023
    paper_value: 0.7276
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
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 34
    true_value: 0.7276
    true_std: 0.0023
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 34
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7276
    sort_std: 0.0023
    is_best: false
  - model: TF-IDF
    model_key: tf-idf
    model_plain: TF-IDF
    value: 0.7223
    std: 0.0021
    paper_value: 0.7223
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
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 48
    true_value: 0.7223
    true_std: 0.0021
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 48
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7223
    sort_std: 0.0021
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.666
    std: 0.0025
    paper_value: 0.666
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
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 91
    true_value: 0.666
    true_std: 0.0025
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 91
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.666
    sort_std: 0.0025
    is_best: false
  - model: ChatGPT (Zero-shot with 2-hop info)
    model_key: chatgpt (zero-shot with 2-hop info)
    model_plain: ChatGPT (Zero-shot with 2-hop info)
    value: 0.55
    std: 0.0283
    paper_value: 0.55
    paper_std: 0.0283
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 102
    true_value: 0.55
    true_std: 0.0283
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 102
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.55
    sort_std: 0.0283
    is_best: false
  - model: ChatGPT (Few-shot with 2-hop info)
    model_key: chatgpt (few-shot with 2-hop info)
    model_plain: ChatGPT (Few-shot with 2-hop info)
    value: 0.5225
    std: 0.0318
    paper_value: 0.5225
    paper_std: 0.0318
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 106
    true_value: 0.5225
    true_std: 0.0318
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 106
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5225
    sort_std: 0.0318
    is_best: false
  - model: ChatGPT (Zero-shot)
    model_key: chatgpt (zero-shot)
    model_plain: ChatGPT (Zero-shot)
    value: 0.5175
    std: 0.0389
    paper_value: 0.5175
    paper_std: 0.0389
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 107
    true_value: 0.5175
    true_std: 0.0389
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 107
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5175
    sort_std: 0.0389
    is_best: false
  - model: ChatGPT (Zero-shot with COT)
    model_key: chatgpt (zero-shot with cot)
    model_plain: ChatGPT (Zero-shot with COT)
    value: 0.505
    std: 0.0141
    paper_value: 0.505
    paper_std: 0.0141
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 109
    true_value: 0.505
    true_std: 0.0141
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 109
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.505
    sort_std: 0.0141
    is_best: false
  - model: ChatGPT (Few-shot)
    model_key: chatgpt (few-shot)
    model_plain: ChatGPT (Few-shot)
    value: 0.5025
    std: 0.0106
    paper_value: 0.5025
    paper_std: 0.0106
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 110
    true_value: 0.5025
    true_std: 0.0106
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 110
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5025
    sort_std: 0.0106
    is_best: false
  - model: ChatGPT (Few-shot with COT)
    model_key: chatgpt (few-shot with cot)
    model_plain: ChatGPT (Few-shot with COT)
    value: 0.4725
    std: 0.0247
    paper_value: 0.4725
    paper_std: 0.0247
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 111
    true_value: 0.4725
    true_std: 0.0247
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 111
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4725
    sort_std: 0.0247
    is_best: false
  - model: Deberta-base
    model_key: deberta-base
    model_plain: Deberta-base
    value: 0.457
    std: 0.0559
    paper_value: 0.457
    paper_std: 0.0559
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 112
    true_value: 0.457
    true_std: 0.0559
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 112
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.457
    sort_std: 0.0559
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id005
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
    paper_value: 0.8736
    paper_std: 0.0007
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 3
    true_value: 0.8736
    true_std: 0.0007
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8736
    sort_std: 0.0007
    is_best: false
  - model: GLEM-LM
    model_key: glem-lm
    model_plain: GLEM-LM
    value: 0.8483
    std: 0.0004
    paper_value: 0.8483
    paper_std: 0.0004
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 4
    true_value: 0.8483
    true_std: 0.0004
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8483
    sort_std: 0.0004
    is_best: false
  - model: GT + HDSE
    model_key: gt + hdse
    model_plain: GT + HDSE
    value: 0.8338
    std: 0.0017
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
    global_rank: 5
    sort_value: 0.8338
    sort_std: 0.0017
    is_best: false
  - model: GCN/SAGE
    model_key: gcn/sage
    model_plain: GCN/SAGE
    value: 0.8251
    std: 0.0053
    paper_value: 0.8251
    paper_std: 0.0053
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 7
    true_value: 0.8251
    true_std: 0.0053
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8251
    sort_std: 0.0053
    is_best: false
  - model: GIANT
    model_key: giant
    model_plain: GIANT
    value: 0.7982
    std: 0.0007
    paper_value: 0.7982
    paper_std: 0.0007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 17
    true_value: 0.7982
    true_std: 0.0007
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7982
    sort_std: 0.0007
    is_best: false
  - model: Fine-tuned Deberta-base
    model_key: fine-tuned deberta-base
    model_plain: Fine-tuned Deberta-base
    value: 0.7908
    std: 0.0023
    paper_value: 0.7908
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
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 23
    true_value: 0.7908
    true_std: 0.0023
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7908
    sort_std: 0.0023
    is_best: false
  - model: LLM Few-shot
    model_key: llm few-shot
    model_plain: LLM Few-shot
    value: 0.7775
    std: 0.0106
    paper_value: 0.7775
    paper_std: 0.0106
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 28
    true_value: 0.7775
    true_std: 0.0106
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 28
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7775
    sort_std: 0.0106
    is_best: false
  - model: e5-large
    model_key: e5-large
    model_plain: e5-large
    value: 0.7749
    std: 0.0029
    paper_value: 0.7749
    paper_std: 0.0029
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 30
    true_value: 0.7749
    true_std: 0.0029
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 30
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7749
    sort_std: 0.0029
    is_best: false
  - model: text-ada-embedding-002
    model_key: text-ada-embedding-002
    model_plain: text-ada-embedding-002
    value: 0.7642
    std: 0.0031
    paper_value: 0.7642
    paper_std: 0.0031
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 33
    true_value: 0.7642
    true_std: 0.0031
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7642
    sort_std: 0.0031
    is_best: false
  - model: LLM Few-Shot with 2-hop info
    model_key: llm few-shot with 2-hop info
    model_plain: LLM Few-Shot with 2-hop info
    value: 0.76
    std: 0.0282
    paper_value: 0.76
    paper_std: 0.0282
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 35
    true_value: 0.76
    true_std: 0.0282
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.76
    sort_std: 0.0282
    is_best: false
  - model: LLM Zero-Shot with 2-hop info
    model_key: llm zero-shot with 2-hop info
    model_plain: LLM Zero-Shot with 2-hop info
    value: 0.7525
    std: 0.0353
    paper_value: 0.7525
    paper_std: 0.0353
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 39
    true_value: 0.7525
    true_std: 0.0353
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7525
    sort_std: 0.0353
    is_best: false
  - model: LLM Few-shot with COT
    model_key: llm few-shot with cot
    model_plain: LLM Few-shot with COT
    value: 0.7325
    std: 0.0177
    paper_value: 0.7325
    paper_std: 0.0177
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 41
    true_value: 0.7325
    true_std: 0.0177
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 41
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7325
    sort_std: 0.0177
    is_best: false
  - model: Sentence-BERT(MiniLM)
    model_key: sentence-bert(minilm)
    model_plain: Sentence-BERT(MiniLM)
    value: 0.7273
    std: 0.0034
    paper_value: 0.7273
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
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 43
    true_value: 0.7273
    true_std: 0.0034
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 43
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7273
    sort_std: 0.0034
    is_best: false
  - model: LLM Zero-shot with COT
    model_key: llm zero-shot with cot
    model_plain: LLM Zero-shot with COT
    value: 0.7125
    std: 0.0106
    paper_value: 0.7125
    paper_std: 0.0106
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 45
    true_value: 0.7125
    true_std: 0.0106
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 45
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7125
    sort_std: 0.0106
    is_best: false
  - model: LLM Zero-shot
    model_key: llm zero-shot
    model_plain: LLM Zero-shot
    value: 0.7075
    std: 0.0248
    paper_value: 0.7075
    paper_std: 0.0248
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 46
    true_value: 0.7075
    true_std: 0.0248
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 46
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7075
    sort_std: 0.0248
    is_best: false
  - model: Word2Vec
    model_key: word2vec
    model_plain: Word2Vec
    value: 0.6927
    std: 0.0054
    paper_value: 0.6927
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
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 48
    true_value: 0.6927
    true_std: 0.0054
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 48
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6927
    sort_std: 0.0054
    is_best: false
  - model: TF-IDF
    model_key: tf-idf
    model_plain: TF-IDF
    value: 0.6442
    std: 0.0018
    paper_value: 0.6442
    paper_std: 0.0018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 49
    true_value: 0.6442
    true_std: 0.0018
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 49
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6442
    sort_std: 0.0018
    is_best: false
  - model: Deberta-base
    model_key: deberta-base
    model_plain: Deberta-base
    value: 0.0718
    std: 0.0109
    paper_value: 0.0718
    paper_std: 0.0109
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    global_rank: 51
    true_value: 0.0718
    true_std: 0.0109
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 51
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.0718
    sort_std: 0.0109
    is_best: false
  metric: Accuracy
  higher_is_better: true
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
  - *id002
  - *id003
- benchmark: OGB
  datasets:
  - *id004
  - *id005
main_figure: /figures/2307.03393/main_figure.png
---

