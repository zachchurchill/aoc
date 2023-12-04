import os
import re

from aocpy.shared import INPUTS_DIR, timer


@timer
def solve():
    with open(os.path.join(INPUTS_DIR, "day4.txt")) as f:
        scratchoffs = [line.strip() for line in f.readlines()]

    # Part #1
    scratchoff_numbers = [
        [
            list(map(int, re.findall(r"(\d+)", nums)))
            for nums in scratchoff.split(":")[1].split(" | ")
        ]
        for scratchoff in scratchoffs
    ]
    num_matches = [
        len(set(winning).intersection(received))
        for winning, received in scratchoff_numbers
    ]
    points = [
        2 ** (n - 1)
        for n in num_matches
        if n > 0
    ]
    print(f"Answer #1: {sum(points)}")
    assert sum(points) == 25010

    # Part #2
    num_scratchoffs = len(scratchoffs)
    num_cards = [1] * num_scratchoffs
    for i in range(num_scratchoffs):
        n = num_matches[i]
        next_card_start = min(i+1, num_scratchoffs)
        next_card_end = min(next_card_start+n, num_scratchoffs)
        for _ in range(num_cards[i]):
            for j in range(next_card_start, next_card_end):
                num_cards[j] += 1
    print(f"Answer #2: {sum(num_cards)}")
    assert sum(num_cards) == 9924412
