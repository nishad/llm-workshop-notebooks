# Getting started with local LLMs: workshop notebooks (SWIB26, 16 November 2026)

This repository holds the notebooks, helper code and data for the SWIB26 workshop "Getting started with local LLMs". You run an open model on your own laptop and use it for library tasks. You extract records from catalogue cards into a fixed format (structured output). You search vocabularies with embeddings, which are lists of numbers that represent the meaning of a text. You answer questions from documents with retrieval-augmented generation (RAG), and you let the model propose lookups that you approve, correct or refuse (tool use with a human in the loop). Nothing leaves your machine.

The workshop page is https://llm-workshop.thalhath.org/v3/. The setup steps, the times and the Zoom details are on https://llm-workshop.thalhath.org/v3/before-you-start/. Questions go to the SWIB26 forum topic: https://forum.swib.org/t/getting-started-with-local-llms/1732.

## Setup (20-30 minutes)

1. Install Ollama 0.40 or newer. The install page on the workshop site has the steps for macOS, Windows and Linux. We built and tested the materials with Ollama 0.40.4 on 15 October 2026.
2. Download the models for your machine (Ollama calls this a pull):

   | Your laptop | Command | Download |
   | --- | --- | --- |
   | 16 GB of memory or more | `ollama pull thalhath/apertus:8b` | 5.1 GB |
   | 8 GB of memory | `ollama pull thalhath/apertus:4b` | 2.4 GB |
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

4. Clone this repository, install the packages and open the first notebook. uv installs Python 3.12 for you if needed. Windows does not come with git: install [Git for Windows](https://git-scm.com/download/win), or click the green Code button on GitHub, choose Download ZIP and unpack the folder. On macOS, the first time you run `git`, the system offers to install its command line tools.

   ```bash
   git clone https://github.com/nishad/llm-workshop-notebooks.git
   cd llm-workshop-notebooks
   uv sync
   uv run jupyter lab
   ```

   Open `00_check_setup.ipynb` and run all cells. Every line should show a check mark. If one does not, see [TROUBLESHOOTING.md](TROUBLESHOOTING.md).

5. Download the two prebuilt vocabulary index files for notebook 03 from the GitHub release https://github.com/nishad/llm-workshop-notebooks/releases/tag/swib26 (the same links are in step 4, sub-step 5 of the workshop's Before you start page, https://llm-workshop.thalhath.org/v3/before-you-start/). Put the files in the `runs/` folder of the repository; create the folder if it does not exist:

   | File | Size | sha256 |
   | --- | --- | --- |
   | `stw-de-labels.sqlite` | 85.7 MB | `d85108cd6d38b949ac6c80decbf405021a61a7db4670495b2dea4e63807559bf` |
   | `unesco-en-labels.sqlite` | 34.4 MB | `47728635aff8bd8fb9d19197c34d1f1e5e05efea039bd9429bbfa4448ddda537` |

   Check a file with `shasum -a 256 runs/stw-de-labels.sqlite` (macOS and Linux) or `Get-FileHash runs\stw-de-labels.sqlite` (Windows PowerShell). Building the two indexes yourself takes about seven minutes for both (about five for STW, two for UNESCO) on an Apple Silicon Mac with 64 GB, and far longer on a CPU-only laptop. On an 8 GB machine, download the files so that you can follow notebook 03 without waiting for the build.

If you prefer pip to uv, use Python 3.12 or 3.13:

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
jupyter lab
```

You need about 20 GB of free disk space and a stable internet connection for the downloads.

## The notebooks

| Notebook | What you do |
| --- | --- |
| `00_check_setup.ipynb` | Check Python, memory, disk, Ollama, both models and one smoke call each |
| `01_python_and_ollama.ipynb` | Chat, system prompts, temperature, streaming, the OpenAI client, provenance logging |
| `02_structured_output.ipynb` | Extract catalogue card records into a Pydantic schema, validate them, measure against a gold file |
| `03_vocabulary_search.ipynb` | Embeddings, cross-lingual search over STW and UNESCO labels, a sqlite-vec index |
| `04_rag.ipynb` | Chunk documents, retrieve, answer with numbered citations, hit the context limit on purpose |
| `05_tool_use.ipynb` | Let the model propose GND, Wikidata and SPARQL calls; approve, correct or refuse each one |

The six notebooks are saved with their outputs from the 16 GB tier (`thalhath/apertus:8b` on a machine with 16 GB of memory or more). The folder `tier-8gb/` holds notebooks 04 and 05 as run on the 8 GB tier (`thalhath/apertus:4b`), so a reader with a smaller machine can see what to expect. In that run (15 October 2026, Ollama 0.40.4) the 4B behaved differently in three ways. In notebook 04 it answered every question in 04.05, 04.06 and 04.08 with only a citation, such as `[3]`, or only a term, such as "Date (http://purl.org/dc/terms/date)" for the `dcterms:issued` question. This includes the Nobel Prize question in 04.06, where the 8B said "The documents do not answer the question". In 04.07 the cell printed "Ollama accepted the long prompt" while the same cell with the 8B had returned an HTTP 400 error. Ollama's server log shows that the server cut the prompt silently from 5,076 to 2,051 tokens. In 05.06, when asked to answer from memory, it first declined and named the `search_gnd` tool, which triggered the tool loop's single reminder. It then invented "100000000000000000000000 Arendt, Hannah", which the loop marked `[UNVERIFIED: 100000000000000000000000 did not come from any tool result.]`.

Tiers. A machine with 8 GB runs the same notebooks with the 4B model: set `WORKSHOP_TIER=8gb` before you start JupyterLab. RAG then retrieves fewer chunks, because the 4B's context window is 4,096 tokens. Tool use needs the `thalhath/apertus:4b` tag, which carries the wrapper template that tool calls need.

```bash
# macOS / Linux
WORKSHOP_TIER=8gb uv run jupyter lab
```

```powershell
# Windows PowerShell
$env:WORKSHOP_TIER = "8gb"; uv run jupyter lab
```

Prebuilt vocabulary indexes. Notebook 03 builds two label indexes: `runs/stw-de-labels.sqlite`, with about 20,000 STW labels, and `runs/unesco-en-labels.sqlite`. When the files already exist, the notebook loads them instead of building them. Step 5 under "Setup" says where to download them.

## During the workshop

- The Zoom link is in the event block of the forum topic (https://forum.swib.org/t/getting-started-with-local-llms/1732). The room opens at 03:30 UTC; the session runs 04:00-08:00 UTC on Monday 16 November 2026.
- Questions: ask in the Zoom chat during the session, or in the forum topic (https://forum.swib.org/t/getting-started-with-local-llms/1732) at any time.
- Run cells from top to bottom. The Checkpoint cell at the end of each notebook tells you where you should be.

## Afterwards

Every notebook is saved with its outputs, so you can read it without running anything. Every chat call through `workshop.llm.chat` appends a line to `runs/log.jsonl`. The RAG helper, the tool loop and the setup check's smoke calls (short test calls) all go through this function. Each line records the time, the model, its digest (a hash that identifies the exact model), the options, the last 300 characters of the prompt and the first 300 characters of the answer. Streamed calls log the request only. The log lets you trace each result to the exact model that produced it. Two calls skip the helper on purpose and are not logged: the OpenAI client in 01.06 and the oversized prompt in 04.07. Embedding calls are not logged either.

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

We build the `thalhath/apertus` tags from the Modelfiles in `models/` with `models/publish.sh`. See [models/README.md](models/README.md) for the base files, templates and verification results.

## Troubleshooting and cheat sheet

- [TROUBLESHOOTING.md](TROUBLESHOOTING.md): symptoms, causes and fixes
- [CHEAT_SHEET.md](CHEAT_SHEET.md): commands and code patterns to keep open while you work through the notebooks

## Author

Nishad Thalhath, ORCID [0000-0001-9845-9714](https://orcid.org/0000-0001-9845-9714).
