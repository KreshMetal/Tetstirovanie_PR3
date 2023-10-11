import json
import random

def checkForWin(to_be_guessed, guessed_letters):
    return guessed_letters == len(to_be_guessed)


def handleWordSubmit(answer, to_be_guessed, guessed_letters):
    if answer == to_be_guessed:
        guessed_letters = len(to_be_guessed)
    return guessed_letters

def charPos(str, char):
    return [i for i, c in enumerate(str) if c == char]

def handleKeySubmit(key, to_be_guessed, to_show, guessed_letters):
    letter = key.lower()
    if letter in to_be_guessed:
        to_rotate = charPos(to_be_guessed, letter)
        for i in to_rotate:
            to_show = to_show[:i] + to_be_guessed[i] + to_show[i+1:]
        guessed_letters += len(to_rotate)
    return to_show, guessed_letters

lib = None

def init():
    jsonFile = open('words', encoding='utf-8')
    return json.load(jsonFile)

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
    global lib
    if not lib:
        lib = init()
    word = getRandomWord(lib)
    to_be_guessed = word[0].lower()
    to_show = "_" * len(word[0])
    desc = word[1]
    desc_to_show = desc[0]
    desc = desc[1:]
    guessed_letters = 0
    attempts = 0
    while not checkForWin(to_be_guessed, guessed_letters):
        print(to_show)
        print(desc_to_show)
        print("Напишите букву или слово\n")
        if test:
            return
        ans, is_letter = getUserInput(test)
        if is_letter:
            to_show, guessed_letters = handleKeySubmit(ans, to_be_guessed, to_show, guessed_letters)
            attempts += 1
            if attempts % 5 == 0 and len(desc):
                desc_to_show += '\n' + desc[0]
                desc = desc[1:]
        else:
            guessed_letters = handleWordSubmit(ans, to_be_guessed, guessed_letters)

    print("ура победа")
    startGame(False)

if __name__ == '__main__':
    startGame(False)