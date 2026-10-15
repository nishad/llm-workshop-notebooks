"""Retrieval-augmented generation without a framework: load, chunk, retrieve, prompt, answer."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from workshop.config import context_limit, load_settings
from workshop.llm import chat
from workshop.search import Index, search


class PromptTooLong(Exception):
    """The retrieved context would not fit the model's context window."""


@dataclass
class Chunk:
    id: str
    text: str
    source: str
    position: int


RAG_INSTRUCTIONS = (
    "Answer the question using only the numbered documents below. "
    "Cite the documents you used as [1], [2] and so on after each statement. "
    "If the documents do not contain the answer, say that the documents do not answer the question. "
    "Do not use outside knowledge."
)


def load_document(path: str) -> str:
    p = Path(path)
    if p.suffix.lower() == ".pdf":
        from pypdf import PdfReader

        reader = PdfReader(str(p))
        return "\n".join((page.extract_text() or "") for page in reader.pages)
    return p.read_text(encoding="utf-8")


def chunk_text(text: str, source: str, *, size: int = 300, overlap: int = 50) -> list[Chunk]:
    """Split on words into chunks of `size` words that share `overlap` words with their neighbour."""
    if overlap >= size:
        raise ValueError("overlap must be smaller than size")
    words = text.split()
    chunks: list[Chunk] = []
    start, position = 0, 0
    while start < len(words):
        piece = " ".join(words[start : start + size])
        chunks.append(Chunk(id=f"{source}#{position}", text=piece, source=source, position=position))
        if start + size >= len(words):
            break
        start += size - overlap
        position += 1
    return chunks


def estimate_tokens(text: str) -> int:
    """Rough upper bound: one token per 3.5 characters (English prose is about 4; German and SPARQL are denser)."""
    return int(len(text) / 3.5) + 1


def build_prompt(question: str, chunks: list[Chunk], *, max_tokens: int) -> str:
    numbered = "\n\n".join(f"[{i}] {c.text}" for i, c in enumerate(chunks, start=1))
    prompt = f"{RAG_INSTRUCTIONS}\n\nDocuments:\n\n{numbered}\n\nQuestion: {question}"
    # Leave room for the system prompt and the answer: budget 75% of the window for the prompt.
    if estimate_tokens(prompt) > int(max_tokens * 0.75):
        raise PromptTooLong(
            f"About {estimate_tokens(prompt)} tokens of prompt for a {max_tokens}-token window. "
            "Use fewer or shorter chunks (lower k or size)."
        )
    return prompt


def answer(
    question: str,
    index: Index,
    chunks_by_id: dict[str, Chunk],
    *,
    k: int = 4,
    model: str | None = None,
) -> tuple[str, list[Chunk]]:
    """Retrieve k chunks, build the grounded prompt, ask the model. Returns (answer, chunks used).

    The call goes through workshop.llm.chat: temperature 0, the tier's num_ctx, one line in runs/log.jsonl."""
    model = model or load_settings().model
    hits = search(question, index, k=k)
    used = [chunks_by_id[hit_id] for hit_id, _, _ in hits]
    prompt = build_prompt(question, used, max_tokens=context_limit(model))
    response = chat([{"role": "user", "content": prompt}], model=model)
    return response.message.content, used
