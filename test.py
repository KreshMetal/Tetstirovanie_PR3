from contextlib import redirect_stdout
from game import checkForWin, getRandomWord, init, startGame
import io
import pytest

def test_for_win():
    assert checkForWin("abcde", 5)

def test_random_is_random():
    assert getRandomWord([1, 2, 3, 4]) in [1, 2, 3, 4]

def test_startgame_output():
    f = io.StringIO()
    with redirect_stdout(f):
        startGame(True)
    out = f.getvalue()
    assert out != ""

def test_just_check_init_size():
    assert len(init()) > 10000


