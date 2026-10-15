"""Thin wrapper around ollama.chat with the workshop defaults, plus provenance recording."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import ollama
import requests

from workshop.config import USER_AGENT, context_limit, load_settings


def _client(client):
    return client or ollama.Client(host=load_settings().host)


def _server_version(host: str) -> str | None:
    """Ask the Ollama server for its version over HTTP; the Python client has no version() call."""
    try:
        r = requests.get(f"{host.rstrip('/')}/api/version", headers={"User-Agent": USER_AGENT}, timeout=5)
        r.raise_for_status()
        return r.json().get("version")
    except (requests.RequestException, ValueError):
        return None


def chat(
    messages: list[dict],
    *,
    model: str | None = None,
    options: dict | None = None,
    format=None,
    tools: list | None = None,
    stream: bool = False,
    client=None,
):
    """Call the model with temperature 0 and the tier's num_ctx unless overridden. Never sends `think`."""
    if tools and format is not None:
        raise ValueError("Do not combine tools with format in one request: Ollama then returns the call as plain JSON.")
    model = model or load_settings().model
    opts = {"temperature": 0, "num_ctx": context_limit(model)}
    opts.update(options or {})
    kwargs = {"model": model, "messages": messages, "options": opts, "stream": stream}
    if format is not None:
        kwargs["format"] = format
    if tools:
        kwargs["tools"] = tools
    return _client(client).chat(**kwargs)


def provenance(model: str | None = None, *, client=None) -> dict:
    """What exactly produced an output: tag, digest, size, quantization, context, template, runtime version."""
    model = model or load_settings().model
    c = _client(client)
    digest = next((m.digest for m in c.list().models if m.model == model), None)
    info = c.show(model)
    modelinfo = getattr(info, "modelinfo", {}) or {}
    context = next((v for k, v in modelinfo.items() if k.endswith(".context_length")), None)
    version = _server_version(load_settings().host)
    return {
        "model": model,
        "digest": digest,
        "parameter_size": getattr(info.details, "parameter_size", None),
        "quantization": getattr(info.details, "quantization_level", None),
        "context_length": context,
        "template_header": (info.template or "").splitlines()[0] if getattr(info, "template", None) else "",
        "ollama_version": version,
        "captured_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }


def log_run(record: dict, path: str = "runs/log.jsonl") -> None:
    """Append one JSON line per model call so every result in the workshop can be traced."""
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(record, ensure_ascii=False) + "\n")
