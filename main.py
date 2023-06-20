from hangman_picks import HANGMAN_PICKS
from words import words
import random

def getRandomWord():
    indexWord = random.randint(0, len(words))
    return words[indexWord]

def displayBoard(misseLetters,secretWord):
    attemps = len(misseLetters)
    print(f"Number of attemps{attemps}")
    print(HANGMAN_PICKS[attemps])
    print()

    blaks = "_" * len(secretWord)

    print(blaks)



def getGuess():
    pass

def playAgain():
    pass

def run():
    print("HANG MAN")
    missedLetter = ""
    correctLetters = ""
    secretWord = getRandomWord()
    gameIsDone = False

while True:
    displayBoard()

if __name__ == "__mian__":
    pass