---
title: Statistics Sources & Discrepancies
type: dev
description: Current aligned counts plus legacy counting-method impact
---

## Statistics Sources & Concrete Differences

Current landing-page counts and dataset-page counts use the same definition, so they should match exactly.

**Landing total (current `benchmarks.json`):** 7868
**Dataset-page total (`content/datasets/*`):** 7868
**Difference (landing - dataset pages):** 0
**Datasets with non-zero differences:** 0
**Datasets present in landing data but missing exported pages:** 29

### What changed vs the old landing statistics

Old landing values counted raw result rows across all variants.
Current values count the same number shown on dataset pages: the exported standard-variant leaderboard rows.

**Legacy landing total (old method):** 11537
**Current landing total (new method):** 7868
**Total impact (old - new):** 3669
**Datasets affected by counting-method change:** 66

Current-definition check: no per-dataset deltas detected.

### Legacy vs current per-dataset impact

| Dataset | Legacy Landing (old) | Current Landing/Page (new) | Impact (old - new) |
|---|---:|---:|---:|
| peptides-func | 764 | 350 | 414 |
| peptides-struct | 741 | 346 | 395 |
| zinc | 601 | 346 | 255 |
| cifar10 | 282 | 119 | 163 |
| mnist | 272 | 115 | 157 |
| pattern | 231 | 94 | 137 |
| minesweeper | 222 | 103 | 119 |
| amazon-ratings | 216 | 104 | 112 |
| cluster | 201 | 89 | 112 |
| roman-empire | 224 | 120 | 104 |
| pascalvoc-sp | 239 | 139 | 100 |
| tolokers | 183 | 83 | 100 |
| ogbg-molhiv | 343 | 251 | 92 |
| proteins | 322 | 230 | 92 |
| cora | 482 | 399 | 83 |
| ogbn-arxiv | 237 | 157 | 80 |
| pcqm-contact | 167 | 90 | 77 |
| texas | 289 | 218 | 71 |
| coco-sp | 164 | 97 | 67 |
| questions | 122 | 60 | 62 |
| cornell | 246 | 188 | 58 |
| mutag | 229 | 171 | 58 |
| chameleon | 217 | 162 | 55 |
| wisconsin | 235 | 180 | 55 |
| citeseer | 348 | 296 | 52 |
| squirrel | 169 | 124 | 45 |
| imdb-binary | 202 | 161 | 41 |
| ogbg-molpcba | 131 | 90 | 41 |
| nci1 | 125 | 86 | 39 |
| pubmed | 274 | 237 | 37 |
| sat-solving | 42 | 5 | 37 |
| lrim | 39 | 6 | 33 |
| flow | 32 | 5 | 27 |
| imdb-multi | 98 | 72 | 26 |
| d-d | 275 | 252 | 23 |
| enzymes | 153 | 130 | 23 |
| bace | 109 | 87 | 22 |
| malnet-tiny | 46 | 25 | 21 |
| wikics | 82 | 67 | 15 |
| collab | 125 | 111 | 14 |
| pcqm4mv2 | 64 | 50 | 14 |
| actor | 169 | 156 | 13 |
| amazon-photo | 94 | 83 | 11 |
| bridges | 16 | 5 | 11 |
| mst | 16 | 5 | 11 |
| ogbn-proteins | 39 | 28 | 11 |
| amazon-computers | 73 | 65 | 8 |
| qm9 | 62 | 54 | 8 |
| tox21 | 85 | 77 | 8 |
| film | 63 | 57 | 6 |
| dblp | 59 | 54 | 5 |
| sider | 50 | 45 | 5 |
| bbbp | 78 | 74 | 4 |
| code | 31 | 27 | 4 |
| deezer | 34 | 30 | 4 |
| len | 30 | 26 | 4 |
| max-clique | 6 | 2 | 4 |
| max-matching | 6 | 2 | 4 |
| steiner-trees | 6 | 2 | 4 |
| topological-sorting | 6 | 2 | 4 |
| clintox | 52 | 49 | 3 |
| coauthor-physics | 40 | 38 | 2 |
| csl | 29 | 27 | 2 |
| ogbn-products | 45 | 43 | 2 |
| toxcast | 40 | 38 | 2 |
| ppi | 14 | 13 | 1 |