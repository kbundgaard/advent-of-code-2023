"""Test day 2 solutions"""
from typing import List

import pytest

from advent_of_code import day2


@pytest.fixture()
def data() -> List[str]:
    """Get the puzzle data"""
    return day2.get_data()


def test_day2_part1(data: List[str]):
    """Test the first solution"""
    result = day2.part1(data)
    assert result == 2551


def test_day2_part2(data: List[str]):
    """Test the second solution"""
    result = day2.part2(data)
    assert result == 62811
