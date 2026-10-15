# tests/test_rag.py
import pytest

from workshop import rag


def test_load_document_reads_utf8(tmp_path):
    p = tmp_path / "t.txt"
    p.write_text("Datensätze éàü", encoding="utf-8")
    assert rag.load_document(str(p)) == "Datensätze éàü"


def test_chunk_text_respects_size_and_overlap():
    words = [f"w{i}" for i in range(100)]
    chunks = rag.chunk_text(" ".join(words), "doc", size=40, overlap=10)
    assert [c.position for c in chunks] == [0, 1, 2]
    assert chunks[-1].text.split()[-1] == "w99"
    assert chunks[0].text.split()[-10:] == chunks[1].text.split()[:10]
    assert all(c.source == "doc" for c in chunks)
    assert chunks[0].id == "doc#0"


def test_chunk_text_rejects_bad_overlap():
    with pytest.raises(ValueError):
        rag.chunk_text("a b c", "doc", size=10, overlap=10)


def test_build_prompt_numbers_chunks_and_includes_rules():
    chunks = [rag.Chunk("d#0", "First passage.", "d", 0), rag.Chunk("d#1", "Second passage.", "d", 1)]
    prompt = rag.build_prompt("What?", chunks, max_tokens=8192)
    assert "[1] First passage." in prompt and "[2] Second passage." in prompt
    assert "say that the documents do not answer" in prompt
    assert prompt.rstrip().endswith("What?")


def test_build_prompt_raises_when_over_budget():
    big = rag.Chunk("d#0", "word " * 5000, "d", 0)
    with pytest.raises(rag.PromptTooLong):
        rag.build_prompt("q", [big], max_tokens=4096)


def test_estimate_tokens_is_conservative():
    assert rag.estimate_tokens("The library catalogue contains three million records.") >= 8
