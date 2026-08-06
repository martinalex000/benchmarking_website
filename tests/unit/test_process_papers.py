import pytest

from scripts import process_papers


def test_no_arguments_prints_help_without_processing(monkeypatch, capsys):
    monkeypatch.setattr(process_papers, "_run_paper", lambda _args: pytest.fail())
    monkeypatch.setattr(process_papers, "_run_dashboard", lambda _args: pytest.fail())

    assert process_papers.main([]) == 0

    assert "ARXIV_ID" in capsys.readouterr().out


def test_arxiv_id_dispatches_direct_processing(monkeypatch):
    calls = []
    monkeypatch.setattr(process_papers, "_run_paper", calls.append)

    assert process_papers.main(["2206.08164", "--force"]) == 0

    assert calls == [["2206.08164", "--force"]]


def test_dashboard_dispatches_dashboard_options(monkeypatch):
    calls = []
    monkeypatch.setattr(process_papers, "_run_dashboard", calls.append)

    assert process_papers.main(["dashboard", "--workers", "4"]) == 0

    assert calls == [["--workers", "4"]]
