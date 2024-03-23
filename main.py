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
from datetime import datetime

from src.play_the_game import start_game
from src.strategies import StrategyName
from data_classes.player import Player
from utils.output_result import output_results


def analyze_shut_the_box(
    strategies: list, iterations: int, verbose: bool = False
) -> None:
    """
    Run each strategy for shut the box the specified number of iterations to get a true understanding of the strategies
    effectiveness
    :param strategies: Strategies for knocking down the tiles
    :param iterations: Number of times each strategy will be run
    :param verbose: Flag for showing individual game details when playing
    """
    for strategy in strategies:
        loops = range(iterations)
        result = []
        game_states = []
        player = Player(name=strategy, strategy=strategy)
        for ii in loops:
            cur_result = start_game(player, verbose)
            game_states.append(cur_result)
            result.append(cur_result.final_score)

        # Do some math on the result
        print(
            f"Number of Shut Boxes for strategy #: {strategy} is {100 * (result.count(0) / len(result)):0.2f} %"
        )
        print(
            f"Average score for strategy #: {strategy} is {sum(result) / len(result):0.0f}"
        )
        print("Thanks for playing")

        # TODO: Save off game results
        # Generate filename with date and timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        csv_filename = f"output/{timestamp}_{strategy}.csv"
        output_results(csv_filename, game_states)


if __name__ == "__main__":
    strategies = [
        StrategyName.remove_largest_number,
        StrategyName.remove_smallest_number,
        StrategyName.remove_random,
        StrategyName.remove_most_numbers,
    ]

    iterations_per_strategy = 10000

    analyze_shut_the_box(strategies, iterations=iterations_per_strategy)

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
    9 sections with tiles remaining, dice roll, tiles selected to knock down

"""
