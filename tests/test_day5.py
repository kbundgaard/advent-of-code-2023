"""Test day 5 solutions"""
from unittest import TestCase

from advent_of_code import day5


class Day5Test(TestCase):
    """Day 2 test class"""

    def setUp(self):
        self.initial, self.order, self.mappings = day5.get_data()

    def test_day5_part1(self):
        """Test the first solution"""
        result = day5.part1(self.initial, self.order, self.mappings)
        self.assertEqual(result, 910845529)

    def test_day5_part2(self):
        """Test the second solution"""
        result = day5.part2(self.initial, self.order, self.mappings)
        self.assertEqual(result, 77435348)
