import pytest
from max_char import max_char

class TestMaxChar:
  def test_single_char(self):
    assert max_char("aaaa") == "a"

  def test_multiple_chars(self):
    assert max_char("abcccccccd") == "c"

  def test_spaces_and_special_chars(self):
    assert max_char("apple 1231111") == "1"

  def test_empty_string(self):
    assert max_char("") == ""