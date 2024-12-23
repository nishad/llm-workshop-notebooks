# Getting Started with Local LLMs

This repository contains supporting resources for the workshop **"Getting Started with Local LLMs"**, presented by **Nishad Thalhath** (ORCID: [0000-0001-9845-9714](https://orcid.org/0000-0001-9845-9714)). The workshop introduces participants to the setup and usage of local large language models (LLMs) using open-source tools.

## Abstract

Local large language models (LLMs) are becoming popular due to their privacy-first approach, security, and cost-effectiveness. This workshop introduces participants to the basics of setting up and running local LLMs using open-source tools.

The workshop covers both basic and intermediate topics:
- **Part 1**: Introduction to LLMs, setting up local LLMs, selecting tools and models, and fundamental prompting techniques.
- **Part 2**: Programmatically using local LLMs, automating tasks, vector embeddings, semantic search, and Retrieval-Augmented Generation (RAG) basics.

This hands-on workshop allows participants to set up their local LLMs during the session or follow up later with the provided materials. It is designed for beginners and those seeking intermediate-level knowledge, making it suitable for participants at various stages of their journey with local LLMs.

### Requirements

Participants are expected to have:
- A computer with at least **8GB RAM** and **20GB free disk space**.
- A recent version of Python installed with Jupyter Notebook support.
- Basic understanding of Python programming (for Part 2).
- A stable internet connection for downloading models and tools.

## Repository Contents

### Notebooks

#### 1. `01_using-ollama-with-python.ipynb`
This notebook introduces the **Ollama** Python library and provides a step-by-step guide on:
- Installing and setting up Ollama.
- Interacting with models for text generation and embedding creation.
- Retrieving and understanding metadata of available models.
- Streaming dynamic Markdown responses.

#### 2. `02_introduction-to-rag-with-ollama.ipynb`
This notebook demonstrates how to implement a **Retrieval-Augmented Generation (RAG)** pipeline using:
- **ChromaDB** for embedding storage and retrieval.
- **Jinja2** for creating structured prompts.
- **Ollama** for embedding generation and context-aware responses.

Topics covered include:
- Setting up a persistent vector database to avoid re-indexing data.
- Retrieving relevant paragraphs for context-aware prompts.
- Comparing model outputs with and without external knowledge augmentation.

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/nishad/llm-workshop-notebooks
   ```
2. Navigate to the repository:
   ```bash
   cd llm-workshop-notebooks
   ```
3. Install required packages:
   ```bash
   pip install jupyter
   ```
4. Open the notebooks in Jupyter Notebook or JupyterLab:
   ```bash
   jupyter notebook
   ```
5. Follow the notebooks:
   - Start with `01_using-ollama-with-python.ipynb` for basic concepts.
   - Proceed to `02_introduction-to-rag-with-ollama.ipynb` for advanced RAG workflows.

## Resources

- [Ollama Python Library Documentation](https://github.com/ollama/ollama-python)
- [ChromaDB](https://www.trychroma.com/)
- [Jinja2 Documentation](https://jinja.palletsprojects.com/)
- [Creative Commons: Made with Creative Commons](https://creativecommons.org/share-your-work/made-with-cc/)

## License

This repository is licensed under the MIT License. The dataset used in the examples is sourced from **"Made with Creative Commons"** and is licensed under Creative Commons Attribution.
