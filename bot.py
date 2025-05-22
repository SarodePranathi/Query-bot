import requests

API_KEY = "b0a115c4-c12f-4928-ad0f-36e2cc1acf1c"  # Replace with your AI21 API key
API_URL = "https://api.ai21.com/studio/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def chat_with_ai21(conversation):
    payload = {
        "model": "jamba-mini",
        "messages": conversation,
        "max_tokens": 150,
        "temperature": 0.7,
        "top_p": 1.0,
        "stop": ["\n"]
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        data = response.json()
        return data["choices"][0]["message"]["content"]
    else:
        return f"Error {response.status_code}: {response.text}"

def main():
    print("🤖 AI21 Jamba Chatbot - type 'exit' to quit")
    conversation = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        # Add user message to conversation
        conversation.append({"role": "user", "content": user_input})
        # Get bot response
        bot_reply = chat_with_ai21(conversation)
        print("Bot:", bot_reply)
        # Add bot reply to conversation
        conversation.append({"role": "assistant", "content": bot_reply})

if __name__ == "__main__":
    main()
