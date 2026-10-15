from pathlib import Path

import nbformat

from scripts import check_notebooks

ROOT = Path(__file__).resolve().parent.parent


def test_every_notebook_meets_conventions():
    for path in sorted(ROOT.glob("0*.ipynb")):
        assert check_notebooks.problems(path) == [], path.name


def test_detects_missing_markdown_before_code(tmp_path):
    nb = nbformat.v4.new_notebook()
    nb.cells = [nbformat.v4.new_markdown_cell("# T ⏱️ 1 minute\nWhat you'll learn\nConfiguration\n✅ Checkpoint"),
                nbformat.v4.new_code_cell("x = 1"), nbformat.v4.new_code_cell("y = 2")]
    p = tmp_path / "x.ipynb"
    nbformat.write(nb, str(p))
    issues = check_notebooks.problems(p)
    assert any("not preceded" in i for i in issues)
