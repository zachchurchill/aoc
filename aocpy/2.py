import os
import re
from dataclasses import dataclass, fields
from typing import List

from aocpy.shared import INPUTS_DIR, timer


@dataclass
class Bag:
    red: int = 0
    green: int = 0
    blue: int = 0

    @classmethod
    @property
    def colors(cls) -> List[str]:
        return [
            field.name
            for field in fields(cls)
        ]

    def __le__(self, other_bag):
        return all(
            [
                self.red <= other_bag.red,
                self.green <= other_bag.green,
                self.blue <= other_bag.blue,
            ]
        )


@timer
def solve():
    with open(os.path.join(INPUTS_DIR, "day2.txt")) as f:
        game_records = f.readlines()

    # Part #1
    maximum_cubes = Bag(red=12, green=13, blue=14)

    def _get_cubes_by_color(reveal_record) -> Bag:
        reveals = Bag()
        for color in Bag.colors:
            cubes = re.search(f"(\\d+) {color}", reveal_record)
            if cubes:
                setattr(reveals, color, int(cubes.group(1)))
        return reveals
    reveals_per_game = [
        [_get_cubes_by_color(reveal) for reveal in record.split(";")]
        for record in game_records
    ]

    def _get_max_colors(bags: List[Bag]) -> Bag:
        max_colors = {
            color: max(getattr(b, color) for b in bags)
            for color in Bag.colors
        }
        return Bag(**max_colors)
    max_colors_in_game = [
        _get_max_colors(reveals)
        for reveals in reveals_per_game
    ]

    total_valid_game_ids = sum(
        game + 1
        for game, max_colors_bag in enumerate(max_colors_in_game)
        if max_colors_bag <= maximum_cubes
    )
    print(f"Answer #1: {total_valid_game_ids}")

    # Part #2
    powers = [
        reveals.red * reveals.green * reveals.blue
        for reveals in max_colors_in_game
    ]
    print(f"Answer #2: {sum(powers)}")
