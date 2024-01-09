# This will become a highlow game sooooonnnn

import random
from guesses import GuessController
from LED import LED
import time

#setup LEDs
red = LED(22)
yellow = LED(24)
green = LED(23)

def HWinit():
    red.setup()
    yellow.setup()
    green.setup()

def LEDsOff():
    red.off()
    yellow.off()
    green.off()

#time.sleep(0.5)
    
def strobe():
    red.on()
    time.sleep(0.25)
    red.off()
    time.sleep(0.25)
    yellow.on()
    time.sleep(0.25)
    yellow.off()
    time.sleep(0.25)
    green.on()
    time.sleep(0.25)
    green.off()
        

gc = GuessController(15)

# global number, askingToPlayAgain, guessing
number = random.randint(0,100)
guessing = True
askingToPlayAgain = True

HWinit()

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
            LEDsOff()
            if not gc.isPreviousGuessTheSame(guess):
                if guess > number:
                    print("Too High")
                    red.on()

                elif guess < number:
                    print("Too Low")
                    yellow.on()

                elif number == guess:
                    print("You did it! The number was " + str(number))
                    for x in range (5):
                        strobe()
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

