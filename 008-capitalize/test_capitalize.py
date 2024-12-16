import pytest
from capitalize import capitalize

class Test_capitalize():

  def test_single_word(Self):
    assert capitalize('word') == 'Word' 

  def test_multiple_words(Self):
    assert capitalize('a short sentence') == 'A Short Sentence' 

  def test_with_punctuation(Self):
    assert capitalize('look, its is working') == 'Look, Its Is Working'

  def test_empty_string(Self):
    assert capitalize('a short sentence') == 'A Short Sentence' 