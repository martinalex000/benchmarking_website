# Dataset Metadata Research Report

## Scope and standard

This report tracks the source-traced review of all dataset entries in
`config/seed_data.yaml`. Public descriptions include only claims supported by the cited
sources. Unresolved, conflicting, or weakly supported claims are recorded here instead of being
presented as facts on the website.

## Current status

- Dataset entries: 142
- Fully researched: 23
- Partially researched: 1
- Not yet researched: 118

## Successes

- The metadata schema, persistence path, website expansion control, and coverage audit have been
  established.
- The pilot established provenance chains for Cora, Texas, Peptides-func, ogbg-code2, and
  Ribonanza-2k. Four could be documented completely enough for the public fields; Ribonanza-2k
  retains explicit reproducibility gaps.

## Challenges and unresolved questions

- Dataset-level provenance is largely absent from the current YAML; sources must be traced for
  each entry.
- A benchmark name can conceal multiple preprocessing, feature, and split variants.
- Some benchmark papers repackage upstream scientific or molecular measurements without fully
  documenting how those measurements were originally produced.

## Dataset review ledger

The ledger will be filled in benchmark-family batches. Each entry will record status, provenance
chain, confirmed facts, excluded claims, conflicts, and remaining questions.

### Peptides-func — complete

- **Provenance:** LRGB benchmark → SATPdb → 22 constituent peptide databases.
- **Confirmed:** graph construction, OGB atom/bond features, omitted folded structure, ten
  non-exclusive function labels, label imbalance, stratification procedure, split ratios, and metric.
- **Challenge:** SATPdb is itself an aggregate; individual peptide measurements and labels may trace
  to different upstream databases.
- **Excluded:** no claim that all upstream functional assays used a uniform experimental protocol.

### ogbg-code2 — complete

- **Provenance:** OGB processing → CodeSearchNet → GitHub repositories.
- **Confirmed:** AST construction and features, method-name masking, next-token/inverse edges,
  project split, target processing, order-insensitive F1, and the predecessor dataset's leakage.
- **Challenge:** papers sometimes abbreviate both the deprecated and corrected datasets as “Code”.
- **Excluded:** no blanket equivalence between ogbg-code and ogbg-code2 results.

### Cora — complete for the Planetoid artifact

- **Provenance:** PyG Planetoid artifact → Planetoid split definition → the larger Cora collection.
- **Confirmed:** task, graph and feature representation, public split, dimensions, and common
  alternative protocols.
- **Challenge:** “Cora” names several related but non-interchangeable corpora and preprocessings.
- **Excluded:** no claim that results using Cora-ML, random splits, or other Cora corpora are
  comparable with the Planetoid split.

### Texas — complete for the Geom-GCN/PyG artifact

- **Provenance:** Geom-GCN/PyG processing → CMU WebKB collection → university webpages.
- **Confirmed:** task, bag-of-words features, hyperlinks, five labels, fixed splits, extreme class
  imbalance, and small-sample evaluation concerns.
- **Challenge:** WebKB, WebKB4, 4 Universities, and university-specific graph subsets have different
  sizes and label selections.
- **Excluded:** no statistics from the broader WebKB collection were attributed to the Texas graph.

### Ribonanza — partial

- **Provenance:** DualEquiNet Ribonanza-2k → Ribonanza experimental collection/Kaggle challenge →
  Eterna and related experimental crowdsourcing.
- **Confirmed:** 2,260 sequences, approximate length, DMS and 2A3 nucleotide targets, predicted
  RhoFold structures in the benchmark pipeline, random 80/10/10 evaluation, and RMSE.
- **Challenge:** the benchmark paper does not explain how Ribonanza-2k was selected from the much
  larger upstream collection and does not fully enumerate the released scalar feature encoding.
- **Excluded:** no inferred subset-selection rule, feature vocabulary, or claim that predicted 3D
  structures are experimental ground truth.

### LRGB family — complete

- **Datasets:** Peptides-func, Peptides-struct, PascalVOC-SP, COCO-SP, and PCQM-Contact.
- **Success:** the local expanded source and official releases document construction, feature fields,
  targets, splits, and evaluation precisely. Upstream SATPdb, Pascal VOC, COCO, and PCQM4Mv2
  provenance was traced separately.
- **Challenges:** superpixel graph variants and the two PCQM tasks are easy to conflate; the public
  text now names the exact default construction and distinguishes contact prediction from gap
  regression.
- **Remaining uncertainty:** SATPdb's constituent records do not share a single experimental assay
  protocol; no such uniformity is claimed.

### OGB family — complete

- **Datasets:** all 16 OGB entries currently represented in the YAML, including graph, node, link,
  knowledge-graph, and PCQM4Mv2 tasks.
- **Success:** official OGB documentation and its upstream sources establish feature construction,
  task-specific splits, sampled-negative semantics, missing-label treatment, and version history.
- **Challenges:** several old and corrected artifacts have nearly identical names. The descriptions
  explicitly separate ogbg-code2 from ogbg-code, ogbl-citation2 from ogbl-citation,
  ogbl-wikikg2 from ogbl-wikikg, and PCQM4Mv2 from PCQM4M.
- **Remaining uncertainty:** aggregate biomedical graphs inherit incomplete and sometimes
  contradictory evidence from multiple repositories; absent edges and labels are not presented as
  confirmed negatives.
