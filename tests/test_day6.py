"""Test day 6 solutions"""
from unittest import TestCase

from advent_of_code import day6


class Day6Test(TestCase):
    """Day 6 test class"""

    def setUp(self):
        self.times, self.distances = day6.get_data()

    def test_day6_part1(self):
        """Test the first solution"""
        result = day6.part1(self.times, self.distances)
        self.assertEqual(result, 5133600)

    def test_day6_part2(self):
        """Test the second solution"""
        result = day6.part2(self.times, self.distances)
        self.assertEqual(result, 40651271)
