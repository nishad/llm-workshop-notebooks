# tests/test_config.py
from workshop import config


def test_defaults_when_env_unset(monkeypatch):
    for var in ("WORKSHOP_MODEL", "WORKSHOP_EMBED_MODEL", "OLLAMA_HOST", "WORKSHOP_TIER"):
        monkeypatch.delenv(var, raising=False)
    s = config.load_settings()
    assert s.model == "nishad/apertus:8b"
    assert s.embed_model == "bge-m3"
    assert s.host == "http://localhost:11434"
    assert s.tier == "16gb"


def test_tier_8gb_switches_model(monkeypatch):
    monkeypatch.delenv("WORKSHOP_MODEL", raising=False)
    monkeypatch.setenv("WORKSHOP_TIER", "8gb")
    assert config.load_settings().model == "nishad/apertus:4b"


def test_explicit_model_wins_over_tier(monkeypatch):
    monkeypatch.setenv("WORKSHOP_TIER", "8gb")
    monkeypatch.setenv("WORKSHOP_MODEL", "nishad/apertus:8b-v1.5-preview")
    assert config.load_settings().model == "nishad/apertus:8b-v1.5-preview"


def test_context_limit_by_model():
    assert config.context_limit("nishad/apertus:4b") == 4096
    assert config.context_limit("nishad/apertus:8b") == 8192
    assert config.context_limit("nishad/apertus:8b-v1.5-preview") == 8192
    assert config.context_limit("llama3.2:3b") == 8192
