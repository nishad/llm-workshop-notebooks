TITLE = "00 · Check your setup"
CELLS = [
    ("md", """# 00 · Check your setup ⏱️ 10 minutes

Run this notebook before Part 2 (and again at the start of Part 2). It checks Python, memory, disk, the Ollama server,
the workshop model tags and the embedding model, and makes one small chat call and one tool call.

**What you'll learn**
1. Whether your machine is ready for the exercises
2. Which hardware tier you are on (8 GB or 16 GB) and which model tag that means
3. What to paste when you ask for help"""),
    ("md", """## 00.01 Configuration

Every notebook starts with this cell. Change `WORKSHOP_TIER` to `8gb` if your laptop has 8 GB of memory;
the model switches to `nishad/apertus:4b` automatically. Nothing else needs editing."""),
    ("code", """import os
os.environ.setdefault("WORKSHOP_TIER", "16gb")   # "8gb" or "16gb"

from workshop.config import load_settings
settings = load_settings()
print(f"Tier: {settings.tier}   Model: {settings.model}   Embeddings: {settings.embed_model}   Host: {settings.host}")"""),
    ("md", """## 00.02 Run the checks

Green lines are fine. For a red line, follow the hint in the message, then run the cell again."""),
    ("code", """from workshop.check import run_all, print_report
ok = print_report(run_all(settings))"""),
    ("md", """## 00.03 What exactly am I running?

This is the provenance record the other notebooks attach to their results: the model tag, its digest (a fingerprint of the
exact weights and template), the quantization and the Ollama version. Two people with the same digest and the same options
get the same answer at temperature 0."""),
    ("code", """import json
from workshop.llm import provenance
print(json.dumps(provenance(settings.model), indent=2))"""),
    ("md", """## 00.04 If something is red

- **Ollama reachable: ❌** Start the Ollama app (or `ollama serve` on Linux). The checks need `http://localhost:11434`.
- **Ollama 0.40 or newer: ❌** Update the Ollama app (menu bar icon → Restart to update, or download it again from ollama.com), then run the checks again.
- **Model not found:** run `ollama pull nishad/apertus:8b` (16 GB) or `ollama pull nishad/apertus:4b` (8 GB) in a terminal, then re-run.
- **Chat template unexpected:** you have a different Apertus build. Pull the tag above; tool calls only work with it.
- **Embedding model missing:** `ollama pull bge-m3`.
- **Smoke tool call ❌ on the 4B:** expected to be slower; wait for it, and if it still fails re-pull `nishad/apertus:4b`.

When asking for help in the shared document, paste the output of the next cell."""),
    ("code", """import platform, sys
print("Python", sys.version.split()[0], "on", platform.platform())
print("Tier", settings.tier, "model", settings.model)
if ok:
    print("All checks passed.")"""),
    ("md", """## ✅ Checkpoint

You have a working Python environment, Ollama answers on your machine, the workshop model and the embedding model are
present, and you know your tier. Continue with `01_python_and_ollama.ipynb`."""),
]
