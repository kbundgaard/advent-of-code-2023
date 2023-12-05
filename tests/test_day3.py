"""Test day 3 solutions"""
from unittest import TestCase

from advent_of_code import day3


class Day3Test(TestCase):
    """Day 2 test class"""

    def setUp(self):
        self.data, self.parts = day3.get_data()

    def test_day3_part1(self):
        """Test the first solution"""
        result = day3.part1(self.data, self.parts)
        self.assertEqual(result, 522726)

    def test_day3_part2(self):
        """Test the second solution"""
        result = day3.part2(self.data, self.parts)
        self.assertEqual(result, 81721933)
