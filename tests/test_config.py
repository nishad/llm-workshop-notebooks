# tests/test_config.py
from workshop import config


def test_defaults_when_env_unset(monkeypatch):
    for var in ("WORKSHOP_MODEL", "WORKSHOP_EMBED_MODEL", "OLLAMA_HOST", "WORKSHOP_TIER"):
        monkeypatch.delenv(var, raising=False)
    s = config.load_settings()
    assert s.model == "nishad/apertus:8b"
    assert s.embed_model == "qwen3-embedding:0.6b"
    assert s.host == "http://localhost:11434"
    assert s.tier == "16gb"


def test_host_without_scheme_gets_http(monkeypatch):
    monkeypatch.setenv("OLLAMA_HOST", "127.0.0.1:11435")
    assert config.load_settings().host == "http://127.0.0.1:11435"
    monkeypatch.setenv("OLLAMA_HOST", "http://localhost:11434/")
    assert config.load_settings().host == "http://localhost:11434"
    monkeypatch.setenv("OLLAMA_HOST", "localhost:11435")
    assert config.load_settings().host == "http://localhost:11435"


def test_host_without_scheme_or_port_gets_the_default_port(monkeypatch):
    for given, expected in [("0.0.0.0", "http://0.0.0.0:11434"), ("localhost", "http://localhost:11434"),
                            ("[::1]", "http://[::1]:11434"), ("[::1]:11435", "http://[::1]:11435"),
                            ("http://myhost", "http://myhost")]:
        monkeypatch.setenv("OLLAMA_HOST", given)
        assert config.load_settings().host == expected, given


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
