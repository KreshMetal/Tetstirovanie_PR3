from behave import given, when, then

import sys
sys.path.insert(0, 'E:\pole')
from game import handleKeySubmit, handleWordSubmit, charPos


@given(u'a word {word}')
def step_impl(context, word):
    context.word = word

@when(u'check word')
def step_impl(context):
    context.changed_value = handleWordSubmit(context.word, context.word, 0)

@then(u'number of guessed letters increase')
def step_impl(context):
    assert context.changed_value > 0