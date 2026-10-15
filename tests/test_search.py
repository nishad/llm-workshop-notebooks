# tests/test_search.py
import numpy as np

from workshop import search


def test_top_k_orders_by_dot_product():
    matrix = np.array([[1, 0], [0, 1], [0.7, 0.7]], dtype=np.float32)
    q = np.array([1.0, 0.0], dtype=np.float32)
    hits = search.top_k(q, matrix, k=2)
    assert [i for i, _ in hits] == [0, 2]
    assert hits[0][1] > hits[1][1]


def test_search_applies_threshold(monkeypatch):
    index = search.Index(
        ids=["a", "b"],
        texts=["Alpha", "Beta"],
        vectors=np.array([[1, 0], [0, 1]], dtype=np.float32),
        model="bge-m3",
    )
    monkeypatch.setattr(search, "_embed_query", lambda text, model: np.array([1.0, 0.0], dtype=np.float32))
    hits = search.search("anything", index, k=5, threshold=0.5)
    assert hits == [("a", "Alpha", 1.0)]


def test_save_and_load_roundtrip(tmp_path):
    index = search.Index(
        ids=["x", "y"],
        texts=["Ex", "Why"],
        vectors=search.normalize(np.array([[1, 2, 3], [3, 2, 1]], dtype=np.float32)),
        model="bge-m3",
    )
    path = tmp_path / "idx.sqlite"
    search.save_index(index, str(path))
    loaded = search.load_index(str(path))
    assert loaded.ids == index.ids
    assert loaded.texts == index.texts
    assert loaded.model == "bge-m3"
    assert np.allclose(loaded.vectors, index.vectors, atol=1e-6)


def test_knn_from_sqlite_matches_numpy(tmp_path):
    vectors = search.normalize(np.array([[1, 0, 0], [0, 1, 0], [0.9, 0.1, 0]], dtype=np.float32))
    index = search.Index(ids=["a", "b", "c"], texts=["A", "B", "C"], vectors=vectors, model="bge-m3")
    path = tmp_path / "idx.sqlite"
    search.save_index(index, str(path))
    q = np.array([1.0, 0.0, 0.0], dtype=np.float32)
    rows = search.knn_sqlite(str(path), q, k=2)
    assert [r[0] for r in rows] == ["a", "c"]
