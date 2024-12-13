import pytest
from fizzbuzz import fizzbuzz

class TestFizzBuzz():
  def test_fizzbuzz_multiple_of_3(self):
    assert fizzbuzz(3) == ["1", "2", "fizz"]

  def test_fizzbuzz_multiple_of_5(self):
    assert fizzbuzz(5) == ["1", "2", "fizz", "4", "buzz"]

  def test_fizzbuzz_multiple_of_3_and_5(self):
    assert fizzbuzz(15)[14] == "fizzbuzz"

  def test_fizzbuzz_non_multiples(self):
    assert fizzbuzz(4) == ["1", "2", "fizz", "4"]

  def test_fizzbuzz_large_number(self):
    result = fizzbuzz(20)
    assert result[2] == "fizz"
    assert result[4] == "buzz"
    assert result[14] == "fizzbuzz"
    assert result[19] == "buzz"