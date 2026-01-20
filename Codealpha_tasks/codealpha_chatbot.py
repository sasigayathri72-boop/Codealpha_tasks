def chatbot():
    print("🤖 Chatbot: Hello! I am RuleBot.")
    print("I can help you with greetings, time, date, basic questions.")
    print("Type 'menu' to see options or 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower()

        # Exit condition
        if user_input == "bye":
            print("🤖 Chatbot: Goodbye! Have a great day 😊")
            break

        # Greetings
        elif user_input in ["hi", "hello", "hey"]:
            print("🤖 Chatbot: Hello! How can I help you?")

        # Asking name
        elif "your name" in user_input:
            print("🤖 Chatbot: My name is RuleBot. I am a rule-based chatbot.")

        # How are you
        elif "how are you" in user_input:
            print("🤖 Chatbot: I'm doing well! Thanks for asking.")

        # Help / Menu
        elif user_input == "menu" or "help" in user_input:
            print("🤖 Chatbot Menu:")
            print("1. hi / hello")
            print("2. your name")
            print("3. time")
            print("4. date")
            print("5. how are you")
            print("6. bye")

        # Time
        elif "time" in user_input:
            from datetime import datetime
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"🤖 Chatbot: Current time is {current_time}")

        # Date
        elif "date" in user_input:
            from datetime import datetime
            today = datetime.now().strftime("%d-%m-%Y")
            print(f"🤖 Chatbot: Today's date is {today}")

        # Thanks
        elif "thank" in user_input:
            print("🤖 Chatbot: You're welcome! 😊")

        # Default response
        else:
            print("🤖 Chatbot: Sorry, I don't understand that. Type 'menu' for options.")

# Run the chatbot
chatbot()