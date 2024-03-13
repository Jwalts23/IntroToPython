# This will become a highlow game sooooonnnn

import random
from guesses import GuessController
import getopt, sys

# Remove 1st argument from the
# list of command line arguments
argumentList = sys.argv[1:]
print("arguments list " , argumentList)
gc = GuessController(10)
lowerLimit = 0
upperLimit = 100


# Options
options = "l:u:h"
# Long options
long_options = ["Help", "Lower=", "Upper="]

try:
    # Parsing argument
    arguments, values = getopt.getopt(argumentList, options, long_options)
    # checking each argument
    for currentArgument, currentValue in arguments:
        if currentArgument in ("-h", "--Help"):
            print("-u | --Upper  upper limit value")
            print("-l | --Lower  lower limit value")

        elif currentArgument in ("-l", "--Lower"):
            print("Lower Limit:", currentValue)
            lowerLimit = int(float(currentValue))

        elif currentArgument in ("-u", "--Upper"):
            print("Upper Limit:", currentValue)
            upperLimit = int(currentValue)

except getopt.error as err:
    # output error, and return with an error code
    print(str(err))

number = random.randint(lowerLimit, upperLimit)
guessing = True
askingToPlayAgain = True

def playAgain():
    global askingToPlayAgain, number, guessing
    while(askingToPlayAgain):
        playAgain = input("Would you like to play again?  ")
        if playAgain == "Y" or playAgain == "y":
            gc.reset()
            number = random.randint(lowerLimit,upperLimit)
            guessing = True
            askingToPlayAgain = False
        elif playAgain == "N" or playAgain == "n":
            guessing = False
            askingToPlayAgain = False
            print("Thanks for playing!")
        else: 
            print("Invalid input")

while guessing:
    print()
    print("You have " + str(gc.remainingGuesses()) + " guesses remaining.")
    if gc.remainingGuesses() > 0:
        gc.printGuesses()
        
        try:
            guess = int(input("Enter a number between " + str(lowerLimit) + "-" + str(upperLimit) + ": "))
            if not gc.isPreviousGuessTheSame(guess):
                if guess > number:
                    print("Too High")

                elif guess < number:
                    print("Too Low")

                elif number == guess:
                    print("You did it! The number was " + str(number))
                    playAgain()
                gc.recordGuess(guess)
            else:
                print("The guess cannot be the same as the previous guess")  
        except ValueError as ve:
            print()
            print(f'Invalid input! Try again.')

    else:
        print("You used all your guesses! The number was " + str(number))
        askingToPlayAgain = True
        playAgain()

