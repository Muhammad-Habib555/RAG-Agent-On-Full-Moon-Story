import requests

API_URL = "http://localhost:8000"

def validate_response(resp_json):
    """
    Check the response structure based on 'type'.
    """
    rtype = resp_json.get("type")
    content = resp_json.get("response")
    history = resp_json.get("history")

    assert history is not None, "Chat history should exist"
    assert isinstance(history, list), "Chat history must be a list"

    if rtype == "qa":
        # QAResponse expects 'answer' and 'sources'
        assert content is not None, "QA response must have content"
    elif rtype == "summary":
        # SummaryResponse expects 'summary' and 'key_points'
        assert content is not None, "Summary response must have content"
    elif rtype == "comparison":
        # ComparisonResponse expects 'similarities' and 'differences'
        assert content is not None, "Comparison response must have content"
    else:
        raise AssertionError(f"Unknown response type: {rtype}")

def main():
    # 1️⃣ Create a new chat
    res = requests.post(f"{API_URL}/new_chat")
    res.raise_for_status()
    chat_id = res.json()["chat_id"]
    print(f"Chat ID: {chat_id}")

    # 2️⃣ Sample questions
    test_cases = [
        ("What is the historical significance of the full moon?", "qa"),
        ("Summarize the full moon document", "summary"),
        ("Compare the phases of the moon", "comparison"),
    ]

    # 3️⃣ Ask questions and validate responses
    for question, expected_type in test_cases:
        res = requests.post(f"{API_URL}/ask", json={"chat_id": chat_id, "question": question})
        res.raise_for_status()
        data = res.json()

        print(f"Testing question: {question}")
        print(f"Response type: {data['type']}")
        validate_response(data)
        assert data['type'] == expected_type, f"Expected {expected_type}, got {data['type']}"
        print("✅ Passed\n")

    # 4️⃣ Clear chat
    res = requests.post(f"{API_URL}/clear", json={"chat_id": chat_id})
    res.raise_for_status()
    print("Chat cleared successfully.")

if __name__ == "__main__":
    main()
