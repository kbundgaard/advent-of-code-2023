"""Test day 1 solutions"""
from typing import List

import pytest

from advent_of_code import day1


@pytest.fixture()
def data() -> List[str]:
    """Get the puzzle data"""
    return day1.get_data()


def test_day1_part1(data: List[str]) -> None:
    """Test the first solution"""
    result = day1.part1(data)
    assert result == 54916


def test_day1_part2(data: List[str]) -> None:
    """Test the second solution"""
    result = day1.part2(data)
    assert result == 54728
