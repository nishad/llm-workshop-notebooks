# Troubleshooting

Find your symptom below, check the likely causes and apply the fix. Commands are for macOS and Linux first, then Windows PowerShell. If nothing helps, see "Asking for help" at the end.

## Ollama is not reachable

Symptom: `Connection refused`, `Failed to connect to Ollama`, or a failed check in notebook 00.

Causes: the app is not running, or another program is using port 11434.

macOS and Linux:

```bash
curl http://localhost:11434/api/version
systemctl status ollama          # Linux only
```

Windows PowerShell:

```powershell
Invoke-RestMethod http://localhost:11434/api/version
```

Fix: start the Ollama app (macOS menu bar, Windows system tray) or run `ollama serve` in a terminal. If the port is in use, start the server on another port and keep it reachable from this machine only (never open it to a shared network):

```bash
OLLAMA_HOST=127.0.0.1:11435 ollama serve
```

```powershell
$env:OLLAMA_HOST = "127.0.0.1:11435"; ollama serve
```

Then start JupyterLab from a terminal where `OLLAMA_HOST=http://127.0.0.1:11435` is set, so the notebooks use the same address.

```bash
# macOS / Linux
export OLLAMA_HOST=http://127.0.0.1:11435
```

```powershell
# Windows PowerShell
$env:OLLAMA_HOST = "http://127.0.0.1:11435"
```

Every `ollama pull`, `ollama run` and notebook started from that terminal then talks to the server on the new port.

## Model not found or wrong tag

Symptom: `model "..." not found`, or notebook 00 reports a missing model.

The valid tags are `nishad/apertus:8b`, `nishad/apertus:4b` and `qwen3-embedding:0.6b`.

```bash
ollama list
ollama pull nishad/apertus:8b
```

If you type only `apertus` in the Ollama app's model picker, it says "No models found". Type the full tag `nishad/apertus:8b` and let it download.

## Tool calls come back as text or never appear

Symptom: the model prints something like `[search_gnd(...)]` instead of proposing a call, or answers without calling a tool.

Causes: the wrong chat template (the format the model expects around each message), a prompt written in German, or a tag someone else published instead of the workshop tag.

```bash
ollama show nishad/apertus:8b --template | head -1
```

```powershell
ollama show nishad/apertus:8b --template | Select-Object -First 1
```

The first line must be `{# Unsloth template fixes #}`. For the 4B, `ollama show nishad/apertus:4b --template | grep -c "Tool Capabilities"` must print `1`. If either check fails, pull the tag again. If the template is right, write your prompt in English; the 8B misses tool calls more often in German prompts. Do not combine `tools` with `format` in one request.

## `exceeds the available context size` (HTTP 400)

Symptom: `the request exceeds the available context size` when asking a question over documents.

Cause: the prompt is longer than `num_ctx`, the context window size set for the model. Notebook 04 triggers this on purpose.

Fix: lower `k`, the number of chunks retrieved, or lower the chunk `size`. Keep the prompt under 75% of `num_ctx`. The 8B uses 8,192 tokens; the 4B cannot go above 4,096, so raising `num_ctx` for it does not help.

## Slow answers or a swapping machine

Symptom: a few tokens per second, a frozen laptop, a noisy fan.

```bash
ollama ps
```

Look at the PROCESSOR column. `100% GPU` is best. A CPU percentage means part of the model runs on the CPU, which is slower. Try these fixes in order:

1. Close browsers and other large apps.
2. On an 8 GB machine use `nishad/apertus:4b` and `WORKSHOP_TIER=8gb`.
3. Stop other loaded models with `ollama stop <tag>`.
4. Set `OLLAMA_KV_CACHE_TYPE=q8_0` before `ollama serve`; it roughly halves the memory the context needs. The Ollama server reads this environment variable, so you must set it where the server can see it. The macOS app reads variables set with `launchctl setenv`. The Windows app reads user environment variables after a restart. On Linux, put it in the systemd unit. You can also quit the app and start `ollama serve` from a terminal where the variable is set. Do not use `q4_0` with Apertus.

Windows machines with only an integrated GPU run the model on the CPU. This is normal, but slower.

## Disk full

macOS and Linux:

```bash
df -h
```

Windows PowerShell:

```powershell
Get-PSDrive -PSProvider FileSystem
```

Remove a model you do not need with `ollama rm <tag>`. Do not delete Ollama's model folders yourself; the app keeps track of them.

## Python and Jupyter

**`uv sync` fails.** Update uv (`uv self update`), check your connection, and run it from the repository folder. uv installs Python 3.12 itself; you do not need to install it first.

**The notebook uses the wrong kernel.** Register this environment and pick `swib26` in the kernel menu:

```bash
uv run python -m ipykernel install --user --name swib26
```

**`ModuleNotFoundError: workshop`.** JupyterLab was started outside the repository. Close it, `cd` into the repository folder and run `uv run jupyter lab`.

**`UnicodeDecodeError` on Windows.** Windows uses an older text encoding by default. Every file the workshop code opens uses `encoding="utf-8"`; do the same in your own code: `open(path, encoding="utf-8")` or `Path(path).read_text(encoding="utf-8")`.

**`enable_load_extension` is missing.** You are running the Python that came with your operating system, and its sqlite3 module was built without support for loading extensions. Use the Python that uv installs: `uv run jupyter lab`.

## Embedding dimension mismatch

Symptom: `Expected 1024, got 768` (or similar numbers) when searching or loading an index.

Cause: the index was built with one embedding model and the query uses another. Vectors from different models cannot be compared.

Fix: use one model for both. Check `WORKSHOP_EMBED_MODEL` and delete the old file in `runs/` (for example `runs/stw-de-labels.sqlite`). Then either rebuild the index or download the prebuilt one from the GitHub release, https://github.com/nishad/llm-workshop-notebooks/releases/tag/swib26 (also linked in step 4, sub-step 5 of the workshop's Before you start page, https://llm-workshop.thalhath.org/v3/before-you-start/). The README section "Setup" has the checksums.

## Embedding model missing

Symptom: notebook 00 or 03 reports that `qwen3-embedding:0.6b` is not installed.

```bash
ollama pull qwen3-embedding:0.6b
```

## LM Studio (Part 1 only)

We use LM Studio only for the Part 1 demonstrations; the notebooks need Ollama.

- Download the classic LM Studio app from the official site, not the Bionic edition.
- "Failed to load the model": pick a smaller build or lower the context length in the model settings.
- LM Studio does not support Intel Macs. Use Ollama.

## Network and proxies

If your network uses a proxy, set it before you start JupyterLab:

```bash
export HTTPS_PROXY=http://proxy.example.org:3128
```

```powershell
$env:HTTPS_PROXY = "http://proxy.example.org:3128"
```

When the tools cannot reach GND, Wikidata or the SPARQL endpoints, they use recorded sample responses (fixtures) instead and mark the result with `"fixture": true`. Treat those results as examples, not live data. A Wikidata 403 error means the request carried a generic User-Agent header; the workshop helpers send their own User-Agent header.

## Asking for help

Post in the SWIB26 forum topic (https://forum.swib.org/t/getting-started-with-local-llms/1732) and include:

1. The output of the last cell of `00_check_setup.ipynb`.
2. The exact error text.
3. Which notebook and which cell.
4. Your operating system and memory.

## Emergency reset

This is safe and removes no models:

```bash
ollama stop nishad/apertus:8b
```

Then restart the Ollama app, run `uv sync --reinstall` in the repository folder, and restart the notebook kernel.
