"""Test day 8 solutions"""
from typing import Dict
from typing import List
from typing import Tuple

import pytest

from advent_of_code import day8


@pytest.fixture()
def data() -> Tuple[List[int], Dict[str, Tuple[str, str]]]:
    """Get the puzzle data"""
    return day8.get_data()


def test_day8_part1(data: Tuple[List[int], Dict[str, Tuple[str, str]]]):
    """Test the first solution"""
    result = day8.part1(data[0], data[1])
    assert result == 16531


def test_day8_part2(data: Tuple[List[int], Dict[str, Tuple[str, str]]]):
    """Test the second solution"""
    result = day8.part2(data[0], data[1])
    assert result == 24035773251517
