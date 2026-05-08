-- Graph Learning Benchmarks — SQLite schema
-- All timestamps stored as ISO-8601 strings (UTC).
PRAGMA foreign_keys = ON;

-- ─────────────────────────────────────────────────────────────────────────────
-- Benchmark suites (e.g. LRGB, GraphBench, OGB)
-- ─────────────────────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS benchmarks (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    name        TEXT NOT NULL,
    short_name  TEXT NOT NULL UNIQUE,
    paper_id    INTEGER REFERENCES papers(id) ON DELETE SET NULL,
    description TEXT,
    url         TEXT,
    created_at  TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ', 'now'))
);

-- ─────────────────────────────────────────────────────────────────────────────
-- Datasets within a benchmark (logical dataset, not a specific split/variant)
-- ─────────────────────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS datasets (
    id               INTEGER PRIMARY KEY AUTOINCREMENT,
    benchmark_id     INTEGER REFERENCES benchmarks(id) ON DELETE SET NULL,
    name             TEXT NOT NULL,
    description      TEXT,
    domain           TEXT,   -- e.g. chemistry, social, citation, computer_vision
    task_type        TEXT,   -- node_classification, graph_classification, link_prediction, graph_regression
    primary_metric   TEXT,   -- e.g. AP, Accuracy, MAE, F1
    higher_is_better INTEGER NOT NULL DEFAULT 1,  -- 1=higher better, 0=lower better
    pyg_url          TEXT,   -- link to PyTorch Geometric dataset page, if available
    -- Canonical graph statistics (may differ across variants)
    num_graphs       INTEGER,
    avg_nodes        REAL,
    avg_edges        REAL,
    num_classes      INTEGER,
    created_at       TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ', 'now'))
);

-- ─────────────────────────────────────────────────────────────────────────────
-- Dataset variants — tracks split differences, sizes, label fractions, etc.
-- e.g. Cora/Planetoid-split vs Cora/random-10fold; ZINC/full vs ZINC/subset
-- ─────────────────────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS dataset_variants (
    id               INTEGER PRIMARY KEY AUTOINCREMENT,
    dataset_id       INTEGER NOT NULL REFERENCES datasets(id) ON DELETE CASCADE,
    name             TEXT NOT NULL,         -- e.g. "standard", "random-10fold", "subset-12k"
    description      TEXT,
    -- Variant-specific statistics (override dataset-level if set)
    num_graphs       INTEGER,
    avg_nodes        REAL,
    avg_edges        REAL,
    label_fraction   REAL,                  -- fraction of labelled nodes (for semi-supervised)
    split_type       TEXT,                  -- fixed, random, scaffold, stratified, …
    is_standard      INTEGER NOT NULL DEFAULT 1,   -- 1 = the canonical/default split
    notes            TEXT,                  -- human-readable warning shown on the website
    created_at       TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ', 'now')),
    UNIQUE(dataset_id, name)
);

-- ─────────────────────────────────────────────────────────────────────────────
-- Papers
-- ─────────────────────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS papers (
    id                 INTEGER PRIMARY KEY AUTOINCREMENT,
    arxiv_id           TEXT UNIQUE,           -- NULL for non-arXiv papers
    arxiv_version      INTEGER,               -- latest downloaded version number
    title              TEXT NOT NULL,
    authors            TEXT,                  -- JSON array of author name strings
    abstract           TEXT,
    published_date     TEXT,                  -- YYYY-MM-DD
    venue              TEXT,                  -- NeurIPS 2022, ICML 2023, …
    pdf_path           TEXT,                  -- relative to project root
    html_path          TEXT,                  -- path to downloaded HTML index file
    main_figure_path   TEXT,                  -- relative path to saved main figure image
    codebase_url       TEXT,
    -- Pipeline state
    extraction_status  TEXT NOT NULL DEFAULT 'pending',
        -- pending | downloaded | extracted | processed | failed
    extraction_model   TEXT,                  -- model name used for last extraction
    discovery_source   TEXT,                  -- lrgb_citation | graphbench_citation | arxiv_scanner | manual
    is_benchmark_paper INTEGER NOT NULL DEFAULT 0,
    created_at         TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ', 'now')),
    updated_at         TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ', 'now'))
);

-- ─────────────────────────────────────────────────────────────────────────────
-- Models / architectures
-- ─────────────────────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS models (
    id             INTEGER PRIMARY KEY AUTOINCREMENT,
    name           TEXT NOT NULL,
    canonical_name TEXT NOT NULL,   -- normalized name for grouping (lowercase, no punctuation)
    paper_id       INTEGER REFERENCES papers(id) ON DELETE SET NULL,
    size_params    INTEGER,         -- parameter count (exact, if known)
    model_type     TEXT,            -- GCN_variant | GAT_variant | GraphTransformer | GNN | Other
    is_baseline    INTEGER NOT NULL DEFAULT 0,
    created_at     TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ', 'now')),
    UNIQUE(canonical_name)
);

-- Aliases enable fuzzy baseline grouping across papers
-- e.g. model "GCN" may appear as "Graph Convolutional Network", "2-layer GCN", etc.
CREATE TABLE IF NOT EXISTS model_aliases (
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    model_id INTEGER NOT NULL REFERENCES models(id) ON DELETE CASCADE,
    alias    TEXT NOT NULL,
    UNIQUE(alias)
);

-- ─────────────────────────────────────────────────────────────────────────────
-- Benchmark results
-- ─────────────────────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS results (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    paper_id            INTEGER NOT NULL REFERENCES papers(id) ON DELETE CASCADE,
    model_id            INTEGER NOT NULL REFERENCES models(id) ON DELETE CASCADE,
    dataset_variant_id  INTEGER NOT NULL REFERENCES dataset_variants(id) ON DELETE CASCADE,
    metric_name         TEXT NOT NULL,      -- e.g. AP, Accuracy, MAE, F1, Hits@50
    metric_value        REAL NOT NULL,
    metric_std          REAL,               -- ±std over seeds/folds (nullable)
    is_baseline         INTEGER NOT NULL DEFAULT 0,
    -- When is_baseline=1 and the result comes from a cited paper, record source
    source_paper_id     INTEGER REFERENCES papers(id) ON DELETE SET NULL,
    higher_is_better    INTEGER NOT NULL DEFAULT 1,
    table_ref           TEXT,               -- e.g. "Table 1"
    source_ref          TEXT,               -- "this paper" or "Author Year"
    extraction_model    TEXT,               -- model name used to extract this result
    uses_external_data  INTEGER,            -- 1=yes, 0=no, NULL=unknown
    -- Human correction system
    is_problematic      INTEGER NOT NULL DEFAULT 0,  -- shown in grey on leaderboard
    problematic_reason  TEXT,
    is_overridden       INTEGER NOT NULL DEFAULT 0,  -- pipeline will NOT overwrite if 1
    override_value      REAL,
    override_std        REAL,
    override_reason     TEXT,
    override_source     TEXT,               -- path to the overrides.yaml that set this
    created_at          TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ', 'now')),
    UNIQUE(paper_id, model_id, dataset_variant_id, metric_name)
);

-- ─────────────────────────────────────────────────────────────────────────────
-- Pipeline audit log
-- ─────────────────────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS pipeline_runs (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    paper_id      INTEGER REFERENCES papers(id) ON DELETE SET NULL,
    stage         TEXT NOT NULL,   -- discover | download | extract | aggregate | export | build
    status        TEXT NOT NULL,   -- success | failed | skipped
    model_used    TEXT,
    error_message TEXT,
    started_at    TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ', 'now'))
);

-- ─────────────────────────────────────────────────────────────────────────────
-- Indexes
-- ─────────────────────────────────────────────────────────────────────────────
CREATE INDEX IF NOT EXISTS idx_papers_arxiv_id       ON papers(arxiv_id);
CREATE INDEX IF NOT EXISTS idx_papers_status         ON papers(extraction_status);
CREATE INDEX IF NOT EXISTS idx_results_paper         ON results(paper_id);
CREATE INDEX IF NOT EXISTS idx_results_variant       ON results(dataset_variant_id);
CREATE INDEX IF NOT EXISTS idx_results_model         ON results(model_id);
CREATE INDEX IF NOT EXISTS idx_pipeline_paper_stage  ON pipeline_runs(paper_id, stage);
CREATE INDEX IF NOT EXISTS idx_model_aliases_alias   ON model_aliases(alias);

-- ─────────────────────────────────────────────────────────────────────────────
-- paper_candidates — full discovery funnel (ALL papers seen, including rejects)
-- ─────────────────────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS paper_candidates (
    id                INTEGER PRIMARY KEY AUTOINCREMENT,
    arxiv_id          TEXT UNIQUE,
    title             TEXT NOT NULL,
    abstract          TEXT,
    published_date    TEXT,
    authors           TEXT,           -- JSON list
    categories        TEXT,           -- JSON list (arXiv categories)

    -- How the paper was found
    discovery_source  TEXT,           -- arxiv_scanner | lrgb_citation | graphbench_citation
    discovery_detail  TEXT,           -- e.g. "arXiv cs.LG sweep 7d" or "cited by 2206.08164"

    -- Stage 1 — cheap relevance filter (is this graph learning?)
    stage1_passed     INTEGER,        -- NULL=not run, 0=failed, 1=passed
    stage1_confidence REAL,
    stage1_reason     TEXT,           -- LLM-provided explanation

    -- Stage 2 — benchmark check (does it report new results?)
    stage2_passed     INTEGER,        -- NULL=not run, 0=failed, 1=passed
    stage2_confidence REAL,
    stage2_reason     TEXT,
    stage2_datasets   TEXT,           -- JSON list of dataset names mentioned

    -- Final disposition
    final_status      TEXT,           -- accepted | rejected_stage1 | rejected_stage2 | duplicate | already_known
    paper_id          INTEGER REFERENCES papers(id) ON DELETE SET NULL,
    created_at        TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ', 'now'))
);
CREATE INDEX IF NOT EXISTS idx_candidates_arxiv_id     ON paper_candidates(arxiv_id);
CREATE INDEX IF NOT EXISTS idx_candidates_final_status ON paper_candidates(final_status);
CREATE INDEX IF NOT EXISTS idx_candidates_source       ON paper_candidates(discovery_source);
