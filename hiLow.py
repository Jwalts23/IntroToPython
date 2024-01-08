# This will become a highlow game sooooonnnn

import random
from guesses import GuessController

gc = GuessController(10)

# global number, askingToPlayAgain, guessing
number = random.randint(0,100)
guessing = True
askingToPlayAgain = True

def playAgain():
    global askingToPlayAgain, number, guessing
    while(askingToPlayAgain):
        playAgain = input("Would you like to play again?  ")
        if playAgain == "Y" or playAgain == "y":
            gc.reset()
            number = random.randint(0,100)
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
            guess = int(input("Enter a number between 0-100: "))
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

