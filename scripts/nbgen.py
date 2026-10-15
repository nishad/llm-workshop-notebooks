"""Build .ipynb files from plain Python cell lists in nbsrc/<name>.py.

Usage: uv run python scripts/nbgen.py [--keep-outputs] [name ...]   (default: every module in nbsrc/)
Each nbsrc module defines TITLE and CELLS = [("md", text), ("code", source), ...].
--keep-outputs carries the outputs of every unchanged code cell over from the existing notebook, so a Markdown-only
change does not need a re-run; changed or new code cells are left without outputs for check_notebooks.py to flag.
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


def keep_outputs(nb: nbformat.NotebookNode, old: nbformat.NotebookNode) -> int:
    """Copy outputs from `old` into `nb` for each code cell whose source is unchanged.

    Code cells are matched by position among the code cells (the first with the first, and so on) and must have
    identical source; Markdown cells may change freely. Unchanged cells also keep their cell ids, so the diff shows
    only what changed. Returns the number of code cells that kept their outputs.
    """
    old_code = [c for c in old.cells if c.cell_type == "code"]
    new_code = [c for c in nb.cells if c.cell_type == "code"]
    kept = 0
    for before, after in zip(old_code, new_code):
        if before.source == after.source:
            after.outputs = before.get("outputs", [])
            after.execution_count = before.get("execution_count")
            after.metadata = before.get("metadata", {})
            if "id" in before:
                after.id = before.id
            kept += 1
    old_md: dict[str, list[str]] = {}
    for c in old.cells:
        if c.cell_type == "markdown" and "id" in c:
            old_md.setdefault(c.source, []).append(c.id)
    for c in nb.cells:
        if c.cell_type == "markdown" and old_md.get(c.source):
            c.id = old_md[c.source].pop(0)
    if kept and "language_info" in old.metadata:  # the outputs came from that kernel
        nb.metadata["language_info"] = old.metadata["language_info"]
    return kept


def write_notebook(nb: nbformat.NotebookNode, path: Path) -> None:
    nbformat.validate(nb)
    nbformat.write(nb, str(path))


def output_name(name: str) -> str:
    """nbsrc modules start with `n` before a digit (a module name cannot start with one); the notebook does not."""
    return f"{name[1:] if name[0] == 'n' and name[1].isdigit() else name}.ipynb"


def main(argv: list[str]) -> None:
    keep = "--keep-outputs" in argv
    argv = [a for a in argv if a != "--keep-outputs"]
    names = argv or [m.name for m in pkgutil.iter_modules([str(ROOT / "nbsrc")]) if not m.name.startswith("_")]
    for name in names:
        module = importlib.import_module(f"nbsrc.{name}")
        nb = build_notebook(module.CELLS)
        out = ROOT / output_name(name)
        note = ""
        if keep and out.exists():
            kept = keep_outputs(nb, nbformat.read(str(out), as_version=4))
            total = sum(c.cell_type == "code" for c in nb.cells)
            note = f", kept outputs of {kept} of {total} code cells"
        write_notebook(nb, out)
        print(f"wrote {out.name} ({len(nb.cells)} cells{note})")


if __name__ == "__main__":
    main(sys.argv[1:])
