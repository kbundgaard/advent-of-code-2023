#!/usr/bin/env python3.12
"""Day 5 Solution"""
import re
from typing import Dict
from typing import List

from advent_of_code.lib import file


def parse_data(data: List[str]) -> (List[int], List[str], Dict[str, List[List[int]]]):
    """Parses the initial data into a more useful format"""
    seeds_regex = re.compile(r"^seeds: ([\d ]*)$")
    header_regex = re.compile(r"^(.*) map:$")
    mapping_regex = re.compile(r"^\d+ \d+ \d+$")
    initial = []
    order = []
    mappings = {}

    for line in data:
        if line == "":
            pass
        elif match := seeds_regex.match(line):
            initial = [int(item) for item in match.group(1).split(" ")]
        elif match := header_regex.match(line):
            order.append(match.group(1))
            mappings[match.group(1)] = []
        elif match := mapping_regex.match(line):
            mappings[order[-1]].append([int(item) for item in line.split(" ")])
        else:
            print(f"Issue parsing line: {line}")

    return (initial, order, mappings)


def part1(
    initial: List[int], order: List[str], mappings: Dict[str, List[List[int]]]
) -> int:
    """Part 1 Solution"""
    destination = initial
    for transformation in order:
        source = destination
        destination = [None] * len(source)
        for mapping in mappings[transformation]:
            for index, seed in enumerate(source):
                if mapping[1] <= seed < mapping[1] + mapping[2]:
                    destination[index] = seed - mapping[1] + mapping[0]
            for index, seed in enumerate(destination):
                if seed is None:
                    destination[index] = source[index]
    return min(destination)


def part2(
    initial: List[int], order: List[str], mappings: Dict[str, List[List[int]]]
) -> int:
    """Part 2 Solution"""
    destination = []
    for index in range(len(initial) >> 1):
        destination.append(
            (initial[2 * index], initial[2 * index] + initial[2 * index + 1])
        )

    for transformation in order:
        source = destination
        destination = []
        for mapping in mappings[transformation]:
            unmapped = []
            for seed_range in source:
                seed_range_start = seed_range[0]
                seed_range_end = seed_range[1]
                # Handle if any of the seed range falls before the mapping
                range_start = min(seed_range_start, mapping[1])
                range_end = min(seed_range_end, mapping[1])
                if range_end - range_start:
                    unmapped.append((range_start, range_end))
                    seed_range_start = range_end
                # Handle if any of the seed range falls after the mapping
                range_start = max(seed_range_start, mapping[1] + mapping[2])
                range_end = max(seed_range_end, mapping[1] + mapping[2])
                if range_end - range_start:
                    unmapped.append((range_start, range_end))
                    seed_range_end = range_start
                # Handle if any of the seed range falls inside the mapping
                range_start = seed_range_start - mapping[1] + mapping[0]
                range_end = seed_range_end - mapping[1] + mapping[0]
                if range_end - range_start:
                    destination.append((range_start, range_end))
            source = unmapped
        destination += source
    return min(location[0] for location in destination)


def get_data() -> (List[int], List[str], Dict[str, List[List[int]]]):
    """Get the data from file and some initial processing"""
    data = file.import_file("puzzles/day5.txt")
    initial, order, mappings = parse_data(data)
    return (initial, order, mappings)


def main() -> None:
    """Run the solver"""
    initial, order, mappings = get_data()
    print(f"Part 1 Answer: {part1(initial, order, mappings)}")
    print(f"Part 2 Answer: {part2(initial, order, mappings)}")


if __name__ == "__main__":
    main()
