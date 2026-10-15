TITLE = "04 · Retrieval-augmented generation over your documents"
CELLS = [
    ("md", """# 04 · Retrieval-augmented generation over your documents ⏱️ 20 minutes

The model knows nothing about your documents, and its context window is small. RAG retrieves the few passages that matter,
puts them in the prompt, and asks for an answer with citations. You will see the retrieved passages **before** the answer,
so you can judge whether the answer had a chance.

Corpus: the IFLA Library Reference Model and the DCMI Metadata Terms (both CC BY 4.0), as text extracts.

**What you'll learn**
1. Load and chunk documents, keeping the source of every chunk
2. Embed once, retrieve by question
3. Prompt for grounded answers with citations and a refusal when the documents are silent
4. Respect the context budget, and measure with five questions"""),
    ("md", "## 04.01 Configuration"),
    ("code", """import os
os.environ.setdefault("WORKSHOP_TIER", "16gb")
from workshop.config import load_settings, context_limit
settings = load_settings(); MODEL = settings.model; EMBED_MODEL = settings.embed_model
LIMIT = context_limit(MODEL)
K = 3 if LIMIT <= 4096 else 4         # fewer chunks on the 4B's 4k window
print("Model:", MODEL, "| context:", LIMIT, "| chunks per question:", K)"""),
    ("md", """## 04.02 Load and chunk

Chunks of about 300 words with a 50-word overlap. Each chunk remembers its file and position; that is what a citation points to."""),
    ("code", """from pathlib import Path
from workshop.rag import load_document, chunk_text
chunks = []
for path in sorted(Path("data/docs").glob("*.md")):
    text = load_document(str(path))
    chunks += chunk_text(text, source=path.stem, size=300, overlap=50)
by_id = {c.id: c for c in chunks}
print(len(chunks), "chunks from", len(set(c.source for c in chunks)), "documents")
print(chunks[5].id, "→", chunks[5].text[:200], "...")"""),
    ("md", """## 04.03 Embed once

A few hundred chunks: this takes under a minute on most laptops. The index is kept in memory for the session."""),
    ("code", """import time
from workshop.search import build_index, search
t = time.time()
index = build_index([c.id for c in chunks], [c.text for c in chunks], model=EMBED_MODEL)
print(f"indexed {len(chunks)} chunks in {time.time()-t:.0f} s")"""),
    ("md", """## 04.04 Look at what was retrieved before you read any answer

If the right passage is not in the top hits, no prompt can fix it. Retrieval quality comes first.

In the October 2026 run the top hits for the DCMI question were mostly generic date terms and `dcterms:issued` was not among them, so the cited answer in 04.05 is wrong; the exercise in 04.10 (smaller chunks) is where to start fixing that."""),
    ("code", """question = "Which DCMI term expresses the date on which a resource was formally issued?"
for cid, text, score in search(question, index, k=K):
    print(f"{score:.3f}  {cid}\\n      {text[:160]}...\\n")"""),
    ("md", """## 04.05 Ask with the documents in the prompt

The prompt numbers the chunks, tells the model to cite them as [n], and to say when the documents do not answer.
`answer()` returns both the text and the chunks it used, so the citation numbers can be checked."""),
    ("code", """from workshop.rag import answer, build_prompt
from workshop.display import show_markdown
text, used = answer(question, index, by_id, k=K, model=MODEL)
show_markdown(text)
print("\\nCited material:")
for n, c in enumerate(used, 1):
    print(f"[{n}] {c.source}#{c.position}: {c.text[:100]}...")"""),
    ("md", """## 04.06 When the documents are silent

A grounded system must refuse. Ask something the corpus cannot know."""),
    ("code", """text, used = answer("Who won the 2026 Nobel Prize in Literature?", index, by_id, k=K, model=MODEL)
show_markdown(text)"""),
    ("md", """## 04.07 The context budget

On the 8 GB tier the window is 4,096 tokens (8,192 on the 8B shown here): system text, retrieved chunks, question and answer must all fit. The helper
estimates the size and refuses to build an oversized prompt; Ollama itself returns an HTTP 400 when a request exceeds the
window. Here is what both look like."""),
    ("code", """from workshop.rag import PromptTooLong
import ollama
many = [by_id[cid] for cid, _, _ in search(question, index, k=40)]
try:
    build_prompt(question, many, max_tokens=LIMIT)
except PromptTooLong as err:
    print("helper refused:", err)
try:
    big = "\\n\\n".join(c.text for c in many)[: int(LIMIT * 1.5 * 3.5)]   # about one and a half windows of text
    ollama.Client(host=settings.host).chat(model=MODEL, messages=[{"role": "user", "content": big + "\\n\\nSummarize."}],
                                          options={"num_ctx": LIMIT, "temperature": 0, "num_predict": 20})
    print("Ollama accepted the long prompt (it may have truncated silently; check num_ctx).")
except ollama.ResponseError as err:
    print("Ollama said:", err)"""),
    ("md", """## 04.08 Five questions, scored by you

Run the prepared questions and compare with the expected answers. The score is a judgement, not a string match; that is deliberate."""),
    ("code", """import json
questions = json.loads(Path("data/docs/questions.json").read_text(encoding="utf-8"))
for q in questions:
    text, used = answer(q["question"], index, by_id, k=K, model=MODEL)
    print("Q:", q["question"]); print("A:", text.strip()[:400]); print("expected:", q["expected"]); print("-" * 80)"""),
    ("md", """## 04.09 Bring your own document

Drop a PDF, Markdown or text file into `data/my/` and run the cell. UTF-8 is assumed for text; two-column PDFs extract
badly (compare the text before you trust the answers)."""),
    ("code", """my = sorted(p for p in Path("data/my").glob("*") if p.suffix.lower() in (".pdf", ".md", ".txt")) if Path("data/my").exists() else []
if not my:
    print("Put a .pdf, .md or .txt file into data/my/ and run this cell again.")
else:
    my_chunks = []
    for p in my:
        my_chunks += chunk_text(load_document(str(p)), source=p.stem)
    my_by_id = {c.id: c for c in my_chunks}
    my_index = build_index([c.id for c in my_chunks], [c.text for c in my_chunks], model=EMBED_MODEL)
    print(len(my_chunks), "chunks. Ask a question:")
    q = input("Question: ") if os.environ.get("WORKSHOP_AUTO_APPROVE") != "1" else "What is this document about?"
    text, used = answer(q, my_index, my_by_id, k=K, model=MODEL)
    show_markdown(text)"""),
    ("md", """## 04.10 Exercises

🖥️ **GUI:** LM Studio's Chat with Documents does this retrieval without code: attach the DCMI file from `data/docs/`
(`dcmi-terms.md`; save a copy as `.txt` if the app does not accept `.md`) and ask the `dcterms:issued` question from 04.04;
compare with 04.05.

🔧 **Run and change:** set `K = 1` and re-run 04.08. Which questions break? Then try `size=150` in 04.02.

🔧 **Run and change:** ask the same question in German. Does retrieval over English documents still find the passage?

🚀 **Stretch:** rerank. Ask the chat model, with `format=` and a tiny Pydantic model `{"relevant": bool, "reason": str}`, whether each
of the top 10 chunks answers the question; keep only the relevant ones and answer again. Compare with 04.05.

🚀 **Stretch:** index this workshop's website pages (download them as Markdown) and ask it about itself."""),
    ("md", """## ✅ Checkpoint

- Documents became chunks with sources; chunks became vectors; questions retrieve the chunks that matter
- Answers are asked to cite the passages and to refuse when the corpus is silent; you saw one of each, and one answer that got it wrong
- You know what the context budget is and what happens when it is exceeded
- You judged five answers against expectations instead of trusting them

Next: `05_tool_use.ipynb`."""),
]
