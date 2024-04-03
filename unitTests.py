import unittest
from guesses import GuessController

gc = GuessController(10)
class TestGuessControler(unittest.TestCase):

    def test_recordGuessNumber0(self):
        self.assertEqual(gc.guess, 0, 'The recorded guess is wrong')
    def test_recordGuessNumber2(self):
        gc.recordGuess(52)
        self.assertEqual(gc.guess, 1, 'The recorded guess is wrong')
    def test_recordGuessNumber3(self):
        gc.recordGuess(65)
        self.assertEqual(gc.guess, 2, 'The recorded guess is wrong')
    def test_recordGuessValue1(self):
        self.assertEqual(gc.guesses[0], 52, 'The recorded guess is wrong')
    def test_recordGuessValue2(self):
        self.assertEqual(gc.guesses[1], 65, 'The recorded guess is wrong')

    def test_reset(self):
        gc.reset()
        self.assertEqual(gc.guess, 0, 'The reset Failed')

    def test_zPreviousGuessTheSame(self):
        gc.recordGuess(54)
        gc.recordGuess(96)
        gc.printGuesses()
        self.assertTrue(gc.isPreviousGuessTheSame(96), "Previous guess checking not working correctly")





