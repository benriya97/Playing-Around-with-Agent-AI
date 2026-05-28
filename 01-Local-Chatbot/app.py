from ollama import chat

print("--- Upgraded Local AI Chatbot (With Memory) ---")
print("Type 'exit' to quit.\n")

# This list will hold the entire conversation history
messages_history = []

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break

    # 1. Add YOUR new message to the history list
    messages_history.append({"role": "user", "content": user_input})

    # 2. Send the ENTIRE history to Llama 3 so it remembers the past
    response = chat(
        model="llama3",
        messages=messages_history
    )

    ai_response = response["message"]["content"]
    print("\nAI:", ai_response)
    print("-" * 30)

    # 3. Add the AI's response to the history list too!
    messages_history.append({"role": "assistant", "content": ai_response})