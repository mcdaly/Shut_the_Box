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

from src.play_the_game import start_game
from src.strageties import StrategyName
from data_classes.player import Player

if __name__ == "__main__":
    strategies = [
        StrategyName.remove_largest_number,
        StrategyName.remove_smallest_number,
        StrategyName.remove_random,
        StrategyName.remove_most_numbers,
    ]
    verbose = False
    for strategy in strategies:
        loops = range(10000)
        result = []
        player = Player(strategy=strategy)
        for ii in loops:
            cur_result = start_game(player, verbose)
            result.insert(ii, cur_result)

        # Do some math on the result
        print(
            "Number of Shut Boxes for strategy #: ",
            strategy,
            " is ",
            100 * (result.count(0) / len(result)),
            "%",
        )
        print(
            "Average score for strategy #: ",
            strategy,
            " is ",
            sum(result) / len(result),
        )
        print("Thanks for playing")

        # TODO: Save off game results

"""
Add different players with unique profiles
* Each player may cheat at different (yet predictable) intervals
    * Time of day, seasonal, geographical, weather, drunkenness
    * Add fake bank accounts and does cheating tie with this?

Cheating techniques:
* Knock down extra tiles
    Intentionally use against important tiles
    Randomly knock down tiles (drunk)  
Loaded dice


Output game moves as a CSV with the following columns:
    Player name, date and time of game, weather, location (home, bar, tournament), 
    9 sections with tiles remaining and dice roll

"""
