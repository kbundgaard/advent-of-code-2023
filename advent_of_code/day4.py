#!/usr/bin/env python3.12
"""Day 4 Solution"""
import re
from typing import List

from advent_of_code.lib import file

CARD_REGEX = re.compile(r"^Card +\d+: ([0-9 ]+) \| ([0-9 ]+)$")


def part1(data: List[str]) -> int:
    """Part 1 Solution"""
    answer = 0
    for line in data:
        if match := CARD_REGEX.match(line):
            winning = {int(number) for number in match.group(1).split(" ") if number}
            actual = {int(number) for number in match.group(2).split(" ") if number}
            winners = len(winning & actual)
            answer += 2 ** (winners - 1) if winners else 0
        else:
            print(f"Issue parsing line: {line}")
    return answer


def part2(data: List[str]) -> int:
    """Part 2 Solution"""
    cards = [1] * len(data)
    for line_no, line in enumerate(data):
        if match := CARD_REGEX.match(line):
            winning = {int(number) for number in match.group(1).split(" ") if number}
            actual = {int(number) for number in match.group(2).split(" ") if number}
            winners = len(winning & actual)
            for index in range(winners):
                cards[line_no + index + 1] += cards[line_no]
        else:
            print(f"Issue parsing line: {line}")
    return sum(cards)


def get_data() -> List[str]:
    """Get the data from file"""
    return file.import_file("puzzles/day4.txt")


def main() -> None:
    """Run the solver"""
    data = get_data()
    print(f"Part 1 Answer: {part1(data)}")
    print(f"Part 2 Answer: {part2(data)}")


if __name__ == "__main__":
    main()
