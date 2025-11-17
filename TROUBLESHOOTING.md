# Troubleshooting Guide

This guide covers common issues you might encounter during the Local LLM Workshop and how to resolve them.

---

## Table of Contents

1. [Ollama Issues](#ollama-issues)
2. [Model Issues](#model-issues)
3. [Python & Library Issues](#python--library-issues)
4. [Memory & Performance Issues](#memory--performance-issues)
5. [Jupyter Notebook Issues](#jupyter-notebook-issues)
6. [ChromaDB & RAG Issues](#chromadb--rag-issues)
7. [Network & Download Issues](#network--download-issues)
8. [Still Stuck?](#still-stuck)

---

## Ollama Issues

### ❌ "Connection refused" or "Cannot connect to Ollama"

**Symptoms:**
```
ConnectionError: Connection refused
Error: could not connect to ollama server
```

**Causes:**
- Ollama service is not running
- Ollama is running on a different port
- Firewall blocking connection

**Solutions:**

**1. Check if Ollama is running:**
```bash
ollama list
```

If this returns an error, Ollama isn't running.

**2. Start Ollama service:**

**macOS/Linux:**
```bash
ollama serve
```

**Windows:**
- Look for Ollama icon in system tray
- If not there, launch Ollama from Start Menu
- Or open a terminal and run: `ollama serve`

**3. Check Ollama status:**

After starting, verify it's working:
```bash
ollama list
```

You should see a list of models (or empty list if no models installed).

**4. Firewall issues:**

If you're on a corporate network or have strict firewall settings:
- Allow Ollama to accept local connections
- Default port is 11434
- Check with: `curl http://localhost:11434`

---

### ❌ Ollama service starts but immediately crashes

**Symptoms:**
- Ollama starts but closes after a few seconds
- Error messages about ports being in use

**Solutions:**

**1. Check if another instance is running:**

**macOS/Linux:**
```bash
ps aux | grep ollama
```

**Windows:**
```powershell
tasklist | findstr ollama
```

**2. Kill existing processes:**

**macOS/Linux:**
```bash
killall ollama
```

**Windows:**
```powershell
taskkill /IM ollama.exe /F
```

**3. Change the port (if default is in use):**

Start Ollama on a different port:
```bash
OLLAMA_HOST=0.0.0.0:11435 ollama serve
```

Then configure Python to use that port:
```python
import ollama
client = ollama.Client(host='http://localhost:11435')
```

---

## Model Issues

### ❌ "Model not found"

**Symptoms:**
```
Error: model 'llama3.2:3b' not found
404: model not found
```

**Cause:**
The model hasn't been downloaded yet.

**Solution:**

**Option 1: Download via command line (recommended):**
```bash
ollama pull llama3.2:3b
ollama pull nomic-embed-text
```

**Option 2: Download via Python:**
```python
import ollama
ollama.pull('llama3.2:3b')
ollama.pull('nomic-embed-text')
```

**Verify models are installed:**
```bash
ollama list
```

---

### ❌ Model download is very slow or stuck

**Symptoms:**
- Download speed is extremely slow
- Progress bar is stuck at certain percentage
- Download appears frozen

**Solutions:**

**1. Check your internet connection:**
```bash
# Test connection speed
curl -o /dev/null http://speedtest.wdc01.softlayer.com/downloads/test10.zip
```

**2. Restart the download:**
- Cancel current download (Ctrl+C)
- Try again: `ollama pull llama3.2:3b`

**3. Try a smaller model first:**
```bash
# Try the 1B model instead (much smaller)
ollama pull llama3.2:1b
```

**4. Download during off-peak hours:**
- Try early morning or late evening
- Network congestion might be the issue

**5. Check available disk space:**
```bash
# macOS/Linux
df -h

# Windows
wmic logicaldisk get size,freespace,caption
```

Models require:
- `llama3.2:1b`: ~1.3 GB
- `llama3.2:3b`: ~2 GB
- `llama3.2:7b`: ~4.7 GB

---

### ❌ "Model is too large for available memory"

**Symptoms:**
```
Error: model requires more memory than available
System appears to freeze when running model
```

**Cause:**
Model is too large for your system's RAM.

**Solutions:**

**1. Use a smaller model:**
```bash
# Instead of 3b, use 1b
ollama pull llama3.2:1b
```

Update your notebook code to use the smaller model:
```python
response = ollama.generate(
    model='llama3.2:1b',  # Changed from 3b
    prompt='Your prompt here'
)
```

**2. Close other applications:**
- Close browsers, IDEs, and other memory-intensive apps
- Restart your computer to free up RAM

**3. Check memory usage:**
```python
import psutil
mem = psutil.virtual_memory()
print(f"Available: {mem.available / (1024**3):.2f} GB")
```

**4. Adjust model parameters (advanced):**
```python
# Some Ollama configurations allow memory limits
# Check Ollama documentation for your version
```

---

## Python & Library Issues

### ❌ "ModuleNotFoundError: No module named 'ollama'"

**Symptoms:**
```python
ModuleNotFoundError: No module named 'ollama'
ImportError: cannot import name 'ollama'
```

**Cause:**
Python libraries not installed or wrong Python environment.

**Solutions:**

**1. Install requirements:**
```bash
pip install -r requirements.txt
```

**2. Verify installation:**
```bash
pip list | grep ollama
```

**3. Check Python version:**
```bash
python --version
```

Must be Python 3.8 or higher.

**4. Virtual environment issues:**

If using a virtual environment, make sure it's activated:
```bash
# Create venv (if not exists)
python -m venv venv

# Activate it
# macOS/Linux:
source venv/bin/activate

# Windows:
venv\Scripts\activate

# Install requirements in venv
pip install -r requirements.txt
```

**5. Jupyter kernel mismatch:**

If Jupyter uses a different Python than your terminal:
```bash
# Install ipykernel
pip install ipykernel

# Create kernel
python -m ipykernel install --user --name=workshop

# In Jupyter, select Kernel > Change Kernel > workshop
```

---

### ❌ Library version conflicts

**Symptoms:**
```
ERROR: pip's dependency resolver does not currently take into account...
Library X requires version Y but you have version Z
```

**Solution:**

**1. Upgrade pip first:**
```bash
pip install --upgrade pip
```

**2. Force reinstall all requirements:**
```bash
pip install -r requirements.txt --force-reinstall
```

**3. Use fresh virtual environment:**
```bash
# Remove old venv
rm -rf venv

# Create new one
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install fresh
pip install -r requirements.txt
```

---

## Memory & Performance Issues

### ⚠️ Model responses are very slow

**Symptoms:**
- Takes minutes to generate responses
- System becomes unresponsive
- Fans running at maximum

**Causes & Solutions:**

**1. Insufficient RAM:**

**Check available memory:**
```python
import psutil
mem = psutil.virtual_memory()
print(f"Available RAM: {mem.available / (1024**3):.2f} GB")
print(f"Total RAM: {mem.total / (1024**3):.2f} GB")
```

**Solution:**
- Use smaller model (1b instead of 3b)
- Close other applications
- Restart computer

**2. CPU-only inference (no GPU):**

Local models run on CPU by default, which is slower than GPU.

**Check if GPU is being used:**
- This depends on your Ollama installation
- Ollama will automatically use GPU if available
- NVIDIA GPUs: Check `nvidia-smi`
- Apple Silicon (M1/M2): Automatically optimized

**Solution:**
- If you have a GPU, ensure drivers are up to date
- Otherwise, accept that CPU inference is slower
- Use smaller models for faster responses

**3. System resources:**

**Monitor system load:**
```python
import psutil
print(f"CPU Usage: {psutil.cpu_percent()}%")
```

**Solution:**
- Close background applications
- Don't run multiple models simultaneously
- Use streaming for better perceived performance

---

### ⚠️ "Disk space is full"

**Symptoms:**
```
Error: no space left on device
OSError: [Errno 28] No space left on device
```

**Cause:**
Models and databases fill up disk space.

**Solutions:**

**1. Check disk space:**
```bash
# macOS/Linux
df -h

# Windows
wmic logicaldisk get size,freespace,caption
```

**2. Remove unused models:**
```bash
# List models
ollama list

# Remove unused models
ollama rm model-name
```

**3. Clear Ollama cache:**
```bash
# macOS
rm -rf ~/.ollama/models/*

# Linux
rm -rf /usr/share/ollama/.ollama/models/*

# Windows
del /s /q C:\Users\<username>\.ollama\models\*
```

**4. Clean ChromaDB data:**
```bash
# From workshop directory
rm -rf vector-db/
```

**Note:** After clearing, you'll need to re-download models!

---

## Jupyter Notebook Issues

### ❌ "Jupyter command not found"

**Symptoms:**
```bash
jupyter: command not found
```

**Solution:**

**1. Install Jupyter:**
```bash
pip install jupyter
```

**2. Verify installation:**
```bash
jupyter --version
```

**3. Check PATH:**

If installed but still not found:
```bash
# Find where pip installs packages
pip show jupyter

# Add to PATH (example for macOS/Linux)
export PATH="$HOME/.local/bin:$PATH"
```

---

### ❌ Kernel keeps dying or restarting

**Symptoms:**
- "The kernel appears to have died" message
- Notebook kernel constantly restarts
- Cells don't execute

**Causes & Solutions:**

**1. Memory exhaustion:**

Running out of RAM crashes the kernel.

**Solution:**
- Close other applications
- Use smaller models
- Restart Jupyter

**2. Infinite loops or errors in code:**

**Solution:**
- Kernel > Restart Kernel
- Check code for infinite loops
- Review error messages carefully

**3. Corrupted notebook:**

**Solution:**
- Create new notebook
- Copy cells manually (don't copy the whole file)

---

### ❌ Can't save notebook changes

**Symptoms:**
- Changes don't persist
- "Save failed" errors

**Solutions:**

**1. Check file permissions:**
```bash
ls -l *.ipynb
```

**2. Fix permissions:**
```bash
chmod 644 *.ipynb
```

**3. Disk space:**

Check if disk is full (see above).

---

## ChromaDB & RAG Issues

### ❌ "ChromaDB collection already exists"

**Symptoms:**
```
Collection 'made-with-cc' already exists
```

**Cause:**
Running the collection creation code multiple times.

**Solution:**

**Option 1: Delete existing collection:**
```python
import chromadb

client = chromadb.PersistentClient(path="./vector-db/made-with-cc")
client.delete_collection("made-with-cc")
```

**Option 2: Get existing collection instead:**
```python
# Instead of create_collection, use get_or_create_collection
collection = client.get_or_create_collection(
    name="made-with-cc",
    metadata={"hnsw:space": "cosine"}
)
```

**Option 3: Delete the directory:**
```bash
rm -rf vector-db/made-with-cc/
```

Then re-run the collection creation code.

---

### ❌ Vector search returns no results

**Symptoms:**
- Queries return empty results
- No similar documents found

**Causes & Solutions:**

**1. Collection is empty:**

**Check:**
```python
collection.count()  # Should return number of documents
```

**Solution:**
- Re-run the indexing cells
- Verify documents were added

**2. Wrong collection name:**

**Check:**
```python
client.list_collections()  # See all collections
```

**3. Embedding model mismatch:**

Make sure you're using the same model for:
- Indexing documents
- Querying

Both should use `nomic-embed-text`.

---

### ❌ "Embedding dimension mismatch"

**Symptoms:**
```
Error: Embedding dimension mismatch
Expected 768, got 384
```

**Cause:**
Using different embedding models for indexing vs. querying.

**Solution:**

**1. Use consistent model:**
```python
# For both indexing and querying
embedding_model = 'nomic-embed-text'
```

**2. Recreate collection:**
```bash
# Delete old collection
rm -rf vector-db/made-with-cc/

# Re-run notebook to recreate with consistent embeddings
```

---

## Network & Download Issues

### ❌ "Connection timeout" during downloads

**Symptoms:**
```
Error: connection timeout
Failed to download model
```

**Solutions:**

**1. Check internet connection:**
```bash
ping ollama.ai
```

**2. Retry with increased timeout:**

Some Ollama configurations allow timeout adjustments.

**3. Download during off-peak hours:**

Network congestion can cause timeouts.

**4. Use mobile hotspot:**

If corporate/school network blocks downloads, try phone hotspot.

---

### ❌ Firewall or proxy blocking connections

**Symptoms:**
- Downloads fail consistently
- Can't reach ollama.ai
- Proxy-related errors

**Solutions:**

**1. Configure proxy (if needed):**
```bash
export HTTP_PROXY=http://proxy.example.com:8080
export HTTPS_PROXY=http://proxy.example.com:8080
```

**2. Check corporate firewall:**

Contact IT department if on corporate network.

**3. Whitelist Ollama:**

Ask IT to whitelist:
- ollama.ai
- registry.ollama.ai

---

## Still Stuck?

### Pre-Workshop Checklist

Before asking for help, verify:

- [ ] Python 3.8+ installed: `python --version`
- [ ] Ollama installed: `ollama --version`
- [ ] Ollama running: `ollama list`
- [ ] Requirements installed: `pip list`
- [ ] Jupyter working: `jupyter --version`
- [ ] At least 8GB RAM available
- [ ] At least 20GB disk space free
- [ ] Internet connection working

### Getting Help

**1. Check error messages carefully:**
- Read the full error message
- Note the exact error type
- Look for file names and line numbers

**2. Search for similar issues:**
- Google the exact error message
- Check Ollama GitHub issues
- Check ChromaDB documentation

**3. Ask for help:**

When asking for help, provide:
- **Error message** (full text)
- **What you were trying to do** (which cell/step)
- **System info** (OS, RAM, Python version)
- **What you've tried** (troubleshooting steps)

**4. During the workshop:**
- Raise your hand
- Ask the instructor
- Help your neighbor (teaching reinforces learning!)

**5. After the workshop:**
- Open a GitHub issue
- Include screenshots if helpful
- Tag with appropriate labels

---

## Quick Reference

### Essential Commands

```bash
# Check Ollama status
ollama list

# Start Ollama
ollama serve

# Download model
ollama pull llama3.2:3b

# Check Python version
python --version

# Install requirements
pip install -r requirements.txt

# Start Jupyter
jupyter notebook

# Check disk space (macOS/Linux)
df -h

# Check disk space (Windows)
wmic logicaldisk get size,freespace,caption

# Check RAM usage
python -c "import psutil; print(f'{psutil.virtual_memory().available/(1024**3):.1f} GB available')"
```

### Emergency Reset

If everything is broken and you want to start fresh:

```bash
# 1. Stop Ollama
killall ollama  # macOS/Linux
# or close Ollama app on Windows

# 2. Delete workshop directory
cd ..
rm -rf llm-workshop-notebooks

# 3. Clone fresh copy
git clone https://github.com/nishad/llm-workshop-notebooks
cd llm-workshop-notebooks

# 4. Create new virtual environment
python -m venv venv
source venv/bin/activate  # macOS/Linux
# or venv\Scripts\activate on Windows

# 5. Install requirements
pip install -r requirements.txt

# 6. Start Ollama
ollama serve

# 7. Download models
ollama pull llama3.2:3b
ollama pull nomic-embed-text

# 8. Start Jupyter
jupyter notebook

# 9. Open 00_setup-and-verification.ipynb
```

---

## Debugging Tips

### Enable Verbose Logging

**Ollama:**
```bash
OLLAMA_DEBUG=1 ollama serve
```

**Python:**
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Check System Resources

```python
import psutil

print(f"CPU: {psutil.cpu_percent()}%")
print(f"RAM: {psutil.virtual_memory().percent}%")
print(f"Disk: {psutil.disk_usage('/').percent}%")
```

### Test Ollama Connectivity

```python
import ollama

try:
    models = ollama.list()
    print("✅ Ollama is working!")
    print(f"Models: {len(models.get('models', []))}")
except Exception as e:
    print(f"❌ Ollama error: {e}")
```

---

**Remember**: Most issues are simple configuration problems. Take a breath, read error messages carefully, and work through the solutions systematically. You've got this! 🚀
