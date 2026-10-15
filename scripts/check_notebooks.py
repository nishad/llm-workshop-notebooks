"""Check notebook conventions: time badge in the H1, 'What you'll learn', a configuration section, a checkpoint,
markdown before every code cell, no empty cells, outputs present on code cells.

Usage: uv run python scripts/check_notebooks.py [paths...]
"""

from __future__ import annotations

import sys
from pathlib import Path

import nbformat

ROOT = Path(__file__).resolve().parent.parent


def problems(path: Path) -> list[str]:
    nb = nbformat.read(str(path), as_version=4)
    out = []
    cells = nb.cells
    if not cells or cells[0].cell_type != "markdown" or "⏱️" not in cells[0].source:
        out.append("first cell must be a markdown H1 with a ⏱️ time budget")
    text = "\n".join(c.source for c in cells if c.cell_type == "markdown")
    for needle in ("What you'll learn", "Configuration", "✅ Checkpoint"):
        if needle not in text:
            out.append(f"missing '{needle}'")
    for i, c in enumerate(cells):
        if not c.source.strip():
            out.append(f"cell {i} is empty")
        if c.cell_type == "code":
            if i == 0 or cells[i - 1].cell_type != "markdown":
                out.append(f"code cell {i} is not preceded by a markdown cell")
            if not c.get("outputs") and "input(" not in c.source:
                out.append(f"code cell {i} has no outputs (run scripts/run_all_notebooks.py)")
    if cells and not cells[-1].source.strip():
        out.append("empty trailing cell")
    return out


def main(argv: list[str]) -> int:
    paths = [Path(p) for p in argv] or sorted(ROOT.glob("0*.ipynb"))
    bad = 0
    for p in paths:
        issues = problems(p)
        print(("OK   " if not issues else "FAIL ") + p.name)
        for issue in issues:
            bad += 1
            print("     -", issue)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
