# Roll a 6 sided die and return result
#
from random import randrange

def roll_dice():

    # seed random number generator
    # roll the dice!
    result = randrange(1, 7, 1)
    return result