#import section, which lets you use the random functions from the random library, and lets you import functions from other files (in this case from rps.py)
import random
from rps import rock_paper_scissors_game

# ---------------- CONSTANTS -------------------------------
WEATHER = "rainy"
lower_bound, upper_bound = 0, 100
RESPONSES = { #Dictionary with question as key, and a list of responses as values
  "whats today's weather?":[
    f"The weather is {WEATHER}",
    f"It's {WEATHER} today",
    f"Let me check, it looks {WEATHER} out"
  ],

  "Are you a robot?":[
    "what do you think?",
    "Maybe yes, maybe no",
    "Yes, im a robot with human feelings"
  ],

  "exit":[
    "Bye, see you later"
  ],

  "number": [
    "The random number is : " + str(random.randint(lower_bound, upper_bound))
  ],

  "default":
    "sorry I didnt understand that?"

  
}

# ---------------- BOT HELPERS -----------------------------------

def respond(message): 
  #randomly chooses ONE response from the value list of the corresponding question
  if message in RESPONSES: 
    bot_message = random.choice(RESPONSES[message]) 
    #RESPONSES[message] will choose the list of responses to a key. One example in our code we have RESPONSES["what's today's weather"] ==  [f"The weather is {Weather" , f"It's {Weather} today", f"Let mecheck, it looks {WEATHER} today"}. Random.choice will then randomly choose one of the strings that are in this list to display as a response to your question
  else: 
    #If the question type in by the use is not one of the other 3 options asking for weather, robotness, or to leave the program, then the program will go to RESPONSES['default'], which just asks you to ask a new question
    bot_message = RESPONSES["default"]
  #returning bot_message will give this function an output of ONE string, that comes from one of the lists in RESPONSES
  return bot_message

# this function will map the key words in the input to a response
def related(x_text): 
  if "weather" in x_text: #checks if your message has the word weather inside, if it does, it defaults to asking 'What's today's weather?' which is defined in responses
    y_text = "whats today's weather?"
  elif "robot" in x_text: #similar idea as above, but with the word robot
    y_text = "Are you a robot?"
  elif "exit" in x_text: #similar idea as above, but with the word exit
    y_text = "exit"
  elif "game" in x_text: #similar idea as above, but with the word game, to initiate the rock_paper_scissors_game() function from the rps.py file you made
    rock_paper_scissors_game()
  elif "number" in x_text:
    y_text = "number"
  else: #if your message doesn't contain any of the words above, your message is treated as a blank message
    y_text = ""
  return y_text #output for the function 'related', becomes one of the strings from the keys of dictionary RESPONSES,

def send_message(message): 
  print(f"USER: {message}") #will retype out whatever you said as the key in RESPONSES
  response = respond(message) #uses whatever you typed as a parameter for respond function
  print(f"BOT: {response}") #will print out bot's response to your question
