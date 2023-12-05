"""Test day 2 solutions"""
from unittest import TestCase

from advent_of_code import day2


class Day2Test(TestCase):
    """Day 2 test class"""

    def setUp(self):
        self.data = day2.get_data()

    def test_day2_part1(self):
        """Test the first solution"""
        result = day2.part1(self.data)
        self.assertEqual(result, 2551)

    def test_day2_part2(self):
        """Test the second solution"""
        result = day2.part2(self.data)
        self.assertEqual(result, 62811)
