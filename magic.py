# This program will simulate the "Magic 8 Ball" game.
#
# This is version 3.1 of the game. It has been reviewed to include more topics
# from the Day One slides. This is the final and only version of the game that 
# will be uploaded. Previous versions of the game has been lost.
#
# 3.1: Refactored to be more organized and fit within an 80 character limit.
#      Also included comments
# 3.0: Changed text prompt. Added use of a dictionary. Overall, refactored to 
#      more accurately replicate the original Magic 8 Ball game.
#
# 2.0: Refactored to include the use of classes. 
# 
# 1,0: This is the first version of the game done all in one file, bad style
import random

# Print instructions on how to play the game
print("This is a Magic 8-Ball Game")
print("When prompt, give a question that can be answered yes or no.")
print("The magic 8 ball will give it's response\n\n")

# Initializing game environment (text prompts)
reply = {
         # Affirmative replies
         0:["It is certain.", 
            "It is decidedly so.", 
            "Without a doubt.", 
            "Yes - definitely.", 
            "You may rely on it.", 
            "As I see it, yes.", 
            "Most likely.", 
            "Outlook good.", 
            "Yes.", 
            "Signs point to yes."],
         # Undecisive replies
         1:["Reply hazy, try again.", 
            "Ask again later.", 
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again."],
         # Denial replies
         2:["Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."]
        }

# Defining game behavior
def game():
    print("What is your question?")
    user_input = input("Press enter to exit: ")
    while user_input is not "":
        # Roll for type of reply
        roll = random.randint(0, 2)
        # Randomly generate reply based on results of the roll
        index_reply = random.randint(0, len(reply[roll]) - 1)
        print(reply[roll][index_reply])
        # Prompt for next question
        print("\nWhat is your question?")
        user_input = input("Press enter to exit: ")

# Executing the game
game()

