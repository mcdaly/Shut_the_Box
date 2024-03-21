from datetime import datetime
from data_classes.player import Player
from data_classes.locations import Locations


class Game:
    def __init__(
        self, player_name: str, date: datetime = None, time: datetime = None, location: Locations = None
    ):
        self.player_name = player_name
        self.game_date = date
        self.game_time = time
        self.location = location

        self.game_history = []
        self.final_score = None

    def record_turn(self, tiles_remaining: list, dice_role: list, tiles_knocked_down: list):
        self.game_history.append({"tiles_up": tiles_remaining,
                                  "roll": dice_role,
                                  "knocked_tiles": tiles_knocked_down})
