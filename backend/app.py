from fastapi import FastAPI
from pydantic import BaseModel
from uuid import uuid4

from backend.rag.memory import add, history, clear
from backend.rag.classifier import classify
from backend.rag.router import route
from backend.rag.chain import build_chain

app = FastAPI()


class AskRequest(BaseModel):
    chat_id: str
    question: str


class ClearRequest(BaseModel):
    chat_id: str


@app.post("/new_chat")
def new_chat():
    return {"chat_id": str(uuid4())}


@app.post("/ask")
def ask(request: AskRequest):
    chat_id = request.chat_id
    question = request.question

    add(chat_id, "user", question)

    try:
        q_type = classify(question)
        system_prompt, _ = route(q_type)

        chain = build_chain(system_prompt)

        # ✅ Convert history to STRING ONLY
        chat_history = history(chat_id)
        history_text = "\n".join(
            f"{m['role'].capitalize()}: {str(m['content'])}" for m in chat_history
        )

        response = chain.invoke({"history": history_text, "question": question})

        # ✅ FORCE STRING RESPONSE
        response_text = (
            response.content if hasattr(response, "content") else str(response)
        )

        add(chat_id, "assistant", response_text)

        return {"type": q_type, "response": response_text, "history": history(chat_id)}

    except Exception as e:
        return {
            "type": "error",
            "response": f"Backend error: {str(e)}",
            "history": history(chat_id),
        }


@app.post("/clear")
def clear_chat(request: ClearRequest):
    clear(request.chat_id)
    return {"status": "cleared"}
