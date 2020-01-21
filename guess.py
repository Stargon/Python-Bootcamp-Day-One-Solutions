# This program will simualte the "Guess The Number Game".
import random as r

def intro(max):
    """
    This function prints out the introduction to the game.
    """
    print("This program allows you to play the guessing game.")
    print("It will guess a number between 1 and %d." % max)
    print("You can guess as many times as needed in order to")
    print("guess the correct number.")
    print("The game will let you know if the right answer is higher")
    print("or lower than your guess.")
    print("If you want to continue playing again, type y/yes when asked.")

def game(max):
    """
    This function represents one match of the guessing game. It will return the
    number of guesses it took to get the correct number.
    """
    # Generate random number for one game.
    rng = r.randint(1, max)
    # Ask the user to guess the number
    print("\nI am guessing a number between 1 to %d..." % max)
    guess = int(input("What is your guess? "))
    guess_number = 1
    # Loop if the user did not guess it correctly the first time
    while rng != guess:
        if rng < guess:
            # guess is greater than rng
            print("It is lower...")
        else:
            # guess is less than rng
            print("It is higher...")
        # Ask again, and increment the number of guesses
        guess = int(input("What is your guess? "))
        guess_number += 1
    # Notify user that they got it correct
    if guess_number == 1:
        # Print messsage that they got won with one guess
        print("You got it correct in 1 guess!")
    else:
        # Print message that they took multiple guesses 
        print("You got it right in %d guesses!" % guess_number)
    return guess_number

def results(stat):
    """
    Given an array of stats:
        [# of games, # of guesses, best game round, lowest # of guesses]  
    ... calculate the statistics of the player performance overall.

    Performance is measured by total number of games, total number of guesses,
    the number of guesses/number of games played, and which match had the least
    number of guesses, and the lowest guess number.
    """
    performance_ratio = stat[1] / stat[0]
    print("\nOverall results:")
    print("\tTotal Games = %d" % stat[0])
    print("\tTotal Guesses = %d" % stat[1])
    print("\tGuesses per Game = %f" % performance_ratio)
    # Print different statements if best number of guesses is 1
    if stat[3] == 1:
        print("\tGame %d was the best game with %d guess" % (stat[2], stat[3]))
    else:
        print("\tGame %d was the best game with %d guesses" % (stat[2], stat[3]))

def main():
    """
    Main function that should contains game environment.
    """
    # Define max here
    max = 100
    # Record stats (# of games, # of guesses, best game round, lowest guess #)
    stats = [0, 0, 0, float("inf")]
    # Record number of rounds
    game_round = 0
    # Keep track if the player wants to continue (1 = yes)
    continue_playing = 1

    # Start the game
    intro(max)
    while continue_playing == 1:
        # Play one match
        game_round += 1
        stats[0] +=1
        number_of_tries = game(max)
        # Update total number of guesses
        stats[1] += number_of_tries
        # Update best number of guesses
        if number_of_tries < stats[3]:
            stats[2] = game_round
            stats[3] = number_of_tries
        # Ask if the user wants to play again
        ask_to_play = input("Do you want to play again? ").lower()
        if ask_to_play != "y" and ask_to_play != "yes":
            # User does not want to continue
            continue_playing = 0
    # Print performance results
    results(stats)
    quit()


main()

