import sqlite3, sys
from pathlib import Path
from helpers import list_tables, load_all_tables, fetch_data_by_dataset, fetch_data_by_benchmarkgroup, compute_percentages_and_counts, plot_stacked_bar_charts

# --- Configuration ---
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
PLOT_DIR = BASE_DIR / "plots"
DB_PATH = DATA_DIR / "benchmarks.db"

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
    "COCO-SP"
]
benchmark_list = [
    "TU Dortmund",
    "OGB",
    "LRGB",
    "Heterophilic Graphs",
    "MoleculeNet"
]
TIME_STEP = "Y" # Choose the time step you want: "M" = 1 month, "3M" = 3 months, "Y" = 1 year

# Date range filter (ISO format strings: "YYYY-MM-DD")
START_DATE = "2017-01-01"
END_DATE = "2025-12-31"

# --- Main ---

# Load all tables from database
conn = sqlite3.connect(str(DB_PATH))
tables = list_tables(conn)
dataframes = load_all_tables(conn, tables, DATA_DIR, save_csv=False, limit=None) # save_csv: save alle tables
conn.close()

# Plot per benchmark group
benchmarks_df = fetch_data_by_benchmarkgroup(DB_PATH, benchmark_list, START_DATE, END_DATE)
benchmarks_pivot_share, benchmarks_pivot_cnt = compute_percentages_and_counts(benchmarks_df, "benchmark", DATA_DIR, TIME_STEP, save_csv=True, print_info=True) # save_csv: save joint benchmark groups table
plot_stacked_bar_charts(benchmarks_pivot_cnt, "benchmarks", PLOT_DIR)

# Plot per dataset
dataset_df = fetch_data_by_dataset(DB_PATH, dataset_list, None, END_DATE)
dataset_pivot_share, dataset_pivot_cnt = compute_percentages_and_counts(dataset_df, "dataset", DATA_DIR, TIME_STEP, save_csv=True, print_info=True) # save_csv: save joint datasets table
plot_stacked_bar_charts(dataset_pivot_cnt, "datasets", PLOT_DIR)