import unittest
from reverse_string import reverse_String

class TestReverseString(unittest.TestCase):
  def test_empty_string(self):
    self.assertEqual(reverse_String(""), "")
  
  def test_single_character(self):
    self.assertEqual(reverse_String("a"), "a")
  
  def test_palindrome(self):
    self.assertEqual(reverse_String("madam"), "madam")
  
  def test_regular_string(self):
    self.assertEqual(reverse_String("python"), "nohtyp")
  
  def test_with_spaces_and_special_characters(self):
    self.assertEqual(reverse_String("hello, world!"), "!dlrow ,olleh")

if __name__ == "__main__":
  unittest.main()