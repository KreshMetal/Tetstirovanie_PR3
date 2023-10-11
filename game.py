import json
import random

def checkForWin(to_be_guessed, guessed_letters):
    return guessed_letters == len(to_be_guessed)
