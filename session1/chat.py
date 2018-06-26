# chat.py - session 1 activty
# the goal of this activity is to use all the fundamental building block of programming,
# but in Python!

# Tasks
# 1) Complete the ChatBot's hi method to get the bot to say "hi" instead.
# Change the bot's response to that method
# 2) Change the respond method to reply "hello" if the user writes a message with < 10 characters
# else respond with "hi"
# 3) Create a new function that is triggered if the user writes a string containing the string
# "your name", and have the bot respond with a name of your choice!
# Hint: look up 'python substrings'
# 4) In the random method, use the list of phrases to respond with a random fact about the bot if 
# a user responds with a string with the word 'fact' it in.
#      ex:  me: "give me a fact about yourself"
#           bot: "my favorite number is 3.14"
#      hint: https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list
# 5) Lastly, create a new function that uses a for loop to write "VAI BRAZIL!!" 100 times when
# the user mentions the words "futebol", "football", or "world cup"

# Challenge: If you get through these tasks rather quickly, expand on this chat bot! Make it more
# interactive. For example, connect to an API to get cool data, or load in a JSON file of text to
# generate responses from. Be creative!

import random

class ChatBot():
    def __init__(self):
        self.response = None
    def respond(self, message):
        self.hello()
        print "bot:" + self.response
    def hello(self):
        self.response = "hello!"
    def hi(self):
        pass
    def random(self):
        #make a list of phrases here
        phrases = ["my favorite number is 3.14", "my favorite color is black - like my soul", "my favorite food is RAM", "The sky is blue", "Every day can be a good day"]
        # import random and add random.choice function commented here
        pass


bot = ChatBot()

while True:
    input = raw_input("me: ")
    bot.respond(input)
