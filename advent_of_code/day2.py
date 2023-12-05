#!/usr/bin/env python3.12
"""Day 2 Solution"""
import re
from typing import List

from advent_of_code.lib import file


def part1(data: List[str]) -> int:
    """Part 1 Solution"""
    cubes = {"red": 12, "green": 13, "blue": 14}
    game_regex = re.compile(r"^Game (\d+): (.*)$")
    answer = 0
    for line in data:
        if match := game_regex.match(line):
            valid = True
            for draw in match.group(2).split("; "):
                for balls in draw.split(", "):
                    amount, color = balls.split(" ")
                    if cubes[color] < int(amount):
                        valid = False
            if valid:
                answer += int(match.group(1))
        else:
            print(f"Issue parsing line: {line}")
    return answer


def part2(data: List[str]) -> int:
    """Part 2 Solution"""
    answer = 0
    game_regex = re.compile(r"^Game (\d+): (.*)$")
    for line in data:
        if match := game_regex.match(line):
            cubes = {"red": 0, "green": 0, "blue": 0}
            for draw in match.group(2).split("; "):
                for balls in draw.split(", "):
                    amount, color = balls.split(" ")
                    cubes[color] = max(cubes[color], int(amount))
            answer += cubes["red"] * cubes["green"] * cubes["blue"]
        else:
            print(f"Issue parsing line: {line}")
    return answer


def get_data() -> List[str]:
    """Get the data from file"""
    return file.import_file("puzzles/day2.txt")


def main() -> None:
    """Run the solver"""
    data = get_data()
    print(f"Part 1 Answer: {part1(data)}")
    print(f"Part 2 Answer: {part2(data)}")


if __name__ == "__main__":
    main()
