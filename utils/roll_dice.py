# Roll a 6 sided die and return result
from random import randrange


def roll_dice() -> int:
    """
    Seed random number generator and roll the die!
    :return: Die roll
    """
    result = randrange(1, 7, 1)
    return result
