#!/usr/bin/env python3.12
"""Day 9 Solution"""
from typing import List

from advent_of_code.lib import file


def differences(reading: List[int]) -> List[int]:
    """Reduces a list to a list of differences"""
    result = []
    for index in range(len(reading) - 1):
        result.append(reading[index + 1] - reading[index])
    return result


def part1(readings: List[List[int]]) -> int:
    """Part 1 Solution"""
    total = 0
    for reading in readings:
        intermediate = reading
        steps = [intermediate]
        while any(intermediate):
            steps.append(differences(intermediate))
            intermediate = steps[-1]
        total += sum(step[-1] for step in steps)
    return total


def part2(readings: List[List[int]]) -> int:
    """Part 2 Solution"""
    total = 0
    for reading in readings:
        intermediate = reading
        steps = [intermediate]
        while any(intermediate):
            steps.append(differences(intermediate))
            intermediate = steps[-1]
        value = 0
        for step in reversed(steps):
            step.insert(0, step[0] - value)
            value = step[0]
        total += steps[0][0]
    return total


def get_data() -> List[List[int]]:
    """Get the data from file and some initial processing"""
    data = file.import_file("puzzles/day9.txt")
    readings = []
    for line in data:
        readings.append([int(value) for value in line.split(" ")])
    return readings


def main() -> None:
    """Run the solver"""
    data = get_data()
    print(f"Part 1 Answer: {part1(data)}")
    print(f"Part 2 Answer: {part2(data)}")


if __name__ == "__main__":
    main()
