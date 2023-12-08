"""Test day 4 solutions"""
from typing import List

import pytest

from advent_of_code import day4


@pytest.fixture()
def data() -> List[str]:
    """Get the puzzle data"""
    return day4.get_data()


def test_day4_part1(data: List[str]):
    """Test the first solution"""
    result = day4.part1(data)
    assert result == 23750


def test_day4_part2(data: List[str]):
    """Test the second solution"""
    result = day4.part2(data)
    assert result == 13261850
