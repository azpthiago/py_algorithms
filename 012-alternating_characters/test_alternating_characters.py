import pytest
from alternating_characters import alternating_characters

class TestAlternatingCharacters:
    def test_empty_string(self):
        assert alternating_characters("") == 0

    def test_no_removals_needed(self):
        assert alternating_characters("ABABAB") == 0

    def test_all_same_characters(self):
        assert alternating_characters("AAAAAA") == 5

    def test_mixed_characters(self):
        assert alternating_characters("AABAAB") == 2

    def test_large_repetitions(self):
        assert alternating_characters("BBBBBBBBBB") == 9
