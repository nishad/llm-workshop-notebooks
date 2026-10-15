import nbformat

from scripts import nbgen


def test_build_notebook_from_cells(tmp_path):
    cells = [("md", "# Title ⏱️ 10 minutes"), ("code", "print('hi')"), ("md", "## 01.01 Section")]
    nb = nbgen.build_notebook(cells)
    assert [c.cell_type for c in nb.cells] == ["markdown", "code", "markdown"]
    assert nb.cells[1].source == "print('hi')"
    assert nb.metadata["kernelspec"]["name"] == "python3"
    out = tmp_path / "x.ipynb"
    nbgen.write_notebook(nb, out)
    assert nbformat.read(str(out), as_version=4).cells[0].source.startswith("# Title")


def test_rejects_empty_trailing_code_cell():
    try:
        nbgen.build_notebook([("md", "a"), ("code", "   ")])
    except ValueError as exc:
        assert "empty" in str(exc)
    else:
        raise AssertionError("expected ValueError")
