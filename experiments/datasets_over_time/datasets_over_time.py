import sqlite3
import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent
PROJECT_ROOT = BASE_DIR.parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from datasets_over_time_helpers import (  # noqa: E402
    compute_percentages_and_counts,
    compute_union_relative_shares,
    fetch_data_by_benchmarkgroup,
    fetch_data_by_dataset,
    list_tables,
    load_all_tables,
    plot_line_charts,
    plot_stacked_bar_charts,
)

from backend.mlp_comparison import load_comparison_results  # noqa: E402
from backend.results_parser import result_is_leaderboard_eligible  # noqa: E402

# --- Configuration ---
DATA_DIR = BASE_DIR / "data"
PLOT_DIR = BASE_DIR / "plots"
DB_PATH = PROJECT_ROOT / "data" / "benchmarks.db"

for d in (DATA_DIR, PLOT_DIR):
    d.mkdir(parents=True, exist_ok=True)

if not DB_PATH.is_file():
    sys.stderr.write(f"Cannot find {DB_PATH}\n")
    sys.exit(1)

# Plotting parameters
dataset_list = [
    "Peptides-func",
    "Peptides-struct",
    "PCQM-Contact",
    "PascalVOC-SP",
    "COCO-SP",
]
benchmark_list = [
    "OGB",
    "LRGB",
    "Heterophilic Graphs",
    "Heterophily Benchmark",
    "TU Dortmund",
]
TIME_STEP = "Y"  # Choose the time step you want: "M" = 1 month, "3M" = 3 months, "Y" = 1 year

# Date range filter (ISO format strings: "YYYY-MM-DD")
START_DATE = "2019-01-01"
END_DATE = "2026-12-31"
BENCHMARK_START_YEARS = {
    "OGB": 2020,
    "Heterophilic Graphs": 2020,
    "Heterophily Benchmark": 2023,
    "LRGB": 2022,
    "TU Dortmund": 2017,
}

# --- Main ---

# Load all tables from database
conn = sqlite3.connect(str(DB_PATH))
tables = list_tables(conn)
dataframes = load_all_tables(
    conn, tables, DATA_DIR, save_csv=False, limit=None
)  # save_csv: save alle tables
conn.close()

# Plot per benchmark group
eligible_result_ids = {
    result.id for result in load_comparison_results() if result_is_leaderboard_eligible(result)
}
benchmarks_df = fetch_data_by_benchmarkgroup(DB_PATH, benchmark_list, START_DATE, END_DATE)
benchmarks_df = benchmarks_df[benchmarks_df["result_id"].isin(eligible_result_ids)]
benchmarks_pivot_share, benchmarks_pivot_cnt = compute_percentages_and_counts(
    benchmarks_df, "benchmark", DATA_DIR, TIME_STEP, save_csv=False, print_info=True
)  # save_csv: save joint benchmark groups table
plot_stacked_bar_charts(benchmarks_pivot_cnt, "benchmarks", PLOT_DIR)
plot_line_charts(
    benchmarks_pivot_cnt,
    "benchmarks_lines",
    PLOT_DIR,
    start_years=BENCHMARK_START_YEARS,
)
benchmarks_union_share = compute_union_relative_shares(benchmarks_df, "benchmark", TIME_STEP)
plot_line_charts(
    benchmarks_union_share,
    "benchmarks_relative_lines",
    PLOT_DIR,
    ylabel="Share of papers (%)",
    start_years=BENCHMARK_START_YEARS,
)

# Plot per dataset
dataset_df = fetch_data_by_dataset(DB_PATH, dataset_list, None, END_DATE)
dataset_df = dataset_df[dataset_df["result_id"].isin(eligible_result_ids)]
dataset_pivot_share, dataset_pivot_cnt = compute_percentages_and_counts(
    dataset_df, "dataset", DATA_DIR, TIME_STEP, save_csv=False, print_info=True
)  # save_csv: save joint datasets table
plot_stacked_bar_charts(dataset_pivot_cnt, "datasets", PLOT_DIR)
