import re
import utils
import numpy as np


class _Game:
    id: int
    min_cube_counts: dict[str, int]

    def __init__(self, line: str):
        id_part, results_part = line.split(":")

        # Init ID
        game_id = re.search(r"\d+", id_part)
        if not game_id:
            raise ValueError(f"Game ID missing from {line}")
        self.id = int(game_id[0])

        # Init cube counts
        self.min_cube_counts = {}
        for result in results_part.split(";"):
            rounds = result.split(",")
            for round in rounds:
                amount, color = round.strip().split(" ")
                self._register_cube_count(color, int(amount))

    def _register_cube_count(self, color: str, amount: int) -> None:
        if not (color in self.min_cube_counts) or amount > self.min_cube_counts[color]:
            self.min_cube_counts[color] = amount

    def compatible_with(self, assumption: dict[str, int]) -> bool:
        for color in self.min_cube_counts:
            if (
                not color in assumption
                or assumption[color] < self.min_cube_counts[color]
            ):
                return False
        return True


def _part1(lines):
    """
    Input is lines of text. Each line is one Game.
    """
    assumption = {"red": 12, "green": 13, "blue": 14}
    games = [_Game(line) for line in lines]
    return np.sum([game.id for game in games if game.compatible_with(assumption)])


def run():
    print("Day 2")
    lines = utils.load_lines("data/day2.txt")
    print(f"Part 1: The sum of the IDs of compatible games is {_part1(lines)}.")
