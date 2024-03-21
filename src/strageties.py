# Strategy to win Shut The Box
from utils.math_stuff import find_tiles_to_knock_down
from random import randint


class StrategyName:
    remove_largest_number = "remove_largest_number"
    remove_smallest_number = "remove_smallest_number"
    remove_most_numbers = "remove_most_numbers"
    remove_least_likely_number = "remove_least_likely_number"
    remove_random = "remove_random"


class Strategy:
    @classmethod
    def run_strategy(
        cls, selection: StrategyName, total: int, current_tiles: list
    ) -> list:
        """
        :param selection: Strategy to use
        :param total: Dice roll total
        :param current_tiles: Tiles still standing at start of turn
        :return: List of tiles to be knocked down
        """
        # Find all addends of the total
        addends = find_tiles_to_knock_down(current_tiles, total)

        if not addends:
            return []
        elif selection == StrategyName.remove_largest_number:
            return cls.remove_largest_number(addends)
        elif selection == StrategyName.remove_smallest_number:
            return cls.remove_smallest_number(addends)
        elif selection == StrategyName.remove_most_numbers:
            return cls.remove_most_numbers(addends)
        elif selection == StrategyName.remove_least_likely_number:
            return cls.remove_least_likely_number(addends)
        elif selection == StrategyName.remove_random:
            return cls.remove_random_numbers(addends)

    @classmethod
    def remove_largest_number(cls, addends: list) -> list:
        """
        Find the set of tiles with the largest number in it to knock down
        """
        max_list_index = max(enumerate(addends), key=lambda x: max(x[1]))[0]
        knock_down = addends[max_list_index]

        return knock_down

    @classmethod
    def remove_smallest_number(cls, addends: list) -> list:
        """
        Return the index of the list of lists with the smallest number in it
            and if there are multiple with that number, take the one with the most numbers in it
        """
        min_list_index = min(enumerate(addends), key=lambda x: (min(x[1]), -len(x[1])))[
            0
        ]
        knock_down = addends[min_list_index]
        return knock_down

    @classmethod
    def remove_most_numbers(cls, addends: list) -> list:
        """
        Find the index of the list with the most ints in it.
        If multiple lists have the same number, I want to take the one with the largest number in it
        """
        index_of_max_list = max(
            enumerate(addends), key=lambda x: (len(x[1]), max(x[1]))
        )[0]
        knock_down = addends[index_of_max_list]
        return knock_down

    @classmethod
    def remove_least_likely_number(cls, addends: list) -> list:
        # TODO: Add logic here for determining least likely combos
        knock_down = addends[len(addends) - 1]
        return knock_down

    @classmethod
    def remove_random_numbers(cls, addends: list) -> list:
        """
        Randomly select the tiles to knock down
        """
        random_index = randint(0, len(addends) - 1)
        knock_down = addends[random_index]
        return knock_down
