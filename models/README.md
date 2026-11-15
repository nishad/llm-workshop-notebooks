# Workshop models: `thalhath/apertus`

The Modelfiles and publish script for the Ollama tags the workshop uses. Pushing to ollama.com needs the key of the account that owns the tags: `PUSH=1 models/publish.sh`. A plain `models/publish.sh` is a dry run that only pulls and builds locally.

## Tags

| Tag | Base GGUF | GGUF sha256 | Template origin | num_ctx | Digest (`ollama list`) |
| --- | --- | --- | --- | --- | --- |
| `thalhath/apertus:8b` (also `:latest`) | `hf.co/unsloth/Apertus-8B-Instruct-2509-GGUF:Q4_K_M` | `87e7f0eb5a1d33e1a8ea4e7fdd2363764e0465061dd92962e0073aec31a7944d` | GGUF's own template with Unsloth's tool-argument fixes (kept, no `TEMPLATE` line) | 8192 | `4a85a6fea0b8` |
| `thalhath/apertus:4b` | `hf.co/jondale/Apertus-v1.1-4B-Instruct-GGUF:Q4_K_M` | not recorded in the Modelfile | Workshop wrapper template that renders tools in Apertus's TypeScript-style format so Ollama parses tool calls | 4096 | `87ca69a79aed` |
| `thalhath/apertus:8b-v1.5-preview` | `hf.co/Colby/apertus-v1.5-8b-text-Q4_K_M-GGUF:Q4_K_M` | `a037df8d87ff6caacee794ee85f55342f2152e0d359b7389033300c3bee5f299` | GGUF's own template | 8192 | `6f25f6ba0b62` |

The digest column is what `ollama list` showed on the build machine; the executed notebooks name these digests. After `ollama pull` from ollama.com, `ollama list` shows a different digest for the same model, because Ollama writes the tag's manifest differently after a pull: `61041b337fa9` for `8b` and `latest`, `0782f56ea89a` for `4b` (checked on Ollama 0.40.16, 15 November 2026). The GGUF sha256 identifies the model file itself.

All three set `temperature 0.8` and `top_p 0.9`. The 8B sets a short system prompt; the 4B wrapper template supplies its own default system prompt. The v1.5 tag is an unofficial community text-only conversion, offered as a preview only.

## Verification

Verified with Ollama **0.40.4** on 2026-10-15 (first on 0.35.1 the same morning; the counts were identical, see the repeat below). The workshop's readiness check requires Ollama 0.40 or newer. A re-verification passes when the tool prompts with structured `tool_calls` are at or above 16/20 for the 8B and 11/20 for the 4B, the rates measured on 15 October 2026.

Template and capability checks:

- `ollama show thalhath/apertus:8b --template | head -1` prints `{# Unsloth template fixes #}`; capabilities are `tools` and `completion`.
- `ollama show thalhath/apertus:4b --template | grep -c "Tool Capabilities"` prints `1`; capabilities are `completion` and `tools`.

Harness run (`scripts/tool_harness.py --only tools,controls,mt,so`, one run per model, OpenAI-compatible endpoint):

| Tag | Tool prompts with structured `tool_calls` | Controls clean | Multi-turn loops | Structured output |
| --- | --- | --- | --- | --- |
| `thalhath/apertus:8b` | 16 of 20 (2 `leak_unparsed`, 2 `no_call`) | 10 of 10 | 5 of 5 ok | 5 of 6 requests return valid JSON; the empty-enum schema returns HTTP 400 (expected) |
| `thalhath/apertus:4b` | 11 of 20 (2 `leak_unparsed`, 7 `no_call`) | 10 of 10 | 3 of 5 ok (2 `answer_mismatch`) | 5 of 6 requests return valid JSON; the empty-enum schema returns HTTP 400 (expected) |

Notes on the structured-output cases: the 8B returns `isbn: null` correctly for the biblio record; the 4B fills `isbn` with `"2 Bände"` (valid JSON, wrong value). The unsatisfiable `minimum 10 / maximum 5` schema yields a number from both models rather than an error. Raw per-request results are in the research results directory (`results/tags-2026-10-15/`, in the planning folder of the workshop project, not in this repository).

### Final run 2026-10-15

Repeat of the harness (`--only tools,controls,mt,so`, same endpoint) after the notebooks and tags were final, first on Ollama 0.35.1 and again on Ollama 0.40.4 after the upgrade: both runs match the earlier table case for case (8B: 16 of 20 tool prompts, 2 leaks, 2 no-calls; 4B: 11 of 20, 2 leaks, 7 no-calls; multi-turn 5 of 5 and 3 of 5; structured output 5 of 6). Raw results: `results/final-2026-10-15/harness.jsonl` and `results/final-2026-10-15-ollama-0.40.4/harness.jsonl`, in the planning folder of the workshop project, not in this repository.

| Tag | Tool prompts with structured `tool_calls` | Controls clean | Multi-turn loops | Structured output |
| --- | --- | --- | --- | --- |
| `thalhath/apertus:8b` | 16 of 20 (2 `leak_unparsed`, 2 `no_call`) | 10 of 10 | 5 of 5 ok | 5 of 6 requests answered (HTTP 200); the empty-enum schema returns HTTP 400 (expected) |
| `thalhath/apertus:4b` | 11 of 20 (2 `leak_unparsed`, 7 `no_call`) | 10 of 10 | 3 of 5 ok (2 `answer_mismatch`) | 5 of 6 requests answered (HTTP 200); the empty-enum schema returns HTTP 400 (expected) |

On the 8 GB tier the 4B can also hit Ollama's repetition guard ("prediction aborted, token repeat limit reached") on multi-step tool prompts, so notebook 05 skips those two cells there.

## Embedding model

Default: `qwen3-embedding:0.6b` (Apache-2.0), chosen on 2026-10-15 by the gold-set evaluation (50 queries over the research corpora; one document per concept, synonym removed).

| Model (prefix mode) | recall@1 | recall@5 | MRR | Licence |
| --- | --- | --- | --- | --- |
| `bge-m3` (none) | 0.34 | 0.48 | 0.42 | MIT, dropped |
| `qwen3-embedding:0.6b` (query instruction) | 0.62 | 0.82 | 0.72 | Apache-2.0, default |
| `embeddinggemma` (prefixes) | 0.68 | 0.92 | 0.78 | Gemma Terms of Use, documented alternative |

Raw results: `scripts/eval_embeddings.py`, run on 2026-10-15.

Per-kind recall@1 for the default, from `03_vocabulary_search.ipynb` (03.07, one document per concept):

| Kind | recall@1 | recall@5 | n |
| --- | --- | --- | --- |
| `A_stw_de_alt_to_concept` | 5 | 9 | 12 |
| `B_stw_en_to_de` (cross-lingual) | 8 | 10 | 12 |
| `C_unesco_fr_to_en` (cross-lingual) | 6 | 8 | 10 |
| `D_unesco_en_to_fr` (cross-lingual) | 10 | 10 | 10 |
| `E_unesco_scopenote_to_concept` | 2 | 4 | 6 |

Label-level index (every preferred and alternative label is an entry, query label held out): kind A recall@1 8/12, recall@5 11/12; kind B recall@1 6/12, recall@5 10/12. Index design matters as much as the model.

Throughput on an M1 Max with Ollama 0.40.4: 19,688 short German labels embedded in 313 s (about 63 per second); the whole notebook runs in about 12 minutes.

## Rebuild

```
models/publish.sh                 # pull base GGUFs, build the four tags, print `ollama show` summaries
NAMESPACE=myname models/publish.sh  # build under another namespace
PUSH=1 models/publish.sh          # also push (facilitator only; needs the machine's key on ollama.com)
```

Prebuilt index files, measured on 2026-10-15 after the final re-execution on Ollama 0.40.4 (`ls -l`, `shasum -a 256`): `runs/stw-de-labels.sqlite` 85,745,664 bytes (85.7 MB), sha256 `d85108cd6d38b949ac6c80decbf405021a61a7db4670495b2dea4e63807559bf`; `runs/unesco-en-labels.sqlite` 34,385,920 bytes (34.4 MB), sha256 `47728635aff8bd8fb9d19197c34d1f1e5e05efea039bd9429bbfa4448ddda537`. The README and the cheat sheet quote these figures. After any rebuild of the index files, re-measure the sizes and checksums and update the README, the cheat sheet and the GitHub release.

## Re-checked on 15 November 2026

- Ollama PR #17555 (Apertus 1.5 parser and renderer): still open.
- llama.cpp PR #26226: still open.
- transformers PR #47662 (Apertus 1.5 model): still open.
- `ollama.com/library/apertus`: still no entry.
- The swiss-ai collection on Hugging Face: Apertus-v1.5-8B and -70B with SFT, RL, DPO and base variants, MLX builds of v1.1; still no official GGUF.
- Ollama's latest release is 0.40.16; the 0.40 floor stands. The harness run above was not repeated.
