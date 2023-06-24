from hangman_picks import HANGMAN_PICKS
from words import words
import random

def getRandomWord():
    indexWord = random.randint(0, len(words))
    return words[indexWord]

def displayBoard(misseLetters,correctLetters, secretWord):
    attemps = len(misseLetters)
    print(f"Number of attemps{attemps}")
    print(HANGMAN_PICKS[attemps])
    print()

    blaks = "_" * len(secretWord) 

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blaks = blaks[:i] + secretWord[i] + blaks[i + 1:]

    for letter in blaks:
        print(letter, end=" ")
        print()



    print(blaks)



def getGuess(alreadyGuessed):
    while True:
        guess = input("Guess a letter")
        guess = guess.lower()

        if guess.isdigit():
            print("please write a number")
            continue
        elif guess in alreadyGuessed:
            print("You already guess that letter")
            continue
        else:
            return guess
        


def playAgain():
    pass

def run():
    print("HANG MAN")
    missedLetter = ""
    correctLetters = ""
    secretWord = getRandomWord()
    gameIsDone = False

    while True:
        displayBoard(missedLetter, correctLetters, secretWord)

        guesse = getGuess(correctLetters + missedLetter)

        if guesse == secretWord:
            correctLetters = guesse
            pass #user win
        elif guesse in secretWord:
            correctLetters += guesse
        else:
            pass #lose

if __name__ == "__mian__":
    run()