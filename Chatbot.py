# Basic Chatbot
# CodeAlpha Python Programming Internship - Task 4

def chatbot():
    print("================================")
    print("       Welcome to Chatbot       ")
    print("================================")
    print("Type 'hello', 'how are you', or 'bye'")
    print()

    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "hello":
            print("Bot: Hi!")

        elif user_input == "how are you":
            print("Bot: I'm fine, thanks!")

        elif user_input == "bye":
            print("Bot: Goodbye!")
            break

        else:
            print("Bot: Sorry, I don't understand that.")


chatbot()