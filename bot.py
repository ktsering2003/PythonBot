# bot.py

import random
from rps import rock_paper_scissors_game

# Constants
WEATHER = "rainy"

# Responses dictionary for different user inputs
RESPONSES = {
    "whats today's weather?": [
        f"The weather is {WEATHER}",
        f"It's {WEATHER} today",
        f"Let me check, it looks {WEATHER} out"
    ],
    "Are you a robot?": [
        "What do you think?",
        "Maybe yes, maybe no",
        "Yes, I'm a robot with human feelings"
    ],
    "exit": [
        "Bye, see you later"
    ],
    "default": "Sorry, I didn't understand that?"
}


def respond(message):
    # Function to respond based on user input
    if message in RESPONSES:
        bot_message = random.choice(RESPONSES[message])
    else:
        bot_message = RESPONSES["default"]
    return bot_message


def related(x_text):
    # Function to map keywords in the input to a response
    if "weather" in x_text:
        y_text = "whats today's weather?"
    elif "robot" in x_text:
        y_text = "Are you a robot?"
    elif "exit" in x_text:
        y_text = "exit"
    elif "game" in x_text:
        rock_paper_scissors_game()
    else:
        y_text = ""
    return y_text


def send_message(message):
    # Function to send messages to the user
    if isinstance(message, dict):
        # If the message is a dictionary (weather information), print each key-value pair
        for key, value in message.items():
            print(f"BOT: {key}: {value}")
    else:
        # If the message is a string, print the string
        print(f"BOT: {message}")
