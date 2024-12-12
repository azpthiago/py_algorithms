import unittest
from palindrome import palindrome

class TestPalindrome(unittest.TestCase):
  def test_empty_string(self):
    self.assertEqual(palindrome(""), True)

  def test_single_character(self):
    self.assertEqual(palindrome("a"), True)

  def test_palindrome(self):
    self.assertEqual(palindrome("arara"), True)

  def test_non_palindrome(self):
    self.assertEqual(palindrome("thiago"), False)

  def test_palindrome_with_spaces(self):
    self.assertEqual(palindrome("nurses run"), True)

  def test_palindrome_with_case_insensitive(self):
    self.assertEqual(palindrome("Arara"), True)
