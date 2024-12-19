import pytest

from grading_students import grading_students

class TestGradingStudents:
    def test_round_up(self):
        assert grading_students([73]) == [75]

    def test_no_rounding_below_38(self):
        assert grading_students([33]) == [33]

    def test_no_rounding_if_difference_is_3_or_more(self):
        assert grading_students([57]) == [57]

    def test_rounding_edge_case(self):
        assert grading_students([38]) == [40]

    def test_multiple_grades(self):
        assert grading_students([73, 67, 38, 33]) == [75, 67, 40, 33]
