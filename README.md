# Getting started with local LLMs: workshop notebooks (SWIB26, 16 November 2026)

This repository holds the notebooks, helper code and data for the SWIB26 workshop "Getting started with local LLMs". You run an open model on your own laptop and use it for library tasks: structured extraction from catalogue cards, vocabulary search with embeddings, retrieval-augmented generation (RAG) and tool use with a human in the loop. Nothing leaves your machine.

The workshop page is https://llm-workshop.thalhath.org/v3/. Questions and announcements go to the SWIB26 forum topic: https://forum.swib.org/t/getting-started-with-local-llms/1732.

## Before the workshop (20-30 minutes)

1. Install Ollama 0.40.1 or newer. The install page on the workshop site has the steps for macOS, Windows and Linux. The materials were built on Ollama 0.35.1 and are re-verified on 0.40 before the workshop.
2. Pull the model for your machine:

   | Your laptop | Command | Download |
   | --- | --- | --- |
   | 16 GB of memory or more | `ollama pull nishad/apertus:8b` | 5.1 GB |
   | 8 GB of memory | `ollama pull nishad/apertus:4b` | 2.4 GB |
   | everyone | `ollama pull qwen3-embedding:0.6b` | 639 MB |

3. Install [uv](https://docs.astral.sh/uv/).

   macOS and Linux:

   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

   Windows PowerShell:

   ```powershell
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

4. Clone this repository, install the packages and open the first notebook. uv installs Python 3.12 for you if needed.

   ```bash
   git clone https://github.com/nishad/llm-workshop-notebooks.git
   cd llm-workshop-notebooks
   uv sync
   uv run jupyter lab
   ```

   Open `00_check_setup.ipynb` and run all cells. Every line should show a check mark. If one does not, see [TROUBLESHOOTING.md](TROUBLESHOOTING.md).

5. Download the two prebuilt vocabulary index files for notebook 03 from the link in the download post on the forum topic (https://forum.swib.org/t/getting-started-with-local-llms/1732) into the `runs/` folder of the repository (create it if it does not exist):

   | File | Size | sha256 |
   | --- | --- | --- |
   | `stw-de-labels.sqlite` | 85.7 MB | `5d89c6704268b0c0ae29656dcfc31ea3d1402469edbd76f80a043f1843b07e8c` |
   | `unesco-en-labels.sqlite` | 34.4 MB | `c4755d17a9c00c742f9f2b601e82e51165f69d5380395adaa083a7ea43ae10c7` |

   Check a file with `shasum -a 256 runs/stw-de-labels.sqlite` (macOS and Linux) or `Get-FileHash runs\stw-de-labels.sqlite` (Windows PowerShell). Building the two indexes takes about five minutes on an Apple Silicon Mac with 64 GB and far longer on a CPU-only laptop, so on the 8 GB tier downloading them is the way to follow notebook 03 live.

If you prefer pip, with Python 3.12 or 3.13:

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
jupyter lab
```

You need about 20 GB of free disk space and a stable connection for the downloads.

## The notebooks

| Notebook | Time | What you do |
| --- | --- | --- |
| `00_check_setup.ipynb` | 10 min | Check Python, memory, disk, Ollama, both models and one smoke call each |
| `01_python_and_ollama.ipynb` | 20 min | Chat, system prompts, temperature, streaming, the OpenAI client, provenance logging |
| `02_structured_output.ipynb` | 25 min | Extract catalogue card records into a Pydantic schema, validate them, measure against a gold file |
| `03_vocabulary_search.ipynb` | 25 min | Embeddings, cross-lingual search over STW and UNESCO labels, a sqlite-vec index |
| `04_rag.ipynb` | 20 min | Chunk documents, retrieve, answer with numbered citations, hit the context limit on purpose |
| `05_tool_use.ipynb` | 15 min | Let the model propose GND, Wikidata and SPARQL calls; approve, correct or refuse each one |

The six notebooks are committed with outputs from the 16 GB tier (`nishad/apertus:8b`). `tier-8gb/` holds notebooks 04 and 05 as executed on the 8 GB tier (`nishad/apertus:4b`), so a reader on a smaller machine can see what to expect. In that run (15 October 2026, Ollama 0.35.1) the 4B behaved differently in three places. In 04.06 it did not refuse the Nobel Prize question but answered with a bare citation, `[2]`, where the 8B said "The documents do not answer the question". In 04.07 the cell printed "Ollama accepted the long prompt" instead of the 8B's HTTP 400; Ollama's server log shows the prompt cut silently from 5,076 to 2,051 tokens. In 05.06, asked to answer from memory, it invented "100000000000000000000000 Arendt, Hannah", which the loop marked `[UNVERIFIED: 100000000000000000000000 did not come from any tool result.]`.

Tiers. A machine with 8 GB runs the same notebooks with the 4B model: set `WORKSHOP_TIER=8gb` before starting JupyterLab. RAG then retrieves fewer chunks (the 4B window is 4,096 tokens), and tool use needs the `nishad/apertus:4b` tag, which carries a wrapper template for tools.

```bash
# macOS / Linux
WORKSHOP_TIER=8gb uv run jupyter lab
```

```powershell
# Windows PowerShell
$env:WORKSHOP_TIER = "8gb"; uv run jupyter lab
```

Prebuilt vocabulary indexes. Notebook 03 builds two label indexes (`runs/stw-de-labels.sqlite`, about 20,000 STW labels, and `runs/unesco-en-labels.sqlite`) and loads them instead when the files exist. Step 5 under "Before the workshop" says where to download them.

## During the workshop

- The Zoom room opens at 03:30 UTC; the session runs 04:00-08:00 UTC on Monday 16 November 2026.
- Questions go to the shared document linked from the workshop page.
- Run cells from top to bottom. The Checkpoint cell at the end of each notebook tells you where you should be.

## Afterwards

Every notebook is committed with its outputs, so you can read it without running anything. Every chat call through `workshop.llm.chat`, which the RAG helper, the tool loop and the setup check's smoke calls also use, appends a line to `runs/log.jsonl` with the time, the model, its digest, the options and the first 300 characters of the prompt and of the answer, so you can trace each result to the exact model. Two calls bypass the helper on purpose and are not logged: the OpenAI client in 01.06 and the oversized prompt in 04.07. Embedding calls are not logged either.

## Helpers (`workshop/`)

| Module | What it does |
| --- | --- |
| `config` | Model, embedding model, Ollama host and hardware tier, with environment overrides |
| `check` | Readiness checks for Python, memory, disk, Ollama, models and one smoke call each |
| `llm` | A thin wrapper around `ollama.chat` with temperature 0, the tier's `num_ctx` and provenance logging |
| `embed` | Embeddings through Ollama, with the query and document prefix each model expects |
| `search` | Semantic search as a dot product over unit vectors, with optional sqlite-vec persistence |
| `rag` | Load, chunk, retrieve, build the prompt and answer, without a framework |
| `tools` | GND, Wikidata and read-only SPARQL tools, and the approve-and-run loop |
| `display` | Markdown and table rendering for notebooks |

## Data and licences

Sources, licences and retrieval dates for every data file are in [data/ATTRIBUTION.md](data/ATTRIBUTION.md).

- Code: MIT (see [LICENSE](LICENSE)).
- Vocabularies: STW under CC BY 4.0, UNESCO Thesaurus under CC BY-SA 3.0 IGO.
- Documents and catalogue cards: CC BY 4.0.
- Model weights: Apache-2.0, with the Apertus LLM Acceptable Use Policy.

## Rebuilding the model tags

The `nishad/apertus` tags are built from the Modelfiles in `models/` with `models/publish.sh`. See [models/README.md](models/README.md) for the base files, templates and verification results.

## Troubleshooting and cheat sheet

- [TROUBLESHOOTING.md](TROUBLESHOOTING.md): symptoms, causes and fixes
- [CHEAT_SHEET.md](CHEAT_SHEET.md): commands and code patterns to keep open during the session

## Author

Nishad Thalhath, ORCID [0000-0001-9845-9714](https://orcid.org/0000-0001-9845-9714).
