import numpy as np

from workshop import embed


def test_bge_m3_has_no_prefixes():
    assert embed.prefix_for("bge-m3", "query") == ""
    assert embed.prefix_for("bge-m3:567m", "document") == ""


def test_qwen3_prefixes_only_queries():
    assert embed.prefix_for("qwen3-embedding:0.6b", "query").startswith("Instruct:")
    assert embed.prefix_for("qwen3-embedding:0.6b", "document") == ""


def test_nomic_prefixes_both_sides():
    assert embed.prefix_for("nomic-embed-text", "query") == "search_query: "
    assert embed.prefix_for("nomic-embed-text-v2-moe", "document") == "search_document: "


def test_hf_e5_matches_by_substring():
    assert embed.prefix_for("hf.co/someone/multilingual-e5-small-GGUF:Q8_0", "query") == "query: "


def test_unknown_model_gets_no_prefix():
    assert embed.prefix_for("mystery-model", "query") == ""


def test_prefixed_applies_prefix_to_each_text():
    out = embed.prefixed(["Bibliothek", "Katalog"], "query", "nomic-embed-text")
    assert out == ["search_query: Bibliothek", "search_query: Katalog"]


def test_normalize_gives_unit_vectors():
    m = np.array([[3.0, 4.0], [0.0, 2.0]], dtype=np.float32)
    n = embed.normalize(m)
    assert np.allclose(np.linalg.norm(n, axis=1), 1.0)


class FakeClient:
    def __init__(self):
        self.calls = []

    def embed(self, model, input):
        self.calls.append((model, list(input)))
        return type("R", (), {"embeddings": [[1.0, 1.0] for _ in input]})()


def test_embed_batches_and_normalizes():
    fake = FakeClient()
    vecs = embed.embed(["a", "b", "c"], "document", model="bge-m3", batch_size=2, client=fake)
    assert vecs.shape == (3, 2)
    assert np.allclose(np.linalg.norm(vecs, axis=1), 1.0)
    assert [len(c[1]) for c in fake.calls] == [2, 1]
