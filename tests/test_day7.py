"""Test day 7 solutions"""
from unittest import TestCase

from advent_of_code import day7


class Day7Test(TestCase):
    """Day 7 test class"""

    def setUp(self):
        self.data = day7.get_data()

    def test_day7_part1(self):
        """Test the first solution"""
        result = day7.part1(self.data)
        self.assertEqual(result, 246424613)

    def test_day7_part2(self):
        """Test the second solution"""
        result = day7.part2(self.data)
        self.assertEqual(result, 248256639)
