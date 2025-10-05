from nlp_scripts.preprocess import preprocess_text

def simple_chatbot(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hi there! How can I help you?"
    elif "name" in user_input:
        return "I’m your Week 1 Chatbot prototype "
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        processed = preprocess_text(user_input)
        return f"I don’t understand yet. But I tokenized your input: {processed['tokens']}"

# Conversation loop
if __name__ == "__main__":
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user = input("You: ")
        if user.lower() == "bye":
            print("Chatbot: Goodbye!")
            break
        print("Chatbot:", simple_chatbot(user))