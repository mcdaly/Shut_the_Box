from utils.roll_dice import roll_dice
from src.strageties import StrategyName, Strategy


class Player:
    """Class for a generic player"""

    def __init__(
        self,
        name: str = "",
        strategy: StrategyName = StrategyName.remove_largest_number,
    ):
        self.name = name
        self.strategy = strategy
        self.dice_roll = []

    def roll(self, tiles) -> int:
        """
        Have the player roll the dice
        :return: Sum of the two dice being rolled
        """
        number_dice = self.decide_number_of_dice_to_roll(tiles)
        if number_dice == 1:
            self.dice_roll = [roll_dice()]
        elif number_dice == 2:
            self.dice_roll = [roll_dice(), roll_dice()]
        else:
            raise ValueError
        return sum(self.dice_roll)

    def decide_number_of_dice_to_roll(self, tiles: list):
        """
        From the tiles still remaining, decide the number of dice to roll

        If 7, 8 and 9 are all covered, the player decides whether to throw one die or two.
        If any of these 3 numbers are still uncovered, the player must use both dice.

        :param tiles: Tiles remaining up
        :return: Number of dice to roll
        """
        # If 7,8,or 9 are knocked down, player decides how many dice to roll
        # Default to always go down to 1 die
        if all(num not in tiles for num in [7, 8, 9]):
            return 1
        else:
            return 2

    def knock_tiles(self, dice_total: int, current_tiles: list) -> list:
        """
        Knock down certain tiles
        :param dice_total: Total value of dice roll
        :param current_tiles: Tiles remaining up
        :return: Latest tiles remaining up
        """
        knock_down = Strategy.run_strategy(self.strategy, dice_total, current_tiles)
        return knock_down
