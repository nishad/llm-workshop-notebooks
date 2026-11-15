TITLE = "01 · Talking to the model from Python"
CELLS = [
    ("md", """# 01 · Talking to the model from Python

In Part 1 you typed into a chat window. Now the same model answers your code, which means you can send it a hundred records,
keep every answer, and record exactly which model produced what.

**What you'll learn**
1. List the models Ollama has and read a model's facts (parameters, context, quantization) from Python
2. Send a chat with a system prompt and control temperature, seed and context length
3. Stream an answer, and swap the Ollama library for the OpenAI client in one line
4. Record provenance for every result

Modes: **Run and change** cells are marked 🔧; **Stretch** cells are marked 🚀 (optional)."""),
    ("md", "## 01.01 Configuration"),
    ("code", """import os
os.environ.setdefault("WORKSHOP_TIER", "16gb")   # "8gb" or "16gb"
from workshop.config import load_settings, context_limit
settings = load_settings()
MODEL = settings.model
print("Model:", MODEL, "| context we use:", context_limit(MODEL), "tokens")"""),
    ("md", """## 01.02 Which models do I have, and what is in the file?

`ollama.list()` shows what is downloaded. `ollama.show()` reads the model's metadata: this is where the Part 1 concepts
(parameters, context length, quantization) live as numbers."""),
    ("code", """import ollama
client = ollama.Client(host=settings.host)
for m in client.list().models:
    print(f"{m.model:45} {m.size/1e9:5.1f} GB  digest {m.digest[:12]}")"""),
    ("md", """Now one model's own metadata. The `capabilities` list is where Ollama says whether this build can call tools."""),
    ("code", """info = client.show(MODEL)
print("parameters:  ", info.details.parameter_size)
print("quantization:", info.details.quantization_level)
print("context:     ", {k: v for k, v in info.modelinfo.items() if k.endswith("context_length")})
print("capabilities:", getattr(info, "capabilities", None))
print("template starts with:", (info.template or "").splitlines()[0])"""),
    ("md", """## 01.03 A first chat with a system prompt

The `messages` list is the whole conversation. The **system** message sets the role; the **user** message is the question.
`workshop.llm.chat` sets temperature 0 and the right `num_ctx` for your tier so results are repeatable."""),
    ("code", """from workshop.llm import chat
from workshop.display import show_markdown

messages = [
    {"role": "system", "content": "You are a cataloguing assistant in a research library. Be brief and precise."},
    {"role": "user", "content": "In two sentences: what is an authority file, and why do catalogues use one?"},
]
response = chat(messages, model=MODEL)
show_markdown(response.message.content)"""),
    ("md", """## 01.04 Temperature, seed and repeatability

Run the same request three times at temperature 0 with a fixed seed, then three times at 0.8. Watch which set varies.
This is the difference between a reproducible pipeline and a creative assistant. For a short factual question the top
candidates dominate, so a higher temperature may change nothing; a creative prompt shows the difference."""),
    ("code", """question = [{"role": "user", "content": "Suggest a title for a newsletter about open data in libraries. One line, no explanation."}]
for temp in (0, 0.8):
    print(f"--- temperature {temp} ---")
    for run in range(3):
        r = chat(question, model=MODEL, options={"temperature": temp, "seed": 42} if temp == 0 else {"temperature": temp})
        print(run + 1, r.message.content.strip().replace("\\n", " | ")[:160])"""),
    ("md", """🔧 **Run and change:** change the seed in one of the temperature-0 runs. Does the answer change? Then change the request
to German ("Schlage einen Titel für einen Newsletter über offene Daten in Bibliotheken vor...") and compare."""),
    ("md", """## 01.05 Streaming

Long answers arrive token by token. Streaming shows them as they come, like the chat window did."""),
    ("code", """from workshop.display import stream_markdown
stream = chat([{"role": "user", "content": "Explain in five short bullet points what a library would use a local language model for."}],
              model=MODEL, stream=True)
text = stream_markdown(stream)"""),
    ("md", """## 01.06 The same call through the OpenAI client

Many tools speak the OpenAI API. Ollama answers it on port 11434 under `/v1`, so the same code can talk to Ollama,
LM Studio (`http://localhost:1234/v1`), llama.cpp's server, or a hosted provider by changing one line: the base URL.
That is what vendor independence looks like in practice."""),
    ("code", """from openai import OpenAI
oa = OpenAI(base_url=f"{settings.host}/v1", api_key="ollama")   # the key is required by the client but ignored by Ollama
completion = oa.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": "Reply with one word: which city is the ETH Zurich in?"}],
    temperature=0,
)
print(completion.choices[0].message.content)"""),
    ("md", """## 01.07 Record what produced the answer

A result without its provenance cannot be checked later. `workshop.llm.chat` does this on every call: it appends one line
to `runs/log.jsonl` with the time, the model, its digest, the options, the end of the prompt and the start of the answer
(300 characters each; streamed calls log the request only).
This cell shows the full provenance record once (quantization, context length, template and Ollama version as well) and
writes it with `log_run`, the same function the helper uses."""),
    ("code", """from workshop.llm import provenance, log_run
prov = provenance(MODEL)
record = {"notebook": "01", "prompt": messages[-1]["content"], "answer": response.message.content, **prov,
          "options": {"temperature": 0, "num_ctx": context_limit(MODEL)}}
log_run(record)
print({k: record[k] for k in ("model", "digest", "quantization", "ollama_version", "captured_at")})
print("appended to runs/log.jsonl")"""),
    ("md", """## 01.08 Exercises

🖥️ **GUI:** ask the question from 01.04 twice in the Ollama app, whose default temperature is above 0 (the workshop tags set
0.8), and compare with the runs above.

🔧 **Run and change:** give the system prompt a persona ("You are a music librarian") and ask the authority-file question again.
What changed, what did not?

🔧 **Run and change:** ask the model to translate this STW scope note into French and English:
*"Herstellung von Kino-, TV- oder Werbefilmen."* Check the French against a dictionary: small models mistranslate specifics.

🚀 **Stretch:** pull `thalhath/apertus:8b-v1.5-preview` (16 GB machines) and run 01.04 against it. Same prompt, different model:
compare the answers and the digests. This is why the digest is in the log."""),
    ("md", """## ✅ Checkpoint

- You listed models and read parameters, context and quantization from the model file
- You sent a chat with a system prompt and saw how temperature and seed change repeatability
- You streamed an answer and made the same call through the OpenAI client
- Every result can now be traced to a model digest and options

Next: `02_structured_output.ipynb`."""),
]
