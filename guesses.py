import array

class GuessController:
    
    def __init__(self, permittedGuesses):
        self.guess = 0
        self.guesses = array.array("i")
        self.permittedGuesses = permittedGuesses


    def printGuesses(self):
        if self.guess > 0:
            print("Your Guesses are:", end=" ")
            for i in range(self.guess):
                g = self.guesses[i]
                if i < (self.guess-1):
                    print(g, end=", ")
                else:
                    print(g)
        else:
            print("No Guesses yet")

    
    def recordGuess(self, guess):
        self.guesses.append(guess)
        self.guess +=1
    
    def reset(self):
        self.guess = 0
        self.guesses = array.array("i")

    def isPreviousGuessTheSame(self, guess):
        if self.guess > 0:
            if guess == self.guesses[self.guess-1]:
                return True
            else :
                return False
        return False

    def remainingGuesses(self):
        return self.permittedGuesses - self.guess
    
# gc = GuessController(15)

# gc.printGuesses()
# gc.recordGuess(15)
# gc.recordGuess(30)
# gc.recordGuess(30)
# gc.recordGuess(22)
# gc.recordGuess(30)
# print("Guess is same as last? "+ str(gc.isPreviousGuessTheSame(22)))
# gc.printGuesses()
# print("Remaining Guesses: "+ str(gc.remainingGuesses()))