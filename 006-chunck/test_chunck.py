import pytest
from chunk import chunk

class TestChunk():
  def test_chunk_even_division(self):
    assert chunk([1,2,3,4],2) == [[1,2], [3,4]]

  def test_chunk_odd_remainder(self):
    assert chunk([1,2,3,4,5],2) == [[1,2], [3,4], [5]]

  def test_chunk_large_size(self):
    assert chunk([1,2,3],10) == [[1,2,3]]

  def test_chunk_single_element(self):
    assert chunk([1,2,3,4],1) == [[1],[2],[3],[4]]

  def test_chunk_empty_array(self):
    assert chunk([],3) == []