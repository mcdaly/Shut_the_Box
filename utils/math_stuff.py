# Calculating random math things
import itertools


def find_tiles_to_knock_down(tiles: list, total: int) -> list:
    """
    Find all the combinations of numbers that can add up to the total
    :param total: Total from the dice roll
    :param tiles: Current tiles still standing
    :return: List of combinations that add up to the total
    """
    combinations = [
        seq
        for i in range(len(tiles), 0, -1)
        for seq in itertools.combinations(tiles, i)
        if sum(seq) == total
    ]
    return combinations
