import csv
from typing import List

from data_classes.game_state import Game


def output_results(csv_filename: str, game_results: List[Game]) -> None:
    """
    Write game results to a CSV
    :param csv_filename: Name of output filename
    :param game_results: List of game results
    """
    # Define header for the CSV file
    header = ["player_name", "date", "time", "final_score"]
    for i in range(1, 10):  # Assuming maximum of 9 turns
        header.extend(
            [f"turn_{i}_tiles_up", f"turn_{i}_dice_roll", f"turn_{i}_knocked_tiles"]
        )

    # Write data to CSV file
    with open(csv_filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)  # Write header row

        # Write each game result as a row in the CSV file
        for result in game_results:
            row = [
                result.player_name,
                result.game_date,
                result.game_time,
                result.final_score,
            ]
            for state in result.game_history:
                row.extend([state["tiles_up"], state["roll"], state["knocked_tiles"]])
            writer.writerow(row)
