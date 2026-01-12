import streamlit as st
import requests

API = "http://localhost:8000"

# --- Page Config ---
st.set_page_config(page_title="RAG Chat", layout="wide")

# --- Initialize Session State ---
if "chat_id" not in st.session_state:
    try:
        res = requests.post(f"{API}/new_chat")
        res.raise_for_status()
        st.session_state.chat_id = res.json()["chat_id"]
        st.session_state.messages = []
    except Exception as e:
        st.error(f"Failed to start a new chat: {e}")
        st.stop()

# --- Sidebar ---
with st.sidebar:
    st.title("📘 RAG Chatbot")
    if st.button("➕ New Chat"):
        try:
            res = requests.post(f"{API}/new_chat")
            res.raise_for_status()
            st.session_state.chat_id = res.json()["chat_id"]
            st.session_state.messages = []
            st.rerun()
        except Exception as e:
            st.error(f"Failed to start a new chat: {e}")

# --- Title ---
st.title("💬 RAG Chatbot (Static)")

# --- Display Chat Messages ---
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --- Chat Input ---
prompt = st.chat_input("Ask something...")
if prompt:
    # Add user message immediately
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Show thinking indicator while waiting
    with st.spinner("🤔 Thinking..."):
        try:
            res = requests.post(
                f"{API}/ask",
                json={"chat_id": st.session_state.chat_id, "question": prompt},
            )
            res.raise_for_status()
            data = res.json()

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": data.get("response", "No response from API."),
                }
            )

        except requests.exceptions.RequestException as e:
            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": "❌ Could not get a response from the API.",
                }
            )
            st.error(f"Request failed: {e}")

        except ValueError:
            st.session_state.messages.append(
                {"role": "assistant", "content": f"❌ Invalid response:\n{res.text}"}
            )
            st.error("Received invalid JSON from API.")

    # Refresh UI
    st.rerun()
