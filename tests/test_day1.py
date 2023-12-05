"""Test day 1 solutions"""
from unittest import TestCase

from advent_of_code import day1


class Day1Test(TestCase):
    """Day 1 test class"""

    def setUp(self):
        self.data = day1.get_data()

    def test_day1_part1(self):
        """Test the first solution"""
        result = day1.part1(self.data)
        self.assertEqual(result, 54916)

    def test_day1_part2(self):
        """Test the second solution"""
        result = day1.part2(self.data)
        self.assertEqual(result, 54728)
