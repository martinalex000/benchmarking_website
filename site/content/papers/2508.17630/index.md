---
title: 'Quantum Graph Attention Network: A Novel Quantum Multi-Head Attention Mechanism
  for Graph Learning'
arxiv_id: '2508.17630'
source_url: ''
authors: []
published_date: Aug 2025
published_date_iso: 2025-08
abstract: We propose the Quantum Graph Attention Network (QGAT), a hybrid graph neural
  network that integrates variational quantum circuits into the attention mechanism.
  At its core, QGAT employs strongly entangling quantum circuits with amplitude-encoded
  node features to enable expressive nonlinear interactions. Distinct from classical
  multi-head attention that separately computes each head, QGAT leverages a single
  quantum circuit to simultaneously generate multiple attention coefficients. This
  quantum parallelism facilitates parameter sharing across heads, substantially reducing
  computational overhead and model complexity. Classical projection weights and quantum
  circuit parameters are optimized jointly in an end-to-end manner, ensuring flexible
  adaptation to learning tasks. Empirical results demonstrate QGAT’s effectiveness
  in capturing complex structural dependencies and improved generalization in inductive
  scenarios, highlighting its potential for scalable quantum-enhanced learning across
  domains such as chemistry, biology, and network analysis. Furthermore, experiments
  confirm that quantum embedding enhances robustness against feature and structural
  noise, suggesting advantages in handling real-world noisy data. The modularity of
  QGAT also ensures straightforward integration into existing architectures, allowing
  it to easily augment classical attention-based models.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- QGAT
mrr: 0.0803
adjusted_mrr: 0.0803
mrr_dataset_count: 4
benchmark_categories:
- Classic
- OGB
task_categories:
- link_prediction
- node_classification
experiment_scopes:
- edge-level
- node-level
results:
- &id002
  dataset: PPI
  rows:
  - model: QGAT
    model_key: qgat
    model_plain: QGAT
    value: 0.989
    std: 0.0012
    paper_value: 0.989
    paper_std: 0.0012
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 1
    true_value: 0.989
    true_std: 0.0012
    value_gap_source_arxiv: '2508.17630'
    value_gap_source_title: 'Quantum Graph Attention Network: A Novel Quantum Multi-Head
      Attention Mechanism for Graph Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.989
    sort_std: 0.0012
    is_best: true
  - model: GATv2
    model_key: gatv2
    model_plain: GATv2
    value: 0.982
    std: 0.0025
    paper_value: 0.982
    paper_std: 0.0025
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Brody et al. 2021
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 2
    true_value: 0.982
    true_std: 0.0025
    value_gap_source_arxiv: '2508.17630'
    value_gap_source_title: 'Quantum Graph Attention Network: A Novel Quantum Multi-Head
      Attention Mechanism for Graph Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.982
    sort_std: 0.0025
    is_best: false
  - model: IGNN*
    model_key: ignn*
    model_plain: IGNN*
    value: 0.976
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.00494'
    title: Graph Neural Networks Gone Hogwild
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 3
    sort_value: 0.976
    sort_std: null
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.973
    std: 0.002
    paper_value: 0.973
    paper_std: 0.002
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hamilton et al. 2017
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 4
    true_value: 0.973
    true_std: null
    value_gap_source_arxiv: '2407.00494'
    value_gap_source_title: Graph Neural Networks Gone Hogwild
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.973
    sort_std: null
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.768
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.00494'
    title: Graph Neural Networks Gone Hogwild
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 5
    sort_value: 0.768
    sort_std: null
    is_best: false
  - model: Energy GNN (edge-wise)
    model_key: energy gnn (edge-wise)
    model_plain: Energy GNN (edge-wise)
    value: 0.762
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.00494'
    title: Graph Neural Networks Gone Hogwild
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 6
    sort_value: 0.762
    sort_std: null
    is_best: false
  metric: F1
  higher_is_better: true
- &id001
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
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.781
    std: 0.0059
    paper_value: 0.781
    paper_std: 0.0059
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Brody et al. 2021
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 6
    true_value: 0.9201
    true_std: 0.0024
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1391
    value_note: ''
    paper_rank: 125
    rank_delta: 119
    rank_delta_abs: 119
    rank_delta_direction: worse
    sort_value: 0.9201
    sort_std: 0.0024
    is_best: false
  - model: GATv2
    model_key: gatv2
    model_plain: GATv2
    value: 0.785
    std: 0.0038
    paper_value: 0.785
    paper_std: 0.0038
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Brody et al. 2021
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 94
    true_value: 0.867
    true_std: 0.008
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08199999999999996
    value_note: ''
    paper_rank: 124
    rank_delta: 30
    rank_delta_abs: 30
    rank_delta_direction: worse
    sort_value: 0.867
    sort_std: 0.008
    is_best: false
  - model: QGAT
    model_key: qgat
    model_plain: QGAT
    value: 0.792
    std: 0.0062
    paper_value: 0.792
    paper_std: 0.0062
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 122
    true_value: 0.792
    true_std: 0.0062
    value_gap_source_arxiv: '2508.17630'
    value_gap_source_title: 'Quantum Graph Attention Network: A Novel Quantum Multi-Head
      Attention Mechanism for Graph Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 122
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.792
    sort_std: 0.0062
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id007
  dataset: ogbl-citation2
  rows:
  - model: QGAT
    model_key: qgat
    model_plain: QGAT
    value: 0.822
    std: 0.0127
    paper_value: 0.822
    paper_std: 0.0127
    metric: MRR
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 1
    true_value: 0.822
    true_std: 0.0127
    value_gap_source_arxiv: '2508.17630'
    value_gap_source_title: 'Quantum Graph Attention Network: A Novel Quantum Multi-Head
      Attention Mechanism for Graph Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.822
    sort_std: 0.0127
    is_best: true
  - model: GATv2
    model_key: gatv2
    model_plain: GATv2
    value: 0.8014
    std: 0.0071
    paper_value: 0.8014
    paper_std: 0.0071
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Brody et al. 2021
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 2
    true_value: 0.8014
    true_std: 0.0071
    value_gap_source_arxiv: '2508.17630'
    value_gap_source_title: 'Quantum Graph Attention Network: A Novel Quantum Multi-Head
      Attention Mechanism for Graph Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8014
    sort_std: 0.0071
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.7595
    std: 0.0131
    paper_value: 0.7595
    paper_std: 0.0131
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Brody et al. 2021
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 3
    true_value: 0.7595
    true_std: 0.0131
    value_gap_source_arxiv: '2508.17630'
    value_gap_source_title: 'Quantum Graph Attention Network: A Novel Quantum Multi-Head
      Attention Mechanism for Graph Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7595
    sort_std: 0.0131
    is_best: false
  metric: MRR
  higher_is_better: true
- &id006
  dataset: ogbl-collab
  rows:
  - model: QGAT
    model_key: qgat
    model_plain: QGAT
    value: 0.512
    std: 0.0192
    paper_value: 0.512
    paper_std: 0.0192
    metric: Hits@50
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 1
    true_value: 0.512
    true_std: 0.0192
    value_gap_source_arxiv: '2508.17630'
    value_gap_source_title: 'Quantum Graph Attention Network: A Novel Quantum Multi-Head
      Attention Mechanism for Graph Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.512
    sort_std: 0.0192
    is_best: true
  - model: GATv2
    model_key: gatv2
    model_plain: GATv2
    value: 0.497
    std: 0.0308
    paper_value: 0.497
    paper_std: 0.0308
    metric: Hits@50
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Brody et al. 2021
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 4
    true_value: 0.497
    true_std: 0.0308
    value_gap_source_arxiv: '2508.17630'
    value_gap_source_title: 'Quantum Graph Attention Network: A Novel Quantum Multi-Head
      Attention Mechanism for Graph Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.497
    sort_std: 0.0308
    is_best: true
  - model: GPM
    model_key: gpm
    model_plain: GPM
    value: 0.497
    std: 0.0059
    metric: Hits@50
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.497
    sort_std: 0.0059
    is_best: true
  - model: Graph transformer
    model_key: graph transformer
    model_plain: Graph transformer
    value: 0.497
    std: 0.0059
    metric: Hits@50
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
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.497
    sort_std: 0.0059
    is_best: true
  - model: GPM w/o PE
    model_key: gpm w/o pe
    model_plain: GPM w/o PE
    value: 0.4959
    std: 0.0065
    metric: Hits@50
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
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    sort_value: 0.4959
    sort_std: 0.0065
    is_best: true
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.4663
    std: 0.028
    paper_value: 0.4663
    paper_std: 0.028
    metric: Hits@50
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Brody et al. 2021
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 13
    true_value: 0.4663
    true_std: 0.028
    value_gap_source_arxiv: '2508.17630'
    value_gap_source_title: 'Quantum Graph Attention Network: A Novel Quantum Multi-Head
      Attention Mechanism for Graph Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4663
    sort_std: 0.028
    is_best: true
  metric: Hits@50
  higher_is_better: true
- &id003
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
  - model: QGAT
    model_key: qgat
    model_plain: QGAT
    value: 0.7362
    std: 0.0042
    paper_value: 0.7362
    paper_std: 0.0042
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 13
    true_value: 0.7362
    true_std: 0.0042
    value_gap_source_arxiv: '2508.17630'
    value_gap_source_title: 'Quantum Graph Attention Network: A Novel Quantum Multi-Head
      Attention Mechanism for Graph Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7362
    sort_std: 0.0042
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.7154
    std: 0.003
    paper_value: 0.7154
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Brody et al. 2021
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 17
    true_value: 0.733
    true_std: 0.0018
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.01759999999999995
    value_note: ''
    paper_rank: 66
    rank_delta: 49
    rank_delta_abs: 49
    rank_delta_direction: worse
    sort_value: 0.733
    sort_std: 0.0018
    is_best: false
  - model: GATv2
    model_key: gatv2
    model_plain: GATv2
    value: 0.7187
    std: 0.0025
    paper_value: 0.7187
    paper_std: 0.0025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Brody et al. 2021
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 62
    true_value: 0.7187
    true_std: 0.0025
    value_gap_source_arxiv: '2508.17630'
    value_gap_source_title: 'Quantum Graph Attention Network: A Novel Quantum Multi-Head
      Attention Mechanism for Graph Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 62
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7187
    sort_std: 0.0025
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
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
  - model: QGAT
    model_key: qgat
    model_plain: QGAT
    value: 0.821
    std: 0.0231
    paper_value: 0.821
    paper_std: 0.0231
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 8
    true_value: 0.821
    true_std: 0.0231
    value_gap_source_arxiv: '2508.17630'
    value_gap_source_title: 'Quantum Graph Attention Network: A Novel Quantum Multi-Head
      Attention Mechanism for Graph Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.821
    sort_std: 0.0231
    is_best: false
  - model: GATv2
    model_key: gatv2
    model_plain: GATv2
    value: 0.8063
    std: 0.007
    paper_value: 0.8063
    paper_std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Brody et al. 2021
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 14
    true_value: 0.8063
    true_std: 0.007
    value_gap_source_arxiv: '2508.17630'
    value_gap_source_title: 'Quantum Graph Attention Network: A Novel Quantum Multi-Head
      Attention Mechanism for Graph Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8063
    sort_std: 0.007
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.7904
    std: 0.0154
    paper_value: 0.7904
    paper_std: 0.0154
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Brody et al. 2021
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 19
    true_value: 0.798
    true_std: 0.003
    value_gap_source_arxiv: '2405.19121'
    value_gap_source_title: Spatio-Spectral Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.007600000000000051
    value_note: global 0.7980 within std
    paper_rank: 23
    rank_delta: 4
    rank_delta_abs: 4
    rank_delta_direction: worse
    sort_value: 0.798
    sort_std: 0.003
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id005
  dataset: ogbn-proteins
  rows:
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.7863
    std: 0.0162
    paper_value: 0.7863
    paper_std: 0.0162
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hamilton 2017
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 1
    true_value: 0.8501
    true_std: 0.0046
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.06379999999999997
    value_note: ''
    paper_rank: 11
    rank_delta: 10
    rank_delta_abs: 10
    rank_delta_direction: worse
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
  - model: GT + HDSE
    model_key: gt + hdse
    model_plain: GT + HDSE
    value: 0.8034
    std: 0.0032
    metric: ROC-AUC
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
    sort_value: 0.8034
    sort_std: 0.0032
    is_best: false
  - model: GATv2
    model_key: gatv2
    model_plain: GATv2
    value: 0.7952
    std: 0.0055
    paper_value: 0.7952
    paper_std: 0.0055
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Brody 2021
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 8
    true_value: 0.7952
    true_std: 0.0055
    value_gap_source_arxiv: '2508.17630'
    value_gap_source_title: 'Quantum Graph Attention Network: A Novel Quantum Multi-Head
      Attention Mechanism for Graph Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7952
    sort_std: 0.0055
    is_best: false
  - model: QGAT
    model_key: qgat
    model_plain: QGAT
    value: 0.7941
    std: 0.0021
    paper_value: 0.7941
    paper_std: 0.0021
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    global_rank: 9
    true_value: 0.7941
    true_std: 0.0021
    value_gap_source_arxiv: '2508.17630'
    value_gap_source_title: 'Quantum Graph Attention Network: A Novel Quantum Multi-Head
      Attention Mechanism for Graph Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7941
    sort_std: 0.0021
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
  - *id002
- benchmark: OGB
  datasets:
  - *id003
  - *id004
  - *id005
  - *id006
  - *id007
single_proposed_model: QGAT
main_figure: /figures/2508.17630/main_figure.png
---

