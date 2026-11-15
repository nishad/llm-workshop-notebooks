# tests/test_docs.py
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def test_readme_mentions_current_facts():
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    for needle in ("Python 3.12", "thalhath/apertus:8b", "thalhath/apertus:4b", "qwen3-embedding:0.6b", "uv sync", "SWIB26"):
        assert needle in text, needle
    for stale in ("Python 3.8", "Kickstarter", "llama3.2:7b", "ollama.ai", "made-with-cc"):
        assert stale not in text, stale


def test_cheat_sheet_uses_current_api():
    text = (ROOT / "CHEAT_SHEET.md").read_text(encoding="utf-8")
    assert "ollama.embeddings(" not in text
    assert "model['name']" not in text and 'model["name"]' not in text
    assert "format=" in text and "tool_calls" in text


def test_troubleshooting_has_no_dangerous_commands():
    text = (ROOT / "TROUBLESHOOTING.md").read_text(encoding="utf-8")
    assert "0.0.0.0" not in text
    assert "rm -rf ~/.ollama/models" not in text
    assert "wmic" not in text
    assert "softlayer" not in text.lower()
    for needle in ("LM Studio", "encoding", "num_ctx", "exceeds the available context size"):
        assert needle in text, needle


def test_requirements_matches_lock():
    text = (ROOT / "requirements.txt").read_text(encoding="utf-8")
    assert "ollama==" in text and "pydantic==" in text and "sqlite-vec==" in text
