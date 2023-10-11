from behave import given, when, then
from game import handleKeySubmit, handleWordSubmit, charPos, getUserInput

@given(u'a word {word}')
def step_impl(context, word):
    context.word = word


@given(u'a letter {letter}')
def step_impl(context, letter):
    context.letter = letter


@when(u'check letter')
def step_impl(context):
    context.changed_value = handleKeySubmit(context.letter, context.word, "_"*len(context.word), 0)[1]

@when(u'check word')
def step_impl(context):
    context.changed_value = handleWordSubmit(context.word, context.word, 0)


@when(u'find char positions')
def step_impl(context):
    context.charArr = charPos(context.word, context.letter)
    
@when(u'get user input')
def step_impl(context):
    context.userInput = getUserInput(True, context.word)

@then(u'number of guessed letters increase')
def step_impl(context):
    assert context.changed_value > 0


@then(u'number of guessed letters not changed')
def step_impl(context):
    assert context.changed_value == 0


@then(u'length of returned array is {number:d}')
def step_impl(context, number):
    assert len(context.charArr) == number
    
@then(u'result is tuple of {user_input} and {is_letter:d}')
def step_impl(context, user_input, is_letter):
    assert context.userInput[1] == is_letter
    assert context.userInput[0] == user_input
    