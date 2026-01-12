from collections import defaultdict
from typing import List, Dict, Any

# A dictionary to store chat history per chat_id
CHAT_MEMORY: Dict[str, List[Dict[str, str]]] = defaultdict(list)

def add(chat_id: str, role: str, content: str) -> None:
    """Add a message to the chat memory."""
    CHAT_MEMORY[chat_id].append({"role": role, "content": content})

def history(chat_id: str) -> List[Dict[str, str]]:
    """Retrieve the chat history for a given chat_id."""
    return CHAT_MEMORY[chat_id]

def clear(chat_id: str) -> None:
    """Clear the chat history for a given chat_id."""
    CHAT_MEMORY[chat_id] = []
