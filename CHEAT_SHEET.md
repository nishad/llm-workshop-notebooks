# Local LLM Workshop - Quick Reference Cheat Sheet

Your go-to reference for common commands and code patterns during the workshop.

---

## 🚀 Quick Start Commands

### Ollama Service

```bash
# Start Ollama service
ollama serve

# Check if Ollama is running
ollama list

# Check Ollama version
ollama --version

# View running status
ps aux | grep ollama  # macOS/Linux
tasklist | findstr ollama  # Windows
```

### Model Management

```bash
# List installed models
ollama list

# Download a model
ollama pull llama3.2:3b
ollama pull nomic-embed-text

# Remove a model
ollama rm llama3.2:3b

# Get model information
ollama show llama3.2:3b

# Run model from command line
ollama run llama3.2:3b "Tell me a joke"
```

### Jupyter Notebook

```bash
# Start Jupyter Notebook
jupyter notebook

# Start on specific port
jupyter notebook --port 8889

# List running notebooks
jupyter notebook list

# Stop all notebooks
jupyter notebook stop
```

---

## 📝 Python Code Snippets

### Basic Ollama Usage

#### Import and Setup

```python
import ollama
```

#### Simple Text Generation

```python
response = ollama.generate(
    model='llama3.2:3b',
    prompt='Explain quantum computing in simple terms'
)

print(response['response'])
```

#### Streaming Responses

```python
stream = ollama.generate(
    model='llama3.2:3b',
    prompt='Write a story about AI',
    stream=True
)

for chunk in stream:
    print(chunk['response'], end='', flush=True)
```

#### Chat Interface

```python
messages = [
    {'role': 'user', 'content': 'What is Python?'},
]

response = ollama.chat(
    model='llama3.2:3b',
    messages=messages
)

print(response['message']['content'])
```

#### Multi-turn Conversation

```python
messages = []

# First turn
messages.append({'role': 'user', 'content': 'Hello! What\'s your purpose?'})
response = ollama.chat(model='llama3.2:3b', messages=messages)
messages.append(response['message'])

# Second turn
messages.append({'role': 'user', 'content': 'Tell me more about that'})
response = ollama.chat(model='llama3.2:3b', messages=messages)
print(response['message']['content'])
```

### Working with Models

#### List All Models

```python
import ollama

models = ollama.list()
for model in models['models']:
    print(f"{model['name']:30s} - {model['size']/(1024**3):.2f} GB")
```

#### Get Model Information

```python
import ollama
import json

info = ollama.show('llama3.2:3b')
print(json.dumps(info, indent=2))
```

#### Download Model Programmatically

```python
import ollama

# This might take a while
ollama.pull('llama3.2:3b')
print("Model downloaded!")
```

### Embeddings

#### Generate Embeddings

```python
embedding = ollama.embeddings(
    model='nomic-embed-text',
    prompt='Machine learning is a subset of AI'
)

# embedding['embedding'] is a list of floats
print(f"Embedding dimensions: {len(embedding['embedding'])}")
```

#### Compare Text Similarity

```python
import ollama
import numpy as np

def get_embedding(text):
    result = ollama.embeddings(
        model='nomic-embed-text',
        prompt=text
    )
    return np.array(result['embedding'])

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# Compare two texts
text1 = "I love programming"
text2 = "I enjoy coding"

emb1 = get_embedding(text1)
emb2 = get_embedding(text2)

similarity = cosine_similarity(emb1, emb2)
print(f"Similarity: {similarity:.4f}")
```

---

## 🗄️ ChromaDB (Vector Database)

### Setup and Initialization

```python
import chromadb

# Create persistent client (data saved to disk)
client = chromadb.PersistentClient(path="./vector-db/my-database")

# Create or get collection
collection = client.get_or_create_collection(
    name="my-collection",
    metadata={"hnsw:space": "cosine"}
)
```

### Adding Documents

```python
# Add documents with automatic IDs
collection.add(
    documents=["This is document 1", "This is document 2"],
    ids=["doc1", "doc2"]
)

# Add with embeddings (if you generated them separately)
collection.add(
    documents=["Document text"],
    embeddings=[[0.1, 0.2, 0.3, ...]],  # Your embedding vector
    ids=["doc1"]
)

# Add with metadata
collection.add(
    documents=["Python is a programming language"],
    metadatas=[{"source": "wikipedia", "category": "programming"}],
    ids=["doc1"]
)
```

### Querying

```python
# Semantic search
results = collection.query(
    query_texts=["programming languages"],
    n_results=5
)

# Access results
for i, doc in enumerate(results['documents'][0]):
    distance = results['distances'][0][i]
    print(f"Distance: {distance:.4f} - {doc}")
```

### Collection Management

```python
# Count documents
count = collection.count()
print(f"Documents in collection: {count}")

# List all collections
collections = client.list_collections()
for coll in collections:
    print(coll.name)

# Delete collection
client.delete_collection("my-collection")
```

---

## 🎯 RAG (Retrieval-Augmented Generation)

### Complete RAG Pipeline

```python
import ollama
import chromadb

# 1. Setup database
client = chromadb.PersistentClient(path="./vector-db/my-rag")
collection = client.get_or_create_collection(
    name="documents",
    metadata={"hnsw:space": "cosine"}
)

# 2. Generate and store embeddings
def add_document(text, doc_id):
    # Generate embedding
    embedding = ollama.embeddings(
        model='nomic-embed-text',
        prompt=text
    )

    # Store in database
    collection.add(
        documents=[text],
        embeddings=[embedding['embedding']],
        ids=[doc_id]
    )

# Add your documents
add_document("Python is a programming language", "doc1")
add_document("JavaScript runs in browsers", "doc2")

# 3. Query function
def query_with_rag(question, n_results=3):
    # Generate embedding for question
    query_embedding = ollama.embeddings(
        model='nomic-embed-text',
        prompt=question
    )

    # Search database
    results = collection.query(
        query_embeddings=[query_embedding['embedding']],
        n_results=n_results
    )

    # Get relevant documents
    context = "\n\n".join(results['documents'][0])

    # Create prompt with context
    prompt = f"""Based on the following context, answer the question.

Context:
{context}

Question: {question}

Answer:"""

    # Generate response
    response = ollama.generate(
        model='llama3.2:3b',
        prompt=prompt
    )

    return response['response']

# Use RAG
answer = query_with_rag("What programming languages are mentioned?")
print(answer)
```

### RAG with Jinja2 Templates

```python
from jinja2 import Template
import ollama

# Define template
template_string = """You are a helpful assistant. Answer the question based on the context provided.

Context:
{% for doc in context_documents %}
{{ doc }}
{% endfor %}

Question: {{ question }}

Answer:"""

template = Template(template_string)

# Use template
def query_with_template(question, context_docs):
    prompt = template.render(
        question=question,
        context_documents=context_docs
    )

    response = ollama.generate(
        model='llama3.2:3b',
        prompt=prompt
    )

    return response['response']
```

---

## 💡 Helpful Utilities

### Display Markdown in Jupyter

```python
from IPython.display import display, Markdown

def display_response(text):
    display(Markdown(text))

# Usage
response = ollama.generate(model='llama3.2:3b', prompt='Hello')
display_response(response['response'])
```

### Streaming with Markdown Display

```python
from IPython.display import display, Markdown, clear_output
import time

def stream_markdown(prompt):
    full_response = ""
    stream = ollama.generate(
        model='llama3.2:3b',
        prompt=prompt,
        stream=True
    )

    for chunk in stream:
        full_response += chunk['response']
        clear_output(wait=True)
        display(Markdown(full_response))
        time.sleep(0.05)  # Small delay for readability
```

### Progress Bar for Processing

```python
from tqdm import tqdm

documents = ["doc1", "doc2", "doc3", ...]

for doc in tqdm(documents, desc="Processing documents"):
    # Process each document
    embedding = ollama.embeddings(
        model='nomic-embed-text',
        prompt=doc
    )
    # Store embedding...
```

### Error Handling

```python
import ollama

def safe_generate(prompt, model='llama3.2:3b'):
    try:
        response = ollama.generate(
            model=model,
            prompt=prompt
        )
        return response['response']
    except Exception as e:
        return f"Error: {str(e)}"

# Usage
result = safe_generate("Hello!")
print(result)
```

### Check System Resources

```python
import psutil

def check_resources():
    # Memory
    mem = psutil.virtual_memory()
    print(f"Total RAM: {mem.total / (1024**3):.2f} GB")
    print(f"Available RAM: {mem.available / (1024**3):.2f} GB")
    print(f"RAM Usage: {mem.percent}%")

    # Disk
    disk = psutil.disk_usage('/')
    print(f"\nFree Disk: {disk.free / (1024**3):.2f} GB")

    # CPU
    print(f"\nCPU Usage: {psutil.cpu_percent()}%")

check_resources()
```

---

## 📊 Common Parameters

### ollama.generate()

```python
response = ollama.generate(
    model='llama3.2:3b',        # Model to use
    prompt='Your prompt here',   # Input text
    stream=False,                # Stream response? (True/False)
    options={
        'temperature': 0.7,      # Randomness (0.0-1.0)
        'top_p': 0.9,           # Nucleus sampling
        'top_k': 40,            # Top-k sampling
        'num_predict': 100,     # Max tokens to generate
    }
)
```

### ollama.chat()

```python
response = ollama.chat(
    model='llama3.2:3b',
    messages=[
        {'role': 'system', 'content': 'You are helpful assistant'},
        {'role': 'user', 'content': 'Hello!'},
    ],
    stream=False,
    options={
        'temperature': 0.7,
    }
)
```

### Temperature Guide

- **0.0-0.3**: Focused, deterministic (good for factual questions)
- **0.4-0.7**: Balanced (default, good for most tasks)
- **0.8-1.0**: Creative, random (good for creative writing)

---

## 🔧 Debugging

### Test Ollama Connection

```python
import ollama

try:
    models = ollama.list()
    print("✅ Ollama is working!")
    print(f"Available models: {len(models['models'])}")
except Exception as e:
    print(f"❌ Error: {e}")
    print("Make sure Ollama is running: ollama serve")
```

### Verbose Output

```python
import logging

logging.basicConfig(level=logging.DEBUG)

# Now run your code - you'll see detailed logs
```

### Measure Response Time

```python
import time
import ollama

start = time.time()
response = ollama.generate(
    model='llama3.2:3b',
    prompt='Tell me a short joke'
)
end = time.time()

print(f"Response time: {end - start:.2f} seconds")
print(f"Response: {response['response']}")
```

---

## 📖 Glossary

| Term | Definition |
|------|------------|
| **LLM** | Large Language Model - AI trained on text to generate human-like responses |
| **Embedding** | Vector representation of text that captures semantic meaning |
| **Vector Database** | Database optimized for storing and searching embeddings |
| **RAG** | Retrieval-Augmented Generation - combining search with LLM generation |
| **Prompt** | Input text given to an LLM |
| **Token** | Basic unit of text (roughly 1 word = 1-2 tokens) |
| **Temperature** | Controls randomness in generation (0=deterministic, 1=creative) |
| **Streaming** | Receiving response progressively instead of all at once |
| **Context Window** | Maximum amount of text an LLM can process at once |
| **Semantic Search** | Searching by meaning rather than exact keywords |
| **Cosine Similarity** | Measure of similarity between two vectors (embeddings) |
| **Quantization** | Compression technique to reduce model size |

---

## 🎓 Model Comparison

| Model | Size | RAM Needed | Speed | Quality | Best For |
|-------|------|------------|-------|---------|----------|
| llama3.2:1b | ~1.3GB | 4GB+ | ⚡⚡⚡ | ⭐⭐ | Testing, low-end hardware |
| llama3.2:3b | ~2GB | 8GB+ | ⚡⚡ | ⭐⭐⭐ | **Workshop default** - balanced |
| mistral:7b | ~4.1GB | 16GB+ | ⚡ | ⭐⭐⭐⭐ | Alternative to Llama |

---

## 🆘 Quick Fixes

| Problem | Quick Fix |
|---------|-----------|
| Ollama not found | Run: `ollama serve` |
| Model not found | Run: `ollama pull llama3.2:3b` |
| Import error | Run: `pip install -r requirements.txt` |
| Kernel died | Restart kernel, close other apps |
| Slow responses | Use smaller model (1b instead of 3b) |
| Out of memory | Close apps, use smaller model |
| No results from RAG | Check collection.count() > 0 |

---

## 📚 Resources

- **Ollama Docs**: https://ollama.ai/docs
- **ChromaDB Docs**: https://docs.trychroma.com/
- **Jinja2 Docs**: https://jinja.palletsprojects.com/
- **TROUBLESHOOTING.md**: Detailed troubleshooting guide in this repository

---

**📌 Tip**: Bookmark this page during the workshop for quick reference!

---

*Last updated: Workshop 2025*
