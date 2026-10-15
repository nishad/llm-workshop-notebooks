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


def test_output_name_strips_module_prefix_before_a_digit():
    assert nbgen.output_name("n00_check_setup") == "00_check_setup.ipynb"
    assert nbgen.output_name("other") == "other.ipynb"


def test_keep_outputs_carries_only_unchanged_code_cells():
    old = nbgen.build_notebook([("md", "# T"), ("code", "a = 1"), ("md", "x"), ("code", "b = 2")])
    for n, cell in enumerate(c for c in old.cells if c.cell_type == "code"):
        cell.outputs = [nbformat.v4.new_output("stream", name="stdout", text=f"out {n}\n")]
        cell.execution_count = n + 1
    new = nbgen.build_notebook([("md", "# T, reworded"), ("md", "a new note"), ("code", "a = 1"), ("md", "x"), ("code", "b = 3")])
    assert nbgen.keep_outputs(new, old) == 1
    code = [c for c in new.cells if c.cell_type == "code"]
    assert code[0].outputs[0]["text"] == "out 0\n" and code[0].execution_count == 1
    assert code[1].outputs == [] and code[1].execution_count is None
