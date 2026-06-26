def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input in ["hello", "hi", "hey"]:
            print("Chatbot: Hii!")

        elif user_input in ["how are you", "how are you?"]:
            print("Chatbot: I'm fine, thanks!")

        elif user_input in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye!")
            break

        elif user_input == "":
            print("Chatbot: Say something...")

        else:
            print("Chatbot: I don't understand that.")
chatbot()