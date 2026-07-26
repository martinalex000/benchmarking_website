from scripts.create_sota_driver_re_evaluation_list import driver_paper_ids, write_list


def test_driver_paper_ids_are_deduplicated(tmp_path):
    report = tmp_path / "audit.md"
    report.write_text(
        "## Source-audited driver rows\n"
        "| Dataset | Driver paper | Model |\n"
        "| Cora | 2401.00001 | A |\n"
        "| PubMed | 2401.00001 | B |\n"
        "| Cora | 2402.00002 | C |\n"
        "## Confirmed and high-priority findings\n",
        encoding="utf-8",
    )

    assert driver_paper_ids(report) == ["2401.00001", "2402.00002"]


def test_write_list_contains_reproducible_marking_command(tmp_path):
    report = tmp_path / "audit.md"
    output = tmp_path / "config" / "drivers.txt"
    report.write_text(
        "## Source-audited driver rows\n| Cora | 2401.00001 |\n"
        "## Confirmed and high-priority findings\n",
        encoding="utf-8",
    )

    assert write_list(report, output) == 1
    contents = output.read_text(encoding="utf-8")
    assert "2401.00001" in contents
    assert "--requeue" in contents
    assert "dataset_sota_concentration_audit" in contents
