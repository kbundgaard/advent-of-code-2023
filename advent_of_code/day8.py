#!/usr/bin/env python3.12
"""Day 8 Solution"""
import re
from math import lcm
from typing import Dict
from typing import List
from typing import Tuple

from advent_of_code.lib import file


def part1(directions: List[int], nodes: Dict[str, Tuple[str, str]]) -> int:
    """Part 1 Solution"""
    current = "AAA"
    steps = 0
    while current != "ZZZ":
        current = nodes[current][directions[steps % len(directions)]]
        steps += 1
    return steps


def part2(directions: List[int], nodes: Dict[str, Tuple[str, str]]) -> int:
    """Part 2 Solution"""
    start_nodes = [node for node in nodes if node.endswith("A")]
    cycle_lengths = []
    for node in start_nodes:
        current = node
        steps = 0
        while not current.endswith("Z"):
            current = nodes[current][directions[steps % len(directions)]]
            steps += 1
        exit_node = current
        to_exit = steps
        current = nodes[current][directions[steps % len(directions)]]
        steps += 1
        while current not in {node, exit_node}:
            current = nodes[current][directions[steps % len(directions)]]
            steps += 1
        # It would appear the distance from "A-node" to "Z-node" is equal to the cycle length
        # Also, there is only one exit node per cycle
        assert to_exit * 2 == steps
        cycle_lengths.append(to_exit)
    return lcm(*cycle_lengths)


def get_data() -> Tuple[List[int], Dict[str, Tuple[str, str]]]:
    """Get the data from file and some initial processing"""
    data = file.import_file("puzzles/day8.txt")
    directions_regex = re.compile(r"^[LR]+$")
    node_regex = re.compile(r"(\w+) = \((\w+), (\w+)\)")
    directions = []
    nodes = {}
    for line in data:
        if line == "":
            continue
        if directions_regex.match(line):
            for char in line:
                directions.append(int(char == "R"))
        elif match := node_regex.match(line):
            nodes[match.group(1)] = (match.group(2), match.group(3))
        else:
            print(f"Issue parsing line: {line}")
    return (directions, nodes)


def main() -> None:
    """Run the solver"""
    data = get_data()
    print(f"Part 1 Answer: {part1(data[0], data[1])}")
    print(f"Part 2 Answer: {part2(data[0], data[1])}")


if __name__ == "__main__":
    main()
