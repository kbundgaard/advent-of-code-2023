#!/usr/bin/env python3.12
"""Day 3 Solution"""
import re
from typing import Dict
from typing import List
from typing import Tuple

from advent_of_code.lib import file

FIND_DIGITS = re.compile(r"^.*?(\d)(\D+(\d)*)?.*$")


def find_part(index: int, parts: Dict[int, str]) -> int:
    """Finds a specific part in a list of parts for a line"""
    found_part = 0
    for offset, part in parts.items():
        if offset <= index:
            found_part = int(part)
    return found_part


def find_parts(
    search_string: str, search_index: int, parts: Dict[int, str]
) -> List[int]:
    """Determines if there are parts to find and locates them"""
    found = []
    if match := FIND_DIGITS.match(search_string):
        if found_part := find_part(match.start(1) + search_index, parts):
            found.append(found_part)
        if match.start(3) != -1:
            if found_part := find_part(match.start(3) + search_index, parts):
                found.append(found_part)
    return found


def part1(data: List[str], parts: List[Dict[int, str]]) -> int:
    """Part 1 Solution"""
    answer = 0
    symbols = re.compile(r"^.*[^.].*$")
    for line_no, line in enumerate(data):
        for index, part in parts[line_no].items():
            size = len(part)
            start = max(index - 1, 0)
            end = min(index + size + 1, len(line))

            above = ""
            if line_no - 1 >= 0:
                above = data[line_no - 1][start:end]

            current = line[start:end]
            current = current.replace(part, "")

            below = ""
            if line_no + 1 < len(data):
                below = data[line_no + 1][start:end]

            surround = "".join([above, current, below])

            if symbols.match(surround):
                answer += int(part)
    return answer


def part2(data: List[str], parts: List[Dict[int, str]]) -> int:
    """Part 2 Solution"""
    answer = 0
    gears_regex = re.compile(r"\*")
    for line_no, line in enumerate(data):
        gears = [match.start(0) for match in gears_regex.finditer(line)]
        for index in gears:
            start = max(index - 1, 0)
            end = min(index + 2, len(line))

            parts_found = []
            if line_no - 1 >= 0:
                parts_found += find_parts(
                    data[line_no - 1][start:end], start, parts[line_no - 1]
                )

            parts_found += find_parts(line[start:end], start, parts[line_no])

            if line_no + 1 < len(data):
                parts_found += find_parts(
                    data[line_no + 1][start:end], start, parts[line_no + 1]
                )

            if len(parts_found) == 2:
                answer += parts_found[0] * parts_found[1]
    return answer


def get_data() -> Tuple[List[str], List[Dict[int, str]]]:
    """Get the data from file and some initial processing"""
    data = file.import_file("puzzles/day3.txt")
    digits = re.compile(r"\d+")
    parts = [
        {match.start(0): match.group(0) for match in digits.finditer(line)}
        for line in data
    ]
    return (data, parts)


def main() -> None:
    """Run the solver"""
    data = get_data()
    print(f"Part 1 Answer: {part1(data[0], data[1])}")
    print(f"Part 2 Answer: {part2(data[0], data[1])}")


if __name__ == "__main__":
    main()
