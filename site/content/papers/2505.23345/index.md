---
title: Graph Positional Autoencoders as Self-supervised Learners
arxiv_id: '2505.23345'
source_url: ''
authors: []
published_date: May 2025
published_date_iso: 2025-05
abstract: Graph self-supervised learning seeks to learn effective graph representations
  without relying on labeled data. Among various approaches, graph autoencoders (GAEs)
  have gained significant attention for their efficiency and scalability. Typically,
  GAEs take incomplete graphs as input and predict missing elements, such as masked
  node features or edges. Although effective, our experimental investigation reveals
  that traditional feature or edge masking paradigms primarily capture low-frequency
  signals in the graph and fail to learn expressive structural information. To address
  these issues, we propose Graph Positional Autoencoders (GraphPAE), which employ
  a dual-path architecture to reconstruct both node features and positions. Specifically,
  the feature path uses positional encoding to enhance the message-passing processing,
  improving the GAEs' ability to predict the corrupted information. The position path,
  on the other hand, leverages node representations to refine positions and approximate
  eigenvectors, thereby enabling the encoder to learn diverse frequency information.
  We conduct extensive experiments to verify the effectiveness of GraphPAE, including
  heterophilic node classification, graph property prediction, and transfer learning.
  The results demonstrate that GraphPAE achieves state-of-the-art performance and
  consistently outperforms the baselines by a large margin.
codebase_url: ''
extraction_model: MiniMaxAI/MiniMax-M2.5
has_results: true
paper_type: dataset
proposed_models: []
mrr: null
adjusted_mrr: null
mrr_dataset_count: 0
benchmark_categories:
- Classic
- Heterophilic Graphs
- OGB
- MoleculeNet
- LINKX Benchmarks
- Quantum Chemistry
task_categories:
- graph_classification
- graph_regression
- node_classification
experiment_scopes:
- graph-level
- node-level
results:
- &id004
  dataset: Actor
  rows:
  - model: GrokFormer
    model_key: grokformer
    model_plain: GrokFormer
    value: 0.4298
    std: 0.0148
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
    sort_value: 0.4298
    sort_std: 0.0148
    is_best: true
  - model: GrokFilter
    model_key: grokfilter
    model_plain: GrokFilter
    value: 0.4215
    std: 0.0129
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
    sort_value: 0.4215
    sort_std: 0.0129
    is_best: true
  - model: SpecFormer
    model_key: specformer
    model_plain: SpecFormer
    value: 0.4193
    std: 0.0104
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
    sort_value: 0.4193
    sort_std: 0.0104
    is_best: true
  - model: GraphMAE
    model_key: graphmae
    model_plain: GraphMAE
    value: 0.3855
    std: 0.0135
    paper_value: 0.3855
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
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 14
    true_value: 0.3855
    true_std: 0.0135
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3855
    sort_std: 0.0135
    is_best: false
  - model: Sp^2GCL
    model_key: sp$^2$gcl
    model_plain: Sp^2GCL
    value: 0.347
    std: 0.0092
    paper_value: 0.347
    paper_std: 0.0092
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 49
    true_value: 0.347
    true_std: 0.0092
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 49
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.347
    sort_std: 0.0092
    is_best: false
  - model: MVGRL
    model_key: mvgrl
    model_plain: MVGRL
    value: 0.3464
    std: 0.002
    paper_value: 0.3464
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
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 50
    true_value: 0.3464
    true_std: 0.002
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 50
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3464
    sort_std: 0.002
    is_best: false
  - model: Supervised
    model_key: supervised
    model_plain: Supervised
    value: 0.3393
    std: 0.0247
    paper_value: 0.3393
    paper_std: 0.0247
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 60
    true_value: 0.3393
    true_std: 0.0247
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 60
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3393
    sort_std: 0.0247
    is_best: false
  - model: MaskGAE
    model_key: maskgae
    model_plain: MaskGAE
    value: 0.3344
    std: 0.0034
    paper_value: 0.3344
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
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 64
    true_value: 0.3344
    true_std: 0.0034
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 64
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3344
    sort_std: 0.0034
    is_best: false
  - model: AUG-MAE
    model_key: aug-mae
    model_plain: AUG-MAE
    value: 0.3342
    std: 0.0038
    paper_value: 0.3342
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
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 65
    true_value: 0.3342
    true_std: 0.0038
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 65
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3342
    sort_std: 0.0038
    is_best: false
  - model: VGAER
    model_key: vgaer
    model_plain: VGAER
    value: 0.3157
    std: 0.0075
    paper_value: 0.3157
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
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 73
    true_value: 0.3157
    true_std: 0.0075
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 73
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3157
    sort_std: 0.0075
    is_best: false
  - model: DGI
    model_key: dgi
    model_plain: DGI
    value: 0.2798
    std: 0.0009
    paper_value: 0.2798
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
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 84
    true_value: 0.2798
    true_std: 0.0009
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 84
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2798
    sort_std: 0.0009
    is_best: false
  - model: CCA-SSG
    model_key: cca-ssg
    model_plain: CCA-SSG
    value: 0.2779
    std: 0.0058
    paper_value: 0.2779
    paper_std: 0.0058
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 85
    true_value: 0.2779
    true_std: 0.0058
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 85
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2779
    sort_std: 0.0058
    is_best: false
  - model: BGRL
    model_key: bgrl
    model_plain: BGRL
    value: 0.2661
    std: 0.0057
    paper_value: 0.2661
    paper_std: 0.0057
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 87
    true_value: 0.2661
    true_std: 0.0057
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 87
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2661
    sort_std: 0.0057
    is_best: false
  - model: S2GAE
    model_key: s2gae
    model_plain: S2GAE
    value: 0.2617
    std: 0.0038
    paper_value: 0.2617
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
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 88
    true_value: 0.2617
    true_std: 0.0038
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 88
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2617
    sort_std: 0.0038
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id006
  dataset: BACE
  rows:
  - model: MPNN + HOPE-WavePE
    model_key: mpnn + hope-wavepe
    model_plain: MPNN + HOPE-WavePE
    value: 0.868
    std: 0.004
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
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
    global_rank: 1
    sort_value: 0.868
    sort_std: 0.004
    is_best: true
  - model: BiScale-GTR (Molecule)
    model_key: biscale-gtr (molecule)
    model_plain: BiScale-GTR (Molecule)
    value: 0.85
    std: 0.011
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.06336'
    title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale Molecular
      Representation Learning'
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    codebase_url: ''
    uses_external_data: true
    is_global_top: true
    global_rank: 2
    sort_value: 0.85
    sort_std: 0.011
    is_best: false
  - model: Subgraphormer
    model_key: subgraphormer
    model_plain: Subgraphormer
    value: 0.8435
    std: 0.0065
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.293
    arxiv_id: '2402.08450'
    title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via Graph
      Products'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.8435
    sort_std: 0.0065
    is_best: false
  - model: GraphMAE
    model_key: graphmae
    model_plain: GraphMAE
    value: 0.8111
    std: 0.0124
    paper_value: 0.8111
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
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 7
    true_value: 0.831
    true_std: 0.009
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.019899999999999918
    value_note: ''
    paper_rank: 14
    rank_delta: 7
    rank_delta_abs: 7
    rank_delta_direction: worse
    sort_value: 0.831
    sort_std: 0.009
    is_best: false
  - model: Supervised
    model_key: supervised
    model_plain: Supervised
    value: 0.8042
    std: 0.0096
    paper_value: 0.8042
    paper_std: 0.0096
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 22
    true_value: 0.8042
    true_std: 0.0096
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8042
    sort_std: 0.0096
    is_best: false
  - model: Sp^2GCL
    model_key: sp$^2$gcl
    model_plain: Sp^2GCL
    value: 0.7876
    std: 0.0143
    paper_value: 0.7876
    paper_std: 0.0143
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 36
    true_value: 0.7876
    true_std: 0.0143
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 36
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7876
    sort_std: 0.0143
    is_best: false
  - model: AUG-MAE
    model_key: aug-mae
    model_plain: AUG-MAE
    value: 0.7854
    std: 0.0249
    paper_value: 0.7854
    paper_std: 0.0249
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 38
    true_value: 0.7854
    true_std: 0.0249
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7854
    sort_std: 0.0249
    is_best: false
  - model: StructMAE
    model_key: structmae
    model_plain: StructMAE
    value: 0.7775
    std: 0.0042
    paper_value: 0.7775
    paper_std: 0.0042
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 47
    true_value: 0.7775
    true_std: 0.0042
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 47
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7775
    sort_std: 0.0042
    is_best: false
  - model: JOAO
    model_key: joao
    model_plain: JOAO
    value: 0.7443
    std: 0.0194
    paper_value: 0.7443
    paper_std: 0.0194
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 48
    true_value: 0.773
    true_std: 0.005
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.02870000000000006
    value_note: ''
    paper_rank: 55
    rank_delta: 7
    rank_delta_abs: 7
    rank_delta_direction: worse
    sort_value: 0.773
    sort_std: 0.005
    is_best: false
  - model: GraphCL
    model_key: graphcl
    model_plain: GraphCL
    value: 0.7332
    std: 0.027
    paper_value: 0.7332
    paper_std: 0.027
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 53
    true_value: 0.754
    true_std: 0.014
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.02080000000000004
    value_note: global 0.7540 within std
    paper_rank: 57
    rank_delta: 4
    rank_delta_abs: 4
    rank_delta_direction: worse
    sort_value: 0.754
    sort_std: 0.014
    is_best: false
  - model: MVGRL
    model_key: mvgrl
    model_plain: MVGRL
    value: 0.7488
    std: 0.0143
    paper_value: 0.7488
    paper_std: 0.0143
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 55
    true_value: 0.7488
    true_std: 0.0143
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 55
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7488
    sort_std: 0.0143
    is_best: false
  - model: InfoGraph
    model_key: infograph
    model_plain: InfoGraph
    value: 0.7364
    std: 0.0364
    paper_value: 0.7364
    paper_std: 0.0364
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 57
    true_value: 0.7364
    true_std: 0.0364
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 57
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7364
    sort_std: 0.0364
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id007
  dataset: BBBP
  rows:
  - model: BiScale-GTR (Fragment)
    model_key: biscale-gtr (fragment)
    model_plain: BiScale-GTR (Fragment)
    value: 0.738
    std: 0.004
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.06336'
    title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale Molecular
      Representation Learning'
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    codebase_url: ''
    uses_external_data: true
    is_global_top: true
    global_rank: 1
    sort_value: 0.738
    sort_std: 0.004
    is_best: true
  - model: GraphGPS+LAC
    model_key: graphgps+lac
    model_plain: GraphGPS+LAC
    value: 0.736
    std: null
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.06336'
    title: 'BiScale-GTR: Fragment-Aware Graph Transformers for Multi-Scale Molecular
      Representation Learning'
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 2
    sort_value: 0.736
    sort_std: null
    is_best: true
  - model: GraphLoG
    model_key: graphlog
    model_plain: GraphLoG
    value: 0.725
    std: 0.008
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    codebase_url: ''
    uses_external_data: true
    is_global_top: true
    global_rank: 3
    sort_value: 0.725
    sort_std: 0.008
    is_best: false
  - model: GraphMAE
    model_key: graphmae
    model_plain: GraphMAE
    value: 0.6856
    std: 0.0071
    paper_value: 0.6856
    paper_std: 0.0071
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 6
    true_value: 0.72
    true_std: 0.006
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.034399999999999986
    value_note: ''
    paper_rank: 31
    rank_delta: 25
    rank_delta_abs: 25
    rank_delta_direction: worse
    sort_value: 0.72
    sort_std: 0.006
    is_best: false
  - model: JOAO
    model_key: joao
    model_plain: JOAO
    value: 0.6762
    std: 0.0129
    paper_value: 0.6762
    paper_std: 0.0129
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 19
    true_value: 0.702
    true_std: 0.01
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.025799999999999934
    value_note: ''
    paper_rank: 35
    rank_delta: 16
    rank_delta_abs: 16
    rank_delta_direction: worse
    sort_value: 0.702
    sort_std: 0.01
    is_best: false
  - model: GraphCL
    model_key: graphcl
    model_plain: GraphCL
    value: 0.6822
    std: 0.0219
    paper_value: 0.6822
    paper_std: 0.0219
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 23
    true_value: 0.697
    true_std: 0.007
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.014799999999999924
    value_note: global 0.6970 within std
    paper_rank: 32
    rank_delta: 9
    rank_delta_abs: 9
    rank_delta_direction: worse
    sort_value: 0.697
    sort_std: 0.007
    is_best: false
  - model: Sp^2GCL
    model_key: sp$^2$gcl
    model_plain: Sp^2GCL
    value: 0.6872
    std: 0.0153
    paper_value: 0.6872
    paper_std: 0.0153
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 30
    true_value: 0.6872
    true_std: 0.0153
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 30
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6872
    sort_std: 0.0153
    is_best: false
  - model: Supervised
    model_key: supervised
    model_plain: Supervised
    value: 0.6817
    std: 0.0148
    paper_value: 0.6817
    paper_std: 0.0148
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 33
    true_value: 0.6817
    true_std: 0.0148
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6817
    sort_std: 0.0148
    is_best: false
  - model: MVGRL
    model_key: mvgrl
    model_plain: MVGRL
    value: 0.6724
    std: 0.0319
    paper_value: 0.6724
    paper_std: 0.0319
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 38
    true_value: 0.6724
    true_std: 0.0319
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6724
    sort_std: 0.0319
    is_best: false
  - model: AUG-MAE
    model_key: aug-mae
    model_plain: AUG-MAE
    value: 0.6705
    std: 0.0063
    paper_value: 0.6705
    paper_std: 0.0063
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 40
    true_value: 0.6705
    true_std: 0.0063
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 40
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6705
    sort_std: 0.0063
    is_best: false
  - model: InfoGraph
    model_key: infograph
    model_plain: InfoGraph
    value: 0.6633
    std: 0.0279
    paper_value: 0.6633
    paper_std: 0.0279
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 44
    true_value: 0.6633
    true_std: 0.0279
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 44
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6633
    sort_std: 0.0279
    is_best: false
  - model: StructMAE
    model_key: structmae
    model_plain: StructMAE
    value: 0.6566
    std: 0.0116
    paper_value: 0.6566
    paper_std: 0.0116
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 48
    true_value: 0.6566
    true_std: 0.0116
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 48
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6566
    sort_std: 0.0116
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id002
  dataset: Chameleon
  rows:
  - model: GraphMAE
    model_key: graphmae
    model_plain: GraphMAE
    value: 0.8051
    std: 0.0125
    paper_value: 0.8051
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
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 1
    true_value: 0.8051
    true_std: 0.0125
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
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
    paper_value: 0.8002
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
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 3
    true_value: 0.8002
    true_std: 0.0087
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8002
    sort_std: 0.0087
    is_best: true
  - model: Dir-GNN
    model_key: dir-gnn
    model_plain: Dir-GNN
    value: 0.7971
    std: 0.0126
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
    sort_value: 0.7971
    sort_std: 0.0126
    is_best: true
  - model: CoCN expanded
    model_key: cocn expanded
    model_plain: CoCN expanded
    value: 0.7935
    std: 0.0142
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
    global_rank: 5
    sort_value: 0.7935
    sort_std: 0.0142
    is_best: true
  - model: Sp^2GCL
    model_key: sp$^2$gcl
    model_plain: Sp^2GCL
    value: 0.7888
    std: 0.0104
    paper_value: 0.7888
    paper_std: 0.0104
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 7
    true_value: 0.7888
    true_std: 0.0104
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7888
    sort_std: 0.0104
    is_best: true
  - model: CCA-SSG
    model_key: cca-ssg
    model_plain: CCA-SSG
    value: 0.75
    std: 0.0075
    paper_value: 0.75
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
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 13
    true_value: 0.75
    true_std: 0.0075
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.75
    sort_std: 0.0075
    is_best: false
  - model: MaskGAE
    model_key: maskgae
    model_plain: MaskGAE
    value: 0.745
    std: 0.0087
    paper_value: 0.745
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
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 16
    true_value: 0.745
    true_std: 0.0087
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.745
    sort_std: 0.0087
    is_best: false
  - model: MVGRL
    model_key: mvgrl
    model_plain: MVGRL
    value: 0.7319
    std: 0.0042
    paper_value: 0.7319
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
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 19
    true_value: 0.7319
    true_std: 0.0042
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7319
    sort_std: 0.0042
    is_best: false
  - model: AUG-MAE
    model_key: aug-mae
    model_plain: AUG-MAE
    value: 0.701
    std: 0.0188
    paper_value: 0.701
    paper_std: 0.0188
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 26
    true_value: 0.701
    true_std: 0.0188
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.701
    sort_std: 0.0188
    is_best: false
  - model: VGAER
    model_key: vgaer
    model_plain: VGAER
    value: 0.6232
    std: 0.019
    paper_value: 0.6232
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
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 59
    true_value: 0.6232
    true_std: 0.019
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 59
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6232
    sort_std: 0.019
    is_best: false
  - model: BGRL
    model_key: bgrl
    model_plain: BGRL
    value: 0.6124
    std: 0.0107
    paper_value: 0.6124
    paper_std: 0.0107
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 63
    true_value: 0.6124
    true_std: 0.0107
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 63
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6124
    sort_std: 0.0107
    is_best: false
  - model: S2GAE
    model_key: s2gae
    model_plain: S2GAE
    value: 0.6024
    std: 0.0037
    paper_value: 0.6024
    paper_std: 0.0037
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 69
    true_value: 0.6024
    true_std: 0.0037
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 69
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6024
    sort_std: 0.0037
    is_best: false
  - model: DGI
    model_key: dgi
    model_plain: DGI
    value: 0.4383
    std: 0.0014
    paper_value: 0.4383
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
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 118
    true_value: 0.4383
    true_std: 0.0014
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 118
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4383
    sort_std: 0.0014
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id008
  dataset: ClinTox
  rows:
  - model: Supervised
    model_key: supervised
    model_plain: Supervised
    value: 0.8814
    std: 0.0251
    paper_value: 0.8814
    paper_std: 0.0251
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 1
    true_value: 0.8814
    true_std: 0.0251
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8814
    sort_std: 0.0251
    is_best: true
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.859
    std: 0.04
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.10651'
    title: Graph Learning via Logic-Based Weisfeiler--Leman Variants and Tabularization
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.859
    sort_std: 0.04
    is_best: true
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.859
    std: 0.04
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.10651'
    title: Graph Learning via Logic-Based Weisfeiler--Leman Variants and Tabularization
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.859
    sort_std: 0.04
    is_best: true
  - model: GraphFP_CP
    model_key: graphfp_cp
    model_plain: GraphFP_CP
    value: 0.847
    std: 0.058
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.03274'
    title: Fragment-based Pretraining and Finetuning on Molecular Graphs
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: true
    is_global_top: true
    global_rank: 4
    sort_value: 0.847
    sort_std: 0.058
    is_best: true
  - model: GraphMAE
    model_key: graphmae
    model_plain: GraphMAE
    value: 0.8269
    std: 0.0339
    paper_value: 0.8269
    paper_std: 0.0339
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 6
    true_value: 0.8269
    true_std: 0.0339
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8269
    sort_std: 0.0339
    is_best: true
  - model: AUG-MAE
    model_key: aug-mae
    model_plain: AUG-MAE
    value: 0.8266
    std: 0.0198
    paper_value: 0.8266
    paper_std: 0.0198
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 7
    true_value: 0.8266
    true_std: 0.0198
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8266
    sort_std: 0.0198
    is_best: false
  - model: JOAO
    model_key: joao
    model_plain: JOAO
    value: 0.7128
    std: 0.0412
    paper_value: 0.7128
    paper_std: 0.0412
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 8
    true_value: 0.813
    true_std: 0.025
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10019999999999996
    value_note: ''
    paper_rank: 31
    rank_delta: 23
    rank_delta_abs: 23
    rank_delta_direction: worse
    sort_value: 0.813
    sort_std: 0.025
    is_best: false
  - model: Sp^2GCL
    model_key: sp$^2$gcl
    model_plain: Sp^2GCL
    value: 0.8088
    std: 0.0386
    paper_value: 0.8088
    paper_std: 0.0386
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 10
    true_value: 0.8088
    true_std: 0.0386
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8088
    sort_std: 0.0386
    is_best: false
  - model: StructMAE
    model_key: structmae
    model_plain: StructMAE
    value: 0.7942
    std: 0.0456
    paper_value: 0.7942
    paper_std: 0.0456
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 11
    true_value: 0.7942
    true_std: 0.0456
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7942
    sort_std: 0.0456
    is_best: false
  - model: GraphCL
    model_key: graphcl
    model_plain: GraphCL
    value: 0.7492
    std: 0.0442
    paper_value: 0.7492
    paper_std: 0.0442
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 20
    true_value: 0.76
    true_std: 0.027
    value_gap_source_arxiv: '2310.03274'
    value_gap_source_title: Fragment-based Pretraining and Finetuning on Molecular
      Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.010800000000000032
    value_note: global 0.7600 within std
    paper_rank: 23
    rank_delta: 3
    rank_delta_abs: 3
    rank_delta_direction: worse
    sort_value: 0.76
    sort_std: 0.027
    is_best: false
  - model: MVGRL
    model_key: mvgrl
    model_plain: MVGRL
    value: 0.7384
    std: 0.0275
    paper_value: 0.7384
    paper_std: 0.0275
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 25
    true_value: 0.7384
    true_std: 0.0275
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7384
    sort_std: 0.0275
    is_best: false
  - model: InfoGraph
    model_key: infograph
    model_plain: InfoGraph
    value: 0.645
    std: 0.0532
    paper_value: 0.645
    paper_std: 0.0532
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 46
    true_value: 0.645
    true_std: 0.0532
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 46
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.645
    sort_std: 0.0532
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id009
  dataset: ESOL
  rows:
  - model: Subgraphormer
    model_key: subgraphormer
    model_plain: Subgraphormer
    value: 0.826
    std: 0.01
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.293
    arxiv_id: '2402.08450'
    title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via Graph
      Products'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.826
    sort_std: 0.01
    is_best: true
  - model: GNN-SSWL+
    model_key: gnn-sswl+
    model_plain: GNN-SSWL+
    value: 0.837
    std: 0.019
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.387
    arxiv_id: '2402.08450'
    title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via Graph
      Products'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.837
    sort_std: 0.019
    is_best: true
  - model: DSS-GNN
    model_key: dss-gnn
    model_plain: DSS-GNN
    value: 0.847
    std: 0.015
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.1
    arxiv_id: '2402.08450'
    title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via Graph
      Products'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.847
    sort_std: 0.015
    is_best: true
  - model: GraphMAE
    model_key: graphmae
    model_plain: GraphMAE
    value: 2.058
    std: 0.188
    paper_value: 2.058
    paper_std: 0.188
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 8
    true_value: 2.058
    true_std: 0.188
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 2.058
    sort_std: 0.188
    is_best: false
  - model: AUG-MAE
    model_key: aug-mae
    model_plain: AUG-MAE
    value: 2.395
    std: 0.158
    paper_value: 2.395
    paper_std: 0.158
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 9
    true_value: 2.395
    true_std: 0.158
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 2.395
    sort_std: 0.158
    is_best: false
  - model: StructMAE
    model_key: structmae
    model_plain: StructMAE
    value: 2.568
    std: 0.262
    paper_value: 2.568
    paper_std: 0.262
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 10
    true_value: 2.568
    true_std: 0.262
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 2.568
    sort_std: 0.262
    is_best: false
  - model: Supervised
    model_key: supervised
    model_plain: Supervised
    value: 2.755
    std: 0.349
    paper_value: 2.755
    paper_std: 0.349
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 11
    true_value: 2.755
    true_std: 0.349
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 2.755
    sort_std: 0.349
    is_best: false
  - model: Sp^2GCL
    model_key: sp$^2$gcl
    model_plain: Sp^2GCL
    value: 4.144
    std: 0.573
    paper_value: 4.144
    paper_std: 0.573
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 12
    true_value: 4.144
    true_std: 0.573
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 4.144
    sort_std: 0.573
    is_best: false
  - model: JOAO
    model_key: joao
    model_plain: JOAO
    value: 5.131
    std: 0.782
    paper_value: 5.131
    paper_std: 0.782
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 13
    true_value: 5.131
    true_std: 0.782
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 5.131
    sort_std: 0.782
    is_best: false
  - model: GraphCL
    model_key: graphcl
    model_plain: GraphCL
    value: 7.679
    std: 2.748
    paper_value: 7.679
    paper_std: 2.748
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 14
    true_value: 7.679
    true_std: 2.748
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 7.679
    sort_std: 2.748
    is_best: false
  - model: MVGRL
    model_key: mvgrl
    model_plain: MVGRL
    value: 9.024
    std: 1.982
    paper_value: 9.024
    paper_std: 1.982
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 15
    true_value: 9.024
    true_std: 1.982
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 9.024
    sort_std: 1.982
    is_best: false
  - model: InfoGraph
    model_key: infograph
    model_plain: InfoGraph
    value: 10.005
    std: 8.147
    paper_value: 10.005
    paper_std: 8.147
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 16
    true_value: 10.005
    true_std: 8.147
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 10.005
    sort_std: 8.147
    is_best: false
  metric: RMSE
  higher_is_better: false
- &id011
  dataset: Penn94
  rows:
  - model: CSNN
    model_key: csnn
    model_plain: CSNN
    value: 0.86
    std: 0.0039000000000000003
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
    global_rank: 1
    sort_value: 0.86
    sort_std: 0.0039000000000000003
    is_best: true
  - model: GLoGNN
    model_key: glognn
    model_plain: GLoGNN
    value: 0.8556999999999999
    std: 0.0034999999999999996
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
    global_rank: 2
    sort_value: 0.8556999999999999
    sort_std: 0.0034999999999999996
    is_best: true
  - model: LINKX
    model_key: linkx
    model_plain: LINKX
    value: 0.8471
    std: 0.0052
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
    global_rank: 3
    sort_value: 0.8471
    sort_std: 0.0052
    is_best: false
  - model: Supervised
    model_key: supervised
    model_plain: Supervised
    value: 0.8153
    std: 0.0055
    paper_value: 0.8153
    paper_std: 0.0055
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 9
    true_value: 0.8153
    true_std: 0.0055
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8153
    sort_std: 0.0055
    is_best: false
  - model: GraphMAE
    model_key: graphmae
    model_plain: GraphMAE
    value: 0.7179
    std: 0.0037
    paper_value: 0.7179
    paper_std: 0.0037
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 14
    true_value: 0.7179
    true_std: 0.0037
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7179
    sort_std: 0.0037
    is_best: false
  - model: S2GAE
    model_key: s2gae
    model_plain: S2GAE
    value: 0.7024
    std: 0.0009
    paper_value: 0.7024
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
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 15
    true_value: 0.7024
    true_std: 0.0009
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7024
    sort_std: 0.0009
    is_best: false
  - model: AUG-MAE
    model_key: aug-mae
    model_plain: AUG-MAE
    value: 0.699
    std: 0.0043
    paper_value: 0.699
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
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 16
    true_value: 0.699
    true_std: 0.0043
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.699
    sort_std: 0.0043
    is_best: false
  - model: Sp^2GCL
    model_key: sp$^2$gcl
    model_plain: Sp^2GCL
    value: 0.688
    std: 0.0045
    paper_value: 0.688
    paper_std: 0.0045
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 17
    true_value: 0.688
    true_std: 0.0045
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.688
    sort_std: 0.0045
    is_best: false
  - model: MaskGAE
    model_key: maskgae
    model_plain: MaskGAE
    value: 0.6384
    std: 0.0003
    paper_value: 0.6384
    paper_std: 0.0003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 18
    true_value: 0.6384
    true_std: 0.0003
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6384
    sort_std: 0.0003
    is_best: false
  - model: BGRL
    model_key: bgrl
    model_plain: BGRL
    value: 0.6331
    std: 0.0049
    paper_value: 0.6331
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
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 19
    true_value: 0.6331
    true_std: 0.0049
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6331
    sort_std: 0.0049
    is_best: false
  - model: CCA-SSG
    model_key: cca-ssg
    model_plain: CCA-SSG
    value: 0.6263
    std: 0.002
    paper_value: 0.6263
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
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 20
    true_value: 0.6263
    true_std: 0.002
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6263
    sort_std: 0.002
    is_best: false
  - model: VGAER
    model_key: vgaer
    model_plain: VGAER
    value: 0.5531
    std: 0.0028
    paper_value: 0.5531
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
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 21
    true_value: 0.5531
    true_std: 0.0028
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5531
    sort_std: 0.0028
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id012
  dataset: QM9
  rows:
  - model: Mace
    model_key: mace
    model_plain: Mace
    value: 0.02
    std: null
    metric: MAE
    higher_is_better: false
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
    sort_value: 0.02
    sort_std: null
    is_best: true
  - model: PST
    model_key: pst
    model_plain: PST
    value: 0.023
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
    global_rank: 2
    sort_value: 0.023
    sort_std: 0.001
    is_best: false
  - model: DropGIN
    model_key: dropgin
    model_plain: DropGIN
    value: 0.02578744427174226
    std: 0.000867405321348238
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
    global_rank: 3
    sort_value: 0.02578744427174226
    sort_std: 0.000867405321348238
    is_best: false
  - model: GraphMAE
    model_key: graphmae
    model_plain: GraphMAE
    value: 0.703
    std: null
    paper_value: 0.703
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 48
    true_value: 0.703
    true_std: null
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 48
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.703
    sort_std: null
    is_best: false
  - model: Mole-BERT
    model_key: mole-bert
    model_plain: Mole-BERT
    value: 1.031
    std: null
    paper_value: 1.031
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 53
    true_value: 1.031
    true_std: null
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 53
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.031
    sort_std: null
    is_best: false
  - model: GraphCL
    model_key: graphcl
    model_plain: GraphCL
    value: 1.035
    std: null
    paper_value: 1.035
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 54
    true_value: 1.035
    true_std: null
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 54
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.035
    sort_std: null
    is_best: false
  - model: SimSGT
    model_key: simsgt
    model_plain: SimSGT
    value: 1.064
    std: null
    paper_value: 1.064
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 55
    true_value: 1.064
    true_std: null
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 55
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.064
    sort_std: null
    is_best: false
  metric: MAE
  higher_is_better: false
- &id003
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
  - model: GraphMAE
    model_key: graphmae
    model_plain: GraphMAE
    value: 0.7205
    std: 0.014
    paper_value: 0.7205
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
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 6
    true_value: 0.7205
    true_std: 0.014
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7205
    sort_std: 0.014
    is_best: false
  - model: Supervised
    model_key: supervised
    model_plain: Supervised
    value: 0.7191
    std: 0.0103
    paper_value: 0.7191
    paper_std: 0.0103
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 7
    true_value: 0.7191
    true_std: 0.0103
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7191
    sort_std: 0.0103
    is_best: false
  - model: S2GAE
    model_key: s2gae
    model_plain: S2GAE
    value: 0.686
    std: 0.0056
    paper_value: 0.686
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
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 9
    true_value: 0.686
    true_std: 0.0056
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.686
    sort_std: 0.0056
    is_best: false
  - model: MaskGAE
    model_key: maskgae
    model_plain: MaskGAE
    value: 0.6853
    std: 0.0044
    paper_value: 0.6853
    paper_std: 0.0044
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 11
    true_value: 0.6853
    true_std: 0.0044
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6853
    sort_std: 0.0044
    is_best: false
  - model: Sp^2GCL
    model_key: sp$^2$gcl
    model_plain: Sp^2GCL
    value: 0.6261
    std: 0.0087
    paper_value: 0.6261
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
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 18
    true_value: 0.6261
    true_std: 0.0087
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6261
    sort_std: 0.0087
    is_best: false
  - model: AUG-MAE
    model_key: aug-mae
    model_plain: AUG-MAE
    value: 0.6257
    std: 0.0067
    paper_value: 0.6257
    paper_std: 0.0067
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 19
    true_value: 0.6257
    true_std: 0.0067
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6257
    sort_std: 0.0067
    is_best: false
  - model: CCA-SSG
    model_key: cca-ssg
    model_plain: CCA-SSG
    value: 0.6158
    std: 0.0198
    paper_value: 0.6158
    paper_std: 0.0198
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 22
    true_value: 0.6158
    true_std: 0.0198
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6158
    sort_std: 0.0198
    is_best: false
  - model: MVGRL
    model_key: mvgrl
    model_plain: MVGRL
    value: 0.6009
    std: 0.0044
    paper_value: 0.6009
    paper_std: 0.0044
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 24
    true_value: 0.6009
    true_std: 0.0044
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6009
    sort_std: 0.0044
    is_best: false
  - model: BGRL
    model_key: bgrl
    model_plain: BGRL
    value: 0.4324
    std: 0.0052
    paper_value: 0.4324
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
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 58
    true_value: 0.4324
    true_std: 0.0052
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 58
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4324
    sort_std: 0.0052
    is_best: false
  - model: VGAER
    model_key: vgaer
    model_plain: VGAER
    value: 0.425
    std: 0.0135
    paper_value: 0.425
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
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 64
    true_value: 0.425
    true_std: 0.0135
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 64
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.425
    sort_std: 0.0135
    is_best: false
  - model: DGI
    model_key: dgi
    model_plain: DGI
    value: 0.3456
    std: 0.001
    paper_value: 0.3456
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
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 104
    true_value: 0.3456
    true_std: 0.001
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 104
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3456
    sort_std: 0.001
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id001
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
  - model: GraphMAE
    model_key: graphmae
    model_plain: GraphMAE
    value: 0.7932
    std: 0.0029
    paper_value: 0.7932
    paper_std: 0.0029
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:additional_exp}"
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 37
    true_value: 0.7932
    true_std: 0.0029
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 37
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7932
    sort_std: 0.0029
    is_best: false
  - model: BGRL
    model_key: bgrl
    model_plain: BGRL
    value: 0.7902
    std: 0.0013
    paper_value: 0.7902
    paper_std: 0.0013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:additional_exp}"
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 40
    true_value: 0.7902
    true_std: 0.0013
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 40
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7902
    sort_std: 0.0013
    is_best: false
  - model: CCA-SSG
    model_key: cca-ssg
    model_plain: CCA-SSG
    value: 0.7885
    std: 0.0032
    paper_value: 0.7885
    paper_std: 0.0032
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:additional_exp}"
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 43
    true_value: 0.7885
    true_std: 0.0032
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 43
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7885
    sort_std: 0.0032
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id010
  dataset: arxiv-year
  rows:
  - model: MRS-Dir-GCN_DA
    model_key: mrs-dir-gcn_da
    model_plain: MRS-Dir-GCN_DA
    value: 0.6603
    std: 0.002
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
    global_rank: 1
    sort_value: 0.6603
    sort_std: 0.002
    is_best: true
  - model: S² DirGCN
    model_key: s² dirgcn
    model_plain: S² DirGCN
    value: 0.6495
    std: 0.0033
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.19121'
    title: Spatio-Spectral Graph Neural Networks
    date: May 29, 2024
    date_display: May 2024
    date_iso: '2024-05-29'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.6495
    sort_std: 0.0033
    is_best: false
  - model: FaberNet
    model_key: fabernet
    model_plain: FaberNet
    value: 0.6462
    std: 0.0101
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.19121'
    title: Spatio-Spectral Graph Neural Networks
    date: May 29, 2024
    date_display: May 2024
    date_iso: '2024-05-29'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.6462
    sort_std: 0.0101
    is_best: false
  - model: Supervised
    model_key: supervised
    model_plain: Supervised
    value: 0.4602
    std: 0.0026
    paper_value: 0.4602
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
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 21
    true_value: 0.4602
    true_std: 0.0026
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4602
    sort_std: 0.0026
    is_best: false
  - model: GraphMAE
    model_key: graphmae
    model_plain: GraphMAE
    value: 0.4185
    std: 0.0004
    paper_value: 0.4185
    paper_std: 0.0004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 25
    true_value: 0.4185
    true_std: 0.0004
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4185
    sort_std: 0.0004
    is_best: false
  - model: BGRL
    model_key: bgrl
    model_plain: BGRL
    value: 0.4143
    std: 0.0004
    paper_value: 0.4143
    paper_std: 0.0004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 26
    true_value: 0.4143
    true_std: 0.0004
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4143
    sort_std: 0.0004
    is_best: false
  - model: CCA-SSG
    model_key: cca-ssg
    model_plain: CCA-SSG
    value: 0.4078
    std: 0.0001
    paper_value: 0.4078
    paper_std: 0.0001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 27
    true_value: 0.4078
    true_std: 0.0001
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 27
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4078
    sort_std: 0.0001
    is_best: false
  - model: MaskGAE
    model_key: maskgae
    model_plain: MaskGAE
    value: 0.4059
    std: 0.0004
    paper_value: 0.4059
    paper_std: 0.0004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 28
    true_value: 0.4059
    true_std: 0.0004
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 28
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4059
    sort_std: 0.0004
    is_best: false
  - model: S2GAE
    model_key: s2gae
    model_plain: S2GAE
    value: 0.4032
    std: 0.0012
    paper_value: 0.4032
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
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 29
    true_value: 0.4032
    true_std: 0.0012
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4032
    sort_std: 0.0012
    is_best: false
  - model: Sp^2GCL
    model_key: sp$^2$gcl
    model_plain: Sp^2GCL
    value: 0.3909
    std: 0.0002
    paper_value: 0.3909
    paper_std: 0.0002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 30
    true_value: 0.3909
    true_std: 0.0002
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 30
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3909
    sort_std: 0.0002
    is_best: false
  - model: AUG-MAE
    model_key: aug-mae
    model_plain: AUG-MAE
    value: 0.371
    std: 0.0013
    paper_value: 0.371
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
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 33
    true_value: 0.371
    true_std: 0.0013
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.371
    sort_std: 0.0013
    is_best: false
  - model: VGAER
    model_key: vgaer
    model_plain: VGAER
    value: 0.3639
    std: 0.0021
    paper_value: 0.3639
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
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 35
    true_value: 0.3639
    true_std: 0.0021
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3639
    sort_std: 0.0021
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
  - model: GraphMAE
    model_key: graphmae
    model_plain: GraphMAE
    value: 0.791
    std: 0.0002
    paper_value: 0.791
    paper_std: 0.0002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 22
    true_value: 0.791
    true_std: 0.0002
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.791
    sort_std: 0.0002
    is_best: false
  - model: BGRL
    model_key: bgrl
    model_plain: BGRL
    value: 0.7859
    std: 0.0002
    paper_value: 0.7859
    paper_std: 0.0002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 26
    true_value: 0.7859
    true_std: 0.0002
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7859
    sort_std: 0.0002
    is_best: false
  - model: CCA-SSG
    model_key: cca-ssg
    model_plain: CCA-SSG
    value: 0.7527
    std: 0.0005
    paper_value: 0.7527
    paper_std: 0.0005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 38
    true_value: 0.7527
    true_std: 0.0005
    value_gap_source_arxiv: '2505.23345'
    value_gap_source_title: Graph Positional Autoencoders as Self-supervised Learners
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7527
    sort_std: 0.0005
    is_best: false
  metric: Accuracy
  higher_is_better: true
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
- benchmark: Heterophilic Graphs
  datasets:
  - *id002
  - *id003
  - *id004
- benchmark: OGB
  datasets:
  - *id005
- benchmark: MoleculeNet
  datasets:
  - *id006
  - *id007
  - *id008
  - *id009
- benchmark: LINKX Benchmarks
  datasets:
  - *id010
  - *id011
- benchmark: Quantum Chemistry
  datasets:
  - *id012
main_figure: /figures/2505.23345/main_figure.png
---

