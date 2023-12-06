#!/usr/bin/env python3.12
"""Day 6 Solution"""
import math
import re
from typing import List

from advent_of_code.lib import file


def part1(times: List[int], distances: List[int]) -> int:
    """Part 1 Solution"""
    answer = 1
    for index, time in enumerate(times):
        min_button_time = math.ceil(
            (time - math.sqrt(time * time - 4 * distances[index])) / 2
        )
        answer *= time - 2 * min_button_time + 1

    return answer


def part2(times: List[int], distances: List[int]) -> int:
    """Part 2 Solution"""
    time = int("".join(map(str, times)))
    distance = int("".join(map(str, distances)))
    min_button_time = math.ceil((time - math.sqrt(time * time - 4 * distance)) / 2)
    return time - 2 * min_button_time + 1


def get_data() -> (List[int], List[int]):
    """Get the data from file and some initial processing"""
    data = file.import_file("puzzles/day6.txt")
    data_regex = re.compile(r"^(Time|Distance):\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)$")
    times = []
    distances = []
    for line in data:
        if match := data_regex.match(line):
            if match.group(1) == "Time":
                times.append(int(match.group(2)))
                times.append(int(match.group(3)))
                times.append(int(match.group(4)))
                times.append(int(match.group(5)))
            elif match.group(1) == "Distance":
                distances.append(int(match.group(2)))
                distances.append(int(match.group(3)))
                distances.append(int(match.group(4)))
                distances.append(int(match.group(5)))
            else:
                print(f"Issue parsing line: {line}")
        else:
            print(f"Issue parsing line: {line}")
    return (times, distances)


def main() -> None:
    """Run the solver"""
    times, distances = get_data()
    print(f"Part 1 Answer: {part1(times, distances)}")
    print(f"Part 2 Answer: {part2(times, distances)}")


if __name__ == "__main__":
    main()
