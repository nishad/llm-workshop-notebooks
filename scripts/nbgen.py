"""Build .ipynb files from plain Python cell lists in nbsrc/<name>.py.

Usage: uv run python scripts/nbgen.py [name ...]   (default: every module in nbsrc/)
Each nbsrc module defines TITLE and CELLS = [("md", text), ("code", source), ...].
"""

from __future__ import annotations

import importlib
import pkgutil
import sys
from pathlib import Path

import nbformat

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:  # run as a file, scripts/ is sys.path[0]; nbsrc lives at the repository root
    sys.path.insert(0, str(ROOT))


def build_notebook(cells: list[tuple[str, str]]) -> nbformat.NotebookNode:
    nb = nbformat.v4.new_notebook()
    for kind, source in cells:
        if kind == "md":
            nb.cells.append(nbformat.v4.new_markdown_cell(source.strip("\n")))
        elif kind == "code":
            if not source.strip():
                raise ValueError("empty code cell is not allowed")
            nb.cells.append(nbformat.v4.new_code_cell(source.strip("\n")))
        else:
            raise ValueError(f"unknown cell kind {kind}")
    nb.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3 (ipykernel)", "language": "python"}
    nb.metadata["language_info"] = {"name": "python"}
    return nb


def write_notebook(nb: nbformat.NotebookNode, path: Path) -> None:
    nbformat.validate(nb)
    nbformat.write(nb, str(path))


def output_name(name: str) -> str:
    """nbsrc modules start with `n` before a digit (a module name cannot start with one); the notebook does not."""
    return f"{name[1:] if name[0] == 'n' and name[1].isdigit() else name}.ipynb"


def main(argv: list[str]) -> None:
    names = argv or [m.name for m in pkgutil.iter_modules([str(ROOT / "nbsrc")]) if not m.name.startswith("_")]
    for name in names:
        module = importlib.import_module(f"nbsrc.{name}")
        nb = build_notebook(module.CELLS)
        out = ROOT / output_name(name)
        write_notebook(nb, out)
        print(f"wrote {out.name} ({len(nb.cells)} cells)")


if __name__ == "__main__":
    main(sys.argv[1:])
