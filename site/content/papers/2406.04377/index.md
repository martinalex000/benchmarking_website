---
title: Combining Graph Neural Network and Mamba to Capture Local and Global Tissue
  Spatial Relationships in Whole Slide Images
arxiv_id: '2406.04377'
authors: []
published_date: Jun 2024
abstract: 'In computational pathology, extracting spatial features from gigapixel
  whole slide images (WSIs) is a fundamental task, but due to their large size, WSIs
  are typically segmented into smaller tiles. A critical aspect of this analysis is
  aggregating information from these tiles to make predictions at the WSI level. We
  introduce a model that combines a message-passing graph neural network (GNN) with
  a state space model (Mamba) to capture both local and global spatial relationships
  among the tiles in WSIs. The model''s effectiveness was demonstrated in predicting
  progression-free survival among patients with early-stage lung adenocarcinomas (LUAD).
  We compared the model with other state-of-the-art methods for tile-level information
  aggregation in WSIs, including tile-level information summary statistics-based aggregation,
  multiple instance learning (MIL)-based aggregation, GNN-based aggregation, and GNN-transformer-based
  aggregation. Additional experiments showed the impact of different types of node
  features and different tile sampling strategies on the model performance. This work
  can be easily extended to any WSI-based analysis. Code: https://github.com/rina-ding/gat-mamba.'
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: false
proposed_models: []
mrr: null
results: []
results_grouped: []
main_figure: /figures/2406.04377/main_figure.png
---

