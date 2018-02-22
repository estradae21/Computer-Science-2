import random

HANGMAN = ('''
   +---+
     |   |
         |
         |
         |
         |
  =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
  =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
  =========''', '''

   +---+
   |   |
   O   |
  /|   |
       |
       |
 =========''', '''
   +---+
   |   |
   O   |
  /|\  |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
=========''')
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret ' \
        'fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon ' \
        'python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad ' \
        'trout turkey turtle weasel whale wolf wombat zebra'.split()

def getrandomword(wordlist):
    return random.choice(wordlist)

def displayBoard(HANGMAN, missedLetters, correctLetters, secretWord):
    print(HANGMAN[len(missedLetters)])
    print("\nMissed Letters: " + missedLetters)
    print("Correct Letters: " + correctLetters)

    blanks = "_" * len(secretWord)
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]


def getGuess(alreadyGuessed):
    while True:
        guess = input("Guess a letter.").lower()
        if len(guess) != 1:
            print("Only one letter.")
        elif guess in alreadyGuessed:
            print("You have already guessed this letter.")
        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print("Only letters allowed")
        else:
            return guess


def playAgain():
    return input("\nWould you like to play again? [Y/N]\n>")

missedLetters = ''
correctLetters = ''
secretWord = getrandomword(words)
gameIsDone = False

while True:
    displayBoard(HANGMAN, missedLetters, correctLetters, secretWord)
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters += guess
        #check if won
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print("Congratulations! The secret word was " + secretWord + ". You won!")
            gameIsDone = True
    else:
        missedLetters += guess
        if len(missedLetters) == len(HANGMAN) - 1:
            displayBoard(HANGMAN, missedLetters, correctLetters, secretWord)
            print("You have guessed to many times and lost. \nAfter " + str(len(missedLetters)) + " missed guesses and "
                  + str(len(correctLetters)) + " correct guesses, the word was " + secretWord + ".")
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            secretWord = getrandomword(words)
            gameIsDone = False
        else:
            break






