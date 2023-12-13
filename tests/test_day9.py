"""Test day 9 solutions"""
from typing import List

import pytest

from advent_of_code import day9


@pytest.fixture()
def data() -> List[List[int]]:
    """Get the puzzle data"""
    return day9.get_data()


def test_day9_part1(data: List[List[int]]) -> None:
    """Test the first solution"""
    result = day9.part1(data)
    assert result == 2175229206


def test_day9_part2(data: List[List[int]]) -> None:
    """Test the second solution"""
    result = day9.part2(data)
    assert result == 942
