#!/usr/bin/env python3.12
"""Day 1 Solution"""
import re
from typing import List

from advent_of_code.lib import file

DIGIT_WORDS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def convert_to_digit(digit: str) -> int:
    """Converts a string to a digit"""
    return DIGIT_WORDS.get(digit) or int(digit)


def part1(data: List[str]) -> int:
    """Part 1 Solution"""
    double_digit = re.compile(r"^.*?(\d).*(\d).*?$")
    single_digit = re.compile(r"^.*?(\d).*?$")
    answer = 0
    for line in data:
        if match := double_digit.match(line):
            first = int(match.group(1))
            last = int(match.group(2))
            answer += 10 * first + last
        elif match := single_digit.match(line):
            digit = int(match.group(1))
            answer += 11 * digit
        else:
            print(f"Issue parsing line: {line}")
    return answer


def part2(data: List[str]) -> int:
    """Part 2 Solution"""
    digits = "|".join(DIGIT_WORDS.keys())
    double_digit = re.compile(rf"^.*?(\d|{digits}).*(\d|{digits}).*?$")
    single_digit = re.compile(rf"^.*?(\d|{digits}).*?$")
    answer = 0
    for line in data:
        if match := double_digit.match(line):
            first = convert_to_digit(match.group(1))
            last = convert_to_digit(match.group(2))
            answer += 10 * first + last
        elif match := single_digit.match(line):
            digit = convert_to_digit(match.group(1))
            answer += 11 * digit
        else:
            print(f"Issue parsing line: {line}")
    return answer


def get_data() -> List[str]:
    """Get the data from file"""
    return file.import_file("puzzles/day1.txt")


def main() -> None:
    """Run the solver"""
    data = get_data()
    print(f"Part 1 Answer: {part1(data)}")
    print(f"Part 2 Answer: {part2(data)}")


if __name__ == "__main__":
    main()
