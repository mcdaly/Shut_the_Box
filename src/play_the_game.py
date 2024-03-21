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

from data_classes.player import Player


def start_game(player: Player, verbose: bool = False):
    # Step 1: Define Player's Tiles
    current_tiles = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    if verbose:
        print("Player Tiles: ", current_tiles)
    keep_playing = True
    turn = 0

    while keep_playing:
        turn += 1
        if verbose:
            print("Turn: ", turn)

        # Step 2: Roll the dice
        dice_total = player.roll(current_tiles)

        # Step 3: Calculate total from dice
        if verbose:
            print("Dice Roll:", player.dice_roll, " ... Total: ", dice_total)

        # Step 4: Which tiles to knock down?
        knock_down = player.knock_tiles(
            dice_total=dice_total, current_tiles=current_tiles
        )
        for ii in knock_down:
            if ii in current_tiles:
                current_tiles.remove(ii)
                if verbose:
                    print("Removed", ii, "... Player Tiles Updated:", current_tiles)
            else:
                if verbose:
                    print("Failed to remove", ii, "... Game Over")
                keep_playing = False

        # Step 5: Check if won or roll dice again
        if not current_tiles:
            if verbose:
                print("Winner Winner! You Shut The Box!")
            keep_playing = False
        elif not knock_down:
            if verbose:
                print("No tiles to knock down... GG")
            keep_playing = False

    # Game Over
    if current_tiles:
        # Calculate final score
        final_score = int("".join(str(num) for num in current_tiles))
        if verbose:
            print(f"Final Score: {final_score}")
    else:
        final_score = 0
        if verbose:
            print("Final Score: 0! You Rock")

    return final_score
