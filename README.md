# 🌕 RAG-Agent-On-Full-Moon-Story

![Project Banner](https://img.shields.io/badge/Project-RAG--Agent-blue?style=for-the-badge)  
![Python Version](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge)  

---

## 🔹 Project Overview

**RAG-Agent-On-Full-Moon-Story** is a Retrieval-Augmented Generation (RAG) project designed to process story data, perform AI-powered queries, and serve results via a **Streamlit web interface**.  

This project includes:

- Modular **backend** for RAG operations
- **Vector database** integration
- **AI query processing**
- User-friendly **Streamlit frontend**
- Pre-configured **testing scripts**

It is designed for easy setup and usage by developers or enthusiasts.

---

## 🚀 Features

- 🧠 AI-powered story retrieval and classification  
- 🗄️ Vector DB support for fast semantic search  
- 🧩 Modular and maintainable Python architecture  
- 🌐 Web-based interface via Streamlit  
- 🧪 Built-in testing support

---

## 📂 Project Structure

```text
RAG-Agent-On-Full-Moon-Story/
│
├─ backend/
│   ├─ __init__.py
│   ├─ app.py
│   ├─ config.py
│   └─ rag/
│       ├─ __init__.py
│       ├─ chain.py
│       ├─ classifier.py
│       ├─ memory.py
│       ├─ prompts.py
│       ├─ retriever.py
│       ├─ router.py
│       └─ schemas.py
│
├─ ingest.py
├─ streamlit_app.py
├─ requirements.txt
├─ pyproject.toml
├─ .gitignore
├─ .python-version
├─ uv.lock
└─ test/
    └─ test_file.py

## 📂 How to Run Project

Follow these commands step-by-step:

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run data ingestion
python ingest.py

# 3. Start backend server
uvicorn backend.app:app --reload

# 4. Launch Streamlit frontend
streamlit run streamlit_app.py


