""" Kunsang Tsering """
# main.py
from bot import related, send_message
from api import get_weather

if __name__ == "__main__":
    # Main script for interacting with the bot
    print("BOT: Hello! What is your name!")
    user_name = input()

    print(f"BOT: Nice meeting you {user_name}!")
    print("BOT: Ask a question!\nExamples:\n- What's the weather\n- Play Game\n- Are you a robot?")

    while True:
        my_input = input().lower()
        related_text = related(my_input)

        if related_text == "whats today's weather?":
            # If the user asks about the weather, get weather information and send the message
            weather_info = get_weather()
            send_message(weather_info)
        else:
            # Otherwise, send the response based on the user input
            send_message(related_text)

        if my_input == "exit":
            # If the user inputs 'exit', exit the program
            exit()
