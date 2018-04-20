from guess import get_random_number
from guess import Game
from unittest.mock import patch
import random
import pytest


@patch.object(random, 'randint')
def test_get_random_number(m):
    m.return_value = 17
    assert get_random_number() == 17


@patch('builtins.input', side_effect=[11, '12', 'Bob', 12,
                                      5, -1, 21, 7, None])
def test_guess(anything):
    game = Game()

    # good inputs
    assert game.guess() == 11
    assert game.guess() == 12

    # not a number
    with pytest.raises(ValueError):
        game.guess()

    # already guessed 12
    with pytest.raises(ValueError):
        game.guess()

    # good input
    assert game.guess() == 5

    # out of range values
    with pytest.raises(ValueError):
        game.guess()

    # already guessed 12
    with pytest.raises(ValueError):
        game.guess()

    # good input
    assert game.guess() == 7

    # user hit 'enter'
    with pytest.raises(ValueError):
        game.guess()


def test_validate_guess(capfd):
    game = Game()
    game._answer = 2

    assert not game._validate_guess(1)
    out, _ = capfd.readouterr()
    assert out.rstrip() == '1 is too low'

    assert not game._validate_guess(3)
    out, _ = capfd.readouterr()
    assert out.rstrip() == '3 is too high'

    assert game._validate_guess(2)
    out, _ = capfd.readouterr()
    assert out.rstrip() == '2 is correct!'
