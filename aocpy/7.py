import os
import re
from collections import Counter
from dataclasses import dataclass, field
from enum import Enum, IntEnum, unique
from typing import Dict, List

from aocpy.shared import INPUTS_DIR, timer


@dataclass
class CamelCardHand:
    cards: str
    counts: Counter
    bid: int


@unique
class HandStrength(IntEnum):
    FIVE_KIND = 7
    FOUR_KIND = 6
    FULL_HOUSE = 5
    THREE_KIND = 4
    TWO_PAIR = 3
    ONE_PAIR = 2
    HIGH_CARD = 1


@dataclass
class HandRank:
    strength: HandStrength
    cards: List[str]
    use_jokers: bool = False
    card_strengths: List[int] = field(init=False)

    def __post_init__(self):
        self.card_strengths = [self.get_card_strength(c) for c in self.cards]

    def get_card_strength(self, card: str) -> int:
        strengths = {
            "A": 13, "K": 12, "Q": 11, "J": 10, "T": 9, "9": 8, "8": 7,
            "7": 6, "6": 5, "5": 4, "4": 3, "3": 2, "2": 1
        }
        if self.use_jokers:
            strengths["J"] = 0
        return strengths[card]

    def __lt__(self, other):
        if self.strength == other.strength:
            return self.card_strengths < self.card_strengths
        else:
            return self.strength < other.strength

    def __gt__(self, other):
        if self.strength == other.strength:
            return self.card_strengths > self.card_strengths
        else:
            return self.strength > other.strength


@timer
def solve():
    with open(os.path.join(INPUTS_DIR, "day7.txt")) as f:
        inputs = [l for line in f.readlines() if (l := line.strip()) != ""]

    # Part #1  (with an admittedly overengineered solution ;) )
    hands = [
        CamelCardHand(
            cards=matches[0], counts=Counter(matches[0]), bid=int(matches[1])
        )
        for i, inp in enumerate(inputs)
        if (matches := re.findall(r"\w+", inp)) != []
    ]
    ranks: Dict[int, HandRank] = {}
    for i, hand in enumerate(hands):
        card, count = hand.counts.most_common(1)[0]
        if count == 5:
            rank = HandStrength.FIVE_KIND
        elif count == 4:
            rank = HandStrength.FOUR_KIND
        elif count == 3:
            second_card, second_count = hand.counts.most_common(2)[1]
            if second_count == 2:
                rank = HandStrength.FULL_HOUSE
            else:
                rank = HandStrength.THREE_KIND
        elif count == 2:
            second_card, second_count = hand.counts.most_common(2)[1]
            if second_count == 2:
                rank = HandStrength.TWO_PAIR
            else:
                rank = HandStrength.ONE_PAIR
        else:
            rank = HandStrength.HIGH_CARD
        ranks[i] = HandRank(rank, hand.cards, use_jokers=False)
    sorted_ranks = sorted(
        ranks.items(),
        key=lambda r: (r[1].strength, r[1].card_strengths)
    )
    winnings = [
        (idx + 1) * hands[i].bid
        for idx, (i, _) in enumerate(sorted_ranks)
    ]
    print(f"Answer #1: {sum(winnings)}")
    assert sum(winnings) == 248812215

    # Part #2
    print("Answer #2: DID NOT WORK OUT THE KINKS")
