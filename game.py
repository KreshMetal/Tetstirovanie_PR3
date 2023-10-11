import json
import random

def checkForWin(to_be_guessed, guessed_letters):
    return guessed_letters == len(to_be_guessed)


def handleWordSubmit(answer, to_be_guessed, guessed_letters):
    if answer == to_be_guessed:
        guessed_letters = len(to_be_guessed)
    return guessed_letters