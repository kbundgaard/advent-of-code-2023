"""Test day 4 solutions"""
from unittest import TestCase

from advent_of_code import day4


class Day4Test(TestCase):
    """Day 4 test class"""

    def setUp(self):
        self.data = day4.get_data()

    def test_day4_part1(self):
        """Test the first solution"""
        result = day4.part1(self.data)
        self.assertEqual(result, 23750)

    def test_day4_part2(self):
        """Test the second solution"""
        result = day4.part2(self.data)
        self.assertEqual(result, 13261850)
