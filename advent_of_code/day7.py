#!/usr/bin/env python3.12
"""Day 7 Solution"""
import re
from enum import Enum
from typing import List

from advent_of_code.lib import file


class HandType(Enum):
    """Enum of possible poker hands"""

    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIRS = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7


class Hand:
    """Base class for implementing a hand of cards"""

    CARD_VALUES = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": 11,
        "T": 10,
        "9": 9,
        "8": 8,
        "7": 7,
        "6": 6,
        "5": 5,
        "4": 4,
        "3": 3,
        "2": 2,
    }
    DATA_REGEX = re.compile(r"^([AKQJT98765432]{5}) (\d+)$")

    bid: int
    cards: List[int]
    hand_type: HandType

    def __init__(self, data: str):
        if match := self.DATA_REGEX.match(data):
            self.bid = int(match.group(2))
            self.cards = []
            for char in match.group(1):
                self.cards.append(self.CARD_VALUES[char])
            self.hand_type = self.identify_hand()
        else:
            raise ValueError

    def __lt__(self, other) -> bool:
        if self.hand_type == other.hand_type:
            for cards in zip(self.cards, other.cards):
                if cards[0] == cards[1]:
                    continue
                return cards[0] < cards[1]
        return self.hand_type.value < other.hand_type.value

    def identify_hand(self) -> HandType:
        """Determines what kind of poker hand this hand represents"""
        distinct_cards = [self.cards.count(card) for card in set(self.cards)]
        hand_type = HandType.HIGH_CARD
        if len(distinct_cards) == 4:
            hand_type = HandType.ONE_PAIR
        elif len(distinct_cards) == 3:
            if max(distinct_cards) < 3:
                hand_type = HandType.TWO_PAIRS
            else:
                hand_type = HandType.THREE_OF_A_KIND
        elif len(distinct_cards) == 2:
            if max(distinct_cards) < 4:
                hand_type = HandType.FULL_HOUSE
            else:
                hand_type = HandType.FOUR_OF_A_KIND
        elif len(distinct_cards) == 1:
            hand_type = HandType.FIVE_OF_A_KIND
        return hand_type


class JokerHand(Hand):
    """Specific implementation of a hand of cards for problem 2"""

    CARD_VALUES = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "T": 10,
        "9": 9,
        "8": 8,
        "7": 7,
        "6": 6,
        "5": 5,
        "4": 4,
        "3": 3,
        "2": 2,
        "J": 1,
    }
    JOKER = 1

    def identify_hand(self) -> HandType:
        """Determines what kind of poker hand this hand represents"""
        distinct_cards = [self.cards.count(card) for card in set(self.cards)]
        num_jokers = self.cards.count(self.JOKER)
        hand_type = HandType.ONE_PAIR
        if num_jokers == 0:
            hand_type = super().identify_hand()
        elif len(distinct_cards) == 4:
            hand_type = HandType.THREE_OF_A_KIND
        elif len(distinct_cards) == 3:
            if max(distinct_cards) < 3 and num_jokers < 2:
                hand_type = HandType.FULL_HOUSE
            else:
                hand_type = HandType.FOUR_OF_A_KIND
        elif len(distinct_cards) < 3:
            hand_type = HandType.FIVE_OF_A_KIND
        return hand_type


def part1(data: List[str]) -> int:
    """Part 1 Solution"""
    ranked_hands = sorted([Hand(line) for line in data])
    answer = 0
    for index, hand in enumerate(ranked_hands):
        answer += (index + 1) * hand.bid
    return answer


def part2(data: List[str]) -> int:
    """Part 2 Solution"""
    ranked_hands = sorted([JokerHand(line) for line in data])
    answer = 0
    for index, hand in enumerate(ranked_hands):
        answer += (index + 1) * hand.bid
    return answer


def get_data() -> List[str]:
    """Get the data from file"""
    return file.import_file("puzzles/day7.txt")


def main() -> None:
    """Run the solver"""
    data = get_data()
    print(f"Part 1 Answer: {part1(data)}")
    print(f"Part 2 Answer: {part2(data)}")


if __name__ == "__main__":
    main()
