# Hangman game

import random

WORDLIST_FILENAME = "C:\Sanket Jain\Coding\Python Code\words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    x = set(secretWord)
    y = [True if i in lettersGuessed else False for i in x]
    return all(y)



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    return "".join(map(str,["_ " if x not in lettersGuessed else x for x in secretWord]))



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    return "".join(map(str,["" if x in lettersGuessed else x for x in "abcdefghijklmnopqrstuvwxyz"]))
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    loadWords()
    print("Welcome to the game Hangman!")
    length_of_chosen_word = len(secretWord)
    print("I am thinking of a word that is "+str(length_of_chosen_word)+" letters long.")
    print("-------------")
    x = 8
    lettersGuessed = []
    while x > 0:
        print("You have "+str(x)+" guesses left.")
        print("Available letters: "+getAvailableLetters(lettersGuessed))
        guess = input("Please guess a letter: ")
        guessInLowerCase = guess.lower()
        if guessInLowerCase in getAvailableLetters(lettersGuessed):
            lettersGuessed.append(guessInLowerCase)
            if isWordGuessed(secretWord, lettersGuessed):
                print("Good guess: "+secretWord)
                print("-------------")
                print("Congratulations, you won!")
                break
            elif guessInLowerCase in set(secretWord):
                print("Good guess: "+getGuessedWord(secretWord, lettersGuessed))
                print("-------------")
                x += 0
            else:
                print("Oops! That letter is not in my word: "+getGuessedWord(secretWord, lettersGuessed))
                print("-------------")
                x-=1
        else:
            print("Oops! You've already guessed that letter: "+getGuessedWord(secretWord, lettersGuessed))
            print("-------------")
            x += 0
    else:
        print("Sorry, you ran out of guesses. The word was "+secretWord+".")


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)