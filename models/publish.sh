#!/usr/bin/env bash
# Build the workshop tags locally and push them to ollama.com.
# Pushing needs this machine's key (~/.ollama/id_ed25519.pub) added at https://ollama.com/settings/keys.
set -euo pipefail
cd "$(dirname "$0")"
NS="${NAMESPACE:-nishad}"

ollama pull hf.co/unsloth/Apertus-8B-Instruct-2509-GGUF:Q4_K_M
ollama pull hf.co/jondale/Apertus-v1.1-4B-Instruct-GGUF:Q4_K_M
ollama pull hf.co/Colby/apertus-v1.5-8b-text-Q4_K_M-GGUF:Q4_K_M

ollama create "$NS/apertus:8b" -f apertus-8b.Modelfile
ollama create "$NS/apertus:4b" -f apertus-4b.Modelfile
ollama create "$NS/apertus:8b-v1.5-preview" -f apertus-8b-v1.5-preview.Modelfile
ollama cp "$NS/apertus:8b" "$NS/apertus:latest"

for tag in 8b 4b 8b-v1.5-preview latest; do
  echo "== $NS/apertus:$tag"
  ollama show "$NS/apertus:$tag" | sed -n '1,20p'
done

if [ "${PUSH:-0}" = "1" ]; then
  for tag in 8b 4b 8b-v1.5-preview latest; do ollama push "$NS/apertus:$tag"; done
else
  echo "Dry run complete. Re-run with PUSH=1 to push to ollama.com."
fi
