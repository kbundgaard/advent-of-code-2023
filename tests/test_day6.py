"""Test day 6 solutions"""
from typing import List
from typing import Tuple

import pytest

from advent_of_code import day6


@pytest.fixture()
def data() -> Tuple[List[int], List[int]]:
    """Get the puzzle data"""
    return day6.get_data()


def test_day6_part1(data: Tuple[List[int], List[int]]) -> None:
    """Test the first solution"""
    result = day6.part1(data[0], data[1])
    assert result == 5133600


def test_day6_part2(data: Tuple[List[int], List[int]]) -> None:
    """Test the second solution"""
    result = day6.part2(data[0], data[1])
    assert result == 40651271
