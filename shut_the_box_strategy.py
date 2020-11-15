# Strategy to win Shut The Box
#

from math_stuff import *

def remove_largest_number(total, current_tiles):
    # Find all addends of the total
    addends = total_addends(total, current_tiles, 0)
    # print(addends)

    if addends:
        knock_down = addends[0]
    else:
        knock_down = []
    return knock_down
