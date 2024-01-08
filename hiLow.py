# This will become a highlow game sooooonnnn

import random
from guesses import GuessController

gc = GuessController(10)

number = random.randint(0,100)
guessing = True
while guessing:
    gc.printGuesses()
    guess = int(input("Enter your guess here: "))

    if guess > number:
        print("Too High")

    elif guess < number:
        print("Too Low")

    elif number == guess:
        print("You did it! The number was " + str(number))
        guessing = False
    gc.recordGuess(guess)
