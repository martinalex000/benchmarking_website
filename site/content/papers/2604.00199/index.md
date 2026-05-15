---
title: 'QUEST: A robust attention formulation using Query-modulated spherical attention'
arxiv_id: '2604.00199'
authors: []
published_date: ''
abstract: Abstract The Transformer model architecture has become one of the most widely
  used in deep learning and the attention mechanism is at its core. The standard attention
  formulation uses a softmax operation applied to a scaled dot product between query
  and key vectors. We explore the role played by norms of the queries and keys, which
  can cause training instabilities when they arbitrarily increase. We demonstrate
  how this can happen even in simple Transformer models, in the presence of easy-to-learn
  spurious patterns in the data. We propose a new attention formulation, QUEry-modulated
  Spherical aTtention (QUEST), that constrains the keys to a hyperspherical latent
  space, while still allowing individual tokens to flexibly control the sharpness
  of the attention distribution. QUEST can be easily used as a drop-in replacement
  for standard attention. We focus on vision applications while also exploring other
  domains to highlight the method’s generality. We show that (1) QUEST trains without
  instabilities and (2) produces models with improved performance (3) that are robust
  to data corruptions and adversarial attacks.
codebase_url: ''
extraction_model: ''
has_results: false
proposed_models: []
mrr: null
results: []
results_grouped: []
---

