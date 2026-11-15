"""Workshop settings: which model, which embedding model, which Ollama host, which hardware tier.

Override with environment variables WORKSHOP_MODEL, WORKSHOP_EMBED_MODEL, OLLAMA_HOST, WORKSHOP_TIER.
"""

from __future__ import annotations

import os
from dataclasses import dataclass

DEFAULT_MODEL = "thalhath/apertus:8b"
SMALL_MODEL = "thalhath/apertus:4b"
PREVIEW_MODEL = "thalhath/apertus:8b-v1.5-preview"
DEFAULT_EMBED_MODEL = "qwen3-embedding:0.6b"
DEFAULT_HOST = "http://localhost:11434"
USER_AGENT = "swib26-llm-workshop/1.0 (https://llm-workshop.thalhath.org/)"


@dataclass(frozen=True)
class Settings:
    model: str
    embed_model: str
    host: str
    tier: str  # "8gb" or "16gb"


def _normalise_host(host: str) -> str:
    """Ollama accepts OLLAMA_HOST without a scheme (127.0.0.1:11435, or 0.0.0.0 with the default port); requests does not.

    Without a scheme, add http:// and, when no port is given, Ollama's default port 11434. With a scheme, the URL is kept
    as given (the user chose the port).
    """
    host = host.rstrip("/")
    if "://" not in host:
        has_port = "]:" in host if host.startswith("[") else ":" in host  # [::1]:11434 is an IPv6 address with a port
        host = "http://" + (host if has_port else f"{host}:11434")
    return host


def load_settings() -> Settings:
    tier = os.environ.get("WORKSHOP_TIER", "16gb").lower()
    default_model = SMALL_MODEL if tier == "8gb" else DEFAULT_MODEL
    return Settings(
        model=os.environ.get("WORKSHOP_MODEL", default_model),
        embed_model=os.environ.get("WORKSHOP_EMBED_MODEL", DEFAULT_EMBED_MODEL),
        host=_normalise_host(os.environ.get("OLLAMA_HOST", DEFAULT_HOST)),
        tier=tier,
    )


def context_limit(model: str) -> int:
    """Tokens of context the notebooks may use with this model.

    The Apertus v1.1 4B was trained with a 4,096-token window; anything larger is clamped by Ollama.
    The 8B tags carry num_ctx 8192 in their Modelfile.
    """
    return 4096 if ":4b" in model else 8192
