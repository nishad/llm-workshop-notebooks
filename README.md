# Getting Started with Local LLMs Workshop Notebooks

This repository contains supporting resources for the workshop **"Getting Started with Local LLMs"**, presented by **Nishad Thalhath** (ORCID: [0000-0001-9845-9714](https://orcid.org/0000-0001-9845-9714)). The workshop introduces participants to the setup and usage of local large language models (LLMs) using open-source tools.

## Abstract

Local large language models (LLMs) are becoming popular due to their privacy-first approach, security, and cost-effectiveness. This workshop introduces participants to the basics of setting up and running local LLMs using open-source tools.

The workshop covers both basic and intermediate topics:
- **Part 1**: Introduction to LLMs, setting up local LLMs, selecting tools and models, and fundamental prompting techniques.
- **Part 2**: Programmatically using local LLMs, automating tasks, vector embeddings, semantic search, and Retrieval-Augmented Generation (RAG) basics.

This hands-on workshop allows participants to set up their local LLMs during the session or follow up later with the provided materials. It is designed for beginners and those seeking intermediate-level knowledge, making it suitable for participants at various stages of their journey with local LLMs.

### Prerequisites

#### System Requirements
- **Operating System**: Windows, macOS, or Linux
- **RAM**: At least 8GB (16GB recommended for better performance)
- **Disk Space**: At least 20GB free (for models and libraries)
- **Internet**: Stable connection for initial setup and model downloads
- **Python**: Version 3.8 or higher
- **Ollama**: Installed and running (see installation instructions below)

#### Knowledge Requirements
- **Part 1**: No prior AI/ML knowledge required - beginner friendly!
- **Part 2**: Basic Python programming familiarity helpful but not required

#### Time Requirements
- **Pre-workshop setup**: 30-60 minutes (do this before attending!)
- **Workshop duration**: 2-3 hours (hands-on)

## Repository Contents

### Notebooks

#### 0. `00_setup-and-verification.ipynb` ⏱️ 30 minutes
**Part 1A: Setup, Verification & LLM Fundamentals**

This notebook covers the essential foundation:
- **What are LLMs?** Understanding concepts and architecture
- **Local vs. Cloud LLMs**: Trade-offs and benefits
- **Environment verification**: System readiness checks
- **Model selection guide**: Choosing the right model for your needs
- **Automated setup**: Download and prepare required models
- **Troubleshooting**: Fix common setup issues

**🎯 Start here if you're attending the workshop!**

#### 1. `01_using-ollama-with-python.ipynb` ⏱️ 30 minutes
**Part 1B: Using Ollama with Python**

This notebook introduces the **Ollama** Python library:
- Installing and setting up Ollama
- Interacting with models for text generation
- Understanding streaming responses
- Retrieving and understanding model metadata
- Prompt engineering basics

#### 2. `02_introduction-to-rag-with-ollama.ipynb` ⏱️ 60 minutes
**Part 2: Retrieval-Augmented Generation**

This notebook demonstrates a complete **RAG pipeline**:
- **Vector embeddings**: Understanding semantic representations
- **ChromaDB**: Setting up persistent vector database
- **Semantic search**: Finding relevant information by meaning
- **RAG implementation**: Combining retrieval with generation
- **Jinja2 templates**: Creating structured, dynamic prompts
- **Comparison**: With and without external knowledge

### Supporting Files

- **`requirements.txt`**: Python dependencies for easy installation
- **`TROUBLESHOOTING.md`**: Common issues and solutions
- **`CHEAT_SHEET.md`**: Quick reference guide
- **`made-with-cc.txt`**: Sample dataset (Creative Commons licensed)

## Quick Start Guide

### Pre-Workshop Setup (Do This First! ⏱️ 30-60 minutes)

**It's highly recommended to complete this setup before attending the workshop** to avoid network/download issues during the session.

#### Step 1: Install Ollama

**macOS:**
```bash
brew install ollama
```

**Linux:**
```bash
curl https://ollama.ai/install.sh | sh
```

**Windows:**
- Download from: https://ollama.com/download
- Run the installer
- Ollama will start automatically

**Verify Installation:**
```bash
ollama --version
```

#### Step 2: Start Ollama Service

**macOS/Linux:**
```bash
ollama serve
```
*Leave this terminal running, or run Ollama from Applications*

**Windows:**
- Ollama starts automatically
- Check system tray for Ollama icon

#### Step 3: Clone This Repository

```bash
git clone https://github.com/nishad/llm-workshop-notebooks
cd llm-workshop-notebooks
```

#### Step 4: Install Python Dependencies

```bash
pip install -r requirements.txt
```

This installs: `ollama`, `chromadb`, `Jinja2`, `jupyter`, `ipython`, `psutil`, `tqdm`

#### Step 5: Start Jupyter

```bash
jupyter notebook
```

This will open your browser with the notebook interface.

#### Step 6: Run Setup Notebook

1. Open `00_setup-and-verification.ipynb`
2. Run all cells (Cell → Run All)
3. This will:
   - Verify your environment
   - Download required models (~2.3GB)
   - Confirm everything is ready

**✅ If all checks pass, you're ready for the workshop!**

---

### During the Workshop

Follow the notebooks in order:

1. **Notebook 00**: Setup & Fundamentals (30 min)
   - *Skip if you completed pre-workshop setup*
   - Or review the LLM concepts section

2. **Notebook 01**: Using Ollama with Python (30 min)
   - Basic model interaction
   - Streaming responses
   - Prompt engineering

3. **Notebook 02**: Introduction to RAG (60 min)
   - Vector embeddings
   - Semantic search
   - Complete RAG pipeline

---

### Self-Paced Learning

If you're working through this on your own:

1. Start with `00_setup-and-verification.ipynb`
2. Take your time with each section
3. Experiment with the code cells
4. Try the "Try It Yourself" challenges
5. Refer to `TROUBLESHOOTING.md` if you encounter issues

## Troubleshooting

### Common Issues

#### "Connection refused" or "Ollama not responding"

**Problem**: Can't connect to Ollama service

**Solution**:
```bash
# Check if Ollama is running
ollama list

# If not, start it
ollama serve
```

#### "Model not found"

**Problem**: Model hasn't been downloaded

**Solution**:
```bash
ollama pull llama3.2:3b
ollama pull nomic-embed-text
```

#### "Not enough memory"

**Problem**: System RAM is insufficient

**Solution**:
- Close other applications
- Use a smaller model: `llama3.2:1b` instead of `llama3.2:3b`
- Consider upgrading RAM or using a more powerful machine

#### Python/Library Issues

**Problem**: Import errors or missing packages

**Solution**:
```bash
# Upgrade pip
pip install --upgrade pip

# Reinstall requirements
pip install -r requirements.txt --force-reinstall
```

**For more detailed troubleshooting, see `TROUBLESHOOTING.md`**

---

## Resources

### Official Documentation
- [Ollama](https://ollama.ai/) - Main website and downloads
- [Ollama Python Library](https://github.com/ollama/ollama-python) - Python client documentation
- [ChromaDB](https://www.trychroma.com/) - Vector database documentation
- [Jinja2](https://jinja.palletsprojects.com/) - Template engine documentation

### Learning Resources
- [Ollama Model Library](https://ollama.ai/library) - Browse available models
- [ChromaDB Cookbook](https://cookbook.chromadb.dev/) - Practical examples
- [Prompt Engineering Guide](https://www.promptingguide.ai/) - Improve your prompts

### Datasets
- [Made with Creative Commons](https://creativecommons.org/share-your-work/made-with-cc/) - Dataset source for RAG examples

---

## Acknowledgments

This workshop was made possible by supporters via Kickstarter. Their feedback helped shape these materials to be more accessible and practical.

Special thanks to:
- The Ollama team for making local LLMs accessible
- The open-source community for ChromaDB, Jinja2, and countless other tools
- Creative Commons for the example dataset

---

## License

This repository is licensed under the **MIT License**.

The dataset used in the examples (`made-with-cc.txt`) is sourced from **"Made with Creative Commons"** and is licensed under **Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)**.

---

## Contributing

Found an issue? Have a suggestion?

- **Issues**: Please open an issue on GitHub
- **Improvements**: Pull requests are welcome!
- **Questions**: Feel free to start a discussion

---

## Author

**Nishad Thalhath**
ORCID: [0000-0001-9845-9714](https://orcid.org/0000-0001-9845-9714)

---

**Happy Learning! 🚀**
