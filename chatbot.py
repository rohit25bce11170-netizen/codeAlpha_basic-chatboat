def get_bot_response(user_input):
    """
    Processes the user input and returns a predefined response.
    Handles basic text normalization by converting to lowercase and stripping spaces.
    """
    # Normalize input
    cleaned_input = user_input.strip().lower()
    
    # Predefined rule-based logic
    if cleaned_input in ["hello", "hi", "hey", "he11o"]:
        return "Hi!"
    elif cleaned_input in ["how are you", "how's it going", "how are you doing"]:
        return "I'm fine, thanks!"
    elif cleaned_input in ["bye", "goodbye", "exit"]:
        return "Goodbye!"
    else:
        return "I'm sorry, I don't understand that. Try saying 'hello', 'how are you', or 'bye'."

def main():
    """
    Main function to run the chatbot loop.
    """
    print("=========================================")
    print("      Welcome to the Basic Chatbot!      ")
    print("   Type 'bye' or 'exit' to end the chat. ")
    print("=========================================\n")
    
    while True:
        # Get input from user
        user_text = input("You: ")
        
        # Process response
        response = get_bot_response(user_text)
        print(f"Bot: {response}")
        
        # Terminate loop if the user wants to say goodbye
        if user_text.strip().lower() in ["bye", "goodbye", "exit"]:
            break

if __name__ == "__main__":
    main()
