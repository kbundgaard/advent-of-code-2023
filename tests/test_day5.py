"""Test day 5 solutions"""
from typing import Dict
from typing import List
from typing import Tuple

import pytest

from advent_of_code import day5


@pytest.fixture()
def data() -> Tuple[List[int], List[str], Dict[str, List[List[int]]]]:
    """Get the puzzle data"""
    return day5.get_data()


def test_day5_part1(
    data: Tuple[List[int], List[str], Dict[str, List[List[int]]]]
) -> None:
    """Test the first solution"""
    result = day5.part1(data[0], data[1], data[2])
    assert result == 910845529


def test_day5_part2(
    data: Tuple[List[int], List[str], Dict[str, List[List[int]]]]
) -> None:
    """Test the second solution"""
    result = day5.part2(data[0], data[1], data[2])
    assert result == 77435348
