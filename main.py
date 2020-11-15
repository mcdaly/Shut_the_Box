# Shut The Box Simulator
# Rules of the game:
# 1. Start with 1-9 number tiles available for user
# 2. Roll 2 dice (2 random number generator between 1-6)
# 3. Add numbers together
# 4. Determine number tiles to knock down
# 5. Check if winner. If not, repeat steps 2-4
#
# Goal:
# Knock down all number tiles
# Obtain the smallest possible number when the remaining tiles are concatenated together

from roll_dice import *
from shut_the_box_strategy import *

if __name__ == '__main__':

    # Step 1: Define Player's Tiles
    current_tiles = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("Player Tiles: ", current_tiles)
    keep_playing = 1
    turn = 0

    while keep_playing and turn < 10:
        turn += 1
        print("Turn: ", turn)
        # Step 2: Roll the dice
        # If 7,8,or 9 are knocked down, player decides how many dice to roll
        roll = [0,0]
        if 7 in current_tiles or 8 in current_tiles or 9 in current_tiles:
            roll[0] = roll_dice()
            roll[1] = roll_dice()
        else:
            roll[0] = roll_dice()

        # Step 3: Calculate total from dice
        print("Dice Roll:", roll)
        total = roll[0] + roll[1]
        print("Total of Roll:", total)

        # Step 4: Which tiles to knock down?
        knock_down = remove_largest_number(total, current_tiles)
        for ii in knock_down:
            if ii in current_tiles:
                current_tiles.remove(ii)
                print("Removed", ii, "... Player Tiles Updated:", current_tiles)
            else:
                print("Failed to remove", ii, "... Game Over")
                keep_playing = 0

        # Step 5: Check if won or roll dice again
        if not current_tiles:
            print('Winner Winner! You Shut The Box!')
            keep_playing = 0
        elif not knock_down:
            print("No tiles to knock down... GG")
            keep_playing = 0

    # Game Over
    if current_tiles:
        # Calculate final score
        final_score = 0
        loop = 0
        for ii in current_tiles:
            loop += 1
            digit_position = len(current_tiles) - loop
            final_score += (ii * pow(10,digit_position))
        print("Final Score:", final_score)
    else:
        print("Final Score: 0! You Rock")