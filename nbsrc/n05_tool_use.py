TITLE = "05 · Tool use with a human in the loop"
CELLS = [
    ("md", """# 05 · Tool use with a human in the loop ⏱️ 15 minutes

A tool call is the model asking your program to do something: look up a name in the GND, query Wikidata, run a SPARQL query.
The model only *proposes*. You approve, correct or refuse; Python executes; the result goes back to the model.

Why the gate: in the October 2026 tests the 8B called tools correctly for every English prompt but for one of nine German
prompts, and when it did not call a tool it sometimes invented a GND number. The gate turns a confident guess into a checked fact.

**What you'll learn**
1. Define tools as plain Python functions with docstrings
2. Let the model propose a call, approve or correct it, feed the result back
3. Chain two tools: GND identifier → Wikidata → Historical Dictionary of Switzerland
4. Recognise the failure modes and what the loop does about them"""),
    ("md", "## 05.01 Configuration"),
    ("code", """import os, json
os.environ.setdefault("WORKSHOP_TIER", "16gb")
from workshop.config import load_settings
settings = load_settings(); MODEL = settings.model
print("Model:", MODEL, "| tool prompts in English work best with the 8B")"""),
    ("md", """## 05.02 Three tools

The docstring is the tool's description to the model; the `Args:` lines describe the parameters. `sparql` only allows SELECT
and ASK on an allow-list of endpoints and forces a LIMIT. If the network fails, each tool returns a recorded fixture and says so."""),
    ("code", """from workshop.tools import search_gnd, wikidata_lookup, sparql, TOOLS
print(json.loads(search_gnd("Hannah Arendt", "Person"))["results"][:2])
print(json.loads(wikidata_lookup("Hannah Arendt", "en"))["results"][:1])
print(json.loads(sparql("SELECT ?item WHERE { ?item wdt:P227 '11850391X' }", "wikidata")))"""),
    ("md", """## 05.03 One proposed call, one decision

Ask in English. The model should propose `search_gnd`; the gate shows the call and waits for **y**, **n**, or corrected JSON arguments."""),
    ("code", """from workshop.tools import run_tool_loop
from workshop.display import show_markdown
messages = [{"role": "system", "content": "You are a cataloguing assistant. Use the tools to look things up; never state an identifier you did not retrieve."},
            {"role": "user", "content": "Find the GND authority record for Hannah Arendt and tell me her GND identifier."}]
out = run_tool_loop(messages, TOOLS, model=MODEL)
for m in out[len(messages):]:
    print(m["role"].upper(), "→", (m.get("content") or "")[:300], m.get("tool_calls", ""))
show_markdown(out[-1]["content"])"""),
    ("md", """## 05.04 Correcting the model

Small models misspell names in tool arguments. Run this cell, and when the gate shows the proposed call, paste corrected JSON,
for example `{"name": "Annemarie Schwarzenbach", "type": "Person"}`."""),
    ("code", """out = run_tool_loop([messages[0], {"role": "user", "content": "Look up the Swiss writer Annemarie Schwarzenbach in the GND."}], TOOLS, model=MODEL)
show_markdown(out[-1]["content"])"""),
    ("md", """## 05.05 Two tools in a row: GND → Wikidata → the Historical Dictionary of Switzerland

Wikidata links authority files: property P227 holds the GND identifier, P902 the HLS article id. One question, two tool rounds.
The loop runs one call per turn, so the second call can only be made after the first result is in.

Two-step chains are where an 8B model at this quantization gets unreliable. In the October 2026 runs it looked up the GND
record correctly every time and then stopped: it pasted the URL form of the id, or announced the second call without making
it, or answered with an empty code block. Nothing was invented, which is the point of the gate. Run the cell and see what
you get; the next cell shows how you finish the chain yourself when the model stops."""),
    ("code", """chain = [messages[0], {"role": "user", "content":
    "Find the GND identifier of Annemarie Schwarzenbach with search_gnd, then use the sparql tool on wikidata to find the item with that "
    "GND id (property wdt:P227, the bare id as a string literal) and return its HLS id (property wdt:P902). "
    "Call the tools one after the other; do not describe the steps."}]
out = run_tool_loop(chain, TOOLS, model=MODEL, max_turns=4)
for m in out[len(chain):]:
    print(m["role"].upper(), "→", (m.get("content") or "")[:300], m.get("tool_calls", ""))"""),
    ("md", """### When the model stops, you finish

The tool result is in the conversation. Take the identifier the tool returned, not one the model wrote, and run the second
step yourself. This is the same query the model was asked to write."""),
    ("code", """first = next((json.loads(m["content"]) for m in out if m["role"] == "tool"), None)
if first and first.get("results"):
    gnd = first["results"][0]["gnd"]
    print("GND from the tool result:", gnd)
    hls = json.loads(sparql(f"SELECT ?hls WHERE {{ ?item wdt:P227 '{gnd}' . ?item wdt:P902 ?hls }}", "wikidata"))
    print("HLS id:", [row["hls"] for row in hls["results"]], "(fixture)" if hls["fixture"] else "(live)")
else:
    print("No tool result in the conversation: run the 05.05 cell first.")"""),
    ("md", """## 05.06 Failure modes the loop catches

- An identifier in the answer that no tool result contained is marked `[UNVERIFIED ...]`, whether the model skipped the tools or made the number up after calling them.
- A tool call written as text (the pattern of the community Ollama tag) stops the loop with an explanation.
- A declined call becomes an error result the model sees, so it can ask you instead of guessing.
- A reply that only announces a tool call, or says nothing, gets one reminder.

Try to provoke the first one."""),
    ("code", """try:
    out = run_tool_loop([{"role": "user", "content": "What is the GND identifier of Hannah Arendt? Answer from memory, do not use tools."}], TOOLS, model=MODEL)
    show_markdown(out[-1]["content"])
except Exception as err:
    print(type(err).__name__, err)"""),
    ("md", """## 05.07 What the SPARQL guard does

Paste any query; the guard parses it and allows only SELECT or ASK, blocks federated SERVICE calls except Wikidata's label service, and caps LIMIT at 50."""),
    ("code", """from workshop.tools import validate_sparql, ToolError
for q in ["SELECT ?s WHERE { ?s ?p ?o }", "SELECT ?s WHERE { ?s ?p ?o } LIMIT 10000", "DELETE WHERE { ?s ?p ?o }"]:
    try:
        print("OK  ", validate_sparql(q).replace("\\n", " "))
    except ToolError as err:
        print("REJECTED", q, "→", err)"""),
    ("md", """## 05.08 Exercises

🔧 **Run and change:** ask 05.03 in German ("Finde den GND-Normdatensatz für Hannah Arendt"). Does the 8B still call the tool?
If not, that is the documented weakness; re-ask in English.

🔧 **Run and change:** write a question that needs `wikidata_lookup` first and `sparql` second (for example: which works by Goethe
does Wikidata list as novels, in German labels).

🚀 **Stretch:** fetch the HLS article found in 05.05 (CC BY-SA) with `requests`, chunk it with `workshop.rag.chunk_text`, index it and
ask a question about Schwarzenbach's travels. That is the full chain: authority file → knowledge graph → text → grounded answer.

🚀 **Stretch (8 GB tier):** run 05.03 with `nishad/apertus:4b`. It needs the wrapper tag and only simple tools; compare behaviour."""),
    ("md", """## ✅ Checkpoint

- Tools are functions; the model proposes calls; you decide; results flow back
- Identifiers that were not looked up are marked, and text-shaped calls stop the loop
- Two tools chained a GND identifier to a Wikidata item and an HLS article
- You know when to re-ask in English and when to refuse a call

You are done with Part 2. Keep `runs/log.jsonl`: it is the record of what model produced which result."""),
]
