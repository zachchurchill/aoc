import functools
import math
import operator
import os
import re

from aocpy.shared import INPUTS_DIR, timer


@timer
def solve():
    with open(os.path.join(INPUTS_DIR, "day6.txt")) as f:
        races = [l for line in f.readlines() if (l := line.strip()) != ""]

    # Part #1
    times = [int(t) for t in re.findall(r"(\d+)", races[0])]
    distances = [int(d) for d in re.findall(r"(\d+)", races[1])]
    ways_to_win = []
    for time, distance in zip(times, distances):
        ways__half = [
            (time_i, traveled)
            for time_i in range(1, math.ceil(time / 2))
            if (traveled := time_i * (time - time_i)) > distance
        ]
        wins = len(ways__half) * 2
        if time % 2 == 0 and (time / 2) * (time - (time / 2)) > distance:
            wins += 1
        ways_to_win.append(wins)
    print(f"Answer #1: {functools.reduce(operator.mul, ways_to_win)}")
    assert functools.reduce(operator.mul, ways_to_win) == 588588

    # Part #2
    time = int("".join(re.findall(r"(\d+)", races[0])))
    distance = int("".join(re.findall(r"(\d+)", races[1])))
    ways__half = [
        (time_i, traveled)
        for time_i in range(1, math.ceil(time / 2))
        if (traveled := time_i * (time - time_i)) > distance
    ]
    wins = len(ways__half) * 2
    if time % 2 == 0 and (time / 2) * (time - (time / 2)) > distance:
        wins += 1
    print(f"Answer #2: {wins}")
    assert wins == 34655848
