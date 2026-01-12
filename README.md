# RAG Chat App (LangChain v1 + Streamlit)

This is a **ChatGPT-style RAG chatbot** built with:

- **Static RAG** using a PDF (`full_moon.pdf`)
- **LangChain v1**
- **Dynamic system prompts**
- **Dynamic structured output schemas**
- **Conversation memory per chat**
- **Streamlit frontend** for ChatGPT-like UI
- **New Chat** button

---

## How to run project
- **1.uv add -r requirements.py**
- **2.uv run ingest.py**
- **3.uvicorn backend.app:app --reload**
- **4.streamlit run streamlit_app.py**

