import pytest
from reverse_int import reverse_int

class TestReverseInt:
  def test_reverse_int_15(self):
    assert reverse_int(15) == 51

  def test_reverse_int_123(self):
    assert reverse_int(123) == 321

  def test_reverse_int_negative(self):
    assert reverse_int(-123) == -321

  def test_reverse_int_single_digit(self):
    assert reverse_int(5) == 5

  def test_reverse_int_with_zeros(self):
    assert reverse_int(100) == 1

  def test_reverse_int_large_number(self):
    assert reverse_int(987654321) == 123456789