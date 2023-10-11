import json
import random

def checkForWin(to_be_guessed, guessed_letters):
    return guessed_letters == len(to_be_guessed)


def handleWordSubmit(answer, to_be_guessed, guessed_letters):
    if answer == to_be_guessed:
        guessed_letters = len(to_be_guessed)
    return guessed_letters

def charPos(str, char):
    raise Exception("Не реализовано")

def handleKeySubmit(key, to_be_guessed, to_show, guessed_letters):
    raise Exception("Не реализовано")

lib = None

def init():
    raise Exception("Не реализовано")

def getRandomWord(lib):
    return lib[random.randint(0, len(lib)-1)]

def getUserInput(test, test_input=''):
    if (test):
        user_input = test_input
    else:
        user_input = str(input())
    if len(user_input) == 1:
        return (user_input, True)
    else:
        return (user_input, False)

def startGame(test):
    raise Exception("Не реализовано")

if __name__ == '__main__':
    startGame(False)