"""Capture a model answer for the website with a provenance line.

Usage: uv run python scripts/capture.py "Prompt text" [--model thalhath/apertus:8b] [--system "..."] [--temperature 0.8] [--runs 1]
Prints a Markdown block ready to paste into a page.
"""

from __future__ import annotations

import argparse
from datetime import date

from workshop.llm import chat, provenance


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("prompt")
    ap.add_argument("--model", default=None)
    ap.add_argument("--system", default=None)
    ap.add_argument("--temperature", type=float, default=0.0)
    ap.add_argument("--runs", type=int, default=1)
    args = ap.parse_args()
    messages = ([{"role": "system", "content": args.system}] if args.system else []) + [{"role": "user", "content": args.prompt}]
    prov = provenance(args.model)
    for i in range(args.runs):
        r = chat(messages, model=args.model, options={"temperature": args.temperature, "seed": 42 + i})
        print(f"**Prompt:**\n\n```\n{args.prompt}\n```\n")
        print(f"**Output** (captured with {prov['model']}, digest {str(prov['digest'])[:12]}, temperature {args.temperature}, {date.today():%d %B %Y}):\n")
        print("```\n" + (r.message.content or "").strip() + "\n```\n")


if __name__ == "__main__":
    main()
