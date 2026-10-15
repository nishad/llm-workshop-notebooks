"""Semantic search as a dot product over unit vectors, with optional sqlite-vec persistence."""

from __future__ import annotations

import json
import sqlite3
from dataclasses import dataclass

import numpy as np
import sqlite_vec

from workshop.embed import embed, normalize

Hit = tuple[str, str, float]  # (id, text, score)


@dataclass
class Index:
    ids: list[str]
    texts: list[str]
    vectors: np.ndarray  # shape (n, d), unit length
    model: str


def top_k(query_vec: np.ndarray, matrix: np.ndarray, k: int) -> list[tuple[int, float]]:
    """Indices and cosine scores of the k rows of `matrix` most similar to `query_vec`."""
    scores = matrix @ query_vec
    order = np.argsort(-scores)[:k]
    return [(int(i), float(scores[i])) for i in order]


def _embed_query(text: str, model: str) -> np.ndarray:
    return embed([text], "query", model=model)[0]


def build_index(ids: list[str], texts: list[str], *, model: str | None = None) -> Index:
    from workshop.config import load_settings

    model = model or load_settings().embed_model
    vectors = embed(texts, "document", model=model)
    return Index(ids=list(ids), texts=list(texts), vectors=vectors, model=model)


def search(query: str, index: Index, *, k: int = 5, threshold: float | None = None) -> list[Hit]:
    q = _embed_query(query, index.model)
    hits = []
    for i, score in top_k(q, index.vectors, k):
        if threshold is not None and score < threshold:
            continue
        hits.append((index.ids[i], index.texts[i], round(score, 4)))
    return hits


def _connect(path: str) -> sqlite3.Connection:
    conn = sqlite3.connect(path)
    conn.enable_load_extension(True)
    sqlite_vec.load(conn)
    conn.enable_load_extension(False)
    return conn


def save_index(index: Index, path: str) -> None:
    dim = int(index.vectors.shape[1])
    conn = _connect(path)
    conn.executescript(
        f"""
        DROP TABLE IF EXISTS items;
        DROP TABLE IF EXISTS vec_items;
        DROP TABLE IF EXISTS meta;
        CREATE TABLE items(rowid INTEGER PRIMARY KEY, id TEXT NOT NULL, text TEXT NOT NULL);
        CREATE VIRTUAL TABLE vec_items USING vec0(embedding float[{dim}]);
        CREATE TABLE meta(key TEXT PRIMARY KEY, value TEXT NOT NULL);
        """
    )
    for row, (id_, text, vec) in enumerate(zip(index.ids, index.texts, index.vectors), start=1):
        conn.execute("INSERT INTO items(rowid, id, text) VALUES (?, ?, ?)", (row, id_, text))
        conn.execute(
            "INSERT INTO vec_items(rowid, embedding) VALUES (?, ?)",
            (row, sqlite_vec.serialize_float32([float(x) for x in vec])),
        )
    conn.execute("INSERT INTO meta(key, value) VALUES ('model', ?)", (index.model,))
    conn.execute("INSERT INTO meta(key, value) VALUES ('dim', ?)", (json.dumps(dim),))
    conn.commit()
    conn.close()


def load_index(path: str) -> Index:
    conn = _connect(path)
    model = conn.execute("SELECT value FROM meta WHERE key = 'model'").fetchone()[0]
    rows = conn.execute("SELECT i.id, i.text, v.embedding FROM items i JOIN vec_items v ON v.rowid = i.rowid ORDER BY i.rowid").fetchall()
    conn.close()
    ids = [r[0] for r in rows]
    texts = [r[1] for r in rows]
    vectors = np.array([np.frombuffer(r[2], dtype=np.float32) for r in rows], dtype=np.float32)
    return Index(ids=ids, texts=texts, vectors=vectors, model=model)


def knn_sqlite(path: str, query_vec: np.ndarray, k: int = 5) -> list[tuple[str, str, float]]:
    """Nearest neighbours straight from sqlite-vec (distance, smaller is closer)."""
    conn = _connect(path)
    rows = conn.execute(
        """
        SELECT i.id, i.text, v.distance
        FROM vec_items v JOIN items i ON i.rowid = v.rowid
        WHERE v.embedding MATCH ? AND k = ?
        ORDER BY v.distance
        """,
        (sqlite_vec.serialize_float32([float(x) for x in query_vec]), k),
    ).fetchall()
    conn.close()
    return [(r[0], r[1], float(r[2])) for r in rows]
