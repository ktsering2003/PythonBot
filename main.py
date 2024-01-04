from bot import related, send_message

if __name__ == "__main__":
    print("BOT: Hello! What is your name!")
    user_name = input()

    print(f"BOT: Nice meeting you {user_name}!")
    print("BOT: Ask a question!\nExamples:\n- Whats the weather\n- Play Game\n- Are you a robot?\n - Random Number Generator from 0 to 100\n- Exit")
    # \n means to use a new line
    while True:
        my_input = input() #input will ask you for a response in terminal
        my_input = my_input.lower() #puts your question into lower case, so that any weird capitalization situations don't cause an unwanted response

        related_text = related(my_input) #puts your inputted message in to the related function to find which question key in responses is similar to whatever your input was
        send_message(related_text) #bot sends a response depending on what your input was

        if my_input == "exit": #exits out of the program if you type out exit as your message
            exit() 