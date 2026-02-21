import unittest
from alternating import alternating_characters


class AlternatingCharactersTest(unittest.TestCase):

    def test_no_deletion_needed(self):
        # Arrange
        s = "ABABAB"
        expected = 0

        # Act
        result = alternating_characters(s)

        # Assert
        self.assertEqual(result, expected)

    def test_all_same_A(self):
        # Arrange
        s = "AAAA"
        expected = 3

        # Act
        result = alternating_characters(s)

        # Assert
        self.assertEqual(result, expected)

    def test_all_same_B(self):
        # Arrange
        s = "BBBBB"
        expected = 4

        # Act
        result = alternating_characters(s)

        # Assert
        self.assertEqual(result, expected)

    def test_mixed_case(self):
        # Arrange
        s = "AAABBB"
        expected = 4

        # Act
        result = alternating_characters(s)

        # Assert
        self.assertEqual(result, expected)

    def test_single_character(self):
        # Arrange
        s = "A"
        expected = 0

        # Act
        result = alternating_characters(s)

        # Assert
        self.assertEqual(result, expected)