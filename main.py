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

def getGuess(alreadyGuessed):
    while True:
        guess = input("Guess a letter: ")
        guess = guess.lower()

        if guess.isdigit():
            print("please write a letter")
            continue
        elif guess in alreadyGuessed:
            print("You already guess that letter")
            continue
        else:
            return guess
        
def checkUserWin(secretWord, corectLettes):
    for i in range(len(secretWord)):
        if secretWord[i] not in corectLettes:
            return False
    
    print(f"Congradulation you win, you found the secret word: {secretWord}")
    return True


def playAgain():
    print("Do you want to play again? (yes/not):")
    return input().lower().startswith("y")

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
            gameIsDone = checkUserWin(secretWord,correctLetters)

        elif guesse in secretWord:
            correctLetters += guesse
            gameIsDone = checkUserWin(secretWord,correctLetters)
        else:
            missedLetter += guesse
            if len(missedLetter) == len(HANGMAN_PICKS) - 1:
                displayBoard(missedLetter,correctLetters, secretWord)
                print(f"Sorry you didn't have the chance to guesse the secret word: {secretWord}")
                print(f"Number of attemps {len(missedLetter)}")
                gameIsDone = True
            
        if gameIsDone: 
            displayBoard(missedLetter,correctLetters, secretWord)
            if playAgain():
                missedLetter = ""
                correctLetters = ""
                secretWord = getRandomWord()
                gameIsDone = False
            else:
                break

if __name__ == "__main__":
    run()