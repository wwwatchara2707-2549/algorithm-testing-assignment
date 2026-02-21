import unittest
from funny import funny_string


class FunnyStringTest(unittest.TestCase):

    def test_funny_case(self):
        # Arrange
        s = "acxz"
        expected = "Funny"

        # Act
        result = funny_string(s)

        # Assert
        self.assertEqual(result, expected)

    def test_not_funny_case(self):
        # Arrange
        s = "bcxz"
        expected = "Not Funny"

        # Act
        result = funny_string(s)

        # Assert
        self.assertEqual(result, expected)

    def test_single_character(self):
        # Arrange
        s = "a"
        expected = "Funny"

        # Act
        result = funny_string(s)

        # Assert
        self.assertEqual(result, expected)

    def test_same_characters(self):
        # Arrange
        s = "aa"
        expected = "Funny"

        # Act
        result = funny_string(s)

        # Assert
        self.assertEqual(result, expected)

    def test_palindrome(self):
        # Arrange
        s = "abcdedcba"
        expected = "Funny"

        # Act
        result = funny_string(s)

        # Assert
        self.assertEqual(result, expected)