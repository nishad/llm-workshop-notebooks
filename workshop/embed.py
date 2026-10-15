"""Embeddings through Ollama's /api/embed, with the prefix each model expects.

Ollama adds no prefixes itself. Documents and queries must be embedded with the same model and
through this helper so the convention is applied consistently.
"""

from __future__ import annotations

import numpy as np
import ollama

from workshop.config import load_settings

# Documented conventions, verified on the model cards (2026-10-09).
PREFIXES: dict[str, dict[str, str]] = {
    "bge-m3": {"query": "", "document": ""},
    "qwen3-embedding": {
        "query": "Instruct: Given a search term, retrieve the matching thesaurus concept\nQuery:",
        "document": "",
    },
    "nomic-embed-text-v2-moe": {"query": "search_query: ", "document": "search_document: "},
    "nomic-embed-text": {"query": "search_query: ", "document": "search_document: "},
    "embeddinggemma-2": {"query": "task: search result | query: ", "document": "title: none | text: "},
    "embeddinggemma": {"query": "task: search result | query: ", "document": "title: none | text: "},
    "multilingual-e5": {"query": "query: ", "document": "passage: "},
    "snowflake-arctic-embed2": {"query": "query: ", "document": ""},
    "granite-embedding": {"query": "", "document": ""},
}


def _base_name(model: str) -> str:
    return model.split("/")[-1].split(":")[0].lower()


def prefix_for(model: str, kind: str) -> str:
    """Return the prefix for 'query' or 'document' texts for this model ('' when none is needed)."""
    if kind not in ("query", "document"):
        raise ValueError("kind must be 'query' or 'document'")
    base = _base_name(model)
    # Longest key first so 'nomic-embed-text-v2-moe' wins over 'nomic-embed-text'.
    for key in sorted(PREFIXES, key=len, reverse=True):
        if key in base:
            return PREFIXES[key][kind]
    return ""


def prefixed(texts: list[str], kind: str, model: str) -> list[str]:
    p = prefix_for(model, kind)
    return [p + t for t in texts]


def normalize(matrix: np.ndarray) -> np.ndarray:
    norms = np.linalg.norm(matrix, axis=1, keepdims=True)
    norms[norms == 0] = 1.0
    return (matrix / norms).astype(np.float32)


def embed(
    texts: list[str],
    kind: str,
    *,
    model: str | None = None,
    batch_size: int = 64,
    client=None,
) -> np.ndarray:
    """Embed texts as 'query' or 'document'. Returns unit-length float32 vectors, one row per text."""
    settings = load_settings()
    model = model or settings.embed_model
    client = client or ollama.Client(host=settings.host)
    inputs = prefixed(texts, kind, model)
    rows: list[list[float]] = []
    for start in range(0, len(inputs), batch_size):
        response = client.embed(model=model, input=inputs[start : start + batch_size])
        rows.extend(response.embeddings)
    return normalize(np.array(rows, dtype=np.float32))
