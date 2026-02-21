import unittest
from grid_challenge import grid_challenge


class TestGridChallenge(unittest.TestCase):

    def test_example_yes(self):
        grid = ["ebacd",
                "fghij",
                "olmkn",
                "trpqs",
                "xywuv"]

        result = grid_challenge(grid)

        self.assertEqual(result, "YES")

    def test_example_no(self):
        grid = ["mpxz",
                "abcd",
                "wlmf"]

        result = grid_challenge(grid)

        self.assertEqual(result, "NO")

    def test_single_row(self):
        grid = ["abc"]

        result = grid_challenge(grid)

        self.assertEqual(result, "YES")

    def test_already_sorted(self):
        grid = ["abc",
                "bcd",
                "cde"]

        result = grid_challenge(grid)

        self.assertEqual(result, "YES")