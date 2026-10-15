"""Execute notebooks in place against the local Ollama so outputs are committed.

Usage: uv run python scripts/run_all_notebooks.py [--tier 8gb|16gb] [--output-dir DIR] [name ...]
Sets WORKSHOP_AUTO_APPROVE=1 so the tool approval gate does not block.
With --output-dir the executed notebook is written to DIR/<name>.ipynb and the notebook at the root is left untouched;
the copy's first Markdown cell gets a note naming the tier, model, date and Ollama version of the run.
"""

from __future__ import annotations

import argparse
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import nbformat
from nbclient import NotebookClient

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:  # run as a file, scripts/ is sys.path[0]; the workshop package lives at the repository root
    sys.path.insert(0, str(ROOT))

from workshop.config import load_settings  # noqa: E402
from workshop.llm import _server_version  # noqa: E402

ORDER = ["00_check_setup", "01_python_and_ollama", "02_structured_output", "03_vocabulary_search", "04_rag", "05_tool_use"]


def tier_note(tier: str, model: str, day: str, version: str | None, folder: str) -> str:
    """The provenance paragraph for an executed copy outside the root, e.g. tier-8gb/04_rag.ipynb."""
    return (
        f"> Executed on the {tier.upper().replace('GB', ' GB')} tier with `{model}` on {day} (Ollama {version or 'version unknown'}). "
        f"The explanatory text is the root notebook's and was written for the 8B; the README's `{folder}` paragraph lists "
        "where this tier behaved differently."
    )


def run(name: str, timeout: int, output_dir: Path | None = None, note: str | None = None) -> float:
    path = ROOT / f"{name}.ipynb"
    nb = nbformat.read(str(path), as_version=4)
    start = time.time()
    NotebookClient(nb, timeout=timeout, kernel_name="python3", resources={"metadata": {"path": str(ROOT)}}).execute()
    if output_dir is not None:
        output_dir.mkdir(parents=True, exist_ok=True)
        path = output_dir / f"{name}.ipynb"
        if note:  # appended to the H1 cell, which must stay first
            first = next(c for c in nb.cells if c.cell_type == "markdown")
            first.source = first.source.rstrip("\n") + "\n\n" + note
    nbformat.write(nb, str(path))
    return time.time() - start


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tier", default="16gb", choices=["8gb", "16gb"])
    ap.add_argument("--timeout", type=int, default=900)
    ap.add_argument("--output-dir", type=Path, default=None, help="write executed notebooks here instead of in place")
    ap.add_argument("names", nargs="*")
    args = ap.parse_args()
    os.environ["WORKSHOP_AUTO_APPROVE"] = "1"
    os.environ["WORKSHOP_TIER"] = args.tier
    note = None
    if args.output_dir is not None:
        settings = load_settings()
        day = datetime.now(timezone.utc).date().isoformat()
        note = tier_note(args.tier, settings.model, day, _server_version(settings.host), args.output_dir.name)
    failures = 0
    for name in args.names or ORDER:
        try:
            secs = run(name, args.timeout, args.output_dir, note)
            print(f"ok   {name} ({secs:.0f} s)")
        except Exception as exc:  # report and continue so one failure does not hide the rest
            failures += 1
            print(f"FAIL {name}: {type(exc).__name__}: {str(exc)[:300]}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
