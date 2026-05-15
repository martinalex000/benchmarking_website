---
title: 'DARTS-GT: Differentiable Architecture Search for Graph Transformers with Quantifiable
  Instance-Specific Interpretability Analysis'
arxiv_id: '2510.14336'
authors: []
published_date: ''
abstract: 'Graph Transformers (GTs) have emerged as powerful architectures for graph-structured
  data, yet remain constrained by rigid designs and lack quantifiable interpretability
  methods. Current state-of-the-art GTs commit to fixed GNN types across all layers,
  missing potential benefits of depth-specific component selection, while their increasingly
  complex architectures become opaque black boxes where performance gains cannot be
  distinguished between meaningful structural patterns and spurious correlations.
  We redesign the GT attention mechanism through asymmetry, decoupling structural
  encoding from feature representation. Queries derive directly from node features,
  while keys and values come from graph neural network (GNN) transformations, separating
  how the model learns features from how it encodes graph structure. Within this asymmetric
  framework, we use Differentiable ARchiTecture Search (DARTS) to select optimal GNN
  operators at each layer, enabling depth-wise heterogeneity inside the transformer
  attention itself, hence the name DARTS-GT. To understand these discovered architectures,
  we develop the first quantitative interpretability framework for GTs through causal
  ablation that identifies which heads and nodes actually drive predictions. Our metrics:
  Head-deviation, Specialization, and Focus, reveal the specific components responsible
  for each prediction while enabling broader model comparison. Experiments across
  eight benchmarks demonstrate that DARTS-GT achieves state-of-the-art performance
  on four datasets while remaining competitive on others, with discovered architectures
  revealing dataset-specific patterns ranging from highly specialized to balanced
  GNN distributions. Our interpretability analysis reveals that visual attention salience
  and causal importance do not necessarily correlate, indicating that widely used
  visualization approaches may miss the components that actually matter for predictions.
  Crucially, the heterogeneous architectures found by DARTS-GT consistently produced
  more interpretable models than baseline GTs, establishing that Graph Transformers
  do not need to choose between performance and interpretability.'
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: false
proposed_models: []
mrr: null
results: []
results_grouped: []
main_figure: /figures/2510.14336/main_figure.png
---

