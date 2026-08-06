from types import SimpleNamespace

import pytest

from backend.guided_table import (
    GuidedDataset,
    GuidedDiscovery,
    GuidedMethod,
    GuidedTableSpec,
    GuidedTask,
    build_table_column_guide,
    extract_guided_results,
    parse_latex_table,
)


def _table(body: str, number: int = 1, caption: str = "Main benchmark results"):
    return SimpleNamespace(number=number, label=f"tab:{number}", caption=caption, body=body)


def test_parse_latex_table_preserves_values_and_multicolumn_headers():
    parsed = parse_latex_table(
        _table(r"""
            \begin{tabular}{lcc}
            \toprule
            Method & Cora & CiteSeer \\
            \midrule
            GCN & 0.812e0 & 81.2 \\
            \bottomrule
            \end{tabular}
            """)
    )
    assert list(parsed.frame.columns) == ["Method", "Cora", "CiteSeer"]
    assert parsed.frame.iloc[0].tolist() == ["GCN", "0.812e0", "81.2"]


def test_table_column_guide_preserves_dataset_metric_groups_without_values():
    table = _table(r"""
        \newcommand{\grouphead}[2]{\multicolumn{3}{#1}{#2}}
        \begin{tabular}{@{}l|ccc|ccc@{}}
        \toprule
        \textbf{Dataset} & \grouphead{c|}{\textbf{products}} & \grouphead{c}{\textbf{papers100m}} \\
        \textbf{Metric} & \szs{Acc} & \szs{Time} & \szs{FLOPs}
            & \szs{Acc} & \szs{Time} & \szs{FLOPs} \\
        \midrule
        SGC & 79.1 & 289.6 & 247.4+434.4 & 63.3 & 19212 & 17.7+253.6 \\
        \bottomrule
        \end{tabular}
        """)
    guide = build_table_column_guide(table)
    assert "dataset 'products'" in guide
    assert "dataset 'papers100m'" in guide
    assert "metrics: Acc, Time, FLOPs" in guide
    assert "79.1" not in guide
    assert "63.3" not in guide


def test_table_column_guide_is_absent_for_flat_tables():
    table = _table(r"""
        \begin{tabular}{lcc}
        Method & Cora & CiteSeer \\
        GCN & 81.2 & 72.1 \\
        \end{tabular}
        """)
    assert build_table_column_guide(table) == ""


def test_guided_extraction_renames_methods_and_normalizes_values(tmp_path, monkeypatch):
    monkeypatch.setattr("backend.guided_table.cfg.logs_dir", tmp_path)
    table = _table(r"""
        \begin{tabular}{lcc}
        Method & Cora Accuracy & Cora F1 \\
        \midrule
        Ours & 82.0 \pm 1.0 & 0.70 (0.02) \\
        GCN & 81.0 & 0.65 \\
        Ablation & 90.0 & 0.99 \\
        \end{tabular}
        """)
    discovery = GuidedDiscovery(
        tables=[
            GuidedTableSpec(
                table_ref="Table 1",
                datasets=[
                    GuidedDataset(
                        name="Cora",
                        tasks=[GuidedTask(metric="Accuracy", columns=["Cora Accuracy"])],
                    )
                ],
                methods=[
                    GuidedMethod(
                        source_names=["Ours"], output_name="GraphMinNet", is_proposed=True
                    ),
                    GuidedMethod(source_names=["GCN"], output_name="GCN"),
                ],
            )
        ]
    )
    output = extract_guided_results([table], discovery, arxiv_id="2401.00001")
    assert {(row.model, row.dataset, row.metric) for row in output.results} == {
        ("GraphMinNet", "Cora", "Accuracy"),
        ("GCN", "Cora", "Accuracy"),
    }
    ours = next(row for row in output.results if row.model == "GraphMinNet")
    assert ours.value == pytest.approx(0.82)
    assert ours.std == pytest.approx(0.01)


def test_guided_extraction_logs_missing_columns(tmp_path, monkeypatch):
    monkeypatch.setattr("backend.guided_table.cfg.logs_dir", tmp_path)
    discovery = GuidedDiscovery(
        tables=[
            GuidedTableSpec(
                table_ref="Table 1",
                datasets=[
                    GuidedDataset(name="Cora", tasks=[GuidedTask(metric="AP", columns=["missing"])])
                ],
                methods=[GuidedMethod(source_names=["GCN"], output_name="GCN")],
            )
        ]
    )
    output = extract_guided_results(
        [_table(r"\begin{tabular}{lc} Method & Cora \\ GCN & 0.8 \\ \end{tabular}")],
        discovery,
        arxiv_id="2401.00002",
    )
    assert output.results == []
    error_log = (tmp_path / "guided_table_errors.jsonl").read_text()
    assert "missing_column" in error_log
