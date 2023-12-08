"""Test day 7 solutions"""
from typing import List

import pytest

from advent_of_code import day7


@pytest.fixture()
def data() -> List[str]:
    """Get the puzzle data"""
    return day7.get_data()


def test_day7_part1(data: List[str]):
    """Test the first solution"""
    result = day7.part1(data)
    assert result == 246424613


def test_day7_part2(data: List[str]):
    """Test the second solution"""
    result = day7.part2(data)
    assert result == 248256639
