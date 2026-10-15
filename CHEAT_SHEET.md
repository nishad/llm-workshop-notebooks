# Cheat sheet: getting started with local LLMs (SWIB26)

Commands and code patterns from the notebooks. For errors see [TROUBLESHOOTING.md](TROUBLESHOOTING.md).

## Ollama CLI

```bash
ollama list                                  # installed models, with sizes
ollama pull nishad/apertus:8b                # download (4b for 8 GB machines)
ollama run nishad/apertus:8b --verbose       # chat; read "eval rate" for tokens per second
ollama ps                                    # loaded models: SIZE, PROCESSOR, CONTEXT
ollama show nishad/apertus:8b                # parameters, quantization, context length, capabilities
ollama rm nishad/apertus:8b                  # remove a model
ollama stop nishad/apertus:8b                # unload from memory
```

Inside `ollama run`:

```text
/set system You are a cataloguing assistant. Be brief.
/set parameter temperature 0
/set parameter num_ctx 8192
/save mytag
/bye
```

## Python with the `ollama` package

```python
import ollama
client = ollama.Client(host="http://localhost:11434")

response = client.chat(
    model="nishad/apertus:8b",
    messages=[{"role": "user", "content": "What is an authority file?"}],
    options={"temperature": 0, "num_ctx": 8192},
)
print(response.message.content)          # dict access also works: response["message"]["content"]
```

Streaming:

```python
for part in client.chat(model="nishad/apertus:8b", messages=messages, stream=True):
    print(part.message.content, end="", flush=True)
```

Embeddings, model details and the list of installed models:

```python
vectors = client.embed(model="qwen3-embedding:0.6b", input=["Kinderzulage", "family allowance"]).embeddings
info = client.show("nishad/apertus:8b")
print(info.details.parameter_size, info.details.quantization_level, info.modelinfo)
for m in client.list().models:
    print(m.model, m.digest[:12])
```

The workshop wrapper sets temperature 0 and the right `num_ctx` for your tier:

```python
from workshop.llm import chat
response = chat(messages, model="nishad/apertus:8b")
```

## Structured output

The `Record` model from notebook 02. Plain strings with `max_length`, an empty string when the card is silent, fields in imprint order:

```python
from typing import Literal
from pydantic import BaseModel, Field, ValidationError

INSTRUCTIONS = "Extract the bibliographic record from this catalogue card into the JSON schema. Copy each value as written; use an empty string for a field the card does not state."
card_text = open("data/cards/card-01.txt", encoding="utf-8").read()

class Record(BaseModel):
    title: str = Field(max_length=200, description="Title proper as written on the card: the part before any ' : ' subtitle, without statement of responsibility")
    creators: list[str] = Field(max_length=6, description="Persons or bodies responsible, as written, surname first")
    place: str = Field(max_length=60, description="Place of publication, the part before the colon in the imprint line; empty string if the imprint has no place. Never guess it from the publisher")
    publisher: str = Field(max_length=100, description="Publisher name only, the part between the colon and the comma in the imprint line; empty string if absent")
    date: str = Field(max_length=20, description="Year of publication as written, for example 1774; empty string if the card says o.J. or s.d. or gives no year")
    language: Literal["de", "en", "fr", "it", "es", "ja", "other"] = Field(description="Language of the work")
    identifier: str = Field(max_length=60, description="ISBN or DOI if the card has one, digits and hyphens only (no 'ISBN' or 'doi:' prefix); empty string if none")

response = chat(
    [{"role": "user", "content": f"{INSTRUCTIONS}\n\nCard:\n{card_text}"}],
    model="nishad/apertus:8b", format=Record.model_json_schema(), options={"num_predict": 300},
)
try:
    record = Record.model_validate_json(response.message.content)
except ValidationError as err:
    print(err.errors()[0]["msg"])
```

Why plain strings and `num_predict`: with `Optional` fields and `null`, the 8B emits null for every optional field and runs away in the first free-text field. The ceiling of 300 tokens stops a runaway answer.

The grammar guarantees well-formed JSON with the right keys and types, not true values. Add validators for what you know about your data.

The same through the OpenAI client:

```python
from openai import OpenAI
oa = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
completion = oa.chat.completions.parse(model="nishad/apertus:8b", messages=messages, response_format=Record)
record = completion.choices[0].message.parsed
```

## Tools

A tool is a plain function. The docstring is the description the model sees:

```python
def search_gnd(name: str, type: str = "Person") -> str:
    """Look up a name in the GND authority file via lobid-gnd.

    Args:
        name: the person, organization or subject to search for
        type: GND entity type, one of Person, CorporateBody, SubjectHeading, PlaceOrGeographicName, Work
    """
```

```python
response = client.chat(model="nishad/apertus:8b", messages=messages, tools=[search_gnd])
call = response.message.tool_calls[0]
name, arguments = call.function.name, call.function.arguments
result = search_gnd(**arguments)           # after you have approved the call
messages.append(response.message)
messages.append({"role": "tool", "tool_name": name, "content": result})
```

Rules:

- Never combine `tools` with `format` in one request. Ollama then returns the call as plain JSON.
- Never send `think` to Apertus.
- Ask for tool use in English; the 8B misses tool calls in German prompts more often.

The workshop loop does the bookkeeping:

```python
from workshop.tools import run_tool_loop, TOOLS
out = run_tool_loop(messages, TOOLS, model="nishad/apertus:8b")
```

`workshop.tools.run_tool_loop` runs one tool call per turn, marks identifiers no tool returned as `[UNVERIFIED ...]`, and reminds the model once when it announces a call or says nothing. `search_gnd` results carry a bare `gnd` field next to lobid's URL id.

## Embeddings and search

```python
from workshop.embed import embed
from workshop.search import build_index, search, save_index, load_index

docs = embed(["Kinderzulage", "Familienleistungsausgleich"], "document")    # unit vectors
query = embed(["Geld für Kinder"], "query")
scores = docs @ query[0]                                                    # dot product = cosine

index = build_index(ids, texts)          # uses WORKSHOP_EMBED_MODEL (qwen3-embedding:0.6b)
for entry_id, text, score in search("Geld für Kinder", index, k=5):
    print(score, entry_id, text)
```

Index and query must use the same model. Prefixes by model (`workshop.embed.prefix_for` adds them):

| Model | Query prefix | Document prefix |
| --- | --- | --- |
| qwen3-embedding (default) | `Instruct: <task>` then `Query:` | none |
| bge-m3 | none | none |
| nomic-embed-text | `search_query: ` | `search_document: ` |
| embeddinggemma | `task: search result \| query: ` | `title: none \| text: ` |

Prebuilt index files for notebook 03 (`runs/stw-de-labels.sqlite`, `runs/unesco-en-labels.sqlite`) will be offered on the workshop page shortly before the session; put them in `runs/`. Building them yourself takes a few minutes on Apple Silicon and much longer on a CPU-only laptop.

## RAG

```python
from workshop.rag import load_document, chunk_text, build_prompt, answer

chunks = chunk_text(load_document("data/docs/dcmi-terms.md"), "dcmi-terms", size=300, overlap=50)   # size in words
by_id = {c.id: c for c in chunks}
index = build_index([c.id for c in chunks], [c.text for c in chunks])
text, used = answer("Which DCMI term expresses the date a resource was issued?", index, by_id, k=4)
```

Budget rule: keep the prompt under 75% of `num_ctx`. `build_prompt` raises `PromptTooLong` otherwise. Look at the retrieved chunks before you read the answer.

## OpenAI client against local servers

```python
from openai import OpenAI
oa = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")    # the key is required but ignored
```

| Server | Base URL |
| --- | --- |
| Ollama | `http://localhost:11434/v1` |
| LM Studio | `http://localhost:1234/v1` |
| llama-server (llama.cpp) | `http://localhost:8080/v1` |
| Llama app | `http://localhost:9931/v1` |

## Memory and speed

Measured in October 2026 on an Apple Silicon laptop with the research footprint script: the 8B Q4_K_M build sits at about 5.4 GB with a 4k context and 6.3 GB with 8k. The KV cache alone is 128 KiB per token (0.5 GiB per 4k tokens; `OLLAMA_KV_CACHE_TYPE=q8_0` halves it); the rest of the growth is compute buffers. The 4B takes about 2.8 GB. Tokens per second are community-reported ranges, not measurements made here: base Apple chips 14 to 24 for the 8B, Pro and Max chips 40 or more, CPU-only laptops 3 to 14.

## Glossary

- **Token**: a piece of a word; models read and write tokens, not letters.
- **Context window (`num_ctx`)**: how many tokens the model sees at once, prompt plus answer.
- **Temperature**: randomness of sampling; 0 is repeatable.
- **Quantization (Q4_K_M)**: weights stored in about 4 bits to save memory.
- **GGUF**: the file format Ollama and llama.cpp load.
- **System prompt**: the instruction that sets the model's role.
- **Embedding**: a vector that places a text in a space where similar meanings are close.
- **Cosine similarity**: closeness of two vectors; a dot product for unit vectors.
- **Chunk**: a piece of a document small enough to retrieve and fit in a prompt.
- **RAG**: retrieve passages, put them in the prompt, answer from them with citations.
- **Grammar-enforced output**: decoding constrained to a JSON schema.
- **Tool call**: the model asking your program to run a function; you decide whether it runs.

## Quick fixes

| Symptom | Try |
| --- | --- |
| Connection refused | Start the Ollama app; `curl http://localhost:11434/api/version` |
| Model not found | `ollama pull nishad/apertus:8b` (type the full tag) |
| Very slow | `ollama ps`: if PROCESSOR shows CPU, close other apps or use the 4B |
| `exceeds the available context size` | Lower `k` or chunk `size`; the 4B tops out at 4,096 tokens |
| Tool call appears as text | `ollama show nishad/apertus:8b --template \| head -1` must print `{# Unsloth template fixes #}` |
| `ModuleNotFoundError: workshop` | Start JupyterLab from the repository folder: `uv run jupyter lab` |
| Embedding size mismatch | Rebuild the index with the model you query with |

---

Tested with Ollama 0.35.1, ollama-python 0.6.3, pydantic 2.14.1, Python 3.12.12 on 2026-10-15.
