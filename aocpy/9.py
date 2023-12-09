import os
import re

from aocpy.shared import INPUTS_DIR, timer


@timer
def solve():
    with open(os.path.join(INPUTS_DIR, "day9.txt")) as f:
        report = [l for line in f.readlines() if (l := line.strip()) != ""]

    extrapolated = []
    for history in report:
        numbers = list(map(int, re.findall(r"(-?\d+)", history)))
        last_diffs = []
        diffs = [n2 - n1 for n1, n2 in zip(numbers[:-1], numbers[1:])]
        while not all(d == 0 for d in diffs):
            last_diffs.append(diffs[-1])
            diffs = [n2 - n1 for n1, n2 in zip(diffs[:-1], diffs[1:])]
        extrapolated.append(numbers[-1] + sum(last_diffs))

    # Part #1
    print(f"Answer #1: {sum(extrapolated)}")
    assert sum(extrapolated) == 1884768153

    # Part #2
    extrapolated = []
    for history in report:
        numbers = list(map(int, re.findall(r"(-?\d+)", history)))[::-1]
        last_diffs = []
        diffs = [n2 - n1 for n1, n2 in zip(numbers[:-1], numbers[1:])]
        while not all(d == 0 for d in diffs):
            last_diffs.append(diffs[-1])
            diffs = [n2 - n1 for n1, n2 in zip(diffs[:-1], diffs[1:])]
        extrapolated.append(numbers[-1] + sum(last_diffs))
    print(f"Answer #2: {sum(extrapolated)}")
    assert sum(extrapolated) == 1031
