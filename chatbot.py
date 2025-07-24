def chatbot():
    
    name= input("Hello! What's your name?")
    print(f"ChatBot: Welcome, {name}! Type something to start chatting (type 'bye' to exit)\n")
    while True:
        user_input = input(f"{name}: ").lower()

        if "hello" in user_input or "hi" in user_input:
            print(f"ChatBot: Hello {name}! How can I help you today?")
        
        elif "how are you" in user_input:
            print("ChatBot: I'm just code, but I'm doing great! Thanks for asking.")
        
        elif "your name" in user_input:
            print("ChatBot: I am a ChatBot!")
        
        elif "thank" in user_input:
            print("ChatBot: You're most welcome!")

        elif "what can you do" in user_input:
            print("ChatBot: I can chat, crack jokes, answer simple questions, and keep you company!")
        
        elif "tell me a joke" in user_input:
            print("ChatBot: Why did the computer go to therapy? Because it had too many bytes from its past! ")

        elif "help" in user_input:
            print("ChatBot: You can try saying: hello, how are you, tell me a joke, what's your name, bye...")
        
        elif "bye" in user_input:
            print("ChatBot: Bye! Have a great day ahead.")
            break
        
        else:
            print("ChatBot: I'm sorry, I didn't understand that. Can you rephrase?")
chatbot()