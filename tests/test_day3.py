"""Test day 3 solutions"""
from typing import Dict
from typing import List
from typing import Tuple

import pytest

from advent_of_code import day3


@pytest.fixture()
def data() -> Tuple[List[str], List[Dict[int, str]]]:
    """Get the puzzle data"""
    return day3.get_data()


def test_day3_part1(data: Tuple[List[str], List[Dict[int, str]]]):
    """Test the first solution"""
    result = day3.part1(data[0], data[1])
    assert result == 522726


def test_day3_part2(data: Tuple[List[str], List[Dict[int, str]]]):
    """Test the second solution"""
    result = day3.part2(data[0], data[1])
    assert result == 81721933
