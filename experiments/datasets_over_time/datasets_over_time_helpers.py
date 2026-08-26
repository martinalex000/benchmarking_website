"""
Helpers for loading benchmark data from SQLite and producing
stacked-bar charts of paper counts per period.

The database schema (simplified):

    benchmarks ─┐
                ├─< datasets  ─┐
                │              ├─< dataset_variants  ─┐
                │              │                      ├─< results >─ papers
                └──────────────┘                      │
                                                      │
Each ``results`` row links a paper to a dataset variant.
"""

import sqlite3
import sys

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.transforms import ScaledTranslation

from backend.venue import is_conference_publication_venue

# --- Database introspection ---


def list_tables(conn):
    """Return the names of all tables in the database.

    Parameters
    ----------
    conn : sqlite3.Connection
        Open SQLite connection.

    Returns
    -------
    list[str]
        Sorted list of table names.
    """
    cur = conn.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
    return [row[0] for row in cur.fetchall()]


def load_table(conn, table_name, limit=None):
    """Load one table into a pandas DataFrame.

    Parameters
    ----------
    conn : sqlite3.Connection
        Open SQLite connection.
    table_name : str
        Name of the table to read.
    limit : int | None, optional
        If given, adds a ``LIMIT <limit>`` clause – useful for huge tables.

    Returns
    -------
    pd.DataFrame
        The full (or limited) contents of *table_name*.
    """
    sql = f"SELECT * FROM {table_name}"
    if limit is not None:
        sql += f" LIMIT {limit}"
    sql += ";"
    return pd.read_sql_query(sql, conn)


def load_all_tables(conn, tables, DATA_DIR, save_csv=False, limit=None):
    """Load every table listed in *tables* into a dict of DataFrames.

    Parameters
    ----------
    conn : sqlite3.Connection
        Open SQLite connection.
    tables : list[str]
        Table names to load.
    DATA_DIR : pathlib.Path
        Directory where CSV files are saved (used when *save_csv* is True).
    save_csv : bool, optional
        If True, write each table to ``<data_dir>/<table>.csv``.
    limit : int | None, optional
        Row limit passed to :func:`load_table`.

    Returns
    -------
    dict[str, pd.DataFrame]
        Mapping from table name to DataFrame.  Empty dict if *tables*
        is empty (the process also exits with status 1).
    """
    if not tables:
        print("No tables found in the database.")
        conn.close()
        sys.exit(1)
        return {}

    print(f"\nFound {len(tables)} table(s): {', '.join(tables)}\n")
    dataframes: dict[str, pd.DataFrame] = {}
    for tbl in tables:
        df = load_table(conn, tbl, limit=limit)
        dataframes[tbl] = df
        if save_csv:
            csv_path = DATA_DIR / f"{tbl}.csv"
            df.to_csv(csv_path, index=False)
    return dataframes


# --- Data fetching ---


def fetch_data_by_dataset(DB_PATH, datasets, start_date=None, end_date=None):
    """Fetch rows for the given datasets.

    Parameters
    ----------
    DB_PATH : pathlib.Path | str
        Path to the SQLite database.
    datasets : list[str]
        Dataset names to filter on (``datasets.name``).
    start_date : str, optional
        ISO format start date (e.g., ``"2017-01-01"``).
    end_date : str, optional
        ISO format end date (e.g., ``"2025-12-31"``).

    Returns
    -------
    pd.DataFrame
        Columns: ``dataset_name``, ``paper_timestamp``,
        ``paper_id``, ``paper_title``.
    """
    conn = sqlite3.connect(str(DB_PATH))
    placeholders = ", ".join(["?"] * len(datasets))

    conditions = [f"d.name IN ({placeholders})"]
    params = list(datasets)

    if start_date:
        conditions.append("p.published_date >= ?")
        params.append(start_date)
    if end_date:
        conditions.append("p.published_date <= ?")
        params.append(end_date)

    where_clause = " AND ".join(conditions)

    sql = f"""
        SELECT
            r.id              AS result_id,
            d.name            AS dataset_name,
            p.published_date  AS paper_timestamp,
            r.paper_id,
            p.title           AS paper_title,
            p.venue           AS paper_venue
        FROM results r
        JOIN dataset_variants dv ON r.dataset_variant_id = dv.id
        JOIN datasets d          ON dv.dataset_id        = d.id
        JOIN papers p            ON r.paper_id          = p.id
        WHERE {where_clause}
    """
    df = pd.read_sql_query(sql, conn, params=params)
    conn.close()
    return df


def fetch_data_by_benchmarkgroup(DB_PATH, benchmark_names, start_date=None, end_date=None):
    """Fetch rows for the given benchmark groups.

    Parameters
    ----------
    DB_PATH : pathlib.Path | str
        Path to the SQLite database.
    benchmark_names : list[str]
        Benchmark names to filter on (``benchmarks.name``).
    start_date : str, optional
        ISO format start date (e.g., ``"2017-01-01"``).
    end_date : str, optional
        ISO format end date (e.g., ``"2025-12-31"``).

    Returns
    -------
    pd.DataFrame
        Columns: ``benchmark_name``, ``paper_timestamp``,
        ``paper_id``, ``paper_title``.
    """
    conn = sqlite3.connect(str(DB_PATH))
    placeholders = ", ".join(["?"] * len(benchmark_names))

    conditions = [f"b.name IN ({placeholders})"]
    params = list(benchmark_names)

    if start_date:
        conditions.append("p.published_date >= ?")
        params.append(start_date)
    if end_date:
        conditions.append("p.published_date <= ?")
        params.append(end_date)

    where_clause = " AND ".join(conditions)

    sql = f"""
        SELECT
            r.id              AS result_id,
            b.name            AS benchmark_name,
            p.published_date  AS paper_timestamp,
            r.paper_id,
            p.title           AS paper_title,
            p.venue           AS paper_venue
        FROM results r
        JOIN dataset_variants dv ON r.dataset_variant_id = dv.id
        JOIN datasets d          ON dv.dataset_id        = d.id
        JOIN benchmarks b        ON d.benchmark_id       = b.id
        JOIN papers p            ON r.paper_id          = p.id
        WHERE {where_clause}
    """
    df = pd.read_sql_query(sql, conn, params=params)
    conn.close()
    return df


def filter_conference_papers(df: pd.DataFrame) -> pd.DataFrame:
    """Keep rows whose source paper has conference-publication evidence."""
    if "paper_venue" not in df.columns:
        raise ValueError("DataFrame must contain paper_venue for conference filtering")
    mask = df["paper_venue"].map(is_conference_publication_venue)
    return df.loc[mask].copy()


# --- Aggregation & plotting ---


def compute_percentages_and_counts(df, group, DATA_DIR, time_step, save_csv=False, print_info=True):
    """Compute per-period paper counts and percentage shares.

    The DataFrame is deduplicated on ``(paper_id, <group>_name,
    period)`` so that each paper contributes at most once per
    group per period.

    Parameters
    ----------
    df : pd.DataFrame
        Must contain ``paper_timestamp``, ``paper_id``, and a
        column named ``<group>_name``.
    group : str
        Grouping key, e.g. ``"benchmark"`` or ``"dataset"``.
        The corresponding column is expected to be
        ``<group>_name``.
    DATA_DIR : pathlib.Path
        Directory for optional CSV export.
    time_step : str
        Pandas period frequency, e.g. ``"Y"``, ``"M"``,
        ``"3M"``.
    save_csv : bool, optional
        Write the deduplicated table to
        ``<DATA_DIR>/joint_<group>_table.csv``.
    print_info : bool, optional
        Print the share and count pivot tables.

    Returns
    -------
    pivot_share : pd.DataFrame
        Wide-format table with percentage shares per group
        per period.
    pivot_cnt : pd.DataFrame
        Wide-format table with raw integer paper counts per
        group per period.
    """
    group_name = group + "_name"

    # Deduplicate: one row per paper per group per period
    df["paper_timestamp"] = pd.to_datetime(df["paper_timestamp"], format="mixed")
    df["period"] = df["paper_timestamp"].dt.to_period(time_step)
    df = df.drop_duplicates(subset=["paper_id", group_name, "period"])
    df = df.sort_values("paper_timestamp")

    if save_csv:
        csv_path = DATA_DIR / f"joint_{group}_table.csv"
        df.to_csv(csv_path, index=False)

    # Count papers per (period, group)
    counts = df.groupby(["period", group_name]).size().reset_index(name="paper_cnt")

    # Compute percentage share of each group within the period
    total_per_period = counts.groupby("period")["paper_cnt"].transform("sum")
    counts["share"] = counts["paper_cnt"] / total_per_period * 100

    # Pivot to wide format: one column per group
    pivot_share = (
        counts.pivot(index="period", columns=group_name, values="share").fillna(0).sort_index()
    )
    pivot_cnt = (
        counts.pivot(index="period", columns=group_name, values="paper_cnt")
        .fillna(0)
        .astype(int)
        .sort_index()
    )

    if print_info:
        print("\n=== SHARE (percentage) table ===")
        print(pivot_share)
        print("\n=== COUNT (raw paper count) table ===")
        print(pivot_cnt)

    return pivot_share, pivot_cnt


def compute_union_relative_shares(df, group, time_step):
    """Compute each group's share of unique papers using any selected group."""
    group_name = group + "_name"
    prepared = df.copy()
    prepared["paper_timestamp"] = pd.to_datetime(prepared["paper_timestamp"], format="mixed")
    prepared["period"] = prepared["paper_timestamp"].dt.to_period(time_step)
    prepared = prepared.drop_duplicates(subset=["paper_id", group_name, "period"])

    group_counts = prepared.groupby(["period", group_name])["paper_id"].nunique()
    union_counts = prepared.groupby("period")["paper_id"].nunique()
    shares = group_counts.div(union_counts, level="period") * 100
    return shares.unstack(fill_value=0).sort_index()


def plot_stacked_bar_charts(pivot_cnt, plot_name, PLOT_DIR):
    """Draw a stacked bar chart of paper counts per period.

    Parameters
    ----------
    pivot_cnt : pd.DataFrame
        Wide-format count table (rows = periods, columns =
        groups).  Produced by
        :func:`compute_percentages_and_counts`.
    plot_name : str
        Name of the png file that the plot is saved as.
    PLOT_DIR : pathlib.Path
        Directory where the figure is saved.

    Returns
    -------
    None
        The figure is saved to disk; nothing is returned.
    """
    PLOT_DIR.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(7, 4.8))

    prop_cycle = plt.rcParams["axes.prop_cycle"]
    colors = prop_cycle.by_key()["color"]

    if "TU Dortmund" in pivot_cnt.columns:
        pivot_cnt = pivot_cnt[
            ["TU Dortmund", *[column for column in pivot_cnt.columns if column != "TU Dortmund"]]
        ]

    bottom = np.zeros(len(pivot_cnt))
    x = np.arange(len(pivot_cnt))

    for i, col in enumerate(pivot_cnt.columns):
        heights = pivot_cnt[col].values
        label = f"{col} (legacy)" if col in {"Heterophilic Graphs", "TU Dortmund"} else col
        ax.bar(
            x,
            heights,
            bottom=bottom,
            label=label,
            color=colors[i],
            edgecolor="white",
            linewidth=0.5,
        )
        bottom = bottom + heights

    # Add n= above each bar
    period_totals = bottom
    for j, total in enumerate(period_totals):
        ax.text(x[j], total + 0.5, f"n={int(total)}", ha="center", va="bottom", fontsize=14)

    ax.set_ylabel("Number of papers", fontsize=20)
    ax.set_xticks(x)
    ax.set_xticklabels(pivot_cnt.index.astype(str))
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
    x_shift = ScaledTranslation(-3 / 72, 0, fig.dpi_scale_trans)
    for label in ax.get_xticklabels():
        label.set_transform(label.get_transform() + x_shift)
    ax.tick_params(axis="both", labelsize=18)
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles[::-1], labels[::-1], loc="upper left", fontsize=16)
    ax.set_ylim(0, period_totals.max() * 1.1)  # Add headroom for the n= labels

    fig.savefig(PLOT_DIR / f"{plot_name}s.png", dpi=150, bbox_inches="tight")
    fig.savefig(PLOT_DIR / f"{plot_name}s.pdf", bbox_inches="tight")

    return


def plot_line_charts(pivot_cnt, plot_name, PLOT_DIR, ylabel="Number of papers", start_years=None):
    """Draw one line per group and period."""
    PLOT_DIR.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(7, 4.8))

    prop_cycle = plt.rcParams["axes.prop_cycle"]
    colors = prop_cycle.by_key()["color"]
    if "TU Dortmund" in pivot_cnt.columns:
        pivot_cnt = pivot_cnt[
            ["TU Dortmund", *[column for column in pivot_cnt.columns if column != "TU Dortmund"]]
        ]

    x = np.arange(len(pivot_cnt))
    for i, col in enumerate(pivot_cnt.columns):
        label = f"{col} (legacy)" if col in {"Heterophilic Graphs", "TU Dortmund"} else col
        values = pivot_cnt[col].astype(float).to_numpy().copy()
        if start_years and col in start_years:
            values[pivot_cnt.index.year < start_years[col]] = np.nan
        ax.plot(
            x,
            values,
            marker="o",
            label=label,
            color=colors[i],
            linewidth=2,
        )

    ax.set_ylabel(ylabel, fontsize=20)
    ax.set_xticks(x)
    ax.set_xticklabels(pivot_cnt.index.astype(str))
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
    ax.tick_params(axis="both", labelsize=18)
    ax.legend(loc="upper right", fontsize=16)
    ax.set_ylim(0, pivot_cnt.to_numpy().max() * 1.1)

    fig.savefig(PLOT_DIR / f"{plot_name}.png", dpi=150, bbox_inches="tight")
    fig.savefig(PLOT_DIR / f"{plot_name}.pdf", bbox_inches="tight")
    plt.close(fig)
