import pytest

from anagrams import anagrams

class TestAnagrams():

  def test_anagrams_valid_anagrams(self):
    assert anagrams('rail safety', 'fairy tales') is True

  def test_anagrams_valid_anagrams_with_punctuation(self):
    assert anagrams('RAIL, SAFETY', 'fairy tales') is True

  def test_anagrams_invalid_anagrams(self):
    assert anagrams('Hi, There', 'Bye There') is False

  def test_anagrams_case_insensitivity(self):
    assert anagrams('Listen', 'Silent') is True

  def test_anagrams_empty_strings(self):
    assert anagrams('', '') is True