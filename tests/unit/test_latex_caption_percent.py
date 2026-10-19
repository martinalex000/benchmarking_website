from backend.latex_source import _extract_tables


def test_escaped_percentage_does_not_truncate_caption_inventory():
    source = r"\begin{table}\caption{Accuracy (\%) averaged over five runs.}\end{table}"
    assert "averaged over five runs" in _extract_tables(source)[0].caption
