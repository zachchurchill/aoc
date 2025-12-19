import os

from aocpy.shared import INPUTS_DIR, timer


@timer
def solve():
    # Part #1
    with open(os.path.join(INPUTS_DIR, "day1.txt")) as f:
        raw_rotations = [entry.strip() for entry in f.readlines()]
    clicks = [
        int(rotation[1:]) if rotation[0] == "R" else -int(rotation[1:])
        for rotation in raw_rotations
    ]
    dial = 50
    zeros = 0
    for click in clicks:
        dial = (dial + click) % 100
        zeros += dial == 0
    print(f"Times dial was at 0: {zeros}")
